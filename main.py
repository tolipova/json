import json 

def save_question(question,answer):
    with open('question_database.json','a') as file:
        data = {'question':question, 'answer':answer}
        json.dump(data,file)
        file.write('\n')

def load_database():
    try:
        with open('question_database.json','r') as file :
            lines =  file.readlines()
            database = [json.loads(line) for line in lines] 
            return database
    except FileNotFoundError :
        return []
    
def get_user_input ():
    user_input = input("Savolingizni kiriting: ")         
    return user_input
    
def ask_questions(user_input, database):
    for entry in database:
        if entry['question'] == user_input:
            return entry['answer']

def main():        
    while True:
        database = load_database()
        user_input = get_user_input()
        answer = ask_questions(user_input, database)

        if answer:
            print(answer)
        else:
            new_answer = input("""Menda bu ma'lumot bo'yicha javob topilmadi. Istasangiz o'zingiz to'g'ri ma'lumot kiriting: """)
            save_question(user_input,new_answer)
            print("Urra men yangi ma'lumotni saqlay oldim")

            continue_prompt = input("sizda yana ma'lumot bo'lsa qabul qilaman ha/yoq ")
            if continue_prompt.lower() == 'n':
                continue

if __name__ == '__main__'   :
    main()




