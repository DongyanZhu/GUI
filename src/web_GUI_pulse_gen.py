import threading
import time
import plotly.graph_objects as go
import numpy as np
import ipywidgets as widgets
import src.all_of_the_parameters as all_of_the_parameters
import src.data_processing as data_processing
import src.fpga_tracing_func as fpga_tracing_func
import src.web_GUI_config_panel as web_GUI_config_panel

from IPython.display import display
dma_recv = data_processing.dma_recv
output_buffer_0 = data_processing.output_buffer_0
GUI_plot = web_GUI_config_panel.GUI_plot()
conf_dict = all_of_the_parameters.conf_dict
mmio = data_processing.mmio

# -------------- 1. Register command address: type integer, object constant -----------------
#dictionary for pulse gen fpga controlling
pulse_gen_dict = all_of_the_parameters.pulse_gen_dict

# -------------- 2. GUI Elements and Display Function -----------------
# --- Textbox for user inputs: CPMG ---
# Experiment number
left_text = widgets.IntText(value=1,description='# Exp.:', layout=widgets.Layout(width='100px', height='24px'),style = {'description_width': '50px'})
# Echo number
right_text = widgets.IntText(value=40,description='# Echo:', layout=widgets.Layout(width='100px', height='24px'),style = {'description_width': '50px'})
# Echo time
left_text1 = widgets.IntText(value=1200,description='TE (us):', layout=widgets.Layout(width='120px', height='24px'),style = {'description_width': '50px'})
# 90 deg TX pulse length
right_text1 = widgets.IntText(value=18,description='P90 (us):', layout=widgets.Layout(width='110px', height='24px'),style = {'description_width': '60px'})
# Pulse delay
left_text2 = widgets.IntText(value=4,description='Pulse Delay (us):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '100px'})
# Acquisition length
right_text2 = widgets.IntText(value=800,description='Len_acqui (us):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '90px'})
# Excitation frequency
left_text3 = widgets.IntText(value=7635,description='f_tx (Hz):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '60px'})
# Receiver frequency
right_text3 = widgets.IntText(value=7635,description='f_rx (Hz):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '60px'}) 
# Phase offset value for CPMG
left_text5 = widgets.IntText(value=0,description='Off_phase (deg):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '100px'})
# 180 deg TX pulse length
right_text5 = widgets.IntText(value=36,description='P180 (us):', layout=widgets.Layout(width='120px', height='24px'),style = {'description_width': '60px'})

# --- Textbox for user inputs: FID ---
# Experiment number
left_text6 = widgets.IntText(value=1,description='# Exp.:', layout=widgets.Layout(width='100px', height='24px'),style = {'description_width': '50px'})
# 90 deg TX pulse length
right_text6 = widgets.IntText(value=20,description='P90(us):', layout=widgets.Layout(width='110px', height='24px'),style = {'description_width': '60px'})
# Dead time
left_text7 = widgets.IntText(value=20,description='Dead Time(us):', layout=widgets.Layout(width='140px', height='24px'),style = {'description_width': '90px'})
# Acquisition length
right_text7 = widgets.IntText(value=30,description='Len_acqui (us):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '90px'})
# TX reference frequency
left_text8 = widgets.IntText(value=7758000,description='f_tx (Hz):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '60px'})
# RX reference frequency
right_text8 = widgets.IntText(value=7758000,description='f_rx (Hz):', layout=widgets.Layout(width='150px', height='24px'),style = {'description_width': '60px'})

# --------------- Start Button ---------------
# To trigger the experiment
b_start_c = widgets.Button( # cpmg
    description = 'Start',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)
b_start_f = widgets.Button( # fid
    description = 'Start',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)
b_start_a = widgets.Button( # arbitrary
    description = 'Start',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)

# --------------- Stop Button ----------------
# To terminate the experiment
b_stop_c = widgets.Button(
    description = 'Stop',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)
b_stop_f = widgets.Button(
    description = 'Stop',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)
b_stop_a = widgets.Button(
    description = 'Stop',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)

# --------------- Configure Button ----------------
# To read parameter from textboxs and write into the IP core
b_config_c = widgets.Button(
    description = 'Configure',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)
b_config_f = widgets.Button(
    description = 'Configure',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)
b_config_a = widgets.Button(
    description = 'Configure',
    button_style = 'warning',
    layout = widgets.Layout(width='100px', height='28px')
)

# --------------- Blank text area ----------------
# blank_block = widgets.Label(value='  ',layout=widgets.Layout(width='20px', height='24px'))
# --------------- Combination for Different Sequences ----------------

# CPMG combination
a0_c = widgets.HBox(
    children = (left_text,right_text,left_text1,right_text1,left_text2,right_text2,left_text3,right_text3,left_text5,right_text5),
    layout = widgets.Layout(
        height='40px', 
        width='1358px',
        border='solid 4px yellow',
        margin='0px 5px 0px 0px',
        padding='0px 0px 0px 0px'
    ),
)
a1_c = widgets.HBox(
    children = (b_config_c,b_start_c,b_stop_c),
    layout = widgets.Layout(
        height='40px', 
        width='300px',
        border='solid 4px yellow',
        margin='0px 5px 0px 0px',
        padding='0px 0px 0px 0px'
    ),
)
a2_c = widgets.HBox(
    children = (a1_c,a0_c),
    layout = widgets.Layout(height='40px', width='auto'),
)

# FID combination
a0_f = widgets.HBox(
    children = (left_text6,right_text6,left_text7,right_text7,left_text8,right_text8),
    layout = widgets.Layout(
        height='40px', 
        width='842px',
        border='solid 4px yellow',
        margin='0px 5px 0px 0px',
        padding='0px 0px 0px 0px'
    ),
)
a1_f = widgets.HBox(
    children = (b_config_f,b_start_f,b_stop_f),
    layout = widgets.Layout(
        height='40px', 
        width='300px',
        border='solid 4px yellow',
        margin='0px 5px 0px 0px',
        padding='0px 0px 0px 0px'
    ),
)
a2_f = widgets.HBox(
    children = (a1_f,a0_f),
    layout = widgets.Layout(height='40px', width='auto'),
)
f = go.FigureWidget()
f.update_layout(
    autosize=True,
    width=1800,
    height=130,
    margin=dict(
        l=10,
        r=10,
        b=30,
        t=30,
        pad=4
    ),
    xaxis = {
        'showgrid': False, # thin lines in the background
        'zeroline': False, # thick line at x=0
        'visible': False,  # numbers below
        }, 
    yaxis = {
        'showgrid': False, # thin lines in the background
        'zeroline': False, # thick line at x=0
        'visible': False,  # numbers below
        }, 
    showlegend=False,
)
f_frame = widgets.HBox(
        children = (f,),
        layout = widgets.Layout(
            height='138px', 
            width='1680px',
            border='solid 4px yellow',
            margin='5px 5px 5px 0px',
            padding='0px 0px 0px 0px'
        ),  
)

# create Vboxes
def make_box():
    
    global w_CPMG
    global w_FID
    global w_ARBITRARY
    
    w_CPMG = widgets.VBox(
        children = (a2_c,f_frame),
    )
    w_FID = widgets.VBox(
        children = (a2_f,f_frame),
    )
    w_A = widgets.HBox(
        children = (b_config_a,b_start_a,b_stop_a),
            layout = widgets.Layout(
                height='40px', 
                width='300px',
                border='solid 4px yellow',
                margin='0px 5px 0px 0px',
                padding='0px 0px 0px 0px'
            ),

    ) 
    w_ARBITRARY = widgets.VBox(
        children = (w_A,f_frame),
    ) 


# --------------- Display Functions and Pull-down Menu to Select----------------

sequence_choice_menu = widgets.Dropdown(
    options = ['User Defined','FID','CPMG'],
    description = 'Choose Sequence Type:',
    layout=widgets.Layout(width='278px', height='24px'),   #  'max-content' to fit max length of content
    style = {'description_width': '143px'}
)
sequence_choice_menu_frame = widgets.HBox(
        children = (sequence_choice_menu,),
        layout = widgets.Layout(
            height='40px', 
            width='300px',
            border='solid 4px yellow',
            margin='5px 5px 0px 5px',
            padding='0px 0px 0px 0px'
        ),  
)

def choiceS(arg):
    output_class.clear_output()
    with output_class:
        if arg.new == 'User Defined':
            display(w_ARBITRARY)
        elif arg.new == 'CPMG':
            display(w_CPMG)
        elif arg.new == 'FID':
            display(w_FID)

sequence_choice_menu.observe(choiceS,names='value')
output_class = widgets.Output()

# -------------- 3. Pulse Generator Classes -----------------
#  This chapter uses class and instantiations to connect input text boxes and IP core on FPGA
# --- Class Definition for CPMG ---
class PulseGen_CPMG:
    
    def __init__(self,IP,No_scans,No_echos,t_echo,P_90,pulse_delay,P_RX,f_TX,f_RX,phase_offset,P_180):
        
        # order according to the text boxes
        self.IP = IP  
        
        # cpmg parameters in unit us
        self.t = 250  # self.t = int(clk_fre)            # 1 unit correspond to (1/f) us => 1 us -- 250 unit with f = 250 MHz             
        self.t_echo = t_echo * self.t    # echo time
        self.P_90 = P_90 * self.t      # 90 deg pulse length
        self.P_180 = P_180 * self.t     # 180 deg pulse length (need not be double P_90!)
        self.P_RX = P_RX * self.t      # acquisition time
        self.No_scans = No_scans       # number of experiments
        self.No_echos = No_echos       # number of echos
        self.f_TX = int(f_TX * 17.18)    # excitation frequency, phase_width = 32
        self.f_RX = int(f_RX * 17.18)     # receiver frequency, phase_width = 32
        self.pulse_delay = pulse_delay * 250
        self.phase_offset = phase_offset * 11930465
        
        # below don't change, system structure
        self.start_pointer = 4 
        self.end_pointer = 11
        self.section_nr = 13
        self.phase_width = 32   # DDS phase width default = 32 bits, see Vivado environment DDS Compiler Configuration
        
        # store length sequence for plotting use, with initial value
        self.t_total = 0 # calculate whole experiment duration after configuration
        self.cpmg_len = [25000,25000,4500,142250,1000,9000,1000,43500,1000,200000,1000,43500,25000] 
        self.cpmg_p0  =  [0,0,0,0,0,0,0,0,0,0,0,0,0]
  
    def Exp_Config(self):
    
        # for experiment parameter configuration
        self.IP.write(pulse_gen_dict['C_SET_NR_SECTIONS'],int(self.section_nr)) # 0-12 for CPMG
        self.IP.write(pulse_gen_dict['C_SET_START_REPEAT_POINTER'],int(self.start_pointer))
        self.IP.write(pulse_gen_dict['C_SET_END_REPEAT_POINTER'],int(self.end_pointer))
        self.IP.write(pulse_gen_dict['C_SET_CYCLE_REPETITION_NUMBER'],int(self.No_echos))
        self.IP.write(pulse_gen_dict['C_SET_EXPERIMENT_REPETITION_NUMBER'],int(self.No_scans))

    def Sec_Config_Basic(self,sec,s_type,delay,mux,p0,f0,p1,f1,rstn):
        
        # for each section's configuration
        # choose section to configure
        self.IP.write(pulse_gen_dict['C_SEL_SECTION'],sec)
        # define section type
        self.IP.write(pulse_gen_dict['C_SET_SECTION_TYPE'],s_type)
        # define delay duration
        self.IP.write(pulse_gen_dict['C_SET_DELAY'],delay)        
        # define multiplexer type
        self.IP.write(pulse_gen_dict['C_SET_MUX'],mux)
        # DDS channel 0 phase
        self.IP.write(pulse_gen_dict['C_SET_PHASE_CH0'],p0)
        # DDS channel 0 frequency
        self.IP.write(pulse_gen_dict['C_SET_FREQUENCY_CH0'],f0)
        # DDS channel 1 phase
        self.IP.write(pulse_gen_dict['C_SET_PHASE_CH1'],p1)
        # DDS channel 1 frequency
        self.IP.write(pulse_gen_dict['C_SET_FREQUENCY_CH1'],f1)
        # resetn for each section
        self.IP.write(pulse_gen_dict['C_SET_RESETN_DDS'],rstn)
        
    def Sec_Config_CPMG(self,b): 
        
        # add a non-use parameter b to avoid strange problem: type error, takes 1 arguments 2 given
        # update self.parameters from text boxes then write into IP core pulse_gen
        global left_text, right_text, left_text1, right_text1, left_text2, right_text2, left_text3, right_text3, left_text4, right_text4
        self.t_echo = left_text1.value * self.t      # echo time
        self.P_90 = right_text1.value * self.t      # 90 deg pulse length
        self.P_180 = right_text5.value * self.t     # 180 deg pulse length (need not be double P_90!)
        self.P_RX = right_text2.value * self.t      # acquisition time
        self.No_scans = left_text.value           # number of experiments
        self.No_echos = right_text.value          # number of echos
        self.f_TX = int(left_text3.value * 17.18)      # excitation frequency, phase_width = 32
        self.f_RX = int(right_text3.value * 17.18)      # receiver frequency, phase_width = 32
        self.pulse_delay = left_text2.value * self.t
        self.phase_offset = left_text5.value * 11930465
        
        # write parameter from Python Object to IP core in FPGA
        f = self.f_TX
        fl = self.f_RX
        p = self.phase_offset
        t0 = (self.t_echo - self.P_90 - self.P_180) / 2 - self.pulse_delay
        t1 = (self.t_echo - self.P_RX - self.P_180) / 2 - self.pulse_delay * 2
        l_type  =  [2,2,0,2,2,0,2,2,2,1,2,2,2]
        l_delay =  [100*self.t,100*self.t,self.P_90,t0,self.pulse_delay,self.P_180,self.pulse_delay,t1,
                    self.pulse_delay,self.P_RX,self.pulse_delay,t1,100*self.t]
        l_mux   =  [0,0,0,0,0,0,0,0,1,1,1,0,0]
        l_p0    =  [0,0,0,0,p,p,p,0,0,0,0,0,0]
        l_f0    =  [f,f,f,f,f,f,f,f,f,f,f,f,f]
        l_p1    =  [0,0,0,0,0,0,0,0,0,0,0,0,0]
        l_f1    =  [f,f,f,fl,fl,fl,fl,fl,fl,fl,fl,fl,fl]
        l_rstn  =  [1,1,1,1,1,1,1,1,1,1,1,1,1]
        
        # First: configure IP core: experiment number and cycle number
        self.Exp_Config()
        # Second: configure IP core: echo number
        # already int type, no need to perform the following lines!
        for i in range(0,len(l_delay)):
            l_delay[i] = int(l_delay[i])
            l_p0[i] = int(l_p0[i])
            l_f0[i] = int(l_f0[i])
            l_p1[i] = int(l_p1[i])
            l_f1[i] = int(l_f1[i])
            l_rstn[i] = int(l_rstn[i])
        # calculate total experiment duration
        t_total = sum(l_delay[0:self.start_pointer - 1]) + self.No_echos * sum(l_delay[self.start_pointer - 1: self.end_pointer]) + sum(l_delay[self.end_pointer:self.section_nr])
        t_total = self.No_scans * t_total / (self.t * 1000)
        
        for i in range(0,self.section_nr):
            self.Sec_Config_Basic(i,l_type[i],l_delay[i],l_mux[i],l_p0[i],l_f0[i],l_p1[i],l_f1[i],l_rstn[i])
        
        self.t_total = t_total  # pass calculated value to instantiation's attribute     
        self.cpmg_phase = l_p0
        self.cpmg_len = l_delay        
        
    def Exp_Start(self,b):
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],0) # first set enable signal 0 then 1.
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],1)
       
        thread = threading.Thread(target=self.Exp_Trigger_Thread)  # create a new thread for showing without disturbing experiment
        thread.start()
        thread.join()

    def Exp_Trigger_Thread(self):
        t_total_s = self.t_total / 1000
        time.sleep(t_total_s)
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],0)

    def Exp_Stop(self,b): # to terminate the experiment before it's finished
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],0)
        
