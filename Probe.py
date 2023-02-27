import asyncio
import time
from telethon.sync import TelegramClient
from telethon import functions, types, utils


api_id = 24437292  # замените на свой api_id
api_hash = '0123456789abcdef0123456789abcdef'  # замените на свой api_hash
phone_number = '+995597784941'  # замените на свой номер телефона
session_file = 'my_session'
image_path = 'C:/Users/7effl/OneDrive/Desktop/ИЩУ.jpg'  # замените на путь к изображению

async def send_message_to_chat(chat_id, message, client, media=None):
    if media:
        await client(functions.messages.SendMediaRequest(
            peer=chat_id,
            media=media,
            message=message
        ))
    else:
        await client(functions.messages.SendMediaRequest(
            peer=chat_id,
            media=media,
            message=message
        ))

async def main():
    async with TelegramClient(session_file, api_id, api_hash) as client:
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input('Please enter the code you received: ')
            await client.sign_in(phone_number, code)

            # Загрузка изображения
            with open(image_path, 'rb') as f:
                result = await client.upload_file(f)
            # Получение InputMedia из загруженного файла
            media = utils.get_input_media(result)

        # Список чатов
        # Список чатов
        chats = [
            ('FIRMAOOOSHOP',
             'Привет! Ищу готовые ООО или ИП, которые хотят открыть счет в Тинькофф Банке. Я не посредник, а сам открываю счета, и готов заплатить тебе 3000-5000 рублей за открытие, за каждый счет. Я также могу подсказать по всем вопросам, касающимся банка. Счет полностью бесплатный, и ты можешь закрыть его в любой момент.\nНе упусти возможность заработать и свяжись со мной прямо сейчас!@rkotinkoff - пиши'),
            ('prodam_firmi',
             'Привет! Ищу готовые ООО или ИП, которые хотят открыть счет в Тинькофф Банке. Я не посредник, а сам открываю счета, и готов заплатить тебе 3000-5000 рублей за открытие, за каждый счет. Я также могу подсказать по всем вопросам, касающимся банка. Счет полностью бесплатный, и ты можешь закрыть его в любой момент.\nНе упусти возможность заработать и свяжись со мной прямо сейчас!@rkotinkoff - пиши'),
            ('RussiaBizzz',
             'Привет! Ищу готовые ООО или ИП, которые хотят открыть счет в Тинькофф Банке. Я не посредник, а сам открываю счета, и готов заплатить тебе 3000-5000 рублей за открытие, за каждый счет. Я также могу подсказать по всем вопросам, касающимся банка. Счет полностью бесплатный, и ты можешь закрыть его в любой момент.\nНе упусти возможность заработать и свяжись со мной прямо сейчас!@rkotinkoff - пиши'),
            ('kartoookyplu',
             'Привет! Ищу готовые ООО или ИП, которые хотят открыть счет в Тинькофф Банке. Я не посредник, а сам открываю счета, и готов заплатить тебе 3000-5000 рублей за открытие, за каждый счет. Я также могу подсказать по всем вопросам, касающимся банка. Счет полностью бесплатный, и ты можешь закрыть его в любой момент.\nНе упусти возможность заработать и свяжись со мной прямо сейчас!@rkotinkoff - пиши'),
             ]

        while True:
            for chat in chats:
                # Получение id чата
                entity = await client.get_entity(chat[0])
                chat_id = entity.id

                # Отправка сообщения в чат
                await send_message_to_chat(chat_id, chat[1], client)
                print(f'Message sent to chat {chat[0]}')

            # Задержка на нужное колво минут
            time.sleep(300)

if __name__ == '__main__':
    asyncio.run(main())



