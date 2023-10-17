import json
import time
import random
import requests
import urllib3


# Disabled Python warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

current_timestamp = time.time() # Get the current Unix timestamp
timestamp_increment_value= 30
# 3 time sleep for 10 
within_funcation_timesleep = 2
out_of_funcation_timesleep = 4
product_code_all = ["12345."]
stop_code="unknown"
fault_code="unknown"
cycle_time =2
qty_producted = 2
product_code = product_code_all[0]

API_Endpoint = 'https://api-demo.fogwing.net/api/v1/iothub/postPayload/withApiKey'
Account_ID = '4510'
API_Key = '626ab5a2cf334d5da75c73c021509df9'
IOTusername = '769ad4fe939d2688'
HMIusername = '769ad4fe939d2688'
access_code = 66783

# def IOTdataup():
#     global current_timestamp
#     payload = {
#         "asset_status": "up",
#         "duration": round(random.randint(5, 100), 2),
#         "current": round(random.randint(0, 140), 2),
#         "temp": round(random.randint(0, 500), 2),
#         "roller_speed": round(random.uniform(300, 25000), 2),
#         "event_code": 666,
#         "euiid": IOTusername,
#         "timestamp": current_timestamp
#     }
#     current_timestamp += timestamp_increment_value  # Add one minute to the timestamp for the next iteration

#     check_msg = json.dumps(payload, indent=4)  # sample payload(data up)
#     return check_msg


# def IOTdatadown():
#     global current_timestamp
#     payload = {
#         "asset_status": "down",
#         "duration": round(random.randint(5, 10), 2),
#         "current": round(random.randint(0, 14), 2),
#         "temp": round(random.randint(0, 500), 2),
#         "roller_speed": round(random.uniform(0, 250), 2),
#         "event_code": 666,
#         "euiid": IOTusername,
#         "timestamp": current_timestamp
#     }
#     current_timestamp += timestamp_increment_value  # Add one minute to the timestamp for the next iteration
#     check_msg = json.dumps(payload, indent=4)  # sample payload(data down)
#     return check_msg


# def HMIdataup():
#     global current_timestamp, product_code
#     payload = {
#                 "event_code": 777,
#                 "asset_status": "up",
#                 "cycle_time": cycle_time,
#                 "product_code": product_code,
#                 "quantity_produced": qty_producted,
#                 "cuts_min": cycle_time,
#                 "feet_min": -100,
#                 "euiid": HMIusername,
#                 "timestamp": current_timestamp
#                 }
#     current_timestamp += timestamp_increment_value  # Add one minute to the timestamp for the next iteration

#     check_msg = json.dumps(payload, indent=4)  # sample payload(data up)
#     return check_msg


def HMIdatadown():
    global current_timestamp, product_code
    payload = {
                "event_code": 777,
                "asset_status": "down",
                "cycle_time": 0,
                "product_code": product_code,
                "quantity_produced": 0,
                "cuts_min": 0,
                "feet_min": 0,
                "euiid": HMIusername,
                "timestamp": current_timestamp
                }
    current_timestamp += timestamp_increment_value  # Add one minute to the timestamp for the next iteration
    check_msg = json.dumps(payload, indent=4)  # sample payload(data down)
    return check_msg


# def HMI_entry_up():
#     global current_timestamp, product_code, access_code
#     payload = {
#         "event_code": 777,
#         "asset_status": "up",
#         "cycle_time": cycle_time,
#         "product_code": product_code,
#         "stop_reason_code": stop_code,
#         "fault_reason_code": fault_code,
#         "access_code": access_code,
#         "euiid": HMIusername,
#         "timestamp": current_timestamp
#     }
# #    current_timestamp += 30  # Add one minute to the timestamp for the next iteration
#     check_msg = json.dumps(payload, indent=4)  # sample payload(data down)
#     return check_msg

# def HMI_entry_down():
#     global current_timestamp, product_code, access_code
#     payload = {
#         "event_code": 777,
#         "asset_status": "down",
#         "cycle_time": cycle_time,
#         "product_code": product_code,
#         "stop_reason_code": stop_code,
#         "fault_reason_code": fault_code,
#         "access_code": access_code,
#         "euiid": HMIusername,
#         "timestamp": current_timestamp
#     }
# #    current_timestamp += 30  # Add one minute to the timestamp for the next iteration
#     check_msg = json.dumps(payload, indent=4)  # sample payload(data down)
#     return check_msg


# def HMIrejection():
#     global current_timestamp, product_code
#     payload = {
#         "event_code": 888,
#         "cycle_time": round(random.randint(5, 100), 2),
#         "product_code": product_code,
#         "weight": round(random.randint(5, 25), 2),
#         "quantity_rejected": round(random.randint(5, 250), 2),
#         "euiid": HMIusername,
#         "timestamp": current_timestamp
#     }
#     check_msg = json.dumps(payload, indent=4)  # sample payload(data down)
#     return check_msg