# --- Class Definition for FID ---
class PulseGen_FID:

    def __init__(self,IP,No_scans,P_90,t_dead,P_RX,f_TX,f_RX):
        self.IP = IP 
        # fid parameters in unit us
        self.t = 250
        self.No_scans = No_scans # experiment number
        self.No_echos = 1        # echo number, for FID is 1, not change
        self.P_90 = P_90 * self.t                 # 90 deg excitation pulse length
        self.dead_time = t_dead * self.t       # dead time between excitation and receiver pulse
        self.P_RX = P_RX * self.t                 # acquisition time
        self.f_TX = int(f_TX * 17.18)     # TX reference frequency
        self.f_RX = int(f_RX * 17.18)     # RX reference frequency
        self.t = 250                      # 1 us -- 250 MHz, user should not change!
        self.phase_width = 32            # DDS phase width 32, change in IP core, user should not change!            
    # FID section setting, below don't change
        self.start_pointer = 1
        self.end_pointer = 3
        self.section_nr = 5
    # to store whole experiment duration after configuration
        self.t_total = 0 # calculate whole experiment duration after configuration
        self.fid_len = [25000,5000,5000,2500000,25000]
        self.fid_p0 = [0,0,0,0,0]
  
    def Exp_Config(self):
        # for experiment parameter configuration
        self.IP.write(pulse_gen_dict['C_SET_NR_SECTIONS'],int(self.section_nr)) # 0-12 for CPMG
        self.IP.write(pulse_gen_dict['C_SET_START_REPEAT_POINTER'],int(self.start_pointer))
        self.IP.write(pulse_gen_dict['C_SET_END_REPEAT_POINTER'],int(self.end_pointer))
        self.IP.write(pulse_gen_dict['C_SET_CYCLE_REPETITION_NUMBER'],int(self.No_echos))
        self.IP.write(pulse_gen_dict['C_SET_EXPERIMENT_REPETITION_NUMBER'],int(self.No_scans))

    def Sec_Config_Basic(self,sec,s_type,delay,mux,p0,f0,p1,f1,rstn):
        # for each section's configuration
        # choose section to configure
        self.IP.write(pulse_gen_dict['C_SEL_SECTION'],sec)
        # define section type
        self.IP.write(pulse_gen_dict['C_SET_SECTION_TYPE'],s_type)
        # define delay duration
        self.IP.write(pulse_gen_dict['C_SET_DELAY'],delay)        
        # define multiplexer type
        self.IP.write(pulse_gen_dict['C_SET_MUX'],mux)
        # DDS channel 0 phase
        self.IP.write(pulse_gen_dict['C_SET_PHASE_CH0'],p0)
        # DDS channel 0 frequency
        self.IP.write(pulse_gen_dict['C_SET_FREQUENCY_CH0'],f0)
        # DDS channel 1 phase
        self.IP.write(pulse_gen_dict['C_SET_PHASE_CH1'],p1)
        # DDS channel 1 frequency
        self.IP.write(pulse_gen_dict['C_SET_FREQUENCY_CH1'],f1)
        # resetn for each section
        self.IP.write(pulse_gen_dict['C_SET_RESETN_DDS'],rstn)
        
    def Sec_Config_FID(self,b): 
        # add a non-use parameter b to avoid strange problem: type error, takes 1 arguments 2 given
        # update self.parameters from sliders
        global left_text6, right_text6, left_text7, right_text7, left_text8, right_text8
        self.No_scans = left_text6.value        # number of experiments
        self.P_90 = right_text6.value * self.t     # 90 deg pulse length
        self.dead_time = left_text7.value * self.t  # dead time
        self.P_RX = right_text7.value * self.t    # acquisition time
        self.f_TX = int(left_text8.value * 17.18)     # excitation frequency
        self.f_RX = int(right_text8.value * 17.18)    # receiver frequency        
            
        # write parameter from Python Object to IP core in FPGA
        f = self.f_TX  # TX frequency
        fl = self.f_RX  # RX frequency
        p = 0          # 0 offset for FID
        l_type  =  [2,0,2,1,2] #0 = TX, 1 = RX, 2 = delay
        l_delay =  [100*self.t, self.P_90, self.dead_time, self.P_RX, 100*self.t]        
        l_mux   =  [0,0,0,1,0]
        l_p0    =  [0,0,0,0,0]
        l_f0    =  [f,f,f,f,f]
        l_p1    =  [0,0,0,0,0]
        l_f1    =  [fl,fl,fl,fl,fl]
        l_rstn  =  [1,1,1,1,1]

        # first configure IP core: experiment number and cycle number
        self.Exp_Config()

        # second configure IP core: echo number
        for i in range(0,len(l_delay)):
            l_delay[i] = int(l_delay[i])
            l_p0[i] = int(l_p0[i])
            l_f0[i] = int(l_f0[i])
            l_p1[i] = int(l_p1[i])
            l_f1[i] = int(l_f1[i])
            l_rstn[i] = int(l_rstn[i])
        
        self.fid_len = l_delay
        
        t_total = sum(l_delay[0:self.start_pointer - 1]) + self.No_echos * sum(l_delay[self.start_pointer - 1: self.end_pointer]) + sum(l_delay[self.end_pointer:self.section_nr])
        t_total = self.No_scans * t_total / (self.t * 1000)
        
        for i in range(0,self.section_nr):
            self.Sec_Config_Basic(i,l_type[i],l_delay[i],l_mux[i],l_p0[i],l_f0[i],l_p1[i],l_f1[i],l_rstn[i])
        
        self.t_total = t_total
        
    def Exp_Start(self,b):
        
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],0) # first set enable signal 0 then 1.
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],1)
       
        thread = threading.Thread(target=self.Exp_Trigger_Thread)  # create a new thread for showing without disturbing experiment
        thread.start()
        thread.join()

    def Exp_Trigger_Thread(self):
        t_total_s = self.t_total / 1000
        time.sleep(t_total_s)
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],0)

    def Exp_Stop(self,b): # to terminate the experiment before it's finished
        self.IP.write(pulse_gen_dict['C_SEQUENCE_GENERATOR_EN'],0)
        
