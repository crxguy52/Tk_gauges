import Tkinter as tk
import meter as m
import time

'''
https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=106349&p=733365#p733365
'''

class Mainframe(tk.Frame):
    
    def __init__(self, master, *args,**kwargs):
        tk.Frame.__init__(self, master)        
        
        meter_min = 0
        meter_max = 1023
        
        #Meter 1
        col = 0
        self.meter1 = m.Meter(self,height=600, width=600, label='Big Meter')
        self.meter1.setrange(meter_min,meter_max)
        self.meter1.grid(row=0, rowspan=2, column=col, sticky='nsew')
        
        '''
        tk.Scale(self, width = 15, length = 500 ,from_ = meter_min, to = meter_max
        ,orient = tk.HORIZONTAL
        ,command = lambda(value): self.setmeter(value, self.meter1),
            ).grid(row=2, column=col)
        '''
        tk.Button(self, command=self.sweep, text='sweep').grid(row=2, column=col)
        
        #Meter 2
        col = 1
        self.meter2 = m.Meter(self,height=300, width=300, 
                              label='Small Meter',
                              tickcolor='black',
                              face='white',
                              needle='red',
                              center='black',
                              labelcolor='black')
        self.meter2.setrange(meter_min,meter_max)
        self.meter2.grid(row=0, column=col, sticky='nsew')
        
        #Meter 3
        self.meter3 = m.Meter(self,height=300, width=300, 
                              label='Small Meter',
                              tickcolor='yellow',
                              face='#000066',
                              needle='red',
                              center='black',
                              labelcolor='yellow')
        self.meter3.setrange(meter_min,meter_max)
        self.meter3.grid(row=1, column=col, sticky='nsew')
          
        tk.Scale(self, width = 15, length=250, from_ = meter_min, to = meter_max
        ,orient = tk.HORIZONTAL
        ,command = lambda(value): self.setmeters(value, self.meter2, self.meter3),
            ).grid(row=2, column=col)        
        
        #Quit button
        tk.Button(self,text = 'Quit',width = 30,command=master.destroy
            ).grid(row=3, column=0, columnspan=2, pady=5)
            
            
      
    def setmeter(self, value, meter):
       value = int(value)
       meter.set(value)
       
    def setmeters(self, value, meter1, meter2):
        value = int(value)
        meter1.set(value)
        meter2.set(value)
        
    def sweep(self):
        for i in range(0,1024,4):
            self.meter1.set(i)
            self.meter1.update()
            time.sleep(0.001)        
 
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
      
        self.title('Gauges Demo')      
        self.mf = Mainframe(self)
        self.mf.pack()
       

app = App()
app.mainloop()



