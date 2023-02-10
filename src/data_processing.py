# ----------------------------------------------------------------------------------
# -- Company: University of Stuttgart (IIS)
# -- Student: Honghao Gu
# -- 
# -- Description: 
# -- This python file include the functions for data processing
# ----------------------------------------------------------------------------------

from pynq import allocate
from pynq import MMIO
import src.all_of_the_parameters as all_of_the_parameters
import src.fpga_tracing_func as fpga_tracing_func
import src.web_GUI_config_panel as web_GUI_config_panel
import numpy as np
import pandas as pd
from scipy import signal
import time

#from hier are all para
Nr_Ana_Ch = all_of_the_parameters.Nr_Ana_Ch
Nr_Dig_Ch = all_of_the_parameters.Nr_Dig_Ch
Nr_Ana_Mem = all_of_the_parameters.Nr_Ana_Mem
Nr_Dig_Mem = all_of_the_parameters.Nr_Dig_Mem
Dep_Mem = all_of_the_parameters.Dep_Mem
sample_size = all_of_the_parameters.sample_size
plot_interval = all_of_the_parameters.plot_interval
sampling_time = all_of_the_parameters.sampling_time
adc_sampling_bit = all_of_the_parameters.adc_sampling_bit
adc_volt = all_of_the_parameters.adc_volt
c_for_convert_a = all_of_the_parameters.c_for_convert_a
# c_for_convert_b = all_of_the_parameters.c_for_convert_b
conf_dict = all_of_the_parameters.conf_dict

dma, dma_send, dma_recv = fpga_tracing_func.dma_init()

output_buffer_0 = allocate(shape=(sample_size * Nr_Ana_Ch,), dtype=np.int16) #define a ram block for data trans
config_buffer = allocate(shape=(40,), dtype=np.int16) #buffer special for config panel
IP_Base_Addr = config_buffer.physical_address
mmio = MMIO(IP_Base_Addr, 40*4)


def mmio_init():
  
    mmio.write(conf_dict['conf_onoff'], 0)#start/stop
    mmio.write(conf_dict['conf_trigger'], 1)#trigger function
    mmio.write(conf_dict['conf_ana_ris'], 0)#ana ris
    mmio.write(conf_dict['conf_ana_fal'], 0)#ana fal
    mmio.write(conf_dict['conf_ana_ch'], 0)#ana ch
    
    mmio.write(conf_dict['conf_ana_tl'], 0)#ana TL
    mmio.write(conf_dict['conf_dig_ris'], 0)#dig ris
    mmio.write(conf_dict['conf_dig_fal'], 0)#dig fal
    mmio.write(conf_dict['conf_enh_sen'], 0)#Enh_sensitivity
    mmio.write(conf_dict['conf_enh_res'], 0)#Enh_Resolution
    
    mmio.write(conf_dict['conf_scale'], 10)#clock step size (Scale)
    mmio.write(conf_dict['conf_position'], -2**(Dep_Mem-1))#Position
    mmio.write(conf_dict['conf_fft_ch'], 0)#FFT_ch (e.g. 0,1,2,3)
    mmio.write(conf_dict['conf_fft_onoff'], 0)#FFT_onoff
    mmio.write(conf_dict['conf_enh_tau'], 0)#enh_tau
    
    mmio.write(conf_dict['conf_enh_dc'], 0)#enh_dc
    mmio.write(conf_dict['conf_enh_bp_low_value'], 0)#enh_bp_low_value
    mmio.write(conf_dict['conf_enh_bp_high_value'], 0)#enh_bp_high_value
    mmio.write(conf_dict['conf_enh_bp_low_cb'], 0)#enh_bp_low_cb
    mmio.write(conf_dict['conf_token'], 0)#Token for config again
    
    mmio.write(conf_dict['conf_enh_bp_high_cb'], 0)#enh_high_cb
    mmio.write(conf_dict['conf_enh_ch'], 0)#enh_ch
    mmio.write(conf_dict['conf_nmr_chip_cfg_ref_curr'], 3)  #011           
    mmio.write(conf_dict['conf_nmr_chip_cfg_vga_gain'], 10)   #1010           
    mmio.write(conf_dict['conf_nmr_chip_cfg_pll_mult'], 3)   #0011

    return


