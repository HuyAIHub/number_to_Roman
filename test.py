class py_solution: #đầu tiên khai báo 1 lớp
    def int_to_Roman(self, num): #khởi tạo hàm có tên là "int_to_Roman" và có thuộc tính là num
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]       #tạo 2 list vs : val[i] = syb[i]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = '' #khoi tao 1 tring rỗng
        i = 0
        while  num > 0: #vòng lặp while khi mà num > 0: thì lặp
            for _ in range(num // val[i]): # chi khi num lon hon val[i] thi ms chay xuong
                # khi val[-1] = 1 thi ms xuong day :
                roman_num += syb[i]  # roman_num = "I"
                num -= val[i] # num = 3 va val=1 moi lan lap giam 1 thi lap 3 lan while dung (dk dung cua while)
            i += 1 # tang index
            print(num)
        return roman_num # tra ve


print(py_solution().int_to_Roman(3)) # khoi tao ra 1 object
#print(py_solution().int_to_Roman(4000))