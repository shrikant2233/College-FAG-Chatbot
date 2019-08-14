import sqlite3
conn=sqlite3.connect('test.db')
c=conn.cursor() 
print("1.Initialize")
print("2.Insert")
print("3.Update")
print("4.View All")
print("5.Delete")
print("6.Exit")
while True:
    i=int(input("Enter the choice "))
    if i==1:
        conn.execute('''CREATE TABLE CHAT
         (id INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
         question           TEXT    NULL,
         response           TEXT     NULL);''')
        print("Table created successfully")
        data = [(1, 'hi', 'Hello!'),
             (2,'Hi','Good to see you again!'),
             (3,'hi','Hi there, how can I help?'),
             (4,'how are you?','Hello'),
             (5,'how are you','Good to see you again!'),
             (6,'How are you?','Hi there, how can I help?'),
             (7,'see you later','Talk to you later'),
             (8,'See you later','Goodbye!'),
             (9,'goodbye','Goodbye!'),
             (10,'Goodbye','Talk to you later'),
             (11,'Is this college accredited?','yes'),
             (12,'is this college accredited?','yes'),
             (13,'can i pay college fee in installments','yes,but permission of principal is required'),
             (14,'what are college hours','We are open 9am-3:20pm Monday-saturday!'),
             (15,'hours of operation','9am-3:20pm Monday-saturday!'),
             (16,'Hours of operation','9am-3:20pm Monday-saturday!'),
             (17,'What are the subjects in 5th sem computer science','subjects in 5th sem are:\nTheory of computation\nMicroprocessor and Interface\nprograming in java\nAnalysis and Design of Algorithm\nDatabase management system\nUnix and Shell Programing'),
             (18,'What are the subjects in 4th sem cse','subjects in 4th sem are:\nComputational Mathematics\nDiscrete Structures\nData Structures\nComputer Systems Architecture\nObject Oriented Concepts & Programming using C++\nOperating System'),
             (19,'what are the subjects in 5th sem cse','subjects in 5th sem are:\nTheory of computation\nMicroprocessor and Interface\nprograming in java\nAnalysis and Design of Algorithm\nDatabase management system\nUnix and Shell Programing'),
             (20,'what are the paymentmode available in college','cheque,debit card,netbanking,credit card are acceptable'),
             (21,'what are the paymentmode available in college','cheque,debit card,netbanking,credit card are acceptable'),
             (22,'Is transportation facility available in college','yes, bus facility is available '),
             (23,'is transportation facility available in college','yes, bus facility is available '),
             (24,'Is hostel facility available in college campus','yes, hostel facility is available '),
             (25,'is hostel facility available in college campus','yes, hostel facility is available '),
             (26,'what are facility available in hostel','Telephone\nInternet access\nIndoor games\nFirst– Aid.\nReading materials\nTelevision\nDining Hall\nVehicle parking\nRound the-clock security, etc '),
             (27,'is canteen facility available in college campus','yes,canteen facility is available '),
             (28,'Is canteen facility available in college campus','yes,canteen facility is available '),
             (29,'Is canteen facility available in college campus','yes,canteen facility is available '),
             (30,'what is the transportation fees of college','Rs 15000/-'),
             (31,'what is the Hostel fees of college','Rs 57500/-'),
             (32,'what is the semester fees of college ','Rs 36115/-'),
             (33,'what are the department available in college','CSE,ET&T,CE,ME,IT,Applied mathematics,Applied physics,Applied chemistry Humanities,MBA'),
             (34,'What are the subjects in 4th sem computer science','subjects in 4th sem are:\nComputational Mathematics\nDiscrete Structures\nData Structures\nComputer Systems Architecture\nObject Oriented Concepts & Programming using C++\nOperating System'),
             (35,'who is the chairman of college','Mr. Nishant Tripathi'),
             (36,'who is the principal of college','Dr. Alok Jain'),
             (37,'this college is affiliated to which university','CSVTU'),
             (38,'This college is approved by whom','All India Council of Technical Education (AICTE), New Delhi'),
             (39,'this college is approved by whom?','AICTE'),
             (40,'this college is affiliated to which university','Chhattisgarh Swami Vivekanand Technical University'),
             (41,'What is the scholarship criteria of college','there is  three scholarship:\nScholarship 1\n\n1.Chhattisgarh Govt. Scholarship Policy:\nEligibility Criteria: Caste Certificate issued from C.G. Govt.\nResidential Certificate issued from C.G. Govt.\nIncome Certificate from the concerned authorized authority/ person.\n\nScholarship 2\n\n2. Central Govt. Scholarship Policy\nMerit Scholarship:- 80 % and above in 12th Class.\nIncome deceleration by parents\nMinority Scholarship:- Minority certificate (Muslim, Sikh, Christian, Buddhists, Parsis and Jain)\n55 % and above in 12th Class.\nIncome deceleration by parents.\n\nScholarship 3\n\n\nPRAGATI Scholarship:- \nEligibility Criteria:Only for two Girls per family.\nFamily income should be less than Rs. 8 Lakhs/ annum.\nStudents Admitted for Diploma/Undergraduate Degree Level Programmes/Courses in AICTE Approved Institutions.\nOnly for the students admitted in first year of their Degree/Diploma for the current academic year '),
             (42,'what is the scholarship criteria of college','there is  three scholarship:\nScholarship 1\n\n1.Chhattisgarh Govt. Scholarship Policy:\nEligibility Criteria: Caste Certificate issued from C.G. Govt.\nResidential Certificate issued from C.G. Govt.\nIncome Certificate from the concerned authorized authority/ person.\n\nScholarship 2\n\n2. Central Govt. Scholarship Policy\nMerit Scholarship:- 80 % and above in 12th Class.\nIncome deceleration by parents\nMinority Scholarship:- Minority certificate (Muslim, Sikh, Christian, Buddhists, Parsis and Jain)\n55 % and above in 12th Class.\nIncome deceleration by parents.\n\nScholarship 3\n\n\nPRAGATI Scholarship:- \nEligibility Criteria:Only for two Girls per family.\nFamily income should be less than Rs. 8 Lakhs/ annum.\nStudents Admitted for Diploma/Undergraduate Degree Level Programmes/Courses in AICTE Approved Institutions.\nOnly for the students admitted in first year of their Degree/Diploma for the current academic year '),

             
             
                        
             ]
        c.executemany('INSERT INTO CHAT VALUES (?,?,?)', data)
        conn.commit()
    elif i==2:
        q=input("Enter question ")
        r=input("Enter response ")
        qry="INSERT INTO CHAT (question,response) VALUES('"+q+"','"+r+"')"
        c.execute(qry)
        conn.commit()
    elif i==3:
        id=int(input("Enter id "))
        a=id
        id=(id,)
        d=c.execute('SELECT * FROM CHAT WHERE id=?',id)
        for row in d:
            print(row)
        a=str(a)
        q=input("Enter question")
        r=input("Enter response")
        qry="UPDATE CHAT SET question='"+q+"',response='"+r+"' WHERE id="+a
        print(qry)
        c.execute(qry)
        conn.commit()
    elif i==4:
        d=c.execute('SELECT * FROM CHAT')
        for row in d:
            print(row)
    elif i==5:
        id=int(input("Enter id"))
        id=(id,)
        d=c.execute('SELECT * FROM CHAT WHERE id=?',id)
        if(d):
            c.execute("DELETE FROM CHAT WHERE id=?",id)
            conn.commit()
        else:
            print("Data not found")
    elif i==6:
        exit()
    else:
        print("Invalid Choice")