def func_update_config_tracing():#communicate conf_para with fpga

    # config tracing
    fpga_tracing_func.enable(0)
    fpga_tracing_func.set_nr_samples(sample_size)
    fpga_tracing_func.trigger_delay(mmio.read(conf_dict['conf_position'])) #Position
    fpga_tracing_func.trigger_channel(mmio.read(conf_dict['conf_ana_ch'])) #ana ch
    fpga_tracing_func.trigger_threshold(mmio.read(conf_dict['conf_ana_tl'])) #ana TL
    fpga_tracing_func.trigger_ris_edge(mmio.read(conf_dict['conf_ana_ris'])) #ana ris
    fpga_tracing_func.trigger_fal_edge(mmio.read(conf_dict['conf_ana_fal'])) #ana fal
    fpga_tracing_func.clock_step_size(mmio.read(conf_dict['conf_scale'])) #clock_step_size (Scale)
    fpga_tracing_func.digtal_trigger_ris_edge(mmio.read(conf_dict['conf_dig_ris'])) #dig ris
    fpga_tracing_func.digtal_trigger_fal_edge(mmio.read(conf_dict['conf_dig_fal'])) #dig fal
    fpga_tracing_func.type_stream(mmio.read(conf_dict['conf_trigger'])) #0 = arm, 1 = single shot
    fpga_tracing_func.set_stream_number_rx_pulse(1)  #set Nr of Packages
    fpga_tracing_func.enable(1)
    fpga_tracing_func.enable(mmio.read(conf_dict['conf_onoff']))#disable
    mmio.write(conf_dict['conf_token'], 0)

    return


def func_update_config_special_for_pulse_gen():#communicate conf_para with fpga

    # config tracing
    fpga_tracing_func.enable(0)
    fpga_tracing_func.set_nr_samples(sample_size)
    fpga_tracing_func.trigger_delay(mmio.read(conf_dict['conf_position'])) #Position
    fpga_tracing_func.trigger_ris_edge(0) #ana ris
    fpga_tracing_func.trigger_fal_edge(0) #ana fal
    fpga_tracing_func.clock_step_size(mmio.read(conf_dict['conf_scale'])) #clock_step_size (Scale)
    fpga_tracing_func.digtal_trigger_ris_edge(1) #dig ris
    fpga_tracing_func.digtal_trigger_fal_edge(0) #dig fal
    fpga_tracing_func.type_stream(0) #0 = arm, 1 = single shot
    fpga_tracing_func.set_stream_number_rx_pulse(1)  #set Nr of Packages
    fpga_tracing_func.enable(1)
    mmio.write(conf_dict['conf_token'], 1)

    return


def func_update_data():#read data from dma and convert in 4 channels outputs all 32768

    dma_recv.transfer(output_buffer_0)
    fpga_tracing_func.type_stream(mmio.read(conf_dict['conf_trigger'])) #0 = arm, 1 = single shot
    fpga_tracing_func.set_stream_number_rx_pulse(1)  #set Nr of Packages
    fpga_tracing_func.start_stream_transfer()
            
    _ch0 = output_buffer_0[0::Nr_Ana_Ch]
    _ch1 = output_buffer_0[1::Nr_Ana_Ch]
    _ch2 = output_buffer_0[2::Nr_Ana_Ch]
    _ch3 = output_buffer_0[3::Nr_Ana_Ch]
            
    return _ch0,_ch1,_ch2,_ch3

