import json

def save_words(en,uz):
    with open('words_database.json' , 'a') as file:
        data = {'en':en , 'uz':uz}
        json.dump(data,file)
        file.write('\n')

def load_database() :
    try:
        with open('words_database.json','r')  as file:
            lines =  file.readlines()
            database = [json.loads(line) for line in lines] 
            return database
    except FileNotFoundError:
        return[]

def get_user_input():
    get_input = input("Englizcha so'zni kiriting: ")   
    return get_input

def ask_words(get_input, database):
    for entry in database:
        if entry['en'] == get_input:
            return entry['uz']
        
def main():        
    while True:
        database = load_database()
        get_input = get_user_input()
        uz = ask_words(get_input, database)

        if uz:
            print(uz)
        else:
            new_word = input("""Menda bu so'z tarjimasi yo'q , bilsangiz kiriting: """)
            save_words(get_input,new_word)
            print("Urra men yangi so'zni saqladim")

            continue_prompt = input("sizda yana so'z bo'lsa qabul qilaman ha/yoq ")
            if continue_prompt.lower() == 'n':
                continue

if __name__ == '__main__':
    main()        
        



