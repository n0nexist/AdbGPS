#!/usr/bin/env python3

"""
github.com/n0nexist/adbgps
use your android device as a gps module
"""

import os
import datetime
import time

class logger:
    info = "* Info"
    warn = "! WARN"
    error = "!!! ERROR"

    def get_timestamp():
        """ timestamp for logging """
        d = datetime.datetime.now()
        return f"[{d.day}-{d.month}-{d.year}|{d.hour}:{d.minute}:{d.second}]"

    def get_timestamp2():
        """ timestamp for file names """
        d = datetime.datetime.now()
        return f"{d.day}-{d.month}-{d.year}_{d.hour}.{d.minute}.{d.second}"

    def create_logging_file(name):
        """ creates a new logging file with name as a parameter """
        if os.path.exists("adbgps_logs") == False:
            os.mkdir("adbgps_logs")
        fname = f"adbgps_logs/{name}"
        os.environ['logfile'] = fname
        logger.log(logger.info, "adbgps started")

    def create_new_logging_file():
        """ creates a new logging file """
        fname = logger.get_timestamp2()+".txt"
        if os.path.exists(fname) == False:
            logger.create_logging_file(fname)

    def log(level,text):
        """ writes to the current logfile """
        t = f"{logger.get_timestamp()} ({level}) {text}"
        print(t)
        f = open(os.getenv('logfile'),"a")
        f.write(f"{t}\n")
        f.close()

    def write_to_locationfile(text):
        """ writes to location.txt """
        logger.log(logger.info,f"Writing {text} to location.txt")
        try:
            f = open("location.txt","w")
            f.write(text)
            f.close()
        except Exception as e:
            logger.log(logger.error,f"Error while writing to location.txt: {e}")

class adb:
    def adb_location():
        """ gets the gps location of the connected adb device """
        output = os.popen("adb shell dumpsys location | grep Location").read()
        temp = output.split("Location[")[1].split(" ")[1].split(",")
        try:
            os.environ['lastpos'] = '{"lat": "'+temp[0]+'", "lon": "'+temp[1]+'"}'
        except:
            pass
        return os.getenv('lastpos')

    def reload_adb():
        """ reloads the adb server """
        logger.log(logger.info,"Showing connected devices:")
        os.system("adb devices")
        logger.log(logger.info,"Starting in 3 seconds")
        time.sleep(3)

def main():
    """ adbgps's main function """
    os.environ['lastpos'] = '{"lat": "0", "lon": "0"}'
    logger.create_new_logging_file()
    adb.reload_adb()
    while True:
        logger.write_to_locationfile(adb.adb_location())
        time.sleep(1)
        


if __name__ == "__main__":
    main()
else:
    print("* Adbgps is being imported in another project")