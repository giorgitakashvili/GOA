#if = თუ
#elif = else if = თუ'თუარადა
#else = სხვა ნებისმიერ შემთხვევაში
მომხმარებლისასაკი = int(input("შეიყვანეთ თქვენი ასაკი: "))

if მომხმარებლისასაკი >= 18 and მომხმარებლისასაკი <= 100:
    print("თქვენ შეგიძ₾იათ ალკოჰოლი იყიდოთ")
elif მომხმარებლისასაკი <= 17:
    print("თქვენ ვერ შეიძენთ ალკოჰოლს.")
else:
    print("შენ ცოცხალი როგორ ხარ?")