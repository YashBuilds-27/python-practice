import random
print("========== 🎯 Welcome to Number Guessing Game 🎯 ==========")
input("\n🔑 Press any key to start...\n")
ch='y'
while ch=='y':
    try:
        num=random.randint(1,100)
        print("🎲 NUMBER IS GENERATED...START GUESSING")
        attempt=0
        while attempt<5:
            guess=int(input("\n👉 Enter your guessed number:"))
            diff=abs(num-guess)
            if guess==num:
                print(f"\n✅ Correct...You guessed in {attempt} attempts")
                break
            elif diff<=5:
                print('\n🔥 Very close')
            elif diff<=10:
                print('\n😊 Close')
            elif diff<=20:
                print('\n😐 Far')
            else:
                print("\n🥶 Very Far")
            attempt+=1
        else:
            print(f'❌ Out of attempts!... The number was {num}')
        ch=input("\n🔄 Want to play again?...Press 'y':")
    except ValueError:
        print("\n⚠️ Invalid value entered...\n")
