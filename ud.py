class udacian:
	
	
	def __init__(self,name,city,enrollment,nandgree,status):
		self.name = name
		self.city = city
		self.enrollment = enrollment
		self.nandgree = nandgree
		self.status = status
		
	def print_udacian(self):
		return ("name is: " + self.name +" , city: "+ self.city +" , enrollment: "+self.enrollment +" , dgree: "+ self.nandgree +" , status: " + self.status)
		
		
v = udacian("maraim","jed","enroll","full","on")
print (v.print_udacian())

