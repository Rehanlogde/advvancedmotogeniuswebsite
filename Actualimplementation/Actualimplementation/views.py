from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import pymysql as sql
import smtplib
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import pymysql as db
import json
import datetime

senderemail = 'rehan17641@gmail.com'
senderpassword = 'vbgwuyrpfkrwwloh'
connection = db.connect(host= "localhost", user= "root", passwd= "Rehanmysql.com", database="chatbotpraticedb", port=3306)

cursor = connection.cursor()
sqlconnection = sql.connect(
            user = "root",
            passwd= "Rehanmysql.com",
            database= "advancedmotogeniuswebsitedb",
            port=3306
        ) 
mycursor = sqlconnection.cursor()

autocot = ChatBot("autocot", read_only = True)

training_data = [
    ["hello",
    "Hey racer, what's in your mind today",],

    ["hola",
    "Hey racer, what's in your mind today",
    ],[
    "hey",
    "Hey racer, what's in your mind today",
    ],[
    "how are u",
    "Iam too good,\n1. Engine oil checking - good,\n2. Coolant - good\nAll good 👍",
],
[
    "who are u", 
    "Iam Autocot - recob's ek lota chatbot. I can help u in solving your problems regarding your vehicles"
],
  [  "how u are doing",
    "Iam too good,\n1. Engine oil checking - good,\n2. Coolant - good\nAll good 👍",
],[
    "what are u doing",
    "Nothing just waiting for carguys and bikers",
],[
    "Book an appointment",
    "need the database",
],[
    "suggest me a car",
    "need the programmer",
],[
    "new car",
    "turn to suggest",
],
[
    "car for family",
    "need the programmer",
],
[
    "give me the specifications",
    "need the programmer"
],
[
    "specification about car",
    "need the programmer"
],
[
    "please give me the specifications",

    "need the programmer"
],
[
    "engine oil",
    "Type engine oil changing duration for cars/bikes to know about when u should change the engine oil of your vehicles."
],
[
    "engine oil changing duration",
    "1. For four wheelers the engine oil chaging duration is around 5000-10000 kilometers 2. For two wheelers the engine oil chaging duration it's around 3000-5000 kilometers"
],
[
    "engine oil changing duration for cars", 
    "For four wheelers the engine oil chaging duration is around 5000-10000 kilometers"
],
[
    "engine oil chaning duration for bike",
    "For two wheelers the engine oil changing duration is around 3000-5000 kilometers"
],
[
    "brake pads duration",
    "For four wheelers the brake pads changing duration is around 40000-100000 \n"
    "For two wheelers the brake pads changing duration is around 12-15kms"
],
[
    "engine overheating issue",
    "Engine overheating can happen due to several mechanical or environmental issues. Here's a breakdown of the main causes:\n"
    "Mechanical/Component-Related Causes:"
"Low Coolant Level: Coolant absorbs engine heat. Low levels can't circulate and cool the engine effectively."

"Coolant Leak: Leaks in radiator, hoses, water pump, or head gasket reduce coolant volume."

"Malfunctioning Thermostat: If the thermostat gets stuck closed, it blocks coolant flow to the radiator."

"Faulty Radiator: A clogged or leaking radiator can't dissipate heat properly."

"Broken Water Pump: The water pump circulates coolant. If it fails, coolant can't move through the system."

"Radiator Fan Failure: Without fan operation,  there's no airflow to cool the radiator, especially in traffic."

"Blocked or Collapsed Hoses: Prevent coolant flow, leading to inefficient cooling."

"Blown Head Gasket: Can allow combustion gases into the cooling system, causing pressure build-up and overheating."

"Low Engine Oil: Oil also cools engine parts by reducing friction. Low oil = higher internal heat."

"Environmental or External Causes like:" 

"Overloading/Towing: Heavier loads make the engine work harder, generating more heat."

"Blocked Grille or Radiator: Obstructions (like leaves or dirt) reduce airflow to the radiator."

"Poor Maintenance: Not flushing the coolant system or using incorrect coolant can reduce cooling efficiency."
],
[
    "how to change the wiper washer fluid",
    "To change the wiper washer fluid follow these steps "
    "1. Open the hood\n2. Locate the washer fluid reservoir (haivng white/blue plastic cover)\n3. Open it\n4. Drain the existing fluid\n5. Pour the new wiper fluid\n6. Close the cap\n7. Close the hood\nAnd you are all set"
]
,
[
    "How to jumpstart the car",
"1. Park both cars close together without touching."

"2. Turn off both cars and remove the keys."

"3. Open the hoods of both vehicles."

"4. Attach the red jumper cable to the + terminal of the dead battery."

"5. Attach the other end of the red jumper cable to the + terminal of the good battery."

"6. Attach the black jumper cable to the terminal of the good battery."

"7. Attach the other end of the black cable to an unpainted metal surface on the dead car (not the battery)."

"8. Start the car with the good battery and let it run for 2-3 minutes."

"9. Start the car with the dead battery."

"10. If it starts, let both cars run for a few minutes."

"11. Remove the jumper cables in this exact reverse order:"

"Black from dead car (engine metal)"

"Black from good battery"

"Red from good battery"

"Red from dead battery"

"12. Close both hoods."

"13. Keep the jumpstarted car running for 15–30 minutes."],
[
    
    "How do i jumpstart the car",
"1. Park both cars close together without touching."

"2. Turn off both cars and remove the keys."

"3. Open the hoods of both vehicles."

"4. Attach the red jumper cable to the + terminal of the dead battery."

"5. Attach the other end of the red jumper cable to the + terminal of the good battery."

"6. Attach the black jumper cable to the terminal of the good battery."

"7. Attach the other end of the black cable to an unpainted metal surface on the dead car (not the battery)."

"8. Start the car with the good battery and let it run for 2-3 minutes."

"9. Start the car with the dead battery."

"10. If it starts, let both cars run for a few minutes."

"11. Remove the jumper cables in this exact reverse order:"

"Black from dead car (engine metal)"

"Black from good battery"

"Red from good battery"

"Red from dead battery"

"12. Close both hoods."

"13. Keep the jumpstarted car running for 15–30 minutes."
],
[
    
    "to jumpstart the car",
"1. Park both cars close together without touching."

"2. Turn off both cars and remove the keys."

"3. Open the hoods of both vehicles."

"4. Attach the red jumper cable to the + terminal of the dead battery."

"5. Attach the other end of the red jumper cable to the + terminal of the good battery."

"6. Attach the black jumper cable to the terminal of the good battery."

"7. Attach the other end of the black cable to an unpainted metal surface on the dead car (not the battery)."

"8. Start the car with the good battery and let it run for 2-3 minutes."

"9. Start the car with the dead battery."

"10. If it starts, let both cars run for a few minutes."

"11. Remove the jumper cables in this exact reverse order:"

"Black from dead car (engine metal)"

"Black from good battery"

"Red from good battery"

"Red from dead battery"

"12. Close both hoods."

"13. Keep the jumpstarted car running for 15–30 minutes."
],
[
    "engine light",
    "What do u want to know?\n1. The reason why the engine light pops up\n2. The solution for the engine light popped up",

],
[
    "why engine light occurs",
"1. Loose or Faulty Fuel Cap"

"2. Oxygen (O2) Sensor Failure"

"3. Mass Air Flow (MAF) Sensor Fault"

"4. Catalytic Converter Issues"

"5. Faulty Spark Plugs or Ignition Coils"

"6. Faulty EGR Valve"

"7. Bad Battery or Charging System"

"8. Vacuum Leak"

"9. Fuel Injector Issues"

"10. Transmission Problems"

"11. Emissions Control System Fault"

"12. Faulty Thermostat"

"13. EVAP System Leak (fuel vapor system)"

"14. Dirty or Clogged Air Filter"

],
[
    "reasons of engine light occuring",
"1. Loose or Faulty Fuel Cap"

"2. Oxygen (O2) Sensor Failure"

"3. Mass Air Flow (MAF) Sensor Fault"

"4. Catalytic Converter Issues"

"5. Faulty Spark Plugs or Ignition Coils"

"6. Faulty EGR Valve"

"7. Bad Battery or Charging System"

"8. Vacuum Leak"

"9. Fuel Injector Issues"

"10. Transmission Problems"

"11. Emissions Control System Fault"

"12. Faulty Thermostat"

"13. EVAP System Leak (fuel vapor system)"

"14. Dirty or Clogged Air Filter"

],
[
    "engine light solution",

"1. Check fuel cap – Ensure it's tight and not damaged."

"2. Restart the engine – Sometimes resets minor temporary faults."
"3. Use an OBD-II scanner – Plug it into the port (usually under the dashboard) to read the error code."
"4. Identify the fault code (e.g., P0171, P0420) – Match it with the component."

"5.Inspect sensors – Clean or replace faulty: 1. O2 sensor 2. MAF sensor 3. Coolant or crankshaft sensor"

"6. Check spark plugs and coils – Replace if worn or misfiring."

"7. Inspect the catalytic converter – Repair or replace if clogged or damaged."

"8. Check air filter and vacuum lines – Clean or replace if dirty or leaking."
"9. Inspect EVAP system – Fix leaks or faulty purge valves."

"10. Clear the code using scanner – After fixing the issue."

"11. Drive the vehicle – Observe if the light stays off."

"12. If light returns – Visit a mechanic for a deeper diagnostic."
],
["how do i solve the engine light issue",
    
"1. Check fuel cap – Ensure it's tight and not damaged."

"2. Restart the engine – Sometimes resets minor temporary faults."
"3. Use an OBD-II scanner – Plug it into the port (usually under the dashboard) to read the error code."
"4. Identify the fault code (e.g., P0171, P0420) – Match it with the component."

"5.Inspect sensors – Clean or replace faulty: 1. O2 sensor 2. MAF sensor 3. Coolant or crankshaft sensor"

"6. Check spark plugs and coils – Replace if worn or misfiring."

"7. Inspect the catalytic converter – Repair or replace if clogged or damaged."

"8. Check air filter and vacuum lines – Clean or replace if dirty or leaking."
"9. Inspect EVAP system – Fix leaks or faulty purge valves."

"10. Clear the code using scanner – After fixing the issue."

"11. Drive the vehicle – Observe if the light stays off."

"12. If light returns – Visit a mechanic for a deeper diagnostic." 
],
[
    "how can i get rid off the engine light popping in my vehicle",
    
"1. Check fuel cap – Ensure it's tight and not damaged."

"2. Restart the engine – Sometimes resets minor temporary faults."
"3. Use an OBD-II scanner – Plug it into the port (usually under the dashboard) to read the error code."
"4. Identify the fault code (e.g., P0171, P0420) – Match it with the component."

"5.Inspect sensors – Clean or replace faulty: 1. O2 sensor 2. MAF sensor 3. Coolant or crankshaft sensor"

"6. Check spark plugs and coils – Replace if worn or misfiring."

"7. Inspect the catalytic converter – Repair or replace if clogged or damaged."

"8. Check air filter and vacuum lines – Clean or replace if dirty or leaking."
"9. Inspect EVAP system – Fix leaks or faulty purge valves."

"10. Clear the code using scanner – After fixing the issue."

"11. Drive the vehicle – Observe if the light stays off."

"12. If light returns – Visit a mechanic for a deeper diagnostic."
],
[
    "washing tips",
    "You should wash your cars and bikes atleast once in a week to ensure it is more cleaner\n"
    "1. Use the spray or bucket full with water\n"
    "2. Apply the foam on your car\n"
    "3. Take a microfibre cloth and spread the foam everywhere and rub each of the area\n"
    "4. Wash it with the spray gently\n"
    "5. Clean the water on the car with the microfibre cloth"
    "If want the car wash by us please book the service"
],
[
    "how do i wash my car",
    "You should wash your cars and bikes atleast once in a week to ensure it is more cleaner\n"
    "1. Use the spray or bucket full with water\n"
    "2. Apply the foam on your car\n"
    "3. Take a microfibre cloth and spread the foam everywhere and rub each of the area\n"
    "4. Wash it with the spray gently\n"
    "5. Clean the water on the car with the microfibre cloth"
    "If want the car wash by us please book the service"
],
[
    "when should i wash my car",
    
    "You should wash your cars and bikes atleast once in a week to ensure it is more cleaner\n"

    "If want the car wash by us please book the service"
],
[
    "does more washing leads to scratches ?",
    "nope until and unless the cloth is microfibre"
],
[
    "washing leads to scracthes on car",
    "nope until and unless the cloth is microfibre"
],
[
    "tell me about the service duration",

"Let me give you the service duration for all of our brands\n"
"1. BMW	- Every 10,000 km or 12 months\n"
"2. Aston Martin - Every 16,000 km or 12 months\n"
"3. Ferrari	Every 12,000 – 15,000 km or annually\n"
"4. KTM - Every 5,000 – 7,500 km or 6 months\n"
"5. Kawasaki - Every 6,000 km or 6 months\n"
"6. Mercedes-Benz -	Every 15,000 km or 12 months\n"
"7. Audi - Every 15,000 km or 12 months\n"
"8. Lexus - Every 10,000 km or 12 months\n"
"9. Porsche - Every 15,000 – 20,000 km or 12 months\n"
"10. Lamborghini - Every 15,000 km or 12 months\n"

],
[
    "service durations",
    "Let me give you the service duration for all of our brands\n"
"1. BMW	- Every 10,000 km or 12 months\n"
"2. Aston Martin - Every 16,000 km or 12 months\n"
"3. Ferrari	Every 12,000 – 15,000 km or annually\n"
"4. KTM - Every 5,000 – 7,500 km or 6 months\n"
"5. Kawasaki - Every 6,000 km or 6 months\n"
"6. Mercedes-Benz -	Every 15,000 km or 12 months\n"
"7. Audi - Every 15,000 km or 12 months\n"
"8. Lexus - Every 10,000 km or 12 months\n"
"9. Porsche - Every 15,000 – 20,000 km or 12 months\n"
"10. Lamborghini - Every 15,000 km or 12 months\n"

],

[
 "what are the service durations for various vehicles",
"Let me give you the service duration for all of our brands\n"
"1. BMW	- Every 10,000 km or 12 months\n"
"2. Aston Martin - Every 16,000 km or 12 months\n"
"3. Ferrari	Every 12,000 – 15,000 km or annually\n"
"4. KTM - Every 5,000 – 7,500 km or 6 months\n"
"5. Kawasaki - Every 6,000 km or 6 months\n"
"6. Mercedes-Benz -	Every 15,000 km or 12 months\n"
"7. Audi - Every 15,000 km or 12 months\n"
"8. Lexus - Every 10,000 km or 12 months\n"
"9. Porsche - Every 15,000 – 20,000 km or 12 months\n"
"10. Lamborghini - Every 15,000 km or 12 months\n"
],
[
    "okay",
    "Hmm.. anything else??"
],
[
    "ok",
    "Hmm.. anything else??"
]
]
trainer=  ListTrainer(autocot)