def Fogwing_IoTHub_client_telemetry_run():
    global product_code, hmiapppub_manual
    #start from seq number 1
    seq = 1
    #From downvaluestart, it'll call the else part
    # addd +1
    downvaluestart = 1111
    #Runtime for the script
    runminute = 100
     #From the Reset point, it'll reset the cyc  le and start from if condition
    #If reset_value example 4, from the 7 seq call the if condition
    #add last ending vlaue 10
    reset_value = 4222
    #once it's reached the upcontinuefrom value, it'll call only the if condition
    upcontinuefrom =1112
    # If the hmiapppub_manual is 'no' means, it send only the every one mint payload structure.
    hmiapppub_manual = 'no'
    # Once reached this count, it will send the payload with one manual entry structure.
    hmipub = 1119

    for _ in range(runminute):
        print("payload sequence: ",seq)
        #Second check the hmipub to publish the production code value
        if (seq) == hmipub and hmiapppub_manual == 'no':
            hmiapppub_manual = 'yes'
            product_code = product_code_all[1]
        
        #And then finally based on the threshold vlaue the if and else condition will call.
        if (seq % reset_value < downvaluestart) and not (seq % reset_value == 0):
            IOTmessage = str()
            HMImessage = str()
            # IOTmessage = IOTdataup()
            # HMImessage = HMIdataup()
            # HMIAPPmessage = HMI_entry_up()
        else:
            IOTmessage = str()
            HMImessage = str()
            # IOTmessage = IOTdatadown()
            HMImessage = HMIdatadown()
            # HMIAPPmessage = HMI_entry_down()
        

        if hmiapppub_manual == 'no':
            try:
                # Add Account ID, API Key and Edge EUI as the headers
                headerIOT = {"accountID": Account_ID, "apiKey": API_Key, "edgeEUI": IOTusername}
                # Send the payload data to the API
                payload_respIOT = requests.post(API_Endpoint, data=IOTmessage, headers=headerIOT, verify=False)
                time.sleep(within_funcation_timesleep)
                print("IOT payload")
                print(IOTmessage)
                headerHMI = {"accountID": Account_ID, "apiKey": API_Key, "edgeEUI": HMIusername}
                # Send the payload data to the API
                payload_respHMI = requests.post(API_Endpoint, data=HMImessage, headers=headerHMI, verify=False)
                time.sleep(within_funcation_timesleep)
                print("HMI payload")
                print(HMImessage)
        #       return payload_resp.status_code
                time.sleep(within_funcation_timesleep)
            except Exception as exapi:
                print("HMI Edge : API Connection and Payload failed: ", exapi)
        elif hmiapppub_manual == 'yes':
            try:                
                # Add Account ID, API Key and Edge EUI as the headers
                headerIOT = {"accountID": Account_ID, "apiKey": API_Key, "edgeEUI": IOTusername}
                # Send the payload data to the API
                payload_respIOT = requests.post(API_Endpoint, data=IOTmessage, headers=headerIOT, verify=False)
                time.sleep(within_funcation_timesleep)
                print("IOT payload")
                print(IOTmessage)
                headerHMI = {"accountID": Account_ID, "apiKey": API_Key, "edgeEUI": HMIusername}
                # Send the payload data to the API
                # payload_respHMI = requests.post(API_Endpoint, data=HMIAPPmessage, headers=headerHMI, verify=False)
                # time.sleep(within_funcation_timesleep)
                # hmiapppub_manual = 'no'
                # print("HMI Device Manual payload")
                # print(HMIAPPmessage)
                headerHMI = {"accountID": Account_ID, "apiKey": API_Key, "edgeEUI": HMIusername}
                # Send the payload data to the API
                payload_respHMI = requests.post(API_Endpoint, data=HMImessage, headers=headerHMI, verify=False)
                time.sleep(within_funcation_timesleep)
                print("HMI payload")
                print(HMImessage)
        #        return payload_resp.status_code
            except Exception as exapi:
                print("HMI Edge : API Connection and Payload failed: ", exapi)
            #Frist check the upcontinuefrom value to call which funcation
        if (seq) % upcontinuefrom == 0:
            downvaluestart = 52        

        
        seq += 1
        time.sleep(out_of_funcation_timesleep)  # This value will publish message to Fogwing IoT Hub after every min/hour once.a


if __name__ == '__main__':
    print("Fogwing IoT Hub: Started to connecting...")
    print("Fogwing IoT Hub: Press Ctrl+C to exit")
    Fogwing_IoTHub_client_telemetry_run()