# -------------- 4. Pulse Generator Class Instantiation function and Connect to GUI functions -----------------
def Object_Create(IP):  # creation instantiation and plotly object
    global pg          # use global variable
    pg = PulseGen_CPMG(IP, left_text.value, right_text.value,
                  left_text1.value, right_text1.value,
                  left_text2.value, right_text2.value,
                  left_text3.value, right_text3.value, 
                  left_text5.value, right_text5.value
                 )
    global pg_1
    pg_1 = PulseGen_FID(IP, left_text6.value, right_text6.value,
                  left_text7.value, right_text7.value,
                  left_text8.value, right_text8.value
                 )
    global y2
    cpmg_len = [250, 250, 45, 1423, 10, 90, 10, 435, 10, 2000, 10, 435, 10]
    cpmg_len = np.array(cpmg_len).tolist()
    y = np.ones(sum(cpmg_len)) + 0.5
    y2 = np.ones(sum(cpmg_len)) + 0.5
    y1 = np.zeros(sum(cpmg_len))
    y[sum(cpmg_len[0:2]) : sum(cpmg_len[0:3]) + 1] = 2
    y[sum(cpmg_len[0:5]) : sum(cpmg_len[0:6]) + 1] = 2
    y1[sum(cpmg_len[0:9]) : sum(cpmg_len[0:10]) + 1] = 0.5
    y2[sum(cpmg_len[0:2]) : sum(cpmg_len[0:3]) + 1] = 2
    
    f.add_scatter(y=y) # trace 2
    f.add_scatter(y=y1) # trace 3

    f.layout.title = r'Pulse Sequence: %d echo(s) %d time(s).' %(0,0)
    
    # add annotations (option to include arrow or text or both)
    
    f.add_annotation(           # 0
      x=1950,  # arrows' head
      y=0.7,  # arrows' head
      ax=4550,  # arrows' tail
      ay=0.7,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 1
      x=4550,  # arrows' head
      y=0.7,  # arrows' head
      ax=1950,  # arrows' tail
      ay=0.7,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 2
      x=50,  # arrows' head
      y=1.7,  # arrows' head
      ax=50,  # arrows' tail
      ay=1.7,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='TX',  # if you want only the arrow
      showarrow=False,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 3
      x=50,  # arrows' head
      y=0.2,  # arrows' head
      ax=50,  # arrows' tail
      ay=0.2,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='RX',  # if you want only the arrow
      showarrow=False,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 4
      x=3200,  # arrows' head
      y=0.9,  # arrows' head
      ax=3200,  # arrows' tail
      ay=0.9,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='Echo duration:%d '%left_text1.value,  # if you want only the arrow
      showarrow=False,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 5
      x=3500,  # arrows' head
      y=0.3,  # arrows' head
      ax=3500,  # arrows' tail
      ay=0.3,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='RX duration:%d '%right_text1.value,  # if you want only the arrow
      showarrow=False,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 6
      x=2550,  # arrows' head
      y=0.1,  # arrows' head
      ax=4500,  # arrows' tail
      ay=0.1,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 7
      x=4500,  # arrows' head
      y=0.1,  # arrows' head
      ax=2550,  # arrows' tail
      ay=0.1,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 8
      x=1950,  # arrows' head
      y=1.6,  # arrows' head
      ax=1450,  # arrows' tail
      ay=1.6,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 9
      x=2080,  # arrows' head
      y=1.6,  # arrows' head
      ax=3080,  # arrows' tail
      ay=1.6,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )    
    f.add_annotation(           # 10
      x=3000,  # arrows' head
      y=1.8,  # arrows' head
      ax=3000,  # arrows' tail
      ay=1.8,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='180 deg TX duration:%d '%right_text5.value,  # if you want only the arrow
      showarrow=False,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )    
    f.add_annotation(           # 11
      x=500,  # arrows' head
      y=1.1,  # arrows' head
      ax=0,  # arrows' tail
      ay=1.1,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 12
      x=545,  # arrows' head
      y=1.1,  # arrows' head
      ax=1545,  # arrows' tail
      ay=1.1,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',  # if you want only the arrow
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )
    f.add_annotation(           # 13
      x=1500,  # arrows' head
      y=1.3,  # arrows' head
      ax=1500,  # arrows' tail
      ay=1.3,  # arrows' tail
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='90 deg TX duration:%d '%right_text1.value,  # if you want only the arrow
      showarrow=False,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=1,
      arrowcolor='black'
    )  
    return pg, pg_1, f