def extract_b0_field(rawdata_I, rawdata_Q, Fs):
    
    # TODO: get the following para from GUI!!!
    omega_reference = 7758000 #[Hz]
    pll = 8

    ## Bandpass Filter
    # order=3 is the best so far
    b, a = signal.butter(3, [15e3, 25e3], 'bandpass', fs=Fs)
    filtered_I = signal.filtfilt(b, a, rawdata_I[:, 0])
    filtered_Q = signal.filtfilt(b, a, rawdata_Q[:, 0])
    filtered_I_Q = filtered_I + 1j * filtered_Q

    ## Extract angular freq and calculate B0
    phi = np.angle(filtered_I_Q)
    phi_unwrap = np.unwrap(phi)
    coeff = np.polyfit(time.flatten(), phi_unwrap.flatten(), 1)
    omega_cal = abs(coeff[0]) #real-time FID angular frequency[Hz]
    #f_cal = abs((coeff[0])/2/math.pi) #real-time FID frequency[Hz]

    realtime_B0 = (omega_cal+omega_reference*pll)/all_of_the_parameters.gyromag_ratio

    return realtime_B0

def func_timeline_update(time_list):

    time_multiplier = mmio.read(conf_dict['conf_scale']) * sampling_time * plot_interval
    time_list_output = list(time_list * time_multiplier)

    return time_list_output
    
    
def func_dc_remove(data):

    mean = int(np.mean(data))
    data = np.clip(data,max(-sample_size, (-sample_size + mean)),min((sample_size - 1), (sample_size - 1 + mean))).tolist()
    data = np.subtract(data, mean)

    return data


def func_save_file(ch0, ch1, ch2, ch3):
    
    time_line_length = max(len(ch0), len(ch1), len(ch2), len(ch3))
    time_stream_root = np.arange(0,time_line_length)
    time_stream = list(time_stream_root * mmio.read(conf_dict['conf_scale']) * sampling_time)  
    _ch0 = list(np.array(ch0) / c_for_convert_a)# + c_for_convert_b)
    _ch1 = list(np.array(ch1) / c_for_convert_a)# + c_for_convert_b)
    _ch2 = list(np.array(ch2) / c_for_convert_a)# + c_for_convert_b)
    _ch3 = list(np.array(ch3) / c_for_convert_a)# + c_for_convert_b)
    
    data = {
        'time(ns)': time_stream, 
        'channel0(mV)': _ch0, 
        'channel1(mV)': _ch1, 
        'channel2(mV)': _ch2, 
        'channel3(mV)': _ch3
    }

    output_data = pd.DataFrame(data)
    if web_GUI_config_panel.GUI_save_name.value == '':
        web_GUI_config_panel.GUI_save_name.value = 'Untitled'
        
    if web_GUI_config_panel.GUI_save_format.value == 0:
        name = 'output/' + web_GUI_config_panel.GUI_save_name.value + '.csv'
        output_data.to_csv(name)
    elif web_GUI_config_panel.GUI_save_format.value == 1:
        name = 'output/' + web_GUI_config_panel.GUI_save_name.value + '.txt'
        output_data.to_csv(name)

    return


def func_data_processing_for_plot(ch0, ch1, ch2, ch3):# compression data into 1000 samples to plot on screen
    
    Analog0_output = ch0[0:sample_size:plot_interval]
    Analog1_output = ch1[0:sample_size:plot_interval]
    Analog2_output = ch2[0:sample_size:plot_interval]
    Analog3_output = ch3[0:sample_size:plot_interval]
    
    # ch0_output = list(np.array(Analog0_output) / c_for_convert_a)# + c_for_convert_b)
    # ch1_output = list(np.array(Analog1_output) / c_for_convert_a)# + c_for_convert_b)
    # ch2_output = list(np.array(Analog2_output) / c_for_convert_a)# + c_for_convert_b)
    # ch3_output = list(np.array(Analog3_output) / c_for_convert_a)# + c_for_convert_b)

    return Analog0_output, Analog1_output, Analog2_output, Analog3_output
    
    
    
    