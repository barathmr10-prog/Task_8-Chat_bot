
def response(question):
    user_input = question.lower()

    name = ["i am","i'm","my name is",]
    if [i for i in name if i in question.lower()]:
        print("Bot : Hi, nice to meet you. How are you?")
    elif "hi" in user_input or "hello" in user_input or "hey" in user_input:
        print("Bot : Hi, yes tell me")
    elif "how are you" in user_input or "good, you?" in user_input or "how about you" in user_input:
        print("Bot : I am good, thanks")
    elif "what" in user_input:
        if 'favorite' in user_input:
            print("Bot : I dont have any favorite, I like them all")
        elif 'name' in user_input:
            print("Bot : I already told you, its PyBOT")
        elif 'best' in user_input:
            print("Bot : Its all up to us mind, everything is best in it own way")
        elif 'age' in user_input:
            print("Bot : I would born new daily but first appearance on 1991, Guido van Rossum gave birth to me")
        else:
            print("Bot : I am not smart enough to answer that")
    elif "do you know" in user_input:
        print("Bot : No I dont, please explain it to me")
    elif "?" in user_input:
        print("Bot : Thats a good question, but I am not yet trained on it")
    else:
        print("Bot : You should check this on chrome")


def bot():
    print('Bot : Hi! there I am PyBOT')
    while True:
        question = input("You : ")
        end = ['bye','goodbye','tata']
        thanks = ['thanks','thank you',]
        if [i for i in end if i in question.lower()]:
            print("Bot : Goodbye! have a nice day")
            break
        elif [i for i in thanks if i in question.lower()]:
            print("Bot : You are welcome")
            break
        bot_response = response(question)

if __name__ == "__main__":
    bot()