for trainingdata in training_data : 
    trainer.train(trainingdata)

print("Training the chatbot is completed")


class forwarding : 
    var = 'none'
    carname = 'none'
    def receving(self, variable) :
        self.var = variable
    def sending(self) : 
        return self.var
    def receivecarname(self, carname) : 
        self.carname = carname
    def sendingcarname(self) : 
        return self.carname
    
fors = forwarding()

class exchangingcolorvalueofbooking : 

    colorname = None
    price = None
    arrayofreturning = []
    def colorreceive(self, color, price) : 
        self.colorname = color
        self.price = price
        self.arrayofreturning.append(color)
        self.arrayofreturning.append(price)
        print(self.arrayofreturning)
    def colorforward(self) : 
        return self.arrayofreturning
    def removearray(self) : 
        self.arrayofreturning.clear()
objforbook = exchangingcolorvalueofbooking()

class Dynamicdetailsofwebpage :
    def __init__(self) :
        pass

    def retrievinghomepageinformation(self, sqlquery) :
        mycursor.execute(query = sqlquery)

        datafromdatabase = mycursor.fetchall()
        element00 = datafromdatabase[0][0]
        element01 = datafromdatabase[0][1]
        element10 = datafromdatabase[1][0]
        element11 = datafromdatabase[1][1]
        element20 = datafromdatabase[2][0]
        element21 = datafromdatabase[2][1]
        element30 = datafromdatabase[3][0]
        element31 = datafromdatabase[3][1]

        return  element00, element01, element10, element11, element20, element21,  element30, element31

    def bookingcontents(self, request, sqlquery):
        mycursor.execute(query=sqlquery)
        result =  mycursor.fetchall()
        vehiclearray = []

        for index,item in enumerate(result) : 
            vehiclearray.append(item[0])
        return vehiclearray

