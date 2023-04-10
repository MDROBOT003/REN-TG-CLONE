# ----------------------------------- https://github.com/m4mallu/clonebot ---------------------------------------------#
import time
import pytz
import asyncio
import datetime
from bot import Bot
from math import trunc
from library.sql import *
from presets import Presets
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait
from plugins.cb_input import update_type_buttons
from library.buttons import reply_markup_stop, reply_markup_finished
from library.chat_support import calc_percentage, calc_progress, save_target_cfg, get_time

#
bot_start_time = time.time()
#
async def clone_medias(bot: Bot, m: Message):
    id = int(m.chat.id)
    query = await query_msg(id)
    clone_cancel_key[id] = int(m.id)
    #
    clone_start_time = time.time()
    start_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%I:%M:%S %p')
    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - bot_start_time))
    #
    file_name = caption = str()
    #
    delay = limit = doc = video = audio = text = voice = photo = total_copied = matching = msg_id = int()
    #
    # Create mandatory variables from the database query
    source_chat = int(query.s_chat)
    target_chat = int(query.d_chat)
    start_id = int(query.from_id)
    end_id = int(query.to_id)
    end_msg_id = int(query.last_msg_id)
    #
    clone_delay = bool(query.delayed_clone)
    default_caption = bool(query.caption)
    fn_caption = bool(query.file_caption)
    #
    # Define the clone delay
    if bool(clone_delay):
        delay = 90
    else:
        delay = 40
    #
    # The vaulues will be swithed if the start message id is greater than the end message id
    if start_id > end_id:
        start_id = start_id ^ end_id
        end_id = end_id ^ start_id
        start_id = start_id ^ end_id
    else:
        pass
    #
    # Creating variables for progress bar and the percentage calculation
    if not bool(start_id):
        sp = 0
    else:
        sp = start_id
    if not bool(end_id):
        ep = end_msg_id
    else:
        ep = end_id
    #
    await m.edit_text(Presets.INITIAL_MESSAGE_TEXT)
    await asyncio.sleep(1)
    msg = await m.reply_text(Presets.WAIT_MSG, reply_markup=reply_markup_stop)
    #
    for offset in reversed(
            range(end_id+1, (1 if not bool(start_id) else start_id)-1, (start_id - 1) if not bool(start_id) else -1)):
        async for user_message in bot.USER.get_chat_history(chat_id=source_chat, offset_id=offset, limit=1):
            if not user_message.empty:
                messages = await bot.USER.get_messages(source_chat, user_message.id, replies=0)
                msg_id = messages.id
                #
                report = Presets.CLONE_REPORT.format(await get_time(), source_chat, target_chat,
                                                     "1" if not bool(start_id) else start_id,
                                                     end_msg_id if not bool(msg_id) else msg_id,
                                                     "🟡" if bool(clone_delay) else "🚫",
                                                     "🟡" if bool(default_caption) else "🚫",
                                                     "🟡" if bool(fn_caption) else "🚫",
                                                     int(total_copied), doc, video, audio, photo, voice, text, matching)
                # If the user cancelled the clone operation
                if id not in clone_cancel_key:
                    await save_target_cfg(id, target_chat)
                    if not int(total_copied):
                        await m.delete()
                    await asyncio.sleep(2)
                    await msg.edit(Presets.CANCELLED_MSG, reply_markup=reply_markup_finished)
                    await bot.USER.send_message("me", report, disable_web_page_preview=True)
                    await reset_all(id)
                    file_types.clear()
                    file_types.extend(Presets.FILE_TYPES)
                    await update_type_buttons()
                    return
                else:
                    pass
                for file_type in file_types:
                    media = getattr(messages, file_type, None)
                    if media is not None:
                        uid = str(media.file_unique_id) if hasattr(media, 'file_unique_id') else None
                        # If the duplicate file id is found while cloning operation
                        if (uid is not None) and (uid in master_index):
                            matching += 1
                            await m.edit(Presets.DUPLICATE_INDEX.format(matching, msg_id))
                        # if the duplicate file is not found while cloning
                        else:
                            if uid is not None:
                                master_index.append(uid) # The unique id of the file is added to the master index list
                            if file_type == 'document': doc += 1; file_name = messages.document.file_name
                            elif file_type == 'video': video += 1; file_name = messages.video.file_name
                            elif file_type == 'audio': audio += 1; file_name = messages.audio.file_name
                            elif file_type == "voice": voice += 1; file_name = messages.caption
                            elif file_type == "photo": photo += 1; file_name = messages.caption
                            elif file_type == "text": text += 1; file_name = str()
                            else: pass
                            #
                            if (file_type != "text") and (id in custom_caption):
                                caption = custom_caption[id]
                            elif bool(default_caption):
                                caption = messages.caption
                            elif bool(fn_caption):
                                try:
                                    caption = str(file_name).rsplit('.', 1)[0]
                                except Exception:
                                    caption = str()
                            else:
                                caption = str()
                            #
                            total_copied = doc + video + audio + voice + photo + text
                            pct = await calc_percentage(sp, ep, msg_id)
                            time_taken = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - clone_start_time))
                            update_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%I:%M:%S %p')
                            try:
                                await m.edit(
                                    Presets.MESSAGE_COUNT.format(
                                        int(msg_id),
                                        int(total_copied),
                                        trunc(pct) if pct <= 100 else "- ",
                                        time_taken,
                                        uptime,
                                        start_time,
                                        update_time
                                    ),
                                    parse_mode=ParseMode.HTML,
                                    disable_web_page_preview=True
                                )
                            except FloodWait as e:
                                await asyncio.sleep(e.value)
                            except Exception:
                                pass
                            progress = await calc_progress(pct)
                            try:
                                await bot.USER.copy_message(
                                    chat_id=target_chat,
                                    from_chat_id=source_chat,
                                    caption=caption if bool(caption) else str(),
                                    message_id=msg_id,
                                    reply_markup=messages.reply_markup,
                                    disable_notification=True
                                )
                            except FloodWait as e:
                                await asyncio.sleep(e.value)
                            except Exception:
                                await msg.edit_text(Presets.COPY_ERROR, reply_markup=reply_markup_finished)
                                await reset_all(id)
                                file_types.clear()
                                file_types.extend(Presets.FILE_TYPES)
                                if not int(total_copied):
                                    await m.delete()
                                return
                            try:
                                await msg.edit("🇮🇳 | " + progress if pct <= 100 else Presets.BLOCK,
                                               reply_markup=reply_markup_stop)
                            except Exception:
                                pass
                            await asyncio.sleep(delay)
                            # If the end id is reached, the clone operation will be aborted and the report is generated
                            if end_id and (int(msg_id) >= end_id):
                                if not int(total_copied):
                                    await m.delete()
                                await msg.edit(Presets.FINISHED_TEXT, reply_markup=reply_markup_finished)
                                await reset_all(id)
                                file_types.clear()
                                file_types.extend(Presets.FILE_TYPES)
                                await update_type_buttons()
                                return
                            else:
                                pass
                    else:
                        pass
            else:
                pass

    # If the clone operation is automatically completed by the bot
    await save_target_cfg(id, target_chat)
    if not int(total_copied):
        await m.delete()
    await m.edit_reply_markup(None)
    await msg.edit(Presets.FINISHED_TEXT, reply_markup=reply_markup_finished)
    file_types.clear()
    await reset_all(id)
    file_types.extend(Presets.FILE_TYPES)
    await update_type_buttons()
