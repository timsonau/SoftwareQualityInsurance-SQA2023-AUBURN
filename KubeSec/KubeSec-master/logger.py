import logging 


def getLogObj(name):
    format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    file_name  = 'Kube-Sec-Acivity.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger(name)
    return loggerObj