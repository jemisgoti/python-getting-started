import time

from telethon import TelegramClient, events

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = '17076701'
api_hash = '0117bfe49bc89e84c75106662277f351'

# fill in your own details here
phone = '+1(458) 204-7711'
  # use your username if unsure
password = ''  # if you have two-step verification enabled

# content of the automatic reply
message = "t.me/indianwifenude"

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient('session_file.txt', api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')