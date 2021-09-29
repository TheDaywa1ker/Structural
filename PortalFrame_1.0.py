# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:35:17 2021

@author: Austin
"""

import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
# plt.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pprint


    #to do
        # - reactions vector                                         - done
        # - pinned column stiffness matrix                           - done
        # - 2-story and 2-bay frames                                 - done
        # - add deflections/reactions to GUI                         -done
        # - add frame sketches to GUI                                -done
        # - update deflection rotation to degrees from radians       -done
        # - multiple tabs in GUI? 2nd tab for member stresses
        # - font types
        # - pick column/beam size from dropdown - option to override
        # - add P-delta                                               -done
        # - destroy gui stuff on re-run...                             -done
    


class master_window:
    
        def __init__(self,master):
            
            # tk.Frame.__init__(self)
            self.master=master
            self.inputs=[]
            self.beam_inputs=[]
           
            
            self.load_types=['Point','Moment','Distributed']
            
            self.height=tk.StringVar()
            self.height2=tk.StringVar()
            self.width=tk.StringVar()
            self.width2=tk.StringVar()
            self.colA=tk.StringVar()
            self.colI=tk.StringVar()
            self.bmA=tk.StringVar()
            self.bmI=tk.StringVar()
            self.V=tk.StringVar()
            self.V2=tk.StringVar()
            self.w=tk.StringVar()
            self.w2=tk.StringVar()
            self.P=tk.StringVar()
            self.P2=tk.StringVar()
            self.x=tk.StringVar()
            self.x2=tk.StringVar()
            self.E=tk.StringVar()
            self.fixity=tk.StringVar()
            self.pdelta=tk.StringVar()
            self.loadstype=tk.StringVar()
            self.colsame=tk.StringVar()
            self.bmsame=tk.StringVar()
            self.frametype=tk.StringVar()
            self.pdeltaconvtol=tk.StringVar()
            
            self.height.set(10)
            self.height2.set(10)
            self.width.set(20)
            self.width2.set(20)
            self.colA.set(20)
            self.colI.set(723)
            self.bmA.set(11.8)
            self.bmI.set(612)
            self.V.set(50)
            self.V2.set(50)
            self.w.set(500)
            self.w2.set(100)
            self.P.set(10000)
            self.P2.set(0)
            self.x.set(10)
            self.x2.set(0)
            self.E.set(29000)
            self.fixity.set(1)
            self.pdelta.set(1)
            self.loadstype.set(0)
            self.colsame.set(0)
            self.bmsame.set(0)
            self.frametype.set('1 bay 1 story')
            self.pdeltaconvtol.set(.995)
       
            dx2_label=0
            dy2_label=0
            rot2_label=0
            dx3_label=0 
            dy3_label=0
            rot3_label=0
            
            rx1_label=0
            ry1_label=0
            M1_label=0
            rx4_label=0 
            ry4_label=0
            M4_label=0
       
            #Font set
            # self.f_size=10
            # self.helv=tkFont.Font(family=' Courier new',size=self.f_size,weight='bold')
            
            
# =============================================================================
#             Inputs
# =============================================================================
            

            
            frame1=tk.Frame(master,bd=2,relief='sunken')
            frame1.grid(row=2,column=1)
            
            tk.Label(frame1,text='Inputs',pady=4).grid(row=1,column=1,columnspan=2)
            
            tk.Label(frame1,text='Frame type',pady=4).grid(row=2,column=1)  
            tk.OptionMenu(frame1,self.frametype,'1 bay 1 story','2 bay 1 story','1 bay 2 story').grid(row=2,column=2)                                          
            
            tk.Label(frame1,text='Columns fixed?',width=15,anchor='w').grid(row=4,column=1)                       
            fixity_entry=tk.Checkbutton(frame1,variable=self.fixity).grid(row=4,column=2)                       
                               
            tk.Label(frame1,text="E (ksi):",width=15,anchor='e').grid(row=5,column=1)
            bmI_entry=tk.Entry(frame1,width=10,textvariable=self.E).grid(row=5,column=2)                                      
            
            tk.Label(frame1,text='Loads Input as:',pady=4).grid(row=7,column=1,columnspan=2)
     
            tk.Label(frame1, text='ASD',width=15,anchor='e').grid(row=8,column=1)
            tk.Label(frame1, text='LRFD',width=15,anchor='e').grid(row=9,column=1)
            
            tk.Radiobutton(frame1,variable=self.loadstype,value=0,anchor='w').grid(row=8,column=2)
            tk.Radiobutton(frame1,variable=self.loadstype,value=1,anchor='w').grid(row=9,column=2)                                                
            
            tk.Label(frame1,text='Include P-delta?',width=15,anchor='w',pady=4).grid(row=12,column=1)                       
            fixity_entry=tk.Checkbutton(frame1,variable=self.pdelta).grid(row=12,column=2)
            
            tk.Label(frame1,text='Pdelta conv. limit:',width=15,anchor='w').grid(row=13,column=1)
            pdeltaiterations_entry=tk.Entry(frame1,width=10,textvariable=self.pdeltaconvtol).grid(row=13,column=2)

            tk.Label(frame1,text='If not converging (nan)',width=20,anchor='w').grid(row=14,column=1,columnspan=3)
            tk.Label(frame1,text='decrease conv. limit',width=20,anchor='w').grid(row=15,column=1,columnspan=3)

            # tk.Label(frame1,text='All columns same?',width=15,anchor='w').grid(row=13,column=1)                       
            # fixity_entry=tk.Checkbutton(frame1,variable=self.colsame).grid(row=13,column=2)
            
            # tk.Label(frame1,text='All beams same?',width=15,anchor='w').grid(row=14,column=1)                       
            # fixity_entry=tk.Checkbutton(frame1,variable=self.bmsame).grid(row=14,column=2)
            
            tk.Label(frame1,text='',height=1).grid(row=16,column=1)   
            
            canvas=tk.Canvas(width=800,height=500,highlightthickness=1,highlightbackground="black")
            canvas.grid(row=1,column=2,padx=30,pady=20,rowspan=2)
            startx=175
            starty=400
            
            def build_frame(self,*event):
                                
                frametype=self.frametype.get()
                canvas.delete('all')
                if frametype=='1 bay 1 story':
                    canvas.delete('all')
                    
                    xdim=250
                    ydim=150
                    
                    V_label=tk.Label(canvas, text="V (k)=")
                    canvas.create_window(startx-95,starty-ydim-22,window=V_label,anchor='nw')
                    V_entry=tk.Entry(width=8,textvariable=self.V)
                    canvas.create_window(startx-60,starty-ydim-22,window=V_entry,anchor='nw')
                    
                    colA_label=tk.Label(canvas,text="Col. Area (in^2):")
                    canvas.create_window(startx-95,starty-ydim/2-20,window=colA_label,anchor='nw')
                    colA_entry=tk.Entry(width=8,textvariable=self.colA)
                    canvas.create_window(startx-60,starty-ydim/2-4,window=colA_entry,anchor='nw')
                                        
                    colI_label=tk.Label(canvas,text="Col Ix (in^4):")
                    canvas.create_window(startx-95,starty-ydim/2+12,window=colI_label,anchor='nw')
                    colI_entry=tk.Entry(width=8,textvariable=self.colI)
                    canvas.create_window(startx-60,starty-ydim/2+28,window=colI_entry,anchor='nw')
                   
                    bmA_label=tk.Label(canvas,text="Beam Area (in^2):")
                    canvas.create_window(startx+xdim/2-60,starty-ydim+2,window=bmA_label,anchor='nw')
                    bmA_entry=tk.Entry(width=8,textvariable=self.bmA)
                    canvas.create_window(startx+xdim/2-60,starty-ydim+18,window=bmA_entry,anchor='nw')
                    
                    bmI_label=tk.Label(canvas,text="Beam I (in^4):")
                    canvas.create_window(startx+xdim/2-60,starty-ydim+34,window=bmI_label,anchor='nw')
                    bmI_entry=tk.Entry(width=8,textvariable=self.bmI)
                    canvas.create_window(startx+xdim/2-60,starty-ydim+50,window=bmI_entry,anchor='nw')
                    
                    w_label=tk.Label(canvas,text="w (plf):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim-64,window=w_label,anchor='nw')
                    w_entry=tk.Entry(width=8,textvariable=self.w)
                    canvas.create_window(startx+xdim/2+5,starty-ydim-64,window=w_entry,anchor='nw')
                    
                    P_label=tk.Label(canvas,text="P (lbs):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim-48,window=P_label,anchor='nw')
                    P_entry=tk.Entry(width=8,textvariable=self.P)
                    canvas.create_window(startx+xdim/2+5,starty-ydim-48,window=P_entry,anchor='nw')
                    
                    x_label=tk.Label(canvas,text="P @ (ft):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim-32,window=x_label,anchor='nw')
                    x_entry=tk.Entry(width=8,textvariable=self.x)
                    canvas.create_window(startx+xdim/2+5,starty-ydim-32,window=x_entry,anchor='nw')                                        
                    
                    height_label=tk.Label(canvas,text="H(ft):")
                    canvas.create_window(startx-150,starty-ydim/2-30,window=height_label,anchor='nw')
                    height_entry=tk.Entry(width=8,textvariable=self.height)
                    canvas.create_window(startx-150,starty-ydim/2-14,window=height_entry,anchor='nw')
                    
                    canvas.create_line(startx-130,starty,startx-130,starty-ydim,arrow=tk.BOTH)
                    
                    width_label=tk.Label(canvas,text="L(ft):")
                    canvas.create_window(startx+xdim/2-30,starty+10,window=width_label,anchor='nw')
                    width_entry=tk.Entry(width=8,textvariable=self.width)
                    canvas.create_window(startx+xdim/2,starty+10,window=width_entry,anchor='nw')
                    
                    canvas.create_line(startx,starty+20,startx+xdim,starty+20,arrow=tk.BOTH)
                    
                    canvas.create_line(startx,starty,startx,starty-ydim,startx+xdim,starty-ydim,startx+xdim,starty,width=3)
                    canvas.create_line(startx,starty-ydim,startx-50,starty-ydim,arrow=tk.FIRST)      
                                  
                if frametype=='2 bay 1 story':
                    canvas.delete('all')
                                                           
                    xdim=500
                    ydim=150
                    
                    V_label=tk.Label(canvas, text="V (k)=")
                    canvas.create_window(startx-95,starty-ydim-22,window=V_label,anchor='nw')
                    V_entry=tk.Entry(width=8,textvariable=self.V)
                    canvas.create_window(startx-60,starty-ydim-22,window=V_entry,anchor='nw')
                    
                    colA_label=tk.Label(canvas,text="Col. Area (in^2):")
                    canvas.create_window(startx-95,starty-ydim/2-20,window=colA_label,anchor='nw')
                    colA_entry=tk.Entry(width=8,textvariable=self.colA)
                    canvas.create_window(startx-60,starty-ydim/2-4,window=colA_entry,anchor='nw')
                                        
                    colI_label=tk.Label(canvas,text="Col Ix (in^4):")
                    canvas.create_window(startx-95,starty-ydim/2+12,window=colI_label,anchor='nw')
                    colI_entry=tk.Entry(width=8,textvariable=self.colI)
                    canvas.create_window(startx-60,starty-ydim/2+28,window=colI_entry,anchor='nw')
                   
                    bmA_label=tk.Label(canvas,text="Beam Area (in^2):")
                    canvas.create_window(startx+xdim/4-60,starty-ydim+2,window=bmA_label,anchor='nw')
                    bmA_entry=tk.Entry(width=8,textvariable=self.bmA)
                    canvas.create_window(startx+xdim/4-60,starty-ydim+18,window=bmA_entry,anchor='nw')
                    
                    bmI_label=tk.Label(canvas,text="Beam I (in^4):")
                    canvas.create_window(startx+xdim/4-60,starty-ydim+34,window=bmI_label,anchor='nw')
                    bmI_entry=tk.Entry(width=8,textvariable=self.bmI)
                    canvas.create_window(startx+xdim/4-60,starty-ydim+50,window=bmI_entry,anchor='nw')
                    
                    w_label=tk.Label(canvas,text="w (plf):")
                    canvas.create_window(startx+xdim/4-50,starty-ydim-64,window=w_label,anchor='nw')
                    w_entry=tk.Entry(width=8,textvariable=self.w)
                    canvas.create_window(startx+xdim/4+5,starty-ydim-64,window=w_entry,anchor='nw')
                    
                    P_label=tk.Label(canvas,text="P (lbs):")
                    canvas.create_window(startx+xdim/4-50,starty-ydim-48,window=P_label,anchor='nw')
                    P_entry=tk.Entry(width=8,textvariable=self.P)
                    canvas.create_window(startx+xdim/4+5,starty-ydim-48,window=P_entry,anchor='nw')
                    
                    x_label=tk.Label(canvas,text="P @ (ft):")
                    canvas.create_window(startx+xdim/4-50,starty-ydim-32,window=x_label,anchor='nw')
                    x_entry=tk.Entry(width=8,textvariable=self.x)
                    canvas.create_window(startx+xdim/4+5,starty-ydim-32,window=x_entry,anchor='nw')
                    
                    w2_label=tk.Label(canvas,text="w (plf):")
                    canvas.create_window(startx+xdim*3/4-50,starty-ydim-64,window=w2_label,anchor='nw')
                    w2_entry=tk.Entry(width=8,textvariable=self.w2)
                    canvas.create_window(startx+xdim*3/4+5,starty-ydim-64,window=w2_entry,anchor='nw')
                    
                    P2_label=tk.Label(canvas,text="P (lbs):")
                    canvas.create_window(startx+xdim*3/4-50,starty-ydim-48,window=P2_label,anchor='nw')
                    P2_entry=tk.Entry(width=8,textvariable=self.P2)
                    canvas.create_window(startx+xdim*3/4+5,starty-ydim-48,window=P2_entry,anchor='nw')
                    
                    x2_label=tk.Label(canvas,text="P @ (ft):")
                    canvas.create_window(startx+xdim*3/4-50,starty-ydim-32,window=x2_label,anchor='nw')
                    x2_entry=tk.Entry(width=8,textvariable=self.x2)
                    canvas.create_window(startx+xdim*3/4+5,starty-ydim-32,window=x2_entry,anchor='nw')
                    
                    height_label=tk.Label(canvas,text="H(ft):")
                    canvas.create_window(startx-150,starty-ydim/2-30,window=height_label,anchor='nw')
                    height_entry=tk.Entry(width=8,textvariable=self.height)
                    canvas.create_window(startx-150,starty-ydim/2-14,window=height_entry,anchor='nw')
                    
                    canvas.create_line(startx-130,starty,startx-130,starty-ydim,arrow=tk.BOTH)
                    
                    width_label=tk.Label(canvas,text="L(ft):")
                    canvas.create_window(startx+xdim/4-30,starty+10,window=width_label,anchor='nw')
                    width_entry=tk.Entry(width=8,textvariable=self.width)
                    canvas.create_window(startx+xdim/4,starty+10,window=width_entry,anchor='nw')
                    
                    canvas.create_line(startx,starty+20,startx+xdim/2,starty+20,arrow=tk.BOTH)        
                    
                    width2_label=tk.Label(canvas,text="L(ft):")
                    canvas.create_window(startx+xdim*3/4-30,starty+10,window=width2_label,anchor='nw')
                    width2_entry=tk.Entry(width=8,textvariable=self.width2)
                    canvas.create_window(startx+xdim*3/4,starty+10,window=width2_entry,anchor='nw')
                    
                    canvas.create_line(startx+xdim/2,starty+20,startx+xdim,starty+20,arrow=tk.BOTH) 
                    
                    canvas.create_line(startx,starty,startx,starty-ydim,startx+xdim,starty-ydim,startx+xdim,starty,width=3)
                    canvas.create_line(startx+xdim/2,starty,startx+xdim/2,starty-ydim,width=3)
                    canvas.create_line(startx,starty-ydim,startx-50,starty-ydim,arrow=tk.FIRST)
                    
                if frametype=='1 bay 2 story':
                    canvas.delete('all')
                    
                    xdim=250
                    ydim=300
                    
                                        
                    V2_label=tk.Label(canvas, text="V (k)=")
                    canvas.create_window(startx-95,starty-ydim-22,window=V2_label,anchor='nw')
                    V2_entry=tk.Entry(width=8,textvariable=self.V2)
                    canvas.create_window(startx-60,starty-ydim-22,window=V2_entry,anchor='nw')
                    
                    V_label=tk.Label(canvas, text="V (k)=")
                    canvas.create_window(startx-95,starty-ydim/2-22,window=V_label,anchor='nw')
                    V_entry=tk.Entry(width=8,textvariable=self.V)
                    canvas.create_window(startx-60,starty-ydim/2-22,window=V_entry,anchor='nw')
                    
                    colA_label=tk.Label(canvas,text="Col. Area (in^2):")
                    canvas.create_window(startx-95,starty-ydim/4-20,window=colA_label,anchor='nw')
                    colA_entry=tk.Entry(width=8,textvariable=self.colA)
                    canvas.create_window(startx-60,starty-ydim/4-4,window=colA_entry,anchor='nw')
                                        
                    colI_label=tk.Label(canvas,text="Col Ix (in^4):")
                    canvas.create_window(startx-95,starty-ydim/4+12,window=colI_label,anchor='nw')
                    colI_entry=tk.Entry(width=8,textvariable=self.colI)
                    canvas.create_window(startx-60,starty-ydim/4+28,window=colI_entry,anchor='nw')
                   
                    bmA_label=tk.Label(canvas,text="Beam Area (in^2):")
                    canvas.create_window(startx+xdim/2-60,starty-ydim/2+2,window=bmA_label,anchor='nw')
                    bmA_entry=tk.Entry(width=8,textvariable=self.bmA)
                    canvas.create_window(startx+xdim/2-60,starty-ydim/2+18,window=bmA_entry,anchor='nw')
                    
                    bmI_label=tk.Label(canvas,text="Beam I (in^4):")
                    canvas.create_window(startx+xdim/2-60,starty-ydim/2+34,window=bmI_label,anchor='nw')
                    bmI_entry=tk.Entry(width=8,textvariable=self.bmI)
                    canvas.create_window(startx+xdim/2-60,starty-ydim/2+50,window=bmI_entry,anchor='nw')
                    
                    w_label=tk.Label(canvas,text="w (plf):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim-64,window=w_label,anchor='nw')
                    w_entry=tk.Entry(width=8,textvariable=self.w)
                    canvas.create_window(startx+xdim/2+5,starty-ydim-64,window=w_entry,anchor='nw')
                    
                    P_label=tk.Label(canvas,text="P (lbs):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim-48,window=P_label,anchor='nw')
                    P_entry=tk.Entry(width=8,textvariable=self.P)
                    canvas.create_window(startx+xdim/2+5,starty-ydim-48,window=P_entry,anchor='nw')
                    
                    x_label=tk.Label(canvas,text="P @ (ft):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim-32,window=x_label,anchor='nw')
                    x_entry=tk.Entry(width=8,textvariable=self.x)
                    canvas.create_window(startx+xdim/2+5,starty-ydim-32,window=x_entry,anchor='nw')
                    
                    w2_label=tk.Label(canvas,text="w (plf):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim/2-64,window=w2_label,anchor='nw')
                    w2_entry=tk.Entry(width=8,textvariable=self.w2)
                    canvas.create_window(startx+xdim/2+5,starty-ydim/2-64,window=w2_entry,anchor='nw')
                    
                    P2_label=tk.Label(canvas,text="P (lbs):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim/2-48,window=P2_label,anchor='nw')
                    P2_entry=tk.Entry(width=8,textvariable=self.P2)
                    canvas.create_window(startx+xdim/2+5,starty-ydim/2-48,window=P2_entry,anchor='nw')
                    
                    x2_label=tk.Label(canvas,text="P @ (ft):")
                    canvas.create_window(startx+xdim/2-50,starty-ydim/2-32,window=x2_label,anchor='nw')
                    x2_entry=tk.Entry(width=8,textvariable=self.x2)
                    canvas.create_window(startx+xdim/2+5,starty-ydim/2-32,window=x2_entry,anchor='nw')
                    
                    height_label=tk.Label(canvas,text="H(ft):")
                    canvas.create_window(startx-150,starty-ydim/4-30,window=height_label,anchor='nw')
                    height_entry=tk.Entry(width=8,textvariable=self.height)
                    canvas.create_window(startx-150,starty-ydim/4-14,window=height_entry,anchor='nw')
                    
                    canvas.create_line(startx-130,starty,startx-130,starty-ydim/2,arrow=tk.BOTH)
                    
                    height2_label=tk.Label(canvas,text="H(ft):")
                    canvas.create_window(startx-150,starty-ydim*3/4-30,window=height2_label,anchor='nw')
                    height2_entry=tk.Entry(width=8,textvariable=self.height2)
                    canvas.create_window(startx-150,starty-ydim*3/4-14,window=height2_entry,anchor='nw')
                    
                    canvas.create_line(startx-130,starty-ydim/2,startx-130,starty-ydim,arrow=tk.BOTH)
                    
                    width_label=tk.Label(canvas,text="L(ft):")
                    canvas.create_window(startx+xdim/2-30,starty+10,window=width_label,anchor='nw')
                    width_entry=tk.Entry(width=8,textvariable=self.width)
                    canvas.create_window(startx+xdim/2,starty+10,window=width_entry,anchor='nw')
                    
                    canvas.create_line(startx,starty+20,startx+xdim,starty+20,arrow=tk.BOTH)        
                    
                    
                    
                    canvas.create_line(startx,starty,startx,starty-ydim,startx+xdim,starty-ydim,startx+xdim,starty,width=3)
                    canvas.create_line(startx,starty-ydim/2,startx+xdim,starty-ydim/2,width=3)
                    canvas.create_line(startx,starty-ydim,startx-50,starty-ydim,arrow=tk.FIRST)
                    canvas.create_line(startx,starty-ydim/2,startx-50,starty-ydim/2,arrow=tk.FIRST)
                    
             
            tk.Button(frame1,text='Update Display',relief='raised',pady=2,width=14,command=lambda : build_frame(self)).grid(row=3,column=2)
            
# =============================================================================
#           Outputs
# =============================================================================
                                                                   
            def T(x,y,L):
                T=np.zeros((6,6))
                T[0][0]=x/L
                T[0][1]=y/L
                T[1][0]=-y/L
                T[1][1]=x/L
                T[2][2]=1
                T[3][3]=x/L
                T[3][4]=y/L
                T[4][3]=-y/L
                T[4][4]=x/L
                T[5][5]=1         
                return T
            
            def k_matrix(E,A,I,L,direction,fixity):

                matrix=np.zeros((6,6))
                if fixity=='1':                #local k fixed
                    matrix[0][0]=((A*L**2)/I)
                    matrix[0][1]=0
                    matrix[0][2]=0
                    matrix[0][3]=-1*matrix[0][0]
                    matrix[0][4]=0
                    matrix[0][5]=0
                    matrix[1][1]=12
                    matrix[1][2]=6*L
                    matrix[1][3]=0
                    matrix[1][4]=-12
                    matrix[1][5]=6*L
                    matrix[2][2]=4*L**2
                    matrix[2][3]=0
                    matrix[2][4]=-6* L
                    matrix[2][5]=2*L**2
                    matrix[3][3]=matrix[0][0]
                    matrix[3][4]=0
                    matrix[3][5]=0
                    matrix[4][4]=12
                    matrix[4][5]=-6*L
                    matrix[5][5]=4*L**2
                    matrix[1][0]=matrix[0][1]
                    matrix[2][0]=matrix[0][2]
                    matrix[2][1]=matrix[1][2]
                    matrix[3][0]=matrix[0][3]
                    matrix[3][1]=matrix[1][3]
                    matrix[3][2]=matrix[2][3]
                    matrix[4][0]=matrix[0][4]
                    matrix[4][1]=matrix[1][4]
                    matrix[4][2]=matrix[2][4]
                    matrix[4][3]=matrix[3][4]
                    matrix[5][0]=matrix[0][5]
                    matrix[5][1]=matrix[1][5]
                    matrix[5][2]=matrix[2][5]
                    matrix[5][3]=matrix[3][5]
                    matrix[5][4]=matrix[4][5]
                    matrix=(matrix*((E*I)/(L**3)))
                if fixity=='0' and direction=='up':
                    matrix=np.zeros((6,6))
                    matrix[0][0]=((A*L**2)/I)
                    matrix[0][1]=0
                    matrix[0][2]=0
                    matrix[0][3]=-1*matrix[0][0]
                    matrix[0][4]=0
                    matrix[0][5]=0
                    matrix[1][1]=3
                    matrix[1][2]=0
                    matrix[1][3]=0
                    matrix[1][4]=-3
                    matrix[1][5]=3*L
                    matrix[2][2]=0
                    matrix[2][3]=0
                    matrix[2][4]=0
                    matrix[2][5]=0
                    matrix[3][3]=matrix[0][0]
                    matrix[3][4]=0
                    matrix[3][5]=0
                    matrix[4][4]=3
                    matrix[4][5]=-3*L
                    matrix[5][5]=3*L**2
                    matrix[1][0]=matrix[0][1]
                    matrix[2][0]=matrix[0][2]
                    matrix[2][1]=matrix[1][2]
                    matrix[3][0]=matrix[0][3]
                    matrix[3][1]=matrix[1][3]
                    matrix[3][2]=matrix[2][3]
                    matrix[4][0]=matrix[0][4]
                    matrix[4][1]=matrix[1][4]
                    matrix[4][2]=matrix[2][4]
                    matrix[4][3]=matrix[3][4]
                    matrix[5][0]=matrix[0][5]
                    matrix[5][1]=matrix[1][5]
                    matrix[5][2]=matrix[2][5]
                    matrix[5][3]=matrix[3][5]
                    matrix[5][4]=matrix[4][5]
                    matrix=(matrix*((E*I)/(L**3)))    
                if fixity=='0' and direction=='dn':
                    matrix=np.zeros((6,6))
                    matrix[0][0]=((A*L**2)/I)
                    matrix[0][1]=0
                    matrix[0][2]=0
                    matrix[0][3]=-1*matrix[0][0]
                    matrix[0][4]=0
                    matrix[0][5]=0
                    matrix[1][1]=3
                    matrix[1][2]=3*L
                    matrix[1][3]=0
                    matrix[1][4]=-3
                    matrix[1][5]=0
                    matrix[2][2]=3*L**2
                    matrix[2][3]=0
                    matrix[2][4]=-3* L
                    matrix[2][5]=0
                    matrix[3][3]=matrix[0][0]
                    matrix[3][4]=0
                    matrix[3][5]=0
                    matrix[4][4]=3
                    matrix[4][5]=0
                    matrix[5][5]=0
                    matrix[1][0]=matrix[0][1]
                    matrix[2][0]=matrix[0][2]
                    matrix[2][1]=matrix[1][2]
                    matrix[3][0]=matrix[0][3]
                    matrix[3][1]=matrix[1][3]
                    matrix[3][2]=matrix[2][3]
                    matrix[4][0]=matrix[0][4]
                    matrix[4][1]=matrix[1][4]
                    matrix[4][2]=matrix[2][4]
                    matrix[4][3]=matrix[3][4]
                    matrix[5][0]=matrix[0][5]
                    matrix[5][1]=matrix[1][5]
                    matrix[5][2]=matrix[2][5]
                    matrix[5][3]=matrix[3][5]
                    matrix[5][4]=matrix[4][5]
                    matrix=(matrix*((E*I)/(L**3)))
                return matrix
                                        
            def global_transform(k,x,y,L):
                Tmat=T(x,y,L)
                Tt=np.transpose(Tmat)
                K=np.matmul(np.matmul(Tt,k),Tmat)
                return K
                         
            def beam_fef(P,L,a,w,x,y):
                cos=x/L
                FM1=0
                FM2=0
                FS1=0
                FS2=0
                if P==0:
                    pass
                else:
                    b=L-a
                    FM1+=(P*a*b**2)/(L**2)
                    FM2+=-(P*b*a**2)/(L**2)
                    FS1+=((P*b**2)/L**3)*(3*a+b)
                    FS2+=((P*a**2)/L**3)*(a+3*b)
                if w==0:
                    pass
                else:
                    FM1+=(w*L**2)/12
                    FM2+=-(w*L**2)/12
                    FS1+=FS1+w*L/2
                    FS2+=FS2+w*L/2
                
                return [0,FS1*cos,FM1,0,FS2*cos,FM2]   
                                           
            def combine_matrices_single_bay(col1_matrix,col2_matrix,bm_matrix):
                global_matrix=np.zeros((12,12))
                       
                global_matrix[0:6,0:6]+=col1_matrix #slice: ['start index':'end index'] - goes up to but will not include end index
                global_matrix[3:9,3:9]+=bm_matrix
                global_matrix[6:,6:]+=col2_matrix
                return global_matrix
            
            def combine_matrices_2s1b(col1matrix,col2matrix,col3matrix,col4matrix,bm1matrix,bm2matrix):
                global_matrix=np.zeros((18,18))
                
                global_matrix[0:6,0:6]+=col1matrix
                global_matrix[3:9,3:9]+=bm1matrix
                global_matrix[6:12,6:12]+=col2matrix
                global_matrix[12:,12:]+=bm2matrix
                global_matrix[3:6,3:6]+=col3matrix[:3,:3]
                global_matrix[12:15,3:6]+=col3matrix[3:,:3]
                global_matrix[3:6,12:15]+=col3matrix[:3,3:]
                global_matrix[12:15,12:15]+=col3matrix[3:,3:]
                global_matrix[6:9,6:9]+=col4matrix[:3,:3]
                global_matrix[15:,6:9]+=col4matrix[3:,:3]
                global_matrix[6:9,15:]+=col4matrix[:3,3:]
                global_matrix[15:,15:]+=col4matrix[3:,3:]
                
                return global_matrix
            
            def combine_matrices_2b1s(col1matrix,col2matrix,col3matrix,bm1matrix,bm2matrix):
                global_matrix=np.zeros((18,18))
                
                global_matrix[0:6,0:6]+=col1matrix
                global_matrix[3:9,3:9]+=bm1matrix
                global_matrix[6:12,6:12]+=col2matrix
                global_matrix[12:,12:]+=col3matrix
                global_matrix[6:9,6:9]+=bm2matrix[0:3,0:3]
                global_matrix[12:15,12:15]+=bm2matrix[3:,3:]
                global_matrix[12:15,6:9]+=bm2matrix[3:,0:3]
                global_matrix[6:9,12:15]+=bm2matrix[0:3,3:]
                
                return global_matrix
            
            def reactions_matrix(globalmatrix):
                rxn_matrix=np.zeros((6,6))
                
                rxn_matrix[0:3,0:3]+=globalmatrix[3:6,:3]
                rxn_matrix[3:,3:]+=globalmatrix[6:9,9:]
               
                return rxn_matrix
            
            def beam_moment(m1,m2,P,a,w,L):
                b=L-a
                l = np.linspace(0, L, 1000)  
                R1=(P*b/L)
                R2=(P*a/L)                
                V=np.zeros(len(l))                
                M=np.zeros(len(l))
                
                
                #point load shear/moment diagram
                for x in range(len(l)):
                    if l[x] <= a:
                        m = R1*l[x]
                        v = R1
                    elif l[x] > a:
                        m = R1*l[x] - P*(l[x]-a)
                        v = -R2
                    M[x]+=m                    
                    V[x]+=v
                    
                #beam end moments moment diagram
                for x in range(len(l)):
                    M[x]+=(-1*abs(m1)/L)*l[x]+abs(m1)
                    M[x]+=(-1*abs(m2)/L)*l[x]
                
                #distributed load moment diagram
                for x in range(len(l)):
                    M[x]+=(w*l[x]/2)*(L-l[x])
                    V[x]+=w*((L/2)-l[x])
                    
                # plt.figure()
                # plt.plot(l,M)
                # plt.show(block=False)
                                  
                return max(M)/12,min(M)/12
                
                     
            def run(self,*event):
                self.inputs=[]
                                                                                                                                                                         
                canvas.delete('all')
                
                frametype=self.frametype.get()
                
                if frametype=='1 bay 1 story':
 
                    xdim=250
                    ydim=150
                    
                    canvas.create_line(startx,starty,startx,starty-ydim,startx+xdim,starty-ydim,startx+xdim,starty,width=3)
                    canvas.create_line(startx,starty-ydim,startx-50,starty-ydim,arrow=tk.FIRST)  
                                
                    height=float(self.height.get())*12.0             #inches
                    width=float(self.width.get())*12.0
                    colA=float(self.colA.get())
                    colI=float(self.colI.get())
                    fixity=self.fixity.get()
                    bmA=float(self.bmA.get())
                    bmI=float(self.bmI.get())
                    E=float(self.E.get())
                    V=float(self.V.get())
                    w=float(self.w.get())/12000.0
                    P=float(self.P.get())/1000.0
                    x=float(self.x.get())*12.0
                    pdelta=self.pdelta.get()
                    loadstype=self.loadstype.get()
                    pdeltaconvtol=float(self.pdeltaconvtol.get())
                  
                    col1props=[E,colA,colI,height,'up',fixity]
                    col1dofs=[0,1,2,3,4,5]
                    col2props=[E,colA,colI,height,'dn',fixity]
                    col2dofs=[6,7,8,9,10,11]
                    bmprops=[E,bmA,bmI,width,'up','1']
                    bmdofs=[3,4,5,6,7,8]
                    
                    col1localk=k_matrix(*col1props)
                    col2localk=k_matrix(*col2props)
                    bmlocalk=k_matrix(*bmprops) 

                    col1globalk=global_transform(col1localk,0,height,height)
                    col2globalk=global_transform(col2localk,0,-1*height,height)
                    bmglobalk=global_transform(bmlocalk,width,0,width)  

                    glmatrix=combine_matrices_single_bay(col1globalk,col2globalk,bmglobalk)
                    fef=beam_fef(P,width,x,w,width,0)  
                    loads=np.zeros(6)
                    loads[0]=V/2
                    loads[3]=V/2
                    F=loads-fef
                    
                    d=np.linalg.solve(glmatrix[3:9,3:9],F)
                    dglob=np.zeros(12)
                    dglob[3:9]+=d
                    
                    col1v=dglob[0:6]
                    col1T=T(0,height,height)
                    col1Tt=np.transpose(col1T)
                    col1u=np.matmul(col1T,col1v)
                    col1Q=np.matmul(col1localk,col1u)        #local
                    col1R=np.matmul(col1Tt,col1Q)       #global
                                                                                
                    col2v=dglob[6:]
                    col2T=T(0,-1*height,height)
                    col2Tt=np.transpose(col2T)
                    col2u=np.matmul(col2T,col2v)
                    col2Q=np.matmul(col2localk,col2u)        #local
                    col2R=np.matmul(col2Tt,col2Q)
                                                             
                    bmv=dglob[3:9]    
                    bmT=T(width,0,width)
                    bmTt=np.transpose(bmT)
                    bmu=np.matmul(bmT,bmv)
                    bmQ=np.matmul(bmlocalk,bmu)-F                                        
                    bmR=np.matmul(bmTt,bmQ)
                                       
                    r=np.zeros(6)
                    r[:3]+=col1R[:3]
                    r[3:]+=col2R[3:]
                    
                    r[2]=r[2]/12
                    r[5]=r[5]/12
                    
                    d[2]=d[2]*180/3.14159
                    d[5]=d[5]*180/3.14159
                                                            
                    if pdelta=='1':
                        convergence=0
                        iterations=0
                                                                       
                        if loadstype=='0':
                            F=F*1.6
                            
                        # number of pdelta iterations
                        while convergence<=pdeltaconvtol:    
                                         
                            dinit=d
                            col1pd_v=d[0]*col1R[4]/height
                            F[0]+=col1pd_v
                            col2pd_v=d[3]*col2R[0]/height
                            F[3]+=col2pd_v
                            
                            d=np.linalg.solve(glmatrix[3:9,3:9],F)      #[x1,y2,rot]
                            dglob=np.zeros(12)
                            dglob[3:9]+=d
                            
                            col1v=dglob[0:6]
                            col2v=dglob[6:]
                            bmv=dglob[3:9] 
                                                        
                            col1u=np.matmul(col1T,col1v)
                            col1Q=np.matmul(col1localk,col1u)        #local
                            col1R=np.matmul(col1Tt,col1Q) 
                            
                            col2u=np.matmul(col2T,col2v)
                            col2Q=np.matmul(col2localk,col2u)        #local
                            col2R=np.matmul(col2Tt,col2Q)
                            
                            bmu=np.matmul(bmT,bmv)
                            bmQ=np.matmul(bmlocalk,bmu)-F                                        
                            bmR=np.matmul(bmTt,bmQ)
                                                        
                            r=np.zeros(6)
                            r[:3]+=col1R[:3]
                            r[3:]+=col2R[3:]
                            
                            r[2]=r[2]/12
                            r[5]=r[5]/12
                            
                            d[2]=d[2]*180/3.14159
                            d[5]=d[5]*180/3.14159
                            
                            convergence=dinit[0]/d[0]*1.6
                            iterations=iterations+1

                            if loadstype=='0':
                                r=r/1.6
                                d=d/1.6
                                col1R=col1R/1.6
                                col2R=col2R/1.6
                                bmR=bmR/1.6

                        convergence_label=tk.Label(canvas,text='Pdelta convergence= '+str(round(convergence,3))) 
                        canvas.create_window((startx+xdim)/2+30, starty+59,window=convergence_label,anchor='nw')    
                        
                        iterations_label=tk.Label(canvas,text='Iterations= '+str(iterations)) 
                        canvas.create_window((startx+xdim)/2+30, starty+75,window=iterations_label,anchor='nw') 
                        
                    bmM=beam_moment(-1*bmR[2],bmR[5],P,x,w,width)
                    col1M=[-1*col1R[2]/12,col1R[5]/12]
                    col2M=[col2R[2]/12,-1*col2R[5]/12]  

                    #displacement label placement
                    #have to use 'create window' because using 'place' wont allow the label to be destroyed each run
                    dx2_label=tk.Label(canvas,text='dx= '+str(round(d[0],3))+' in')
                    canvas.create_window(startx,starty-ydim-62,window=dx2_label,anchor='nw')
                    dy2_label=tk.Label(canvas,text='dy= '+str(round(d[1],3))+' in')
                    canvas.create_window(startx,starty-ydim-45,window=dy2_label,anchor='nw')
                    rot2_label=tk.Label(canvas,text='rot='+str(round(d[2],3))+' deg')
                    canvas.create_window(startx,starty-ydim-28,window=rot2_label,anchor='nw')                
                    dx3_label=tk.Label(canvas,text='dx= '+str(round(d[3],3))+' in') 
                    canvas.create_window(startx+xdim,starty-ydim-62,window=dx3_label,anchor='nw')
                    dy3_label=tk.Label(canvas,text='dy= '+str(round(d[4],3))+' in')
                    canvas.create_window(startx+xdim,starty-ydim-45,window=dy3_label,anchor='nw')
                    rot3_label=tk.Label(canvas,text='rot= '+str(round(d[5],3))+' deg')
                    canvas.create_window(startx+xdim,starty-ydim-28,window=rot3_label,anchor='nw')
                                    
                    #reaction label placement
                    rx1_label=tk.Label(canvas,text='Rx= '+str(round(r[0],3))+' k')
                    canvas.create_window(startx,starty,window=rx1_label,anchor='nw')                
                    ry1_label=tk.Label(canvas,text='Ry= '+str(round(r[1],3))+' k')
                    canvas.create_window(startx,starty+17,window=ry1_label,anchor='nw')
                    M1_label=tk.Label(canvas,text='M= '+str(round(r[2],3))+' ft-k')
                    canvas.create_window(startx,starty+34,window=M1_label,anchor='nw')
                    rx4_label=tk.Label(canvas,text='Rx= '+str(round(r[3],3))+' k')   
                    canvas.create_window(startx+xdim,starty,window=rx4_label,anchor='nw')
                    ry4_label=tk.Label(canvas,text='Ry= '+str(round(r[4],3))+' k')
                    canvas.create_window(startx+xdim,starty+17,window=ry4_label,anchor='nw')
                    M4_label=tk.Label(canvas,text='M= '+str(round(r[5],3))+' ft-k')
                    canvas.create_window(startx+xdim,starty+34,window=M4_label,anchor='nw')
                    
                    #max moment label placement
                    bmMmax_label=tk.Label(canvas,text='Mmax= '+str(round(bmM[0],1))+' ft-k')
                    canvas.create_window(startx+xdim/3,starty-ydim+2,window=bmMmax_label,anchor='nw')
                    bmMmin_label=tk.Label(canvas,text='Mmin= '+str(round(bmM[1],1))+' ft-k')
                    canvas.create_window(startx+xdim/3,starty-ydim+18,window=bmMmin_label,anchor='nw')
                    c1Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col1M[1],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim/2-8,window=c1Mmax_label,anchor='nw')
                    c1Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col1M[0],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim/2+8,window=c1Mmin_label,anchor='nw')
                    c2Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col2M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim/2-8,window=c2Mmax_label,anchor='nw')
                    c2Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col2M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim/2+8,window=c2Mmin_label,anchor='nw')
    
                    drift_label=tk.Label(canvas,text='Drift = L/'+str(int(round(height/max(d[0],d[3]),0))))
                    canvas.create_window((startx+xdim)/2-50,starty+60,window=drift_label,anchor='nw')
                                
                if frametype=='2 bay 1 story':
 
                    xdim=500
                    ydim=150
                    
                    canvas.create_line(startx,starty,startx,starty-ydim,startx+xdim,starty-ydim,startx+xdim,starty,width=3)
                    canvas.create_line(startx+xdim/2,starty,startx+xdim/2,starty-ydim,width=3)
                    canvas.create_line(startx,starty-ydim,startx-50,starty-ydim,arrow=tk.FIRST)
                                
                    height=float(self.height.get())*12.0
                    width=float(self.width.get())*12.0
                    width2=float(self.width2.get())*12.0
                    colA=float(self.colA.get())
                    colI=float(self.colI.get())
                    fixity=self.fixity.get()
                    bmA=float(self.bmA.get())
                    bmI=float(self.bmI.get())
                    E=float(self.E.get())
                    V=float(self.V.get())
                    w=float(self.w.get())/12000.0
                    w2=float(self.w2.get())/12000.0
                    P=float(self.P.get())/1000.0
                    P2=float(self.P2.get())/1000.0
                    x=float(self.x.get())*12.0
                    x2=float(self.x2.get())*12.0
                    pdelta=self.pdelta.get()
                    loadstype=self.loadstype.get()
                    pdeltaconvtol=float(self.pdeltaconvtol.get())
                  
                    col1props=[E,colA,colI,height,'up',fixity]
                    col1dofs=[0,1,2,3,4,5]
                    col2props=[E,colA,colI,height,'dn',fixity]
                    col2dofs=[6,7,8,9,10,11]
                    col3props=[E,colA,colI,height,'dn',fixity]
                    col3dofs=[]
                    bm1props=[E,bmA,bmI,width,'up','1']
                    bm1dofs=[3,4,5,6,7,8]
                    bm2props=[E,bmA,bmI,width,'up','1']
                    bm2dofs=[3,4,5,6,7,8]
                    
                    col1localk=k_matrix(*col1props)
                    col2localk=k_matrix(*col2props)
                    col3localk=k_matrix(*col3props)
                    bm1localk=k_matrix(*bm1props) 
                    bm2localk=k_matrix(*bm2props)

                    col1globalk=global_transform(col1localk,0,height,height)
                    col2globalk=global_transform(col2localk,0,-1*height,height)
                    col3globalk=global_transform(col3localk,0,-1*height,height)
                    bm1globalk=global_transform(bm1localk,width,0,width)
                    bm2globalk=global_transform(bm2localk,width2,0,width2)

                    glmatrix=combine_matrices_2b1s(col1globalk,col2globalk,col3globalk,bm1globalk,bm2globalk)
                    new_indexes=[3,4,5,6,7,8,12,13,14,0,1,2,9,10,11,15,16,17]
                    glmatrix_rearranged=np.zeros((18,18))
                    glmatrix_rearranged+=[[glmatrix[i][j] for j in new_indexes] for i in new_indexes]
                    
                    fef=np.zeros(9)
                    fef1=beam_fef(P,width,x,w,width,0)
                    fef2=beam_fef(P2,width2,x2,w2,width2,0)
                    fef[:6]+=fef1
                    fef[3:]+=fef2
                    loads=np.zeros(9)
                    loads[0]=V/3
                    loads[3]=V/3
                    loads[6]=V/3
                    
                    F=loads-fef                    
                    d=np.linalg.solve(glmatrix_rearranged[0:9,0:9],F)
                    dglob=np.zeros(18)
                    dglob[:9]+=d
                                                            
                    col1v=np.zeros((6))
                    col1v[:3]+=dglob[9:12]
                    col1v[3:]+=dglob[:3]
                    col1T=T(0,height,height)
                    col1Tt=np.transpose(col1T)
                    col1u=np.matmul(col1T,col1v)
                    col1Q=np.matmul(col1localk,col1u)        #local
                    col1R=np.matmul(col1Tt,col1Q)       #global
                    
                    col2v=np.zeros(6)
                    col2v[:3]+=dglob[3:6]
                    col2v[3:]+=dglob[12:15]
                    col2T=T(0,-1*height,height)
                    col2Tt=np.transpose(col2T)
                    col2u=np.matmul(col2T,col2v)
                    col2Q=np.matmul(col2localk,col2u)        #local
                    col2R=np.matmul(col2Tt,col2Q)
                    
                    col3v=np.zeros(6)
                    col3v[:3]+=dglob[6:9]
                    col3v[3:]+=dglob[15:]
                    col3T=T(0,-1*height,height)
                    col3Tt=np.transpose(col3T)
                    col3u=np.matmul(col3T,col3v)
                    col3Q=np.matmul(col3localk,col3u)        #local
                    col3R=np.matmul(col3Tt,col3Q)
                    
                    bm1v=dglob[:6]    
                    bm1T=T(width,0,width)
                    bm1Tt=np.transpose(bm1T)
                    bm1u=np.matmul(bm1T,bm1v)
                    bm1Q=np.matmul(bm1localk,bm1u)-F[0:6]                                        
                    bm1R=np.matmul(bm1Tt,bm1Q)
                    
                    bm2v=dglob[3:9]    
                    bm2T=T(width2,0,width2)
                    bm2Tt=np.transpose(bm2T)
                    bm2u=np.matmul(bm2T,bm2v)
                    bm2Q=np.matmul(bm2localk,bm2u)-F[3:]                                        
                    bm2R=np.matmul(bm2Tt,bm2Q)
                                                            
                    r=np.zeros(9)
                    r[:3]+=col1R[:3]
                    r[3:6]+=col2R[3:]
                    r[6:]+=col3R[3:]
                                        
                    r[2]=r[2]/12
                    r[5]=r[5]/12
                    r[8]=r[8]/12
                    
                    d[2]=d[2]*180/3.14159
                    d[5]=d[5]*180/3.14159
                    d[8]=d[8]*180/3.14159
                                                        
                    if pdelta=='1':
                        convergence=0
                        iterations=0
                        
                        if loadstype=='0':
                            F=F*1.6
                            
                        # number of pdelta iterations
                        while convergence <= pdeltaconvtol:    
                                         
                            dinit=d
                            col1pd_v=d[0]*col1R[4]/height
                            F[0]+=col1pd_v
                            col2pd_v=d[3]*col2R[0]/height
                            F[3]+=col2pd_v
                            col3pd_v=d[6]*col3R[0]/height
                            F[6]+=col3pd_v
                            
                            d=np.linalg.solve(glmatrix_rearranged[:9,:9],F)      #[x1,y2,rot]
                            dglob=np.zeros(18)
                            dglob[:9]+=d                                                                                    
                            
                            col1v=np.zeros((6))
                            col1v[:3]+=dglob[9:12]
                            col1v[3:]+=dglob[:3]
                            col1u=np.matmul(col1T,col1v)
                            col1Q=np.matmul(col1localk,col1u)        #local
                            col1R=np.matmul(col1Tt,col1Q) 
                            
                            col2v=np.zeros(6)
                            col2v[:3]+=dglob[3:6]
                            col2v[3:]+=dglob[12:15]
                            col2u=np.matmul(col2T,col2v)
                            col2Q=np.matmul(col2localk,col2u)        #local
                            col2R=np.matmul(col2Tt,col2Q)
                            
                            col3v=np.zeros(6)
                            col3v[:3]+=dglob[6:9]
                            col3v[3:]+=dglob[15:]
                            col3u=np.matmul(col3T,col3v)
                            col3Q=np.matmul(col3localk,col3u)        #local
                            col3R=np.matmul(col3Tt,col3Q)
                            
                            bm1v=dglob[:6]    
                            bm1T=T(width,0,width)
                            bm1Tt=np.transpose(bm1T)
                            bm1u=np.matmul(bm1T,bm1v)
                            bm1Q=np.matmul(bm1localk,bm1u)-F[0:6]                                        
                            bm1R=np.matmul(bm1Tt,bm1Q)
                            
                            bm2v=dglob[3:9]    
                            bm2T=T(width,0,width)
                            bm2Tt=np.transpose(bm2T)
                            bm2u=np.matmul(bm2T,bm2v)
                            bm2Q=np.matmul(bm2localk,bm2u)-F[3:]                                        
                            bm2R=np.matmul(bm2Tt,bm2Q)
                            
                            r=np.zeros(9)
                            r[:3]+=col1R[:3]
                            r[3:6]+=col2R[3:]
                            r[6:]+=col3R[3:]
                            
                            r[2]=r[2]/12
                            r[5]=r[5]/12
                            r[8]=r[8]/12
                            
                            d[2]=d[2]*180/3.14159
                            d[5]=d[5]*180/3.14159
                            d[8]=d[8]*180/3.14159
                                                        
                            convergence=dinit[0]/d[0]*1.6
                            iterations=iterations+1
                            
                            if loadstype=='0':
                                r=r/1.6
                                d=d/1.6
                                col1R=col1R/1.6
                                col2R=col2R/1.6
                                col3R=col3R/1.6
                                bm1R=bm1R/1.6
                                bm2R=bm2R/1.6
                                
                        convergence_label=tk.Label(canvas,text='Pdelta convergence= '+str(round(convergence,3))) 
                        canvas.create_window((startx+xdim)/2+30, starty+59,window=convergence_label,anchor='nw')    
                        
                        iterations_label=tk.Label(canvas,text='Iterations= '+str(iterations)) 
                        canvas.create_window((startx+xdim)/2+30, starty+75,window=iterations_label,anchor='nw')                     
                    
                    
                    bm1M=beam_moment(-1*bm1R[2],bm1R[5],P,x,w,width)
                    bm2M=beam_moment(-1*bm2R[2],bm2R[5],P2,x2,w2,width2)
                    col1M=[-1*col1R[2]/12,col1R[5]/12]
                    col2M=[col2R[2]/12,-1*col2R[5]/12]     
                    col3M=[col3R[2]/12,-1*col3R[5]/12]  
                    
                    
                    
                    #displacement label placement
                    #have to use 'create window' because using 'place' wont allow the label to be destroyed each run
                    dx2_label=tk.Label(canvas,text='dx= '+str(round(d[0],3))+' in')
                    canvas.create_window(startx,starty-ydim-62,window=dx2_label,anchor='nw')
                    dy2_label=tk.Label(canvas,text='dy= '+str(round(d[1],3))+' in')
                    canvas.create_window(startx,starty-ydim-45,window=dy2_label,anchor='nw')
                    rot2_label=tk.Label(canvas,text='rot='+str(round(d[2],3))+' deg')
                    canvas.create_window(startx,starty-ydim-28,window=rot2_label,anchor='nw')                
                    dx3_label=tk.Label(canvas,text='dx= '+str(round(d[3],3))+' in') 
                    canvas.create_window(startx+xdim/2,starty-ydim-62,window=dx3_label,anchor='nw')
                    dy3_label=tk.Label(canvas,text='dy= '+str(round(d[4],3))+' in')
                    canvas.create_window(startx+xdim/2,starty-ydim-45,window=dy3_label,anchor='nw')
                    rot3_label=tk.Label(canvas,text='rot= '+str(round(d[5],3))+' deg')
                    canvas.create_window(startx+xdim/2,starty-ydim-28,window=rot3_label,anchor='nw')
                    dx5_label=tk.Label(canvas,text='dx= '+str(round(d[6],3))+' in') 
                    canvas.create_window(startx+xdim,starty-ydim-62,window=dx5_label,anchor='nw')
                    dy5_label=tk.Label(canvas,text='dy= '+str(round(d[7],3))+' in')
                    canvas.create_window(startx+xdim,starty-ydim-45,window=dy5_label,anchor='nw')
                    rot5_label=tk.Label(canvas,text='rot= '+str(round(d[8],3))+' deg')
                    canvas.create_window(startx+xdim,starty-ydim-28,window=rot5_label,anchor='nw')
                                    
                    #reaction label placement
                    rx1_label=tk.Label(canvas,text='Rx= '+str(round(r[0],3))+' k')
                    canvas.create_window(startx,starty,window=rx1_label,anchor='nw')                
                    ry1_label=tk.Label(canvas,text='Ry= '+str(round(r[1],3))+' k')
                    canvas.create_window(startx,starty+17,window=ry1_label,anchor='nw')
                    M1_label=tk.Label(canvas,text='M= '+str(round(r[2],3))+' ft-k')
                    canvas.create_window(startx,starty+34,window=M1_label,anchor='nw')
                    rx4_label=tk.Label(canvas,text='Rx= '+str(round(r[3],3))+' k')   
                    canvas.create_window(startx+xdim/2,starty,window=rx4_label,anchor='nw')
                    ry4_label=tk.Label(canvas,text='Ry= '+str(round(r[4],3))+' k')
                    canvas.create_window(startx+xdim/2,starty+17,window=ry4_label,anchor='nw')
                    M4_label=tk.Label(canvas,text='M= '+str(round(r[5],3))+' ft-k')
                    canvas.create_window(startx+xdim/2,starty+34,window=M4_label,anchor='nw')
                    rx6_label=tk.Label(canvas,text='Rx= '+str(round(r[6],3))+' k')   
                    canvas.create_window(startx+xdim,starty,window=rx6_label,anchor='nw')
                    ry6_label=tk.Label(canvas,text='Ry= '+str(round(r[7],3))+' k')
                    canvas.create_window(startx+xdim,starty+17,window=ry6_label,anchor='nw')
                    M6_label=tk.Label(canvas,text='M= '+str(round(r[8],3))+' ft-k')
                    canvas.create_window(startx+xdim,starty+34,window=M6_label,anchor='nw')
                    
                    #max moment label placement
                    bm1Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(bm1M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim/6,starty-ydim+2,window=bm1Mmax_label,anchor='nw')
                    bm1Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(bm1M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim/6,starty-ydim+18,window=bm1Mmin_label,anchor='nw')
                    bm2Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(bm2M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim*5/8,starty-ydim+2,window=bm2Mmax_label,anchor='nw')
                    bm2Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(bm2M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim*5/8,starty-ydim+18,window=bm2Mmin_label,anchor='nw')                   
                    c1Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col1M[1],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim/2-8,window=c1Mmax_label,anchor='nw')
                    c1Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col1M[0],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim/2+8,window=c1Mmin_label,anchor='nw')
                    c2Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col2M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim/2+2,starty-ydim/2-8,window=c2Mmax_label,anchor='nw')
                    c2Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col2M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim/2+2,starty-ydim/2+8,window=c2Mmin_label,anchor='nw')
                    c3Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col3M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim/2-8,window=c3Mmax_label,anchor='nw')
                    c3Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col3M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim/2+8,window=c3Mmin_label,anchor='nw')
    
                    drift_label=tk.Label(canvas,text='Drift = L/'+str(int(round(height/max(d[0],d[3]),0))))
                    canvas.create_window((startx+xdim)/2-50,starty+60,window=drift_label,anchor='nw')
                    
                if frametype=='1 bay 2 story':
                    
                    xdim=250
                    ydim=300
                    
                    canvas.create_line(startx,starty,startx,starty-ydim,startx+xdim,starty-ydim,startx+xdim,starty,width=3)
                    canvas.create_line(startx,starty-ydim/2,startx+xdim,starty-ydim/2,width=3)
                    canvas.create_line(startx,starty-ydim,startx-50,starty-ydim,arrow=tk.FIRST)
                    canvas.create_line(startx,starty-ydim/2,startx-50,starty-ydim/2,arrow=tk.FIRST)
                    
                    height=float(self.height.get())*12.0
                    height2=float(self.height2.get())*12.0
                    width=float(self.width.get())*12.0
                    colA=float(self.colA.get())
                    colI=float(self.colI.get())
                    fixity=self.fixity.get()
                    bmA=float(self.bmA.get())
                    bmI=float(self.bmI.get())
                    E=float(self.E.get())
                    V=float(self.V.get())
                    V2=float(self.V2.get())
                    w=float(self.w.get())/12000.0
                    w2=float(self.w2.get())/12000.0
                    P=float(self.P.get())/1000.0
                    P2=float(self.P2.get())/1000.0
                    x=float(self.x.get())*12.0
                    x2=float(self.x2.get())*12.0
                    pdelta=self.pdelta.get()
                    loadstype=self.loadstype.get()
                    pdeltaconvtol=float(self.pdeltaconvtol.get())
                    
                    col1props=[E,colA,colI,height,'up',fixity]
                    col1dofs=[0,1,2,3,4,5]
                    col2props=[E,colA,colI,height,'dn',fixity]
                    col2dofs=[6,7,8,9,10,11]
                    col3props=[E,colA,colI,height2,'up',fixity]
                    col3dofs=[3,4,5,12,13,14]
                    col4props=[E,colA,colI,height2,'up',fixity]
                    col4dofs=[6,7,8,15,16,17]
                    bm1props=[E,bmA,bmI,width,'up','1']
                    bm1dofs=[3,4,5,6,7,8]
                    bm2props=[E,bmA,bmI,width,'up','1']
                    bm2dofs=[12,13,14,15,16,17]
                    
                    col1localk=k_matrix(*col1props)
                    col2localk=k_matrix(*col2props)
                    col3localk=k_matrix(*col3props)
                    col4localk=k_matrix(*col4props)
                    bm1localk=k_matrix(*bm1props) 
                    bm2localk=k_matrix(*bm2props)
                    
                    col1globalk=global_transform(col1localk,0,height,height)
                    col2globalk=global_transform(col2localk,0,-1*height,height)
                    col3globalk=global_transform(col3localk,0,height2,height)
                    col4globalk=global_transform(col4localk,0,height2,height)
                    bm1globalk=global_transform(bm1localk,width,0,width)
                    bm2globalk=global_transform(bm2localk,width,0,width)
                    
                    glmatrix=combine_matrices_2s1b(col1globalk,col2globalk,col3globalk,col4globalk,bm1globalk,bm2globalk)
                    new_indexes=[3,4,5,6,7,8,12,13,14,15,16,17,0,1,2,9,10,11]
                    glmatrix_rearranged=np.zeros((18,18))
                    glmatrix_rearranged+=[[glmatrix[i][j] for j in new_indexes] for i in new_indexes]
                    
                    fef=np.zeros(12)
                    fef1=beam_fef(P,width,x,w,width,0)
                    fef2=beam_fef(P2,width,x2,w2,width,0)
                    fef[:6]+=fef1
                    fef[6:]+=fef2
                    loads=np.zeros(12)
                    loads[0]=V/2
                    loads[3]=V/2
                    loads[6]=V2/2
                    loads[9]=V2/2
                    
                    F=loads-fef                    
                    d=np.linalg.solve(glmatrix_rearranged[0:12,0:12],F)
                    dglob=np.zeros(18)
                    dglob[:12]+=d
                    
                    col1v=np.zeros((6))
                    col1v[:3]+=dglob[12:15]
                    col1v[3:]+=dglob[:3]
                    col1T=T(0,height,height)
                    col1Tt=np.transpose(col1T)
                    col1u=np.matmul(col1T,col1v)
                    col1Q=np.matmul(col1localk,col1u)        #local
                    col1R=np.matmul(col1Tt,col1Q)       #global
                    
                    col2v=np.zeros(6)
                    col2v[:3]+=dglob[3:6]
                    col2v[3:]+=dglob[15:]
                    col2T=T(0,-1*height,height)
                    col2Tt=np.transpose(col2T)
                    col2u=np.matmul(col2T,col2v)
                    col2Q=np.matmul(col2localk,col2u)        #local
                    col2R=np.matmul(col2Tt,col2Q)
                    
                    col3v=np.zeros(6)
                    col3v[:3]+=dglob[6:9]
                    col3v[3:]+=dglob[0:3]
                    col3T=T(0,-1*height,height)
                    col3Tt=np.transpose(col3T)
                    col3u=np.matmul(col3T,col3v)
                    col3Q=np.matmul(col3localk,col3u)        #local
                    col3R=np.matmul(col3Tt,col3Q)
                    
                    col4v=np.zeros(6)
                    col4v[:3]+=dglob[9:12]
                    col4v[3:]+=dglob[3:6]
                    col4T=T(0,-1*height,height)
                    col4Tt=np.transpose(col2T)
                    col4u=np.matmul(col4T,col4v)
                    col4Q=np.matmul(col4localk,col4u)        #local
                    col4R=np.matmul(col4Tt,col4Q)
                    
                    bm1v=dglob[:6]    
                    bm1T=T(width,0,width)
                    bm1Tt=np.transpose(bm1T)
                    bm1u=np.matmul(bm1T,bm1v)
                    bm1Q=np.matmul(bm1localk,bm1u)-F[0:6]                                        
                    bm1R=np.matmul(bm1Tt,bm1Q)
                    
                    bm2v=dglob[6:12]    
                    bm2T=T(width,0,width)
                    bm2Tt=np.transpose(bm2T)
                    bm2u=np.matmul(bm2T,bm2v)
                    bm2Q=np.matmul(bm2localk,bm2u)-F[6:]                                        
                    bm2R=np.matmul(bm2Tt,bm2Q)
                    
                    r=np.zeros(6)
                    r[:3]+=col1R[:3]
                    r[3:6]+=col2R[3:]
                                                            
                    r[2]=r[2]/12
                    r[5]=r[5]/12
                                        
                    d[2]=d[2]*180/3.14159
                    d[5]=d[5]*180/3.14159
                    d[8]=d[8]*180/3.14159
                    d[11]=d[11]*180/3.14159
                    
                    if pdelta=='1':
                        convergence=0
                        iterations=0
                        
                        if loadstype=='0':
                            F=F*1.6
                            
                        # number of pdelta iterations
                        while convergence<=pdeltaconvtol:    
                                         
                            dinit=d
                            col1pd_v=d[0]*col1R[4]/height
                            F[0]+=col1pd_v
                            col2pd_v=d[3]*col2R[0]/height
                            F[3]+=col2pd_v
                            col3pd_v=d[6]*col3R[4]/height2
                            F[6]+=col3pd_v
                            col4pd_v=d[9]*col4R[4]/height2
                            F[9]+=col4pd_v
                            
                            d=np.linalg.solve(glmatrix_rearranged[:12,:12],F)      #[x1,y2,rot]
                            dglob=np.zeros(18)
                            dglob[:12]+=d                                                                                    
                            
                            col1v=np.zeros((6))
                            col1v[:3]+=dglob[12:15]
                            col1v[3:]+=dglob[:3]
                            col1u=np.matmul(col1T,col1v)
                            col1Q=np.matmul(col1localk,col1u)        #local
                            col1R=np.matmul(col1Tt,col1Q) 
                            
                            col2v=np.zeros(6)
                            col2v[:3]+=dglob[3:6]
                            col2v[3:]+=dglob[15:]
                            col2u=np.matmul(col2T,col2v)
                            col2Q=np.matmul(col2localk,col2u)        #local
                            col2R=np.matmul(col2Tt,col2Q)
                            
                            col3v=np.zeros(6)
                            col3v[:3]+=dglob[6:9]
                            col3v[3:]+=dglob[:3]
                            col3u=np.matmul(col3T,col3v)
                            col3Q=np.matmul(col3localk,col3u)        #local
                            col3R=np.matmul(col3Tt,col3Q)
                            
                            col4v=np.zeros(6)
                            col4v[:3]+=dglob[9:12]
                            col4v[3:]+=dglob[3:6]
                            col4u=np.matmul(col4T,col4v)
                            col4Q=np.matmul(col4localk,col4u)        #local
                            col4R=np.matmul(col4Tt,col4Q)
                            
                            bm1v=dglob[:6]    
                            bm1T=T(width,0,width)
                            bm1Tt=np.transpose(bm1T)
                            bm1u=np.matmul(bm1T,bm1v)
                            bm1Q=np.matmul(bm1localk,bm1u)-F[0:6]                                        
                            bm1R=np.matmul(bm1Tt,bm1Q)
                            
                            bm2v=dglob[6:12]    
                            bm2T=T(width,0,width)
                            bm2Tt=np.transpose(bm2T)
                            bm2u=np.matmul(bm2T,bm2v)
                            bm2Q=np.matmul(bm2localk,bm2u)-F[6:]                                        
                            bm2R=np.matmul(bm2Tt,bm2Q)
                            
                            r=np.zeros(6)
                            r[:3]+=col1R[:3]
                            r[3:6]+=col2R[3:]
                            
                            
                            r[2]=r[2]/12
                            r[5]=r[5]/12
                                                        
                            d[2]=d[2]*180/3.14159
                            d[5]=d[5]*180/3.14159
                            d[8]=d[8]*180/3.14159
                            d[11]=d[11]*180/3.14159
                                                        
                            convergence=dinit[6]/d[6]*1.6
                            iterations=iterations+1
                            
                            if loadstype=='0':
                                r=r/1.6
                                d=d/1.6
                                col1R=col1R/1.6
                                col2R=col2R/1.6
                                col3R=col3R/1.6
                                col4R=col4R/1.6
                                bm1R=bm1R/1.6
                                bm2R=bm2R/1.6
                                
                        convergence_label=tk.Label(canvas,text='Pdelta convergence= '+str(round(convergence,3))) 
                        canvas.create_window((startx+xdim)/2+30, starty+59,window=convergence_label,anchor='nw')    
                        
                        iterations_label=tk.Label(canvas,text='Iterations= '+str(iterations)) 
                        canvas.create_window((startx+xdim)/2+30, starty+75,window=iterations_label,anchor='nw') 
                    
                    bm1M=beam_moment(-1*bm1R[2],bm1R[5],P,x,w,width)
                    bm2M=beam_moment(-1*bm2R[2],bm2R[5],P,x,w,width)
                    col1M=[-1*col1R[2]/12,col1R[5]/12]
                    col2M=[col2R[2]/12,-1*col2R[5]/12]     
                    col3M=[col3R[2]/12,-1*col3R[5]/12]  
                    col4M=[col4R[2]/12,-1*col4R[5]/12]
                    
                    #displacement label placement
                    #have to use 'create window' because using 'place' wont allow the label to be destroyed each run
                    dx2_label=tk.Label(canvas,text='dx= '+str(round(d[0],3))+' in')
                    canvas.create_window(startx+2,starty-ydim/2-62,window=dx2_label,anchor='nw')
                    dy2_label=tk.Label(canvas,text='dy= '+str(round(d[1],3))+' in')
                    canvas.create_window(startx+2,starty-ydim/2-45,window=dy2_label,anchor='nw')
                    rot2_label=tk.Label(canvas,text='rot='+str(round(d[2],3))+' deg')
                    canvas.create_window(startx+2,starty-ydim/2-28,window=rot2_label,anchor='nw')                
                    dx3_label=tk.Label(canvas,text='dx= '+str(round(d[3],3))+' in') 
                    canvas.create_window(startx+2+xdim,starty-ydim/2-62,window=dx3_label,anchor='nw')
                    dy3_label=tk.Label(canvas,text='dy= '+str(round(d[4],3))+' in')
                    canvas.create_window(startx+2+xdim,starty-ydim/2-45,window=dy3_label,anchor='nw')
                    rot3_label=tk.Label(canvas,text='rot= '+str(round(d[5],3))+' deg')
                    canvas.create_window(startx+2+xdim,starty-ydim/2-28,window=rot3_label,anchor='nw')
                    dx5_label=tk.Label(canvas,text='dx= '+str(round(d[6],3))+' in') 
                    canvas.create_window(startx,starty-ydim-62,window=dx5_label,anchor='nw')
                    dy5_label=tk.Label(canvas,text='dy= '+str(round(d[7],3))+' in')
                    canvas.create_window(startx,starty-ydim-45,window=dy5_label,anchor='nw')
                    rot5_label=tk.Label(canvas,text='rot= '+str(round(d[8],3))+' deg')
                    canvas.create_window(startx,starty-ydim-28,window=rot5_label,anchor='nw')
                    dx6_label=tk.Label(canvas,text='dx= '+str(round(d[9],3))+' in') 
                    canvas.create_window(startx+xdim,starty-ydim-62,window=dx6_label,anchor='nw')
                    dy6_label=tk.Label(canvas,text='dy= '+str(round(d[10],3))+' in')
                    canvas.create_window(startx+xdim,starty-ydim-45,window=dy6_label,anchor='nw')
                    rot6_label=tk.Label(canvas,text='rot= '+str(round(d[11],3))+' deg')
                    canvas.create_window(startx+xdim,starty-ydim-28,window=rot6_label,anchor='nw')
                                    
                    #reaction label placement
                    rx1_label=tk.Label(canvas,text='Rx= '+str(round(r[0],3))+' k')
                    canvas.create_window(startx,starty,window=rx1_label,anchor='nw')                
                    ry1_label=tk.Label(canvas,text='Ry= '+str(round(r[1],3))+' k')
                    canvas.create_window(startx,starty+17,window=ry1_label,anchor='nw')
                    M1_label=tk.Label(canvas,text='M= '+str(round(r[2],3))+' ft-k')
                    canvas.create_window(startx,starty+34,window=M1_label,anchor='nw')
                    rx4_label=tk.Label(canvas,text='Rx= '+str(round(r[3],3))+' k')   
                    canvas.create_window(startx+xdim,starty,window=rx4_label,anchor='nw')
                    ry4_label=tk.Label(canvas,text='Ry= '+str(round(r[4],3))+' k')
                    canvas.create_window(startx+xdim,starty+17,window=ry4_label,anchor='nw')
                    M4_label=tk.Label(canvas,text='M= '+str(round(r[5],3))+' ft-k')
                    canvas.create_window(startx+xdim,starty+34,window=M4_label,anchor='nw')
                    
                    #max moment label placement
                    bm1Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(bm1M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim/3,starty-ydim/2+2,window=bm1Mmax_label,anchor='nw')
                    bm1Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(bm1M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim/3,starty-ydim/2+18,window=bm1Mmin_label,anchor='nw')
                    bm2Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(bm2M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim/3,starty-ydim+2,window=bm2Mmax_label,anchor='nw')
                    bm2Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(bm2M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim/3,starty-ydim+18,window=bm2Mmin_label,anchor='nw')                    
                    c1Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col1M[1],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim/4-8,window=c1Mmax_label,anchor='nw')
                    c1Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col1M[0],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim/4+8,window=c1Mmin_label,anchor='nw')
                    c2Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col2M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim/4-8,window=c2Mmax_label,anchor='nw')
                    c2Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col2M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim/4+8,window=c2Mmin_label,anchor='nw')
                    c3Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col3M[0],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim*3/4-24,window=c3Mmax_label,anchor='nw')
                    c3Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col3M[1],1))+' ft-k')
                    canvas.create_window(startx+2,starty-ydim*3/4-8,window=c3Mmin_label,anchor='nw')
                    c4Mmax_label=tk.Label(canvas,text='Mmax= '+str(round(col4M[0],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim*3/4-24,window=c4Mmax_label,anchor='nw')
                    c4Mmin_label=tk.Label(canvas,text='Mmin= '+str(round(col4M[1],1))+' ft-k')
                    canvas.create_window(startx+xdim+2,starty-ydim*3/4-8,window=c4Mmin_label,anchor='nw')
    
                    drift_label1=tk.Label(canvas,text='Story Drift = L/'+str(int(round(height/max(d[0],d[3]),0))))
                    canvas.create_window((startx+xdim)/2-175,starty-ydim/4,window=drift_label1,anchor='nw')
                    
                    drift_label2=tk.Label(canvas,text='Story Drift = L/'+str(int(round(height2/max(d[6]-d[0],d[9]-d[3]),0))))
                    canvas.create_window((startx+xdim)/2-175,starty-ydim*3/4,window=drift_label2,anchor='nw')
                    
                return d,r
           
            def quit_app(self,*args):
                self.master.quit()
                self.master.destroy()
            
            tk.Button(frame1,text='Run',relief='raised',pady=5,width=10,command=lambda : run(self)).grid(row=17,column=1,columnspan=3)
            tk.Button(frame1,text='Quit',relief='raised',pady=5,width=10,command=lambda : quit_app(self)).grid(row=18,column=1,columnspan=3)

            
def main():
    root=tk.Tk()
    root.title('Portal Frame')
    master_window(root)
    root.geometry("1150x600")
    root.mainloop()
    
if __name__=='__main__':
    main()


