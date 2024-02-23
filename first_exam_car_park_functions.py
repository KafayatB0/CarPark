# first_exam_car_park_functions.py

import csv
import os
import datetime
import random
import re

class FirstExamCarPark:
    def __init__(self, csv_filename="first_exam_car_park_list.csv"):
        self.csv_filename = csv_filename
        self.CreateCsv()
        self.first_exam_car_park_list = self.ReadFirstEXamList()


    def CreateCsv(self):
        if not os.path.exists(self.csv_filename):
            with open(self.csv_filename, 'w', newline='') as file:
                fieldnames = ['ID', 'TicketNumber', 'CarRegistrationNumber', 'CarID', 'EntryTimestamp', 'ExitTimestamp', 'Duration', 'CarParkID']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def ReadFirstEXamList(self):
        with open(self.csv_filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def UpdateParkDetails(self):
        with open(self.csv_filename, 'w', newline='') as file:
            fieldnames = ['ID', 'TicketNumber', 'CarRegistrationNumber', 'CarID', 'EntryTimestamp', 'ExitTimestamp', 'Duration', 'CarParkID']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.first_exam_car_park_list)
 
    def Enter_the_Car_Park(self, reg_number):
        reg_number = reg_number.strip().upper()
        # Check if car is not already in the car park
        active_cars_parked = [FirstExamList['CarRegistrationNumber'] for FirstExamList in self.first_exam_car_park_list if FirstExamList['ExitTimestamp'] =='']
        
        # Check if it is a standard UK Number
        if not re.compile(r'^[A-Z]{2}\d{2}\s[A-Z]{3}$').match(reg_number):
            return "Error: Car registration number is not valid"            

        if reg_number in active_cars_parked:
            return "Error: Car with this registration number is already in the car park."


        entry_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Check for parking space
        availPKSPace =self.AvailableParkingSpace()
        if len(availPKSPace) >0:
            
            car_park_id = availPKSPace[0]
            ticket_number = int(datetime.datetime.now().timestamp()) # get a unique ticket number
    
            car_id = f"CarID-{len(self.first_exam_car_park_list) + 1}"
            FirstExamList = {
                'ID': len(self.first_exam_car_park_list) + 1,
                'TicketNumber': str(ticket_number),
                'CarRegistrationNumber': str(reg_number),
                'CarID': str(car_id),
                'EntryTimestamp': entry_timestamp,
                'ExitTimestamp': '',
                'Duration': '',
                'CarParkID': str(car_park_id)
            }
    
            self.first_exam_car_park_list.append(FirstExamList)
            self.UpdateParkDetails()  # Save FirstExamLists concurrently
            return f"Car entered. Your ticket Number is {ticket_number}, {car_park_id} is assigned. The available spaces are {availPKSPace}."
        else:
            return f"Sorry! Car Park is full"

    def Exit_the_Car_Park(self, reg_number):
        reg_number = reg_number.strip().upper()

        # Check if car already exited the car park
        cars_already_exited = [FirstExamList['CarRegistrationNumber'] for FirstExamList in self.first_exam_car_park_list if FirstExamList['ExitTimestamp'] !='']
        
        # Check if it is a standard UK Number
        if not re.compile(r'^[A-Z]{2}\d{2}\s[A-Z]{3}$').match(reg_number):
            return "Error: Car registration number is not valid"            

        if reg_number in cars_already_exited:
            return "Error: This car already left the park."
        
        # Check for parking space
        availPKSPace = self.AvailableParkingSpace()

        exit_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for FirstExamList in self.first_exam_car_park_list:
            if str(FirstExamList['CarRegistrationNumber']) == str(reg_number) and FirstExamList['ExitTimestamp'] == '':
                FirstExamList['ExitTimestamp'] = exit_timestamp
                entry_timestamp = datetime.datetime.strptime(FirstExamList['EntryTimestamp'], '%Y-%m-%d %H:%M:%S')
                exit_timestamp = datetime.datetime.strptime(FirstExamList['ExitTimestamp'], '%Y-%m-%d %H:%M:%S')
                duration = exit_timestamp - entry_timestamp
                FirstExamList['Duration'] = duration.total_seconds() / 3600  # Convert duration to hours

                parking_fee = self.ParkingAmount(FirstExamList['Duration'])
                self.UpdateParkDetails()  # Save FirstExamLists concurrently
                return f"Your car with registration number: {reg_number} and  parking space: {FirstExamList['CarParkID']} exited, Please pay £{parking_fee:.2f} at the exit. We have {availPKSPace} available. "

        return "Error: Invalid Car registration number."

    def View_Available_Parking_Spaces(self):
        occupied_spaces = {FirstExamList['CarParkID'] for FirstExamList in self.first_exam_car_park_list if 'ExitTimestamp' not in FirstExamList}
        all_spaces = {f"SPACE-{i}" for i in range(1, 21)}
        available_spaces = all_spaces - occupied_spaces


        # Filter out occupied spaces
        available_spaces = [space for space in available_spaces if space not in occupied_spaces]

        return available_spaces, len(occupied_spaces), len(all_spaces), len(self.first_exam_car_park_list)

    def Query_Parking_Record_by_TicketNumber(self, value=None):
            if value:

                check_if_ticket_exist = [record for record in self.first_exam_car_park_list if record['TicketNumber'] == value]

                if check_if_ticket_exist:
                
                    return check_if_ticket_exist
                else:
                    return "Invalid ticket number."

            else:
                return "Error: Ticket number is required."



    def AvailableParkingSpace(self):
        occupied_spaces = [FirstExamList['CarParkID'] for FirstExamList in self.first_exam_car_park_list if FirstExamList['ExitTimestamp'] =='']
        available_spaces = []
        
        for i in range(1,21):
            space = f"SPACE-{i}"
            if space not in occupied_spaces:
                available_spaces.append(space)


        return available_spaces
    
    def ParkingAmount(self, duration):
        hourly_rate = 2
        return duration * hourly_rate


a = FirstExamCarPark()