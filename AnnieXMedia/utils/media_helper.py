from pyrogram.enums import MessageMediaType
import mimetypes
import os

async def send_smart_media(client, chat_id, url_or_file, caption=None, reply_markup=None, reply_to_message_id=None):
    """
    Sends media (Photo or Video) based on the file extension or content type.
    """
    if not url_or_file:
        return None

    # Simple extension check
    ext = os.path.splitext(str(url_or_file))[1].lower()

    # If no extension in url (e.g. some api links), try to guess or default to photo
    # But usually config variables have extensions like .jpg or .mp4

    is_video = ext in ['.mp4', '.mkv', '.webm', '.avi', '.mov', '.flv']
    is_photo = ext in ['.jpg', '.jpeg', '.png', '.webp', '.bmp']
    is_gif = ext in ['.gif']

    try:
        if is_video:
            return await client.send_video(
                chat_id=chat_id,
                video=url_or_file,
                caption=caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif is_photo:
            return await client.send_photo(
                chat_id=chat_id,
                photo=url_or_file,
                caption=caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        elif is_gif:
             return await client.send_animation(
                chat_id=chat_id,
                animation=url_or_file,
                caption=caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        else:
            # Fallback: Try photo first as it's most common for this bot's config
            # If it fails, one might try document, but user specifically disliked "File" format.
            # So we will try send_photo. If it's a video link sent as photo, Telegram might fail or send as file?
            # Actually Telegram send_photo supports video URLs sometimes as static previews? No.
            # Let's check if there is a way to peek. For now, default to Photo as it was the previous behavior.
            return await client.send_photo(
                chat_id=chat_id,
                photo=url_or_file,
                caption=caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
    except Exception as e:
        print(f"Smart media send failed: {e}")
        # Final fallback to document if everything else fails (optional, but safer to deliver something than nothing)
        # But user hates documents. So we might just re-raise or try one last time as document.
        # Let's try sending as document only if photo/video failed.
        try:
             return await client.send_document(
                chat_id=chat_id,
                document=url_or_file,
                caption=caption,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id
            )
        except:
            return None
