import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
        
        self.error_message=error_message
        _,_,_exc_tb=error_detail.exc_info()
        
        self.lineno=_exc_tb.tb_lineno
        self.filename=_exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))

# if __name__=="__main__":
#     try:
#         logger.logging.info("Starting the test for NetworkSecurityException")
#         a=1/0
#         print("Hello World",a)
#     except Exception as e:
#        raise NetworkSecurityException(e,sys)