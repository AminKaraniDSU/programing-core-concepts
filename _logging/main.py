import logging


# # 5 levels of logging
# # by default it will show warning and above level log
# logging.debug("Debug") # will not print anything
# logging.info("Info") # will not print anything
# logging.warning("Warning") # will print a message to the console
# logging.error("Error") # will print a message to the console
# logging.critical("Critical") # will print a message to the console


logging.basicConfig(level=logging.INFO,# filename="log.log", filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("_Debug")
logging.info("_Info")
logging.warning("_Warning")
logging.error("_Error")
logging.critical("_Critical")



try:
    a = 1/0

except ZeroDivisionError as e:
    logging.error("ZeroDivisionError", exc_info=True)
    logging.exception("Test")
