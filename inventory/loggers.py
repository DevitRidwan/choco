import logging
import datetime

class MyDbLogHandler(logging.Handler):
	def __init__(self):
		logging.Handler.__init__(self)

	def emit(self, record):
		try:
			from .models import SystemLog
			logEntry = SystemLog(level=record.levelname, message=record.message, timestamp=datetime.datetime.now())
			logEntry.save()
		except:
			pass

		return