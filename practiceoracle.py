import


"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
# [ 파이썬 + 디비 절차 ]
# 1. 연결객체 얻어오기(Connection)
# 2. sql 문장
# 3. cursor 객체 얻어오기
# 4. 실행
# 5. cursor 객체 닫기
# 6. 연결객체 닫기
import cx_Oracle as oci


class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_name = phone_number
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input('메뉴선택:').format()
    return int(menu)


def createTable():
    #연결객체얻어오기
    conn=



def set_contact():
   pass

def print_contact():
   pass


def delete_contact(name):
   pass

def run():
    while True:
        menu = print_menu()
        if menu == 4:  # 종료를 선택하면
            break
        elif menu == 1:  # 입력을 선택하면
            set_contact()
        elif menu == 2:  # 출력을 선택하면
            print_contact()
        elif menu == 3:  # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":

