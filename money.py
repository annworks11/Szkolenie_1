n = 2137                                                 #input value

m_200 = n/200
if m_200 >= 1:
    print("200 zl:" , int(m_200)) 

m_100 = (n - 200 * int(m_200)) / 100
if m_100 >= 1:
    print("100 zl:" , int(m_100))

m_50 = (n - (200 * int(m_200) + 100 * int(m_100))) / 50
if m_50 >= 1:
    print("50 zl:" , int(m_50))

m_20 = (n - (200 * int(m_200) + 100 * int(m_100) + 50 * 
int(m_50))) / 20
if m_20 >= 1:
    print("20 zl:" , int(m_20))

m_10 = (n - (200 * int(m_200) + 100 * int(m_100) + 50 * 
int(m_50) + 20 * int(m_20))) / 10
if m_10 >= 1:
    print("10 zl:" , int(m_10))

m_5 = (n - (200 * int(m_200) + 100 * int(m_100) + 50 * 
int(m_50) + 20 * int(m_20) + 10 * int(m_10))) / 5
if m_5 >= 1:
    print("5 zl:" , int(m_5))

m_2 = (n - (200 * int(m_200) + 100 * int(m_100) + 50 * 
int(m_50) + 20 * int(m_20) + 10 * int(m_10) + 5 * 
int(m_5))) / 2
if m_2 >= 1:
    print("2 zl:" , int(m_2))

m_1 = (n - (200 * int(m_200) + 100 * int(m_100) + 50 * 
int(m_50) + 20 * int(m_20) + 10 * int(m_10) + 5 * 
int(m_5) + 2 * int(m_2)))
if m_1 >= 1:
    print("1 zl:" , int(m_1))