# ----------------------------------------------------------------------------------
# -- Company: University of Stuttgart (IIS)
# -- Engineer: Honghao Gu
# -- 
# -- Description: 
# -- This python file is for communicate with fpga (Pynq Z2)
# ----------------------------------------------------------------------------------

import src.all_of_the_parameters as all_of_the_parameters
from pynq import Overlay

chip_cfg_data_default = all_of_the_parameters.chip_cfg_data_default
path_to_bitstream = all_of_the_parameters.path_to_bitstream
Dep_Mem = all_of_the_parameters.Dep_Mem
sample_size = all_of_the_parameters.sample_size


ol = Overlay(path_to_bitstream)
pulse_gen = ol.fpga_pulse_generator_0    # DACs  Pulse control unit
osci = ol.fpga_tracing_0    # ADCs  visualization unit
adc0 = ol.fpga_adc_max11198_0
adc1 = ol.fpga_adc_max11198_1
chip_cfg = ol.fpga_nmr_chip_config_0 #chip config control unit define

#dictionary for tracing fpga controlling
fpga_func_dict = all_of_the_parameters.fpga_func_dict
#dictionary for pulse gen fpga controlling
pulse_gen_dict = all_of_the_parameters.pulse_gen_dict

"""
Controlling Functions for nmr chip config
"""


def fpga_func_chip_cfg(input):
    chip_cfg.write(0 * 4, input)  #config data to chip config 
    chip_cfg.write(1 * 4, 1)  #chip config start
    return 


"""
Controlling Functions for tracing part
"""


def enable(input):
    osci.write(fpga_func_dict['C_ENABLE_CMD'],input)
    return 

def disable():
    osci.write(fpga_func_dict['C_ENABLE_CMD'],0)
    return 

def single_shot(input):
    osci.write(fpga_func_dict['C_SINGLE_SHOT_CMD'],input)
    return 

def trigger_channel(data):
    osci.write(fpga_func_dict['C_SELECT_ANALOG_TRIGGER_CHANNEL_CMD'],data)
    return 

def trigger_ris_edge(input):#0/1
    osci.write(fpga_func_dict['C_SET_ANALOG_TRIGGER_RISING_EDGE_CMD'],input)
    return 

def trigger_fal_edge(input):#0/1
    osci.write(fpga_func_dict['C_SET_ANALOG_TRIGGER_FALLING_EDGE_CMD'],input)
    return 

def digtal_trigger_ris_edge(input):#0/1
    osci.write(fpga_func_dict['C_BIN_CH_RE_TRIG_EN_CMD'],input)
    return 

def digtal_trigger_fal_edge(input):#0/1
    osci.write(fpga_func_dict['C_BIN_CH_FE_TRIG_EN_CMD'],input)
    return 

def arm():
    osci.write(fpga_func_dict['C_ARM_CMD'],1)
    return 

def set_nr_samples(data):
    osci.write(fpga_func_dict['C_SET_NR_SAMPLES_CMD'],data)
    return 
    
def clock_step_size(data):
    osci.write(fpga_func_dict['C_CLOCK_STEP_SIZE_CMD'],data)
    return 
    
def trigger_delay(data):
    osci.write(fpga_func_dict['C_SET_TRIGGER_DELAY_CMD'],data)
    return 
    
def select_read_memory(data):
    osci.write(fpga_func_dict['C_SELECT_READ_MEMORY_CMD'],data)
    return 
    
def reset_current_read_addr():
    osci.write(fpga_func_dict['C_SET_CURRENT_READ_ADDRESS_CMD'],0)
    return 

def set_read_addr(data):
    osci.write(fpga_func_dict['C_SET_CURRENT_READ_ADDRESS_CMD'],data)
    return 
    
def rd_date():
    data = osci.read(fpga_func_dict['C_READ_DATA'])
    return data

def get_nr_AnalogChannel():
    data = osci.read(fpga_func_dict['C_GET_NR_ANALOG_CHANNELS_CMD'])
    return data

def get_nr_DigitalChannel():
    data = osci.read(fpga_func_dict['C_GET_NR_DIGITAL_CHANNELS_CMD'])
    return data

def get_nr_AnalogMemories():
    data = osci.read(fpga_func_dict['C_GET_NR_ANALOG_MEMORIES_CMD'])
    return data

def get_nr_DigitalMemories():
    data = osci.read(fpga_func_dict['C_GET_NR_DIGITAL_MEMORIES_CMD'])
    return data

def get_nr_MemDepth():
    data = osci.read(fpga_func_dict['C_GET_MEMORY_DEPTH_CMD'])
    return data

def busy():
    data = osci.read(fpga_func_dict['C_READ_BUSY_SIGNAL_CMD'])
    return data

def ready():
    data = osci.read(fpga_func_dict['C_READ_READY_SIGNAL_CMD'])
    return data

def led(input):
    osci.write(fpga_func_dict['C_TOGGLE_LED_CMD'],input)
    return 
    
def trigger_threshold(data):
    osci.write(fpga_func_dict['C_SET_ANALOG_TRIGGER_THRESHOLD_CMD'],data)
    return 
    
def mux_Memory(data):
    osci.write(fpga_func_dict['C_CTRL_MUX_SELECT_ANALOG_MEMORY_CMD'],data)
    return 
    
def mux_Channel(data):
    osci.write(fpga_func_dict['C_CTRL_MUX_SELECT_ANALOG_CH_CMD'],data)
    return 

def set_stream_number_rx_pulse(data):
    osci.write(fpga_func_dict['C_SET_STREAM_NR_RX_PULSE'],data)
    return 
    
def start_stream_transfer():
    osci.write(fpga_func_dict['C_START_STREAM'],1)
    return 
    
def type_stream(data):
    osci.write(fpga_func_dict['C_TYPE_STREAM'],data)
    return 

def dma_init():
    dma    = ol.axi_dma_0
    dma_send = ol.axi_dma_0.sendchannel
    dma_recv = ol.axi_dma_0.recvchannel
    return dma, dma_send, dma_recv

def mux():
    for item in range(0,3):
        mux_Channel(item)
        mux_Memory(item)
    return 

def fpga_tracing_init():
    
    #adc cfg
    mode = 1
    #0 = rising , 1 = falling
    adc0.write(0x0,mode)  
    adc1.write(0x0,mode)  
    
    chip_cfg.write(0 * 4, chip_cfg_data_default)  #config data to chip config 
    chip_cfg.write(1 * 4, 1)  #chip config start

    set_nr_samples(sample_size) #2**15
    trigger_delay(-2**(Dep_Mem-1)+1)  
    trigger_channel(0)          #which channel triggered
    trigger_threshold(0)     #trigger Lv.

    trigger_ris_edge(0)
    trigger_fal_edge(0)

    clock_step_size(10)
    digtal_trigger_ris_edge(0)
    digtal_trigger_fal_edge(0)
    return
