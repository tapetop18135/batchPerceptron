
import numpy as np 

class BatchPerceptron:
	def __init__(self,input_all,target,weight,lerning_rate):

		self.input_x_all = np.array(self.creat_Input_xAll(input_all)) 
		self.target = target
		self.weight = np.array(weight)
		self.lerning_rate =   lerning_rate

	def creat_Input_xAll(self,input_all):

		for i in range(len(input_all)):
			input_all[i] = [-1] + input_all[i]  

		return input_all

	def batchAlgorithm(self):
		
		i = 0
		while True:
			i+=1
			print("\nintrator : ",i,"\n")
			
			err_array = self.loopBatchCheckErr(self.input_x_all,self.weight)

			if(err_array == []):
				return self.weight

			self.updateloopBatchWeight(err_array,self.weight,self.lerning_rate)		

	def loopBatchCheckErr(self,input_all,weight):
		result_err = []
		check = 0
		for i in range(len(input_all)):
			if(self.target == "or"):
				if(self.input_x_all[i][1] == 0 and self.input_x_all[i][2] == 0):
					use_target = -1
				else:
					use_target = 1
			else:
				if(self.input_x_all[i][1] == 1 and self.input_x_all[i][2] == 1):
					use_target = 1
				else:
					use_target = -1

			if(self.checkErr(input_all[i],weight,use_target)):
				pass
			else:
				result_err.append(	input_all[i])
		print(result_err)
		return result_err

	def checkErr(self,input_each,weight,target):
		# checkerr = d * w(transpose) * x(each input)
		result = target * np.matmul(weight,input_each) 
		
		print(weight," * ",target," * ",input_each," = ",result)
		
		if(result > 0):
			return True
		else:
			return False

	def updateloopBatchWeight(self,input_a,weight,lerning_rate):
		# w(n+1) = w(n) + summation(h * d * x(input))
		result = 0
		text = str(weight)+" + "
		for i in range(len(input_a)):
			if(self.target == "or"):
				if(input_a[i][1] == 0 and input_a[i][2] == 0):
					use_target = -1
				else:
					use_target = 1
			else:
				if(input_a[i][1] == 1 and input_a[i][2] == 1):
					use_target = 1
				else:
					use_target = -1

			print (i," : ",use_target)

			text += str(lerning_rate * use_target * np.array(input_a[i]))+" " 
			result += (lerning_rate * use_target * np.array(input_a[i]))
			print(str(lerning_rate * use_target * np.array(input_a[i])))

		result = weight + result 
		print(text+"= "+str(result))
		self.weight = result




########################## End Class ###############################

#     OR Gate 
#
#	x1		x2		OR		class
#	0		0		0		  c2
#	0		1		1		  c1
#	1		0		1		  c1	
#	1		1		1		  c1
#

input_all = [
			[0,0],
			[0,1],
			[1,0],
			[1,1]]

# weight = [0.5,1.5,1.5]
weight = [0,0,0]
# class  c2 => -1 , c1 => 1

target = "and" 

h = 0.5 		


sample = BatchPerceptron(input_all,target,weight,h)
print(sample.batchAlgorithm())






