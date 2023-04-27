import os
import openai

openai.api_key = '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'
completion = openai.Completion()

start_sequence = "\nBot Đa Di Năng:"
restart_sequence = "\n\nPerson:"
session_prompt = "Hello, you are chatting with Bot Đa Di Năng, a chat bot built on the GPT-3 model\n" \
                 "I will answer your questions like on Chat GPT\n" \
                 "\n\nPerson: Who are you?\nBot Đa Di Năng: I am Bot Đa Di Năng." \
                 "\n\nPerson: Are you ready to chat with me?\nBot Đa Di Năng: Yes, I am very pleased."
# sử dụng mô hình ngôn ngữ GPT-3 của OpenAI để tạo phản hồi dựa trên question cuộc trò chuyện trước đó được lưu trữ trong tệp chat_log.

def ask(question, chat_log=None):
#Đây là một hàm Python sử dụng API OpenAI để tạo câu trả lời cho một câu hỏi nhất định.
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    # tạo một chuỗi prompt_text bằng cách nối chat_log và question, được phân tách bằng các mã thông báo đặc biệt restart_sequence và start_sequence, tương ứng
    # sử dụng để cho biết thời điểm bắt đầu một cuộc trò chuyện hoặc lời nhắc mới.
    response = openai.Completion.create(
        # phương thức để tạo phản hồi bằng API OpenAI.
        engine="davinci",
        # mô hình ngôn ngữ sẽ sử dụng
        prompt=prompt_text,
        # dấu nhắc văn bản 
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        # các tham số khác nhau kiểm soát hành vi của mô hình
        stop=["\n"],
        # stop: danh sách các chuỗi mà mô hình sẽ sử dụng để chấm dứt văn bản được tạo.
    )
    story = response['choices'][0]['text']
    return str(story)
    # Hàm cuối cùng sẽ trích xuất văn bản phản hồi đã tạo từ phản hồi API và trả về dưới dạng một chuỗi.


def append_interaction_to_chat_log(question, answer, chat_log=None):
# Đây là một hàm Python nối thêm tương tác trả lời câu hỏi vào nhật ký trò chuyện
    if chat_log is None:
        chat_log = session_prompt
        # Nếu chat_loglà None, hàm sẽ đặt giá trị đó thành session_promptgiá trị mặc định.
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
    # hàm trả về một chuỗi được định dạng nối chuỗi 
    #Chuỗi này đại diện cho nhật ký trò chuyện được cập nhật với tương tác mới được thêm vào cuối.