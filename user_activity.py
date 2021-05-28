import win32gui
import time
import pymysql
import re 

def userActivityTracking(stop, email, testid):
    email_id = email
    TestID = testid
    a=1
    w=win32gui
    cheating_counter = 0
    my_file = open("copy_websites.txt", "r")
    content = my_file.read()

    MS_Forms = "Microsoft Forms - Google Chrome"
    MS_Teams = "Microsoft Teams - Google Chrome"
    MS_Teams_1 = "Microsoft Teams - initializing... - Google Chrome"

    copy_websites_list = content.split(",")
    print(copy_websites_list)
    my_file.close()


    while a==1:
        time.sleep(1)
        curr = w.GetWindowText(w.GetForegroundWindow())

        res = [ele for ele in copy_websites_list if(ele in curr)] 
        
        if((bool(res))):
            if(re.search(MS_Forms,curr) or re.search(MS_Teams,curr) or re.search(MS_Teams_1,curr)):
                continue
            else:
                cheating_counter = cheating_counter + 1
                print(curr)
                print(cheating_counter)
                connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
                curr = connect.cursor()
                curr.execute("SELECT * from ONLINE where EMAIL=%s AND TEST_ID=%s", (email_id, TestID))
                rows = curr.fetchone()
                cur = connect.cursor()
                if rows[7] == 0:
                    cur.execute("UPDATE ONLINE SET STUDY_MATERIAL_DETECTION=%s WHERE EMAIL=%s AND TEST_ID=%s",(1, email, TestID))
                else:
                    current_counter = int(rows[7]) + 1
                    cur.execute("UPDATE ONLINE SET STUDY_MATERIAL_DETECTION=%s WHERE EMAIL=%s AND TEST_ID=%s",(current_counter, email, TestID))
                connect.commit()
                connect.close()
        if stop():
            break
                
       



