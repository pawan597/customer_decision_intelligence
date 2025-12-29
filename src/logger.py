"""

WHY LOGGING EXISTS (INTUITION)

print() sirf screen par message dikhata hai aur program band hote hi sab gayab ho jata hai.
Real-world applications, ML pipelines, APIs aur production systems mein ye kaafi nahi hota.

Logging ek permanent record hota hai — program ki diary / black box.
Ye batata hai:
- kya hua
- kab hua
- kis level ka event tha (normal ya serious)
- aur agar error hua to kaha hua

Agar system kal fail hua ho, logging ke bina tum blind ho.
Logs ke saath tum investigation kar sakte ho.


LOGGING VS PRINT (MENTAL MODEL)

print()  = aadmi chillata hai (temporary, no structure)
logging  = CCTV + register + timestamp + severity

Production mein koi print nahi padhta.
Logs padhe jaate hain.


LOGGER KYA HOTA HAI?

Logger ek object hota hai jo actual likhne ka kaam karta hai.
Socho:
- Logging = notebook
- Logger  = pen

Har jagah print likhne ke bajay hum logger.info(), logger.error() likhte hain.
Logger decide karta hai:
- message likhna hai ya nahi
- kis severity ke saath
- kaha likhna hai (file / console / cloud)


LOG LEVELS (IMPORTANCE SCALE)

DEBUG    → developer ke liye deep details
INFO     → normal flow ki information
WARNING  → kuch unexpected, par program chalu hai
ERROR    → kaam fail ho gaya
CRITICAL → system crash / shutdown situation

Isse hum samajh paate hain ki issue kitna serious hai.


LOGGER.PY FILE KYU BANATE HAIN?

Python mein 'logging' built-in module hota hai,
lekin 'logger.py' hum khud banate hain.

Iska purpose:
- logging ka setup ek hi jagah likhna
- har file mein same logging behavior maintain karna
- duplication avoid karna

logger.py = logging factory
baaki files = sirf logger use karti hain


LOGGING + EXCEPTIONS KA CONNECTION

Jab exception aata hai, hum sirf error message nahi chahte.
Hume chahiye:
- file ka naam
- line number
- full traceback

logger.error("message", exc_info=True)
internally sys.exc_info() use karta hai
aur poora error ka route log kar deta hai.

Isse debugging bahut easy ho jaati hai.


DATA SCIENCE / ML CONTEXT

Logging ML projects mein critical hota hai:
- model training start / end
- dataset shape
- feature issues
- pipeline failure points
- production monitoring

Agar model fail ho jaye aur logs na ho,
to tum kabhi nahi jaan paoge "kyun fail hua".

"""

# Python ka built-in logging module import kar rahe hain.
# Ye module program ke events (info, warning, error, etc.) ko
# structured way mein record karne ke kaam aata hai.
import logging


# os module import kar rahe hain taaki operating system ke saath
# interact kar sakein — jaise folders banana, paths join karna, etc.
import os


# datetime module se datetime import kar rahe hain
# taaki current date aur time nikaal kar use log file ka naam bana sakein.
from datetime import datetime


# Current date aur time ko string format mein convert karke
# har run ke liye ek unique log file ka naam bana rahe hain.
# Isse purane logs overwrite nahi honge.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Current working directory (project root) ke andar
# "logs" naam ka folder aur uske andar log file ka path bana rahe hain.
# Yahan LOG_FILE ko path ke saath jod diya gaya hai.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)


# Agar upar diya gaya path exist nahi karta to usko create karne ki koshish kar rahe hain.
# exist_ok=True ka matlab: agar folder already exist karta ho to error mat dena.
# (Yahan function ka naam aur path logic important hote hain.)
os.makedirs(logs_path, exist_ok=True)


# Yahan hum log file ka final full path banana chah rahe hain
# jisme folder path aur file name dono include hon.
# Is path ka use logging system karega file likhne ke liye.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Logging system ka global configuration set kar rahe hain.
# Ye configuration poore program ke logging behavior ko control karegi.
logging.basicConfig(

    # filename specify karta hai ki saare logs kis file ke andar likhe jayenge.
    filename=LOG_FILE_PATH,

    # format define karta hai ki har log line ka structure kaisa hoga:
    # - asctime  → log likhne ka exact time
    # - lineno   → jis line number par log call hua
    # - name     → logger ka naam
    # - levelname→ log ka level (INFO, ERROR, etc.)
    # - message  → actual log message
    format="[%(%asctime)] %(lineno)d %(name)s -%(levelname)s -%(message)s",

    # level=logging.INFO ka matlab:
    # INFO aur usse upar ke logs (WARNING, ERROR, CRITICAL) record honge,
    # DEBUG level ke logs ignore ho jayenge.
    level=logging.INFO,
)

