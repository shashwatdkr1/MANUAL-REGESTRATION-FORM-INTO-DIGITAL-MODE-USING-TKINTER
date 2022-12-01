from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window = Tk()
window.title(&#39;SET 3&#39;)
window.geometry(&#39;1000x1000&#39;)
l4 = Label(window, text=&quot;REGISTRATION
INFORMATION&quot;,height=5).grid(row=0, columnspan=5)
Reg_period = Label(window, text=&quot;Registration period:(check
one)&quot;).grid(row=1, column=0)
CheckVar1 = IntVar()
C1 = Checkbutton(window, text = &quot;One year&quot;, variable = CheckVar1,
onvalue =1, offvalue = 0, width = 10).grid(row=1, column=1)
C1 = Checkbutton(window, text = &quot;Two years ($2 discount applies)&quot;,
variable =CheckVar1, onvalue = 1, offvalue = 0, width =
25).grid(row=1, column=2)
C1 = Checkbutton(window, text = &quot;Three years ($3 discount applies)&quot;,
variable= CheckVar1, onvalue = 1, offvalue = 0, width =
25).grid(row=1, column=3)
Reg_type = Label(window, text=&quot;Registration type:(check
one)&quot;).grid(row=2,column=0)
CheckVar1 = IntVar()
C1 = Checkbutton(window, text = &quot;Original&quot;, variable = CheckVar1,
onvalue = 1,offvalue = 0, height=2, width = 10).grid(row=2,
column=1)
C1 = Checkbutton(window, text = &quot;Renewal&quot;, variable = CheckVar1,
onvalue =1, offvalue = 0, height=2, width = 10).grid(row=2,
column=2)
C1 = Checkbutton(window, text = &quot;Private&quot;, variable = CheckVar1,
onvalue = 1,offvalue = 0, height=2, width = 10).grid(row=2,
column=3)
C1 = Checkbutton(window, text = &quot;Reissue (Plates &amp; Decals)&quot;,
variable =CheckVar1, onvalue = 1, offvalue = 0, height=2, width =
20).grid(row=2,column=4)
CheckVar1 = IntVar()
C1 = Checkbutton(window, text = &quot;Reissue (Decals only)&quot;, variable =
CheckVar1, onvalue = 1, offvalue = 0, width = 18).grid(row=3,
column=0)
C1 = Checkbutton(window, text = &quot;Rental Vehicle&quot;, variable =
CheckVar1,onvalue = 1, offvalue = 0, width = 13).grid(row=3,
column=1)
C1 = Checkbutton(window, text = &quot;Transfer Liscence plate no.&quot;,
variable = CheckVar1, onvalue = 1, offvalue = 0, width =
22).grid(row=3, column=2)

e1=Entry(window).grid(row=2,column=3)
l1 = Label(window, text=&quot;See reissue plates below \n under plates
information &quot;).grid(row=4, column=4)
C1 = Checkbutton(window, text = &quot;For Hire (complete &#39;For Hire \n
information&#39; section)&quot;, variable = CheckVar1, width =
30).grid(row=4, columnspan=2)
C1 = Checkbutton(window, text = &quot;Ridesharing (vanpool)(cannot exceed
16 passengers including driver.) &quot;, variable = CheckVar1, width =
55).grid(row=4, columnspan=6)
l1=Label(window, text=&quot;seating \n capacity&quot;).grid(row=3, column=4)
e1=Entry(window, width=5).grid(row=3,column=5)
C1 = Checkbutton(window, text = &quot;Amateur Radio Operator Call \n
Letters - specify letters&quot;, variable = CheckVar1, width =
22).grid(row=5, columnspan=1)
e1=Entry(window, width=10).grid(row=4,column=1)
C1 = Checkbutton(window, text = &quot;Other (specify)&quot;, variable =
CheckVar1, onvalue = 1, offvalue = 0, width = 20).grid(row=5,
column=1)
e1=Entry(window, width=10).grid(row=4,column=2)
l4 = Label(window, text=&quot;OWNER INFORMATION&quot;, height=5).grid(row=6,
columnspan=5)
l5 = Label(window, text=&quot;OWNER FULL LEGAL NAME OR BUSINESS NAME(if
business owned)&quot;).grid(row=7, column=1)
e1=Entry(window, width=45).grid(row=8,column=1)
l5 = Label(window, text=&quot;TELEPHONE NUMBER&quot;).grid(row=7, column=2)
e1=Entry(window, width=20).grid(row=8,column=2)
l5 = Label(window, text=&quot;DMV CUSTOMER NUMBER / FEIN /
SSN&quot;).grid(row=7, column=3)
e1=Entry(window, width=30).grid(row=8,column=3)
l5 = Label(window, text=&quot;OWNER FULL LEGAL NAME OR BUSINESS NAME(if
business owned)&quot;).grid(row=9, column=1)
e1=Entry(window, width=45).grid(row=10,column=1)
l5 = Label(window, text=&quot;TELEPHONE NUMBER&quot;).grid(row=9, column=2)
e1=Entry(window, width=20).grid(row=10,column=2)
l5 = Label(window, text=&quot;DMV CUSTOMER NUMBER / FEIN /
SSN&quot;).grid(row=9, column=3)
e1=Entry(window, width=30).grid(row=10,column=3)
l6 = Label(window, text = &quot;Owners must provide their residence/
home/ business \n address where requested, this address cannot be a
P.O.Box \n your must complete ISD form if you would like your
address updated&quot;).grid(row=11, column=1)
l7=Label(window, text = &quot;RESIDENCE/ BUSINESS
JURISDICTION&quot;).grid(row=11, column=2)
e=Entry(window).grid(row=11, column=3)

l5 = Label(window, text=&quot;OWNER&#39;s RESIDENCE/ HOME/ BUSINESS
ADDRESS&quot;).grid(row=12, column=1)
e1=Entry(window, width=45).grid(row=13,column=1)
l5 = Label(window, text=&quot;CITY&quot;).grid(row=12, column=2)

e1=Entry(window, width=20).grid(row=13,column=2)
l5 = Label(window, text=&quot;ZIP CODE&quot;).grid(row=12, column=3)
e1=Entry(window, width=15).grid(row=13,column=3)
l5 = Label(window, text=&quot;CO-OWNER&#39;s RESIDENCE/ HOME/ BUSINESS
ADDRESS&quot;).grid(row=14, column=1)
e1=Entry(window, width=45).grid(row=15,column=1)
l5 = Label(window, text=&quot;CITY&quot;).grid(row=14, column=2)
e1=Entry(window, width=20).grid(row=15,column=2)
l5 = Label(window, text=&quot;ZIP CODE&quot;).grid(row=14, column=3)
e1=Entry(window, width=15).grid(row=15,column=3)
l5 = Label(window, text=&quot;OWNER EMAIL ADDRESS&quot;).grid(row=16,
column=1)
e1=Entry(window, width=20).grid(row=17,column=1)
l5 = Label(window, text=&quot;CO-OWNER EMAIL
ADDRESS&quot;).grid(row=16,column=2)
e1=Entry(window, width=20).grid(row=17,column=2)

window.mainloop()