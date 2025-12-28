from setuptools import find_packages,setup
from typing import List

hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:

 #this funtion will go to oure file and get all the str and make it into a list str

   requirements =[]
   with open (file_path) as file_obj:
      requirements=file_obj.readlines()# this will go in  our particular file and start reading everythging line by line but tha problem is that it will read  \n with it so it can give an error
      [req.replace ("\n"," ") for req in requirements]# that is why we build this line 

      if hypen_e_dot in requirements:
         requirements.remove(hypen_e_dot)


         return requirements 


setup(

name="customer_decision_intelligence",
version="0.0.1",
author="Pawan",
author_email="pwnpwn567@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")# this will basically get our all needed pacages from this pariticlar file 


 )