def homepage(request) : 

    dynamiccontents = Dynamicdetailsofwebpage()
    sqlquery = 'SELECT * FROM dynamiccontents'
    element00, element01,  element10, element11, element20, element21, element30, element31= dynamiccontents.retrievinghomepageinformation(sqlquery)
    extraparams = { 
        'vehicle1name' : element00,
        'vehicle1description' : element01,
        'vehicle2name' : element10,
        'vehicle2description' : element11,
        'vehicle3name' : element20,
        'vehicle3description' : element21,
        'vehicle4name' : element30,
        'vehicle4description' : element31,
    }
    return render(request, 'homepage.html', extraparams)

def test_db_connection(request):
    try:
        connection = sql.connect(
            host="localhost",
            user="root",
            password="Rehanmysql.com",
            database="advancedmotogeniuswebsitedb",
            port= 3306
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        return HttpResponse("Database connection successful!")
    except Exception as e:
        return HttpResponse(f"Database connection failed !")
def showroom(request) : 

    return render(request, 'showroom.html')

def sustainabilitypage(request) : 

    return render(request, 'learnmore.html')

def loginuser(request) : 

    if request.user.is_authenticated :
       
       username = request.user.username
       query = "SELECT * from users where username= %s"
       mycursor.execute(query, (username,))
       result = mycursor.fetchall()

       extraparams = {
            "username" : username,
            "userage" : result[0][2],
            "useremail" : result[0][4],
            "userphonenumber" : result[0][5],
            "userfullname" : result[0][6]
        }
       return redirect("/dashboard")
    
    return render(request, 'loginpage.html')

    
def registration(request) : 

    return render(request, 'registerpage.html')

def registrationresult(request) : 

    fullname = request.GET.get('userfullname', 'invalidinput')
    useremail = request.GET.get('useremail', 'invalidinput')
    userage = request.GET.get('userage', 'invalidinput')
    phonenumber = request.GET.get('userphonenumber', 'invalidinput')
    userpasswordinput = request.GET.get('userpassword', 'invalidinput')
    usernameinput = request.GET.get('username', 'invalidinput')
    password = request.GET.get('userpassword', 'invalidinput')
    
    userdetails = User.objects.create_user(username= usernameinput, password=userpasswordinput)
    userdetails.email = useremail

    sqlquery0 = "insert into users(username, age, userpassword, emailid, phonenumber, fullname) values(%s, %s, %s, %s, %s, %s);"
    mycursor.execute(sqlquery0,[usernameinput, userage, userpasswordinput, useremail, phonenumber,fullname])
    sqlconnection.commit()
    print("successfully inserted the user")
    sqlquery = f"SELECT emailid FROM users where username = {usernameinput}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    receiversemail = useremail
    msg = "You have successfully registered to the RECOB. We are hoping that you will be having a lot of new experiences and a good relation with your machine"
    server.starttls()       
    server.login(senderemail, senderpassword)
    server.sendmail(senderemail, receiversemail, msg)
    print("success")
    return render(request, 'registrationresult.html')

def userdashboard(request) : 

    if request.user.is_authenticated :
        
        username = request.user.username
        if request.user.is_superuser : 
            superuser = True
            query = "SELECT * from users where username= %s"
            mycursor.execute(query, (username,))
            result = mycursor.fetchall()

            query2 = "SELECT * from userssparepartsorders where username = %s"
            mycursor.execute(query2,(username,))
            result2 = mycursor.fetchall()

            orderresults = []
            for row in result2 : 
                orderresults.append({
                        "orderid" : row[0],
                        "partname" : row[2],
                        "partprice" : row[3], 
                        "quantity" : row[4],
                    }) 
            query3 = "SELECT * FROM userssparepartsorders"
            mycursor.execute(query3)
            result3 = mycursor.fetchall()

            alluserorders = []
            for row in result3 : 
                alluserorders.append({
                        "orderid" : row[0],
                        "username" : row[1],
                        "partname" : row[2],
                        "partprice" : row[3],
                        "quantity" : row[4] 
                    })
            vehiclesnames = result[0][7]
            vehiclesnamestolist = json.loads(vehiclesnames)
            vehiclesfinalnames = ",  ".join(vehiclesnamestolist)

            extraparams = {
                        "username" : username,
                        "userage" : result[0][2],
                        "useremail" : result[0][4],
                        "userphonenumber" : result[0][5],
                        "userfullname" : result[0][6],
                        "vehiclenames" : vehiclesfinalnames,
                        "orderdetails" : orderresults,
                        "alluserorderdetails" : alluserorders,
                        "superuser" : superuser
                    }
            return render(request, 'userdashboard.html', extraparams)
        else :
            query = "SELECT * from users where username= %s"
            mycursor.execute(query, (username,))
            result = mycursor.fetchall()

            query2 = "SELECT * from userssparepartsorders where username = %s"
            mycursor.execute(query2,(username,))
            result2 = mycursor.fetchall()

            orderresults = []
            for row in result2 : 
                orderresults.append({
                            "orderid" : row[0],
                            "partname" : row[2],
                            "partprice" : row[3], 
                            "quantity" : row[4],
                        }) 
            extraparams = {
                            "username" : username,
                            "userage" : result[0][2],
                            "useremail" : result[0][4],
                            "userphonenumber" : result[0][5],
                            "userfullname" : result[0][6],
                            "orderdetails" : orderresults,
                        }
            return render(request, 'userdashboard.html', extraparams)
        
    else : 
            
        username = request.POST.get("username")
        userpassword = request.POST.get('password', "invalidinput")

        user = authenticate(username = username, password = userpassword)
        print(user)

        if user is not None: 
            login(request,user) 
            if user.is_superuser : 
                superuser = True
                query = "SELECT * from users where username= %s"
                mycursor.execute(query, (username,))
                result = mycursor.fetchall()

                query2 = "SELECT * from userssparepartsorders where username = %s"
                mycursor.execute(query2,(username,))
                result2 = mycursor.fetchall()

                orderresults = []
                for row in result2 : 
                    orderresults.append({
                        "orderid" : row[0],
                        "partname" : row[2],
                        "partprice" : row[3], 
                        "quantity" : row[4],
                    }) 
                query3 = "SELECT * FROM userssparepartsorders"
                mycursor.execute(query3)
                result3 = mycursor.fetchall()

                alluserorders = []
                for row in result3 : 
                    alluserorders.append({
                        "orderid" : row[0],
                        "username" : row[1],
                        "partname" : row[2],
                        "partprice" : row[3],
                        "quantity" : row[4] 
                    })
                
                extraparams = {
                        "username" : username,
                        "userage" : result[0][2],
                        "useremail" : result[0][4],
                        "userphonenumber" : result[0][5],
                        "userfullname" : result[0][6],
                        "orderdetails" : orderresults,
                        "alluserorderdetails" : alluserorders,
                        "superuser" : superuser
                    }
                return render(request, 'userdashboard.html', extraparams)
            else :
                query = "SELECT * from users where username= %s"
                mycursor.execute(query, (username,))
                result = mycursor.fetchall()

                query2 = "SELECT * from userssparepartsorders where username = %s"
                mycursor.execute(query2,(username,))
                result2 = mycursor.fetchall()

                orderresults = []
                for row in result2 : 
                    orderresults.append({
                        "orderid" : row[0],
                        "partname" : row[2],
                        "partprice" : row[3], 
                        "quantity" : row[4],
                    }) 
                extraparams = {
                        "username" : username,
                        "userage" : result[0][2],
                        "useremail" : result[0][4],
                        "userphonenumber" : result[0][5],
                        "userfullname" : result[0][6],
                        "orderdetails" : orderresults,
                    }
                return render(request, 'userdashboard.html', extraparams)
            
        else : 
            
            return redirect('/login')
def booking(request) : 

    if request.user.is_authenticated : 

        print(request.user) 
        actualuser = request.user.username
        fors.receving(actualuser)
        
        button = request.GET.get('buttons', 'invalidbutton')
        
        dynamiccontent = Dynamicdetailsofwebpage()
        sqlquery = "SELECT fullvehiclename, price FROM VehicleDetails where urlcarname = %s"
        mycursor.execute(sqlquery, (button))
        result = mycursor.fetchall()
        fors.receivecarname(result[0][0])

        colorvalue = int(request.GET.get('color', 'invalidcoloroption'))
        colorname = None
        if colorvalue == 1 : 
            imgpathtype = "basicimgpath1"
            colorname = "Red"
        elif colorvalue == 2 : 
            imgpathtype = "basicimgpath2"
            colorname = "Black"
        elif colorvalue == 3 : 
            imgpathtype = "basicimgpath3"
            colorname = "White"
        elif colorvalue == 4 : 
            imgpathtype = "basicimgpath4"
            colorname = "Yellow"

        print(imgpathtype)
        query2 = f"SELECT {imgpathtype} FROM vehicleDetails WHERE urlcarname = %s"
        mycursor.execute(query2,(button,))
        result2 = mycursor.fetchall()
        imgpath = result2[0][0]
        print(imgpath)
        extraparams = {
            "name" : result[0][0],
            "price" : result[0][1],
            "imgpath" : imgpath,
        }
        objforbook.colorreceive(colorname, extraparams["price"])
        return render(request, 'booking.html', extraparams)
    else : 
        return redirect("/login")
    
def bookingsuccess(request) : 


    actualuser = fors.sending() 
    print(actualuser)
    sqlquery = "SELECT emailid from users where username = %s"
    mycursor.execute(sqlquery,(actualuser,))
    result = mycursor.fetchall()
    carname = fors.sendingcarname();

    datetimeofbooking = datetime.datetime.now()
    query2 = """INSERT into uservehiclesbooking values (%s,%s,%s, 0);"""
    mycursor.execute(query2, (actualuser, carname, datetimeofbooking))
    sqlconnection.commit()
    print("booked successfully and inserted in uservehiclesbooking")
    receiversemail = result[0][0]
    colorname,price = objforbook.colorforward()
    objforbook.removearray()
    msg = f"Booking is done and following are the details of the vehicle that you have booked\n1. Name : {carname}\n2. Price : {price}\n3. Color : {colorname}"
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.login(senderemail, senderpassword)
    email.sendmail(senderemail, receiversemail, msg.encode("utf-8"))

    query5 = "UPDATE VehicleDetails set stock = stock-1 where fullvehiclename = %s"
    mycursor.execute(query5, (carname,))
    sqlconnection.commit()

    """ query6 = "SELECT vehicles from users where username = %s "
    mycursor.execute(query6, ('Adina@1910'))
    result1 = mycursor.fetchall() 
    print(result1[0][0])   
    vehiclesdetailes = json.loads(result[0][0])
    print(vehiclesdetailes)
    vehiclesdetailes.append(carname)
    print(vehiclesdetailes) """
    return redirect('/showroom')


def loggingout(request) :

    logout(request)

    return redirect('/homepage')

def cardetaildynamicone(request)  :

    carnamefromurl = request.GET.get("carname")  
    query = "SELECT * FROM VehicleDetails where urlcarname = %s"
    mycursor.execute(query, (carnamefromurl,))
    result = mycursor.fetchall()
    extraparams ={
        "fullvehiclename" : result[0][3],
        "vehicledescription" : result[0][2],
        "engine" : result[0][5],
        "hp" : result[0][6],
        "speed" : result[0][7],
        "mph" : result[0][8],
        "transmission" : result[0][9],
        "fueleconomy" : result[0][10],
        "price" : result[0][11],
        "urlvehiclename" : carnamefromurl,
        "img1" : result[0][14],
        "img2" : result[0][15],
        "img3" : result[0][16],
        "img4" : result[0][17]
    } 
    print(extraparams["img4"])
    return render(request,  "vehicledetailspage.html", extraparams)

def virtualassistance(request) : 

    return render(request, 'ai.html')

def sparepartsfinder(request) : 

    query = "SELECT * FROM spareparts"
    mycursor.execute(query)
    result = mycursor.fetchall()

    extraparams = {
    "brand1part1name" : result[0][0],
    "brand1part1brand" : result[0][1],
    "brand1part1price" : result[0][2],
    "brand1part1numberofparts" : result[0][3],
    "brand1part1urlforimg" : result[0][4],
    "brand1part1actualpartname" : result[0][5],

    "brand1part2name" : result[1][0],
    "brand1part2brand" : result[1][1],
    "brand1part2price" : result[1][2],
    "brand1part2numberofparts" : result[1][3],
    "brand1part2urlforimg" : result[1][4],
    "brand1part2actualpartname" : result[1][5],

    "brand1part3name" : result[2][0],
    "brand1part3brand" : result[2][1],
    "brand1part3price" : result[2][2],
    "brand1part3numberofparts" : result[2][3],
    "brand1part3urlforimg" : result[2][4],
    "brand1part3actualpartname" : result[2][5],

    "brand1part4name" : result[3][0],
    "brand1part4brand" : result[3][1],
    "brand1part4price" : result[3][2],
    "brand1part4numberofparts" : result[3][3],
    "brand1part4urlforimg" : result[3][4],
    "brand1part4actualpartname" : result[3][5],

    "brand2part1name" : result[4][0],
    "brand2part1brand" : result[4][1],
    "brand2part1price" : result[4][2],
    "brand2part1numberofparts" : result[4][3],
    "brand2part1urlforimg" : result[4][4],
    "brand2part1actualpartname" : result[4][5],

    "brand2part2name" : result[5][0],
    "brand2part2brand" : result[5][1],
    "brand2part2price" : result[5][2],
    "brand2part2numberofparts" : result[5][3],
    "brand2part2urlforimg" : result[5][4],
    "brand2part2actualpartname" : result[5][5],

    "brand2part3name" : result[6][0],
    "brand2part3brand" : result[6][1],
    "brand2part3price" : result[6][2],
    "brand2part3numberofparts" : result[6][3],
    "brand2part3urlforimg" : result[6][4],
    "brand2part3actualpartname" : result[6][5],

    "brand2part4name" : result[7][0],
    "brand2part4brand" : result[7][1],
    "brand2part4price" : result[7][2],
    "brand2part4numberofparts" : result[7][3],
    "brand2part4urlforimg" : result[7][4],
    "brand2part4actualpartname" : result[7][5],

    "brand3part1name" : result[8][0],
    "brand3part1brand" : result[8][1],
    "brand3part1price" : result[8][2],
    "brand3part1numberofparts" : result[8][3],
    "brand3part1urlforimg" : result[8][4],
    "brand3part1actualpartname" : result[8][5],

    "brand3part2name" : result[9][0],
    "brand3part2brand" : result[9][1],
    "brand3part2price" : result[9][2],
    "brand3part2numberofparts" : result[9][3],
    "brand3part2urlforimg" : result[9][4],
    "brand3part2actualpartname" : result[9][5],

    "brand3part3name" : result[10][0],
    "brand3part3brand" : result[10][1],
    "brand3part3price" : result[10][2],
    "brand3part3numberofparts" : result[10][3],
    "brand3part3urlforimg" : result[10][4],
    "brand3part3actualpartname" : result[10][5],

    "brand3part4name" : result[11][0],
    "brand3part4brand" : result[11][1],
    "brand3part4price" : result[11][2],
    "brand3part4numberofparts" : result[11][3],
    "brand3part4urlforimg" : result[11][4],
    "brand3part4actualpartname" : result[11][5],

    "brand4part1name" : result[12][0],
    "brand4part1brand" : result[12][1],
    "brand4part1price" : result[12][2],
    "brand4part1numberofparts" : result[12][3],
    "brand4part1urlforimg" : result[12][4],
    "brand4part1actualpartname" : result[12][5],

    "brand4part2name" : result[13][0],
    "brand4part2brand" : result[13][1],
    "brand4part2price" : result[13][2],
    "brand4part2numberofparts" : result[13][3],
    "brand4part2urlforimg" : result[13][4],
    "brand4part2actualpartname" : result[13][5],

    "brand4part3name" : result[14][0],
    "brand4part3brand" : result[14][1],
    "brand4part3price" : result[14][2],
    "brand4part3numberofparts" : result[14][3],
    "brand4part3urlforimg" : result[14][4],
    "brand4part3actualpartname" : result[14][5],

    "brand4part4name" : result[15][0],
    "brand4part4brand" : result[15][1],
    "brand4part4price" : result[15][2],
    "brand4part4numberofparts" : result[15][3],
    "brand4part4urlforimg" : result[15][4],
    "brand4part4actualpartname" : result[15][5],
    
    "brand5part1name" : result[16][0],
    "brand5part1brand" : result[16][1],
    "brand5part1price" : result[16][2],
    "brand5part1numberofparts" : result[16][3],
    "brand5part1urlforimg" : result[16][4],
    "brand5part1actualpartname" : result[16][5],

    "brand5part2name" : result[17][0],
    "brand5part2brand" : result[17][1],
    "brand5part2price" : result[17][2],
    "brand5part2numberofparts" : result[17][3],
    "brand5part2urlforimg" : result[17][4],
    "brand5part2actualpartname" : result[17][5],
    
    "brand5part3name" : result[18][0],
    "brand5part3brand" : result[18][1],
    "brand5part3price" : result[18][2],
    "brand5part3numberofparts" : result[18][3],
    "brand5part3urlforimg" : result[18][4],
    "brand5part3actualpartname" : result[18][5],

    "brand5part4name" : result[19][0],
    "brand5part4brand" : result[19][1],
    "brand5part4price" : result[19][2],
    "brand5part4numberofparts" : result[19][3],
    "brand5part4urlforimg" : result[19][4],
    "brand5part4actualpartname" : result[19][5],


    "brand6part1name" : result[20][0],
    "brand6part1brand" : result[20][1],
    "brand6part1price" : result[20][2],
    "brand6part1numberofparts" : result[20][3],
    "brand6part1urlforimg" : result[20][4],
    "brand6part1actualpartname" : result[20][5],

    "brand6part2name" : result[21][0],
    "brand6part2brand" : result[21][1],
    "brand6part2price" : result[21][2],
    "brand6part2numberofparts" : result[21][3],
    "brand6part2urlforimg" : result[21][4],
    "brand6part2actualpartname" : result[21][5],

    "brand6part3name" : result[22][0],
    "brand6part3brand" : result[22][1],
    "brand6part3price" : result[22][2],
    "brand6part3numberofparts" : result[22][3],
    "brand6part3urlforimg" : result[22][4],
    "brand6part3actualpartname" : result[22][5],

    "brand6part4name" : result[23][0],
    "brand6part4brand" : result[23][1],
    "brand6part4price" : result[23][2],
    "brand6part4numberofparts" : result[23][3],
    "brand6part4urlforimg" : result[23][4],
    "brand6part4actualpartname" : result[23][5],

    "brand7part1name" : result[24][0],
    "brand7part1brand" : result[24][1],
    "brand7part1price" : result[24][2],
    "brand7part1numberofparts" : result[24][3],
    "brand7part1urlforimg" : result[24][4],
    "brand7part1actualpartname" : result[24][5],

    "brand7part2name" : result[25][0],
    "brand7part2brand" : result[25][1],
    "brand7part2price" : result[25][2],
    "brand7part2numberofparts" : result[25][3],
    "brand7part2urlforimg" : result[25][4],
    "brand7part2actualpartname" : result[25][5],

    "brand7part3name" : result[26][0],
    "brand7part3brand" : result[26][1],
    "brand7part3price" : result[26][2],
    "brand7part3numberofparts" : result[26][3],
    "brand7part3urlforimg" : result[26][4],
    "brand7part3actualpartname" : result[26][5],


    "brand7part4name" : result[27][0],
    "brand7part4brand" : result[27][1],
    "brand7part4price" : result[27][2],
    "brand7part4numberofparts" : result[27][3],
    "brand7part4urlforimg" : result[27][4],
    "brand7part4actualpartname" : result[27][5],

    "brand8part1name" : result[28][0],
    "brand8part1brand" : result[28][1],
    "brand8part1price" : result[28][2],
    "brand8part1numberofparts" : result[28][3],
    "brand8part1urlforimg" : result[28][4],
    "brand8part1actualpartname" : result[28][5],

    "brand8part2name" : result[29][0],
    "brand8part2brand" : result[29][1],
    "brand8part2price" : result[29][2],
    "brand8part2numberofparts" : result[29][3],
    "brand8part2urlforimg" : result[29][4],
    "brand8part2actualpartname" : result[29][5],

    "brand8part3name" : result[30][0],
    "brand8part3brand" : result[30][1],
    "brand8part3price" : result[30][2],
    "brand8part3numberofparts" : result[30][3],
    "brand8part3urlforimg" : result[30][4],
    "brand8part3actualpartname" : result[30][5],

    "brand8part4name" : result[31][0],
    "brand8part4brand" : result[31][1],
    "brand8part4price" : result[31][2],
    "brand8part4numberofparts" : result[31][3],
    "brand8part4urlforimg" : result[31][4],
    "brand8part4actualpartname" : result[31][5]

    }
    return render(request, 'spareparts.html', extraparams)

def spfinderordering(request) : 
    if request.user.is_authenticated : 
        partname = request.GET.get("partname")
        query = "SELECT * FROM spareparts where partname = %s"
        mycursor.execute(query,(partname))
        result = mycursor.fetchall()
        extraparams = {
            "partname" : result[0][0],
            "partprice" : result[0][2],
            "partstocks" : result[0][3],
            "partnameimgurl" : result[0][4],
            "actualpartname" : result[0][5] 
        }
        return render(request, "sparepartsorder.html", extraparams)
    else : 
        return redirect("/login")
def ordersuccess(request) : 

    username = request.user.username
    randomnumber= random.randint(0, 100000)
    orderid = f"{username}#{randomnumber}"
    ordername = request.GET.get("partname")
    orderprice = request.GET.get("partprice")
    quantity = request.GET.get("quantity")

    if request.user.is_authenticated : 
        query = """INSERT INTO userssparepartsorders values(%s,%s,%s,%s,%s)"""
        mycursor.execute(query, (orderid, username, ordername,orderprice,quantity,))
        connection.commit()
        query = """UPDATE spareparts set stockpieces = stockpieces-1 where partname = %s"""
        mycursor.execute(query, (ordername,))
        sqlconnection.commit()
        
        query = "SELECT emailid from users where username = %s"
        mycursor.execute(query, (username,))
        result= mycursor.fetchall()
        receiversemail = result[0][0]
        server = smtplib.SMTP("smtp.gmail.com", 587)
        msg = f"You have placed an order for \n1. Partname : {ordername}\n2. Price : {orderprice}\n3. Quantity : {quantity}\n4. Orderid (for tracking) : {orderid}"
        server.starttls()
        server.login(senderemail, senderpassword)
        server.sendmail(senderemail, receiversemail, msg)
        print("email sent successfully")
        return redirect("/")
    else: 
        return redirect("")

def chatbot(request) : 

    return render(request, "ai.html")

def chatbotresponse(request) : 
    
    usermsg = request.GET.get("message")
    print("Starting the chat")
    while True :
         
        if request.session.get("budgetwaitingsession") : 
            carnames = []
            budget = usermsg
            query = """SELECT Name from vehiclesinfo where Price >= 0 AND Price <= %s"""
            mycursor.execute(query, (budget,))
            result = mycursor.fetchall()
                        
            for item in range(0, len(result)) : 
                for item2 in range(0, len(result[item])) : 
                    carnames.append(result[item][item2])
            
            request.session["budgetwaitingsession"] = False
            
            if len(carnames) > 0 : 
                replytext = f"Here are the car names under your budget : {carnames}"
            else : 
                replytext = "No cars found under your budget. You need to increase your budget"
            
            return JsonResponse({"reply" : replytext})

        if request.session.get("specificationbasedsession") : 
            carname = usermsg
            query =  "SELECT Engine, HP,Speed,Acceleration,Transmission,FuelEconomy from VehicleDetails where fullvehiclename = %s"
            mycursor.execute(query, (carname,))
            result = mycursor.fetchall()
            specs = []
            for item in range(0, len(result[0])) : 
                specs.append(result[0][item])

            if len(specs) > 0 : 
                replytext = f"Here are the specifications for {carname} : \n {specs}"
            else : 
                replytext =  "No such vehicle name found !!"
            
            request.session["specificationbasedsession"] = False
            return JsonResponse({"reply" : replytext})
        if request.session.get("appointmentbasedsession") : 
            date = usermsg
            username = request.user.username
            print(username)
            query = """insert into appointments(username, age, phonenumber,emailid) select username,age, phonenumber,emailid from users where username = %s"""
            mycursor.execute(query, (username,))
            print("inserted")
            query = """update appointments set bookedfordate = %s where username = %s"""
            mycursor.execute(query, (date,username))
            connection.commit()

            request.session["appointmentbasedsession"] = False
            replytext = f"Your appointment is successfully booked for the date : {date}"
            return JsonResponse({"reply" : replytext})
        
        if usermsg == "exit"  :
            break
        
        else : 
            botmsg = autocot.get_response(usermsg) 
            if botmsg.text == "turn to suggest" :
                usermsg = "suggest"
                botmsg.text = "need the programmer"

            if botmsg.text == "need the programmer" : 
                if "specification" in usermsg or "specifications" in usermsg: 
                    request.session["specificationbasedsession"] = True
                    return JsonResponse({"reply" : "Enter the vehicle name you want the specifications about : "})

                elif "suggest" in usermsg : 
                    if "car" in usermsg :
                    
                        request.session["budgetwaitingsession"] = True

                        return JsonResponse({"reply" : "Enter the budget under which you want the suggestion : "})
                    
                    elif "bike" in usermsg  : 
                        userbudget = input("Enter your budget : ")
                        #query = """SELECT Name from vehiclesinfo where Price >= 50000 AND Price <= %s and category = %s"""
                        query = """SELECT Name from vehiclesinfo where Price >= 50000 AND Price <= %s"""
                        mycursor.execute(query, (userbudget,))
                        result = mycursor.fetchall()
                        print(result)
                        for item in range(0, len(result)) : 
                            for item2 in range(0, len(result[item])) : 
                                print(result[item][item2])
                    else :
                        vehiclecategory = input("Enter the vehicle category you want (ex : car, bike) : ")   
                        if "car" in vehiclecategory : 
                            userbudget = input("Enter your budget : ")
                        elif "bike" in vehiclecategory  : 
                            userbudget = input("Enter your budget : ")
                        else :
                            print("wrong page")
                else :
                    print("something went wrong")
            elif botmsg.text == "need the database" : 
                    if "appointment" in usermsg : 
                        request.session["appointmentbasedsession"] = True
                        print("hey")
                        return JsonResponse({"reply" : "Enter the date when you want to book the appointment"})
            else: 

                return JsonResponse({"reply" : botmsg.text})


        print("Chat exited !")

def customization(request) : 

    carname = request.GET.get("urlcarname")
    
    query = """SELECT viewsarray FROM VehicleDetails WHERE urlcarname = %s"""
    mycursor.execute(query, (carname,))
    result = mycursor.fetchall()
    print("hey")
    
    imgpath = result[0][0]
    imgpathsfreely = json.loads(imgpath)
    
    views_mapping = {
        "red_front_view": imgpathsfreely[0],
        "red_left_alloy1_view": imgpathsfreely[1],
        "red_left_alloy2_view": imgpathsfreely[2],
        "red_left_alloy3_view": imgpathsfreely[3],
        "red_left_alloy4_view": imgpathsfreely[4],
        "red_right_alloy1_view": imgpathsfreely[5],
        "red_right_alloy2_view": imgpathsfreely[6],
        "red_right_alloy3_view": imgpathsfreely[7],
        "red_right_alloy4_view": imgpathsfreely[8],
        "red_rear_view": imgpathsfreely[9],

        "black_front_view": imgpathsfreely[10],
        "black_left_alloy1_view": imgpathsfreely[11],
        "black_left_alloy2_view": imgpathsfreely[12],
        "black_left_alloy3_view": imgpathsfreely[13],
        "black_left_alloy4_view": imgpathsfreely[14],
        "black_right_alloy1_view": imgpathsfreely[15],
        "black_right_alloy2_view": imgpathsfreely[16],
        "black_right_alloy3_view": imgpathsfreely[17],
        "black_right_alloy4_view": imgpathsfreely[18],
        "black_rear_view": imgpathsfreely[19],

        "white_front_view": imgpathsfreely[20],
        "white_left_alloy1_view": imgpathsfreely[21],
        "white_left_alloy2_view": imgpathsfreely[22],
        "white_left_alloy3_view": imgpathsfreely[23],
        "white_left_alloy4_view": imgpathsfreely[24],
        "white_right_alloy1_view": imgpathsfreely[25],
        "white_right_alloy2_view": imgpathsfreely[26],
        "white_right_alloy3_view": imgpathsfreely[27],
        "white_right_alloy4_view": imgpathsfreely[28],
        "white_rear_view": imgpathsfreely[29],

        "yellow_front_view": imgpathsfreely[30],
        "yellow_left_alloy1_view": imgpathsfreely[31],
        "yellow_left_alloy2_view": imgpathsfreely[32],
        "yellow_left_alloy3_view": imgpathsfreely[33],
        "yellow_left_alloy4_view": imgpathsfreely[34],
        "yellow_right_alloy1_view": imgpathsfreely[35],
        "yellow_right_alloy2_view": imgpathsfreely[36],
        "yellow_right_alloy3_view": imgpathsfreely[37],
        "yellow_right_alloy4_view": imgpathsfreely[38],
        "yellow_rear_view": imgpathsfreely[39]
    }
    views_mapping_json = json.dumps(views_mapping)
    return render(request,"customization2.html", views_mapping)
def logoutuser(request) :   

    logout(request)
    return redirect("/login")