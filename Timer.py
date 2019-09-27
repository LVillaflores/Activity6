import time


class Timer:
	def __init__(self):
		self.start = time.time()

	def restart(self):
		self.start = time.time()

	def get_new_time(self):
		value = time.time() - self.start
		self.restart()
		return value

	def print_new_time(self):
		print(self.get_new_time())

	def get_time(self):
		return time.time() - self.start
		self.restart()

	def print_time(self):
		print(self.get_time)

	def get_time_hhmmss(self):
		end = time.time()
		m, s = divmod(end - self.start, 60)
		h, m = divmod(m, 60)
		time_str = "%02d:%02d:%02d" % (h, m, s)
		return time_str
