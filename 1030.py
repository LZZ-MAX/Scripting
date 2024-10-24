class MiniDataBase:
    def __init__(self):
        self.data = []

    def add_new_data(self):
        while True:
            department = input("請輸入部門：")
            name = input("請輸入姓名：")
            age = input("請輸入年齡：")
            phone = input("請輸入電話：")
            self.data.append({
                "department": department,
                "name": name,
                "age": age,
                "phone": phone
            })
            cont = input("是否繼續新增資料？(y/n): ")
            if cont.lower() != 'y':
                break

    def find_data(self):
        if self.data:
            name = input("請輸入要查詢的姓名：")
            for record in self.data:
                if record['name'] == name:
                    print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
                    print("----------------------------------------")
                    print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']:<15}")
                    break
            else:
                print("查無此人")

    def modify_data(self):
        pass

    def delete_data(self):
        pass

    def show_data(self):
        if not self.data:
            print("目前沒有任何資料")
        else:
            print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
            print("----------------------------------------")
            for record in self.data:
                print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']:<15}")
        return


    def exit(self):
        print("系統退出")
        exit()

    def main(self):
        print("--- 人事資料管理系統 ---")
        print("1. 新增資料")
        print("2. 查詢資料")
        print("3. 修改資料")
        print("4. 刪除資料")
        print("5. 顯示所有資料")
        print("6. 退出系統")
        print("----------------------")

        while True:
            try:
                choice = int(input("請選擇功能 ："))
                match choice:
                    case 1:
                        self.add_new_data()
                    case 2:
                        self.find_data()
                    case 3:
                        self.modify_data()
                    case 4:
                        self.delete_data()
                    case 5:
                        self.show_data()
                    case 6:
                        self.exit()
            except ValueError:
                print("請輸入有效的數字")

if __name__ == "__main__":
    data = MiniDataBase()
    data.main()