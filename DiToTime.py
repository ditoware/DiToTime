# module TEST nxpnfc
#
#
#
import nxpnfc as nfc
import time
import datetime

uid = 0
last = -1

id = {
      "042F50415B2380" : "Paul",
      "04DCC842333580" : "Joe ",
      "044DC7DA452B80" : "Peter",
}

try:
    while True:

        uid = nfc.uid()
        if (str(uid) == "None"):
          uid = last

        if (uid != last):
          last = uid
          try:
            print("----------[ "+ id[uid] + " ]-----------")

            if ( str(nfc.readBlock(10)) == "true" ):
              end_of_work = datetime.datetime.now()
              nfc.writeData(10, "fals")
              try:
                start_of_work = datetime.datetime.fromtimestamp(int(nfc.read(10, 13)[4:14]))
              except ValueError:
                print("NFC_Chip defekt")
                continue
              print(id[uid] +" hat sich am: " + end_of_work.strftime("%d.%m.%Y") +" abgemeldet")
              # print("Startzeit: "+ start_of_work.strftime("%d.%m.%Y - %H:%M:%S") +" Endzeit: "+ end_of_work.strftime("%d.%m.%Y - %H:%M:%S") +" Arbeitszeit: "+ str(end_of_work - start_of_work).split(".")[0])
              print("  Startzeit: "+ start_of_work.strftime("%H:%M:%S = %d.%m.%Y"))
              print("    Endzeit: "+ end_of_work.strftime("%H:%M:%S = %d.%m.%Y"))
              # print("Arbeitszeit: "+ str(end_of_work - start_of_work).split(".")[0])
              print("Arbeitszeit: %8s" %(str(end_of_work - start_of_work).split(".")[0]) )

            else:
              start_of_work = time.time()
              print(id[uid] +" hat sich am: " + datetime.datetime.fromtimestamp(start_of_work).strftime("%d.%m.%Y - %d.%m.%Y") +" angemeldet")
              nfc.writeData(10, "true")
              nfc.writeData(11, str(start_of_work).split(".")[0])
            print("---------------------------------------")
          except KeyError:
            print("NFC nicht Registriert!")
        time.sleep(1)
except KeyboardInterrupt:
  pass
