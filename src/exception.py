# sys module import kar rahe hain kyunki Python ke system-level details
# jaise currently aayi hui error ki full information) yahin se milti hai.
# Ye OS aur Python runtime ke beech ka bridge hai.
import sys
import logging


# Ye function ka kaam sirf ek cheez hai:
# Normal, confusing Python error ko uthana aur usko ek clean,
# human-readable, professional error message me convert kar dena.
def error_message_detail(error, error_detail: sys):

    # error_detail.exc_info() teen cheeze return karta hai:
    # 1) error ka type (jaise ValueError, ZeroDivisionError)
    # 2) error ka actual object / message
    # 3) traceback object (error kaha-kaha se pass hoke aaya)
    #
    # Humein "error kya hai" se zyada "error kaha hua" matter karta hai,
    # isliye pehle do values ko ignore kar rahe hain (_),
    # aur sirf traceback (exc_tb) ko store kar rahe hain.
    _, _, exc_tb = error_detail.exc_info()

    # exc_tb (traceback) ke andar jaakar ye line nikalti hai:
    # - jis Python file me error actually raise hua
    # Ye basically error ka exact address hai (file ka naam / path).
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Ab hum ek detailed, readable error message bana rahe hain
    # jisme teen important cheeze hongi:
    # 1) kaunsi Python file me error aaya
    # 2) kaunsi line number par error aaya
    # 3) actual error message kya tha
    
    # Ye message debugging, logging aur production ke liye kaafi useful hota hai.
    error_message = (
        "error occured in python script name [{0}] line number [{1}] error message [{2}]"
        .format(
            file_name,          # error wali file ka naam
            exc_tb.tb_lineno,   # error wali exact line number
            str(error)          # original error ka message
        )
    )

    # Final formatted error message return kar rahe hain
    # taaki ise custom exception ya logger me use kiya ja sake.
    return error_message


# Ye class Python ki built-in Exception class ka extension hai.
# Matlab hum apni khud ki exception bana rahe hain,
# jo normal exception se zyada informative hogi.
class customException(Exception):

    # Jab bhi customException raise hogi, ye constructor chalega.
    # Yahan hum raw error aur sys module dono pass kar rahe hain
    # taaki error ki deep details nikaal sakein.
    def __init__(self, error_message, error_detail: sys):

        # Parent Exception class ka constructor call kar rahe hain
        # taaki normal Exception behavior break na ho.
        super().__init__(error_message)

        # Raw error ko lekar hum apna detailed error message bana rahe hain
        # jisme file name, line number aur actual error sab include hota hai.
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    # Ye method tab call hota hai jab hum exception ko print karte hain
    # ya uska string representation chahte hain.
    #
    # Isse faida ye hota hai ki print(e) karne par
    # ek clean, readable, professional error message dikhega
    # na ki confusing Python traceback.
    def __str__(self):
        return self.error_message




  