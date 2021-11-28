name_birth = {}

while True :
    print()

    print("1. 날짜 계산기")
    print("2. 요일 계산기")
    print("3. 생일 메모장")

    select1 = int(input(" 위 기능 중에서 원하는 기능의 번호를 입력해주세요! : "))
    print()
# 기능 선택 (기능1, 기능2, 기능3)

    if select1 == 1 :
# 기능1

        print("1. n일 후의 날짜구하기")
        print("2. n일 전의 날짜구하기")
        print("3. 지정일로부터 남은 일수 구하기")
              
        select2 = int(input(" 다음 기능 중에서 원하는 기능의 번호를 입력해주세요! : "))
        print()
# 기능1에서의 기능선택 (기능1_1, 기능1_2, 기능1_3)
    
        if select2 == 1 :
    # 기능1_1
            import datetime
        
            y = int(input("지정연도는 언제입니까? : "))
            m = int(input("지정달는 언제입니까? : "))
            n = int(input("지정일은 언제입니까? : "))
            w = int(input("며칠 후를 알고 싶으싶니까? : "))
            d=datetime.date(y,m,n)
            t=datetime.timedelta(days=w)
            date_after=" 지정일로부터 " +str(w)+ "일 후는 "+ str(t+d) +" 입니다."
            print()
            print(date_after)

        elif select2 == 2 :
    # 기능1_2
            import datetime
             
             
            y = int(input("지정연도는 언제입니까? : "))
            m = int(input("지정달는 언제입니까? : "))
            n = int(input("지정일은 언제입니까? : "))
            w = -int(input("며칠 전을 알고 싶으싶니까? : "))
            d=datetime.date(y,m,n)
            t=datetime.timedelta(days=w)
            date_before=" 지정일로부터 " +str(-w)+ "일 전은 "+ str(t+d) +" 입니다."
            print()
            print(date_before)

        elif select2 == 3 :
    # 기능1_3
            import datetime              

            y = int(input("지정연도는 언제입니까? : "))
            m = int(input("지정달는 언제입니까? : "))
            n = int(input("지정일은 언제입니까? : "))
            d=datetime.date(y,m,n)
            t=datetime.date.today()
            print(d-t)

        else :
    # 1,2,3 그 외의 번호 입력 시    
            print(" 없는 번호입니다. 다시한번 확인해 주세요!")
                    
    elif select1 == 2 :
# 기능2
        import datetime
    
        u={0:"월요일",1:"화요일", 2:"수요일",3:"목요일",4:"금요일",5:"토요일",6:"일요일"}
        y = int(input("지정연도는 언제입니까? : "))
        m = int(input("지정달는 언제입니까? : "))
        n = int(input("지정일은 언제입니까? : "))
        d=datetime.date(y,m,n)
        date_day=" "+ str(y)+"년 "+ str(m)+"월 "+ str(n)+ "일은 "+str(u[d.weekday()])+ "입니다."
        print()
        print(date_day)
    #print(u[d.weekday()])


    elif select1 == 3 :
# 기능3
        

        Q = 0

        print("1. 생일 추가하기")
        print("2. 생일 확인하기")
        print("0. 종료하기")
    
        Q = int(input(" 위 기능중 원하는 기능의 번호를 입력해주세요. : "))
        print()

        if Q == 1 :
        # 기능3_1(생일추가)
            birthday_m=input("생일의 날짜는 몇 월입니까? (숫자만 입력하세요) : ")
            birthday_d=input("생일의 날짜는 며칠입니까? (숫자만 입력하세요) : ")
            birthday = birthday_m+"월 "+birthday_d+"일"
            name = input("이름은 무엇입니까? : ")
            name_birth[name] = birthday
            
            print()
            
        elif Q == 2 :
        # 기능3_2(생일확인)
            print(name_birth)
            print()
            
        elif Q == 0 :
            print(" 프로그램이 종료되었습니다.")
        # 기능3_3(종료조건, 0을 입력시 종료)
            break
        else :
            print('없는 번호입니다 다시한번 확인해 주세요!')

        

    else :
        print("없는 번호입니다 다시한번 확인해 주세요!")
    
input()


      
