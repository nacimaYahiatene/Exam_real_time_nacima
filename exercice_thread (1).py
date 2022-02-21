from asyncio import Task
import datetime
import time
import threading


stop_thread = False
global_fifo= []

## stock variables
stock1 = 0
stock2=  0

################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task(threading.Thread):


	name = None
	period = None
	execution_time = None
	priority=-1


    	############################################################################
	def __init__(self, name, period, execution_time, fifo_write = 0,fifo_read = 0, priority= 0):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.fifo_write = fifo_write
		self.fifo_read= fifo_read
		self.priority = priority
		
		threading.Thread.__init__(self)


	    ###########################################################################
	def run(self):

		global global_fifo

		while(not stop_thread):
				
			print(self.name + " : Starting task")
			
			for i in range(self.fifo_write) :
			
				global_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
			for i in range(self.fifo_read) :
				del global_fifo[len(global_fifo)-1]

			print(len(global_fifo))
			time.sleep(self.execution_time)
			print(self.name + " : Stopping task")
			time.sleep(self.period - self.execution_time)
			if(self.name=="Machine_1"):
				stock1=stock1+1
			if(self.name=="Machine_2"):
				stock2=stock2+1

			print(stock1+" and "+stock2)



	
####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':


	task_list = []

	# Instanciation of task objects

	task_list.append(my_task(name="pump_1", period=5, execution_time=2, fifo_write=10 ,fifo_read = 0, priority = 2))
	task_list.append(my_task(name="pump_2", period=15, execution_time=3, fifo_write=20,fifo_read = 0, priority = 2))
	task_list.append(my_task(name="Machine_1", period=5, execution_time=5, fifo_write=0, fifo_read = 25,priority = 1))
	task_list.append(my_task(name="Machine_2", period=5, execution_time=3, fifo_write=0, fifo_read = 5,priority = 1))
		


	for current_task in task_list :
		current_task.start()