# ------------- Connect function with GUI and IP core ------------
def config_plot_c(a):       # must pass function (name) to Button on_click without calling it
    # config + plot
    data_processing.func_update_config_tracing()
    web_GUI_config_panel.GUI_TBtn_run_stop.value = 0
    global pg
    pg.Sec_Config_CPMG(0)
    cpmg_plot_modify(pg.No_scans, pg.No_echos)
def config_plot_f(a):       # must pass function (name) to Button on_click without calling it
    # config + plot
    data_processing.func_update_config_tracing()
    web_GUI_config_panel.GUI_TBtn_run_stop.value = 0
    global pg_1
    pg_1.Sec_Config_FID(0)
    fid_plot_modify(pg_1.No_scans, pg_1.No_echos)    
def config_plot_a(a):       # must pass function (name) to Button on_click without calling it
    # config + plot
    data_processing.func_update_config_tracing()
    web_GUI_config_panel.GUI_TBtn_run_stop.value = 0
    global pg_2
    pg_2.Sec_Config_CPMG(0)
    cpmg_plot_modify(pg_2.No_scans, pg_2.No_echos)

# -------------- 5. GUI Plot Functions Using matplotlib.pyplot-----------------
def cpmg_plot_modify(exp_num, echo_num):
    global f
    f.layout.title = r'CPMG Pulse Sequence: %d echos %d time(s)' %(echo_num,exp_num)
    f['layout']['annotations'][4]['text'] = 'Echo duration:%d '%left_text1.value
    f['layout']['annotations'][5]['text'] = 'RX duration:%d '%right_text2.value
    f['layout']['annotations'][10]['text'] = '180 deg TX duration:%d '%right_text5.value
    f['layout']['annotations'][13]['text'] = '90 deg TX duration:%d '%right_text1.value
def fid_plot_modify(exp_num, echo_num):
    global f
    global y2
    f.layout.title = r'FID Pulse Sequence: %d echos %d time(s)' %(echo_num,exp_num)
    f['layout']['annotations'][4]['text'] = ''
    f['layout']['annotations'][5]['text'] = 'RX duration:%d '%right_text7.value
    f['layout']['annotations'][10]['text'] = ''
    f['layout']['annotations'][13]['text'] = '90 deg TX duration:%d '%right_text6.value
    f['layout']['annotations'][8]['showarrow'] = False
    f['layout']['annotations'][9]['showarrow'] = False
    f['layout']['annotations'][0]['showarrow'] = False
    f['layout']['annotations'][1]['showarrow'] = False
    f.data[0]['y'] = y2