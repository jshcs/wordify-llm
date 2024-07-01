import sys 
from wordifyllm import WordifyLLM

user_input, model, type = None, "gpt-3.5-turbo-0125", "idiom"

for args in sys.argv:
    if args.startswith("-u"):
        user_input = args.split("=")[1]
    elif args.startswith("-m"):
        model = args.split("=")[1]
    elif args.startswith("-t"):
        type = args.split("=")[1]

if user_input==None:
    print("User input is required.")
else: 
    wordify = WordifyLLM(user_input=user_input, model=model, type=type)
    output = wordify.main()

    print(output)