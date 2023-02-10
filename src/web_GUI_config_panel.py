# ----------------------------------------------------------------------------------
# -- Company: University of Stuttgart (IIS)
# -- Engineer: Honghao Gu
# -- Modified by: Dongyan Zhu (B0 Control)
# -- 
# -- Description: 
# -- This python file include all the widgets used in the GUI
# ----------------------------------------------------------------------------------

import ipywidgets as widgets
import plotly.graph_objects as go
import src.data_processing as data_processing
import src.all_of_the_parameters as all_of_the_parameters
import src.fpga_tracing_func as fpga_tracing_func

Dep_Mem = all_of_the_parameters.Dep_Mem
sample_value_half = all_of_the_parameters.sample_value_half
sample_size = all_of_the_parameters.sample_size
adc_volt = all_of_the_parameters.adc_volt
point_number_on_screen = all_of_the_parameters.point_number_on_screen

"""
hier begin the GUI for NMR_CHIP_CFG
"""

def GUI_chip_cfg_ref_current():
    
    GUI_chip_cfg_ref_current = widgets.Dropdown(      
        options=[
            ('-15%', 0), 
            ('-10%', 1),
            ('-5%', 2),
            ('+0%', 3),
            ('+5%', 4),
            ('+10%', 5),
            ('+15%', 6),
            ('+20%', 7)
        ],
        value=3,
        description='Reference Current:',
        disabled=False,
        style = {'description_width': '120px'},
        layout={
            'width': '278px',
            'height':'30px',
        }, 
    )
    return GUI_chip_cfg_ref_current

def GUI_chip_cfg_vga_gain():
    
    GUI_chip_cfg_vga_gain = widgets.Dropdown(      
        options=[
            ('0dB', 0), 
            ('3dB', 1),
            ('6dB', 2),
            ('9dB', 3),
            ('10dB', 4),
            ('11dB', 5),
            ('13dB', 6),
            ('15dB', 7),
            ('20dB', 8), 
            ('23dB', 9),
            ('25dB', 10),
            ('28dB', 11),
            ('29dB', 12),
            ('30dB', 13),
            ('32dB', 14),
            ('34dB', 15)
        ],
        value=10,
        description='VGA Gain:',
        disabled=False,
        style = {'description_width': '120px'},
        layout={
            'width': '278px',
            'height':'30px',
        }, 
    )
    return GUI_chip_cfg_vga_gain

def GUI_chip_cfg_pll_mult():
    
    GUI_chip_cfg_pll_mult = widgets.Dropdown(
        options=[
            ('64x', 0), 
            ('32x', 1),
            ('16x', 2),
            ('8x', 3),
            ('4x', 4),
            ('2x', 5),
            ('1x', 6),
            ('set to Bridge', 8)
        ],
        value=3,
        description='PLL Multiplier:',
        disabled=False,
        style = {'description_width': '120px'},
        layout={
            'width': '278px',
            'height':'30px',
        }, 
    )
    return GUI_chip_cfg_pll_mult

def GUI_chip_cfg_ref_current_box(a):
    
    GUI_chip_cfg_ref_current_box = widgets.VBox(
        [
            a,
        ],
        layout = widgets.Layout(
            height='42px',
            width='300px',
            border='solid 4px red',
            margin='0px 5px 0px 5px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_chip_cfg_ref_current_box

def GUI_chip_cfg_vga_gain_box(a):
    
    GUI_chip_cfg_vga_gain_box = widgets.VBox(
        [
            a,
        ],
        layout = widgets.Layout(
            height='42px',
            width='300px',
            border='solid 4px red',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_chip_cfg_vga_gain_box

def GUI_chip_cfg_pll_mult_box(a):
    
    GUI_chip_cfg_pll_mult_box = widgets.VBox(
        [
            a,
        ],
        layout = widgets.Layout(
            height='42px',
            width='300px',
            border='solid 4px red',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_chip_cfg_pll_mult_box

def GUI_chip_cfg_box(a, b, c):
    
    GUI_chip_cfg_box = widgets.HBox(
        [
            a,
            b,
            c,
        ],
        layout = widgets.Layout(height='42px', width='970px'),
        align_items='flex-start',
    )
    return GUI_chip_cfg_box

"""
hier begin the GUI for TRACING PART
"""

"""
logo of iis on the title box
"""

def GUI_logo():
    
    file_GUI_logo = open("src/icons/logo_iis.png", "rb")
    image = file_GUI_logo.read()
    GUI_logo = widgets.Image(
        value=image,
        format='png',
        width=320, #4x
        height=80, #x
    )
    return GUI_logo

def GUI_logo_iis():
    
    file_GUI_logo_iis = open("src/icons/logo_iis_blue.png", "rb")
    image = file_GUI_logo_iis.read()
    GUI_logo_iis = widgets.Image(
        value=image,
        format='png',
        width=80, #4x
        height=80, #x
    )
    return GUI_logo_iis

def ris_edge():
    
    file_ris_edge = open("src/icons/ris_edge.png", "rb")
    image = file_ris_edge.read()
    ris_edge = widgets.Image(
        value=image,
        format='png',
        width=25, 
        height=8,
    )
    return ris_edge

def fal_edge():
    
    file_fal_edge = open("src/icons/fal_edge.png", "rb")
    image = file_fal_edge.read()
    fal_edge = widgets.Image(
        value=image,
        format='png',
        width=25, 
        height=8,
    )
    return fal_edge

"""
settings on the function bar
"""

def GUI_title():
    
    GUI_title = widgets.Label(
        value="-----------------Tracing for NMR Signal-----------------",
        layout = widgets.Layout(height='25px', width='320px'),
        align_items='flex-start'
    )
    return GUI_title

def GUI_sys_title():
    
    GUI_sys_title = widgets.Label(
        value="System:",
        layout = widgets.Layout(height='25px', width='60px'),
        align_items='flex-start'
    )
    return GUI_sys_title

def GUI_TBtn_arm():
    
    GUI_TBtn_arm = widgets.ToggleButton(
        value=False,
        description='Trigger Activate',
        disabled=False,
        button_style='',
        tooltip='set patameters before activate',
        icon='',
        layout = widgets.Layout(height='30px', width='128px'), #min118px
    )
    return GUI_TBtn_arm

def GUI_TBtn_run_stop():
    
    GUI_TBtn_run_stop = widgets.ToggleButton(
        value=False,
        description='Run/Stop',
        disabled=False,
        button_style='',
        tooltip='Freeze Screen',
        icon='',
        layout = widgets.Layout(height='30px', width='128px'),
    )
    return GUI_TBtn_run_stop

def GUI_onoff(a, b):
    
    GUI_onoff = widgets.VBox(
        [
            GUI_sys_title(),
            a,
            b, 
        ],
        layout = widgets.Layout(
            height='110px',
            width='150px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 5px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_onoff

"""
part 1 ana trigger cbox
"""

def GUI_ana_label():
    
    GUI_ana_label = widgets.Label(
        value="Analog Trigger:",
        layout = widgets.Layout(height='25px', width='92px'),
        align_items='flex-start'
    )
    return GUI_ana_label

#set analog rising edge
def GUI_checkbox_ana_ris():
    
    GUI_checkbox_ana_ris = widgets.Checkbox(
        value=False,
        layout = widgets.Layout(height='22px', width='94px'),
        description='Rising Edge',
        disabled=False,
        indent=False
    )
    return GUI_checkbox_ana_ris

def GUI_checkbox_ana_fal():
    
    GUI_checkbox_ana_fal = widgets.Checkbox(
        value=False,
        layout = widgets.Layout(height='22px', width='94px'),
        description='Falling Edge',
        disabled=False,
        indent=False
    )
    return GUI_checkbox_ana_fal

def GUI_hbox_ana_ris(a,b):
    
    GUI_hbox_ana_ris = widgets.HBox(
        [
            a,
            b
        ],
        layout = widgets.Layout(height='30px', width='128px'), #min 30 x 123
        align_items='flex-start'
    )
    return GUI_hbox_ana_ris

def GUI_hbox_ana_fal(a,b):
    
    GUI_hbox_ana_fal = widgets.HBox(
        [
            a,
            b
        ],
        layout = widgets.Layout(height='30px', width='128px'), #min 30 x 123
        align_items='flex-start'
    )
    return GUI_hbox_ana_fal

def GUI_ana_cbox(a, b, c):

    GUI_ana_cbox = widgets.VBox(
        [
            a,
            b,
            c,
        ],
        layout = widgets.Layout(
            height='90px', 
            width='150px'
        ),
        align_items='flex-start',
    )
    return GUI_ana_cbox

"""
part 2 ana trigger ch tl
"""

def GUI_ana_label_blank():
    
    GUI_ana_label_blank = widgets.Label(
        value=" ",
        layout = widgets.Layout(height='25px', width='10px'),
        align_items='flex-start'
    )
    return GUI_ana_label_blank

#set the trigger channel
def GUI_Dropdown_analog_ch():
    
    GUI_Dropdown_analog_ch = widgets.Dropdown(      
        options=[('0', 0), ('1', 1), ('2', 2), ('3', 3)],
        value=0,
        description='ch: ',
        disabled=False,
        style = {'description_width': '37px'},
        layout={'width': '128px'}, 
    )
    return GUI_Dropdown_analog_ch

#set the analog trigger level
def GUI_Analog_Level():
    
    GUI_Analog_Level = widgets.FloatText(
        value=0.0,
        description='TL(V):',
        disabled=False,
        style = {'description_width': '37px'},
        layout={'width': '128px'}, 
    )
    return GUI_Analog_Level

def GUI_ana_ch_tl(a, b, c):
    
    GUI_ana_ch_tl = widgets.VBox(
        [
            a,
            b, 
            c, 
        ],
        layout = widgets.Layout(
            height='90px', 
            width='150px'
        ),
        align_items='flex-start',
    )
    return GUI_ana_ch_tl

def GUI_ana_all(a,b):

    GUI_ana_all = widgets.HBox(
        [
            a,
            b, 
        ],
        layout = widgets.Layout(
            height='110px', 
            width='300px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_ana_all

"""
part 3 dig cbox
"""

def GUI_dig_label():
    
    GUI_dig_label = widgets.Label(
        value="Digital Trigger:",
        layout = widgets.Layout(height='25px', width='100px'),
        align_items='flex-start'
    )
    return GUI_dig_label

def GUI_checkbox_dig_ris():
    
    GUI_checkbox_dig_ris = widgets.Checkbox(
        value=False,
        layout = widgets.Layout(height='22px', width='94px'),
        description='Rising Edge',
        disabled=False,
        indent=False
    )
    return GUI_checkbox_dig_ris

def GUI_checkbox_dig_fal():
    
    GUI_checkbox_dig_fal = widgets.Checkbox(
        value=False,
        layout = widgets.Layout(height='22px', width='94px'),
        description='Falling Edge',
        disabled=False,
        indent=False
    )
    return GUI_checkbox_dig_fal

def GUI_hbox_dig_ris(a, b):
    
    GUI_hbox_dig_ris = widgets.HBox(
        [
            a,
            b
        ],
        layout = widgets.Layout(height='30px', width='128px'),
        align_items='flex-start'
    )
    return GUI_hbox_dig_ris

def GUI_hbox_dig_fal(a, b):
    
    GUI_hbox_dig_fal = widgets.HBox(
        [
            a,
            b
        ],
        layout = widgets.Layout(height='30px', width='128px'),
        align_items='flex-start'
    )
    return GUI_hbox_dig_fal

def GUI_dig_cbox(a, b, c):
    
    GUI_dig_cbox = widgets.VBox(
        [
            a,
            b,
            c,
        ],
        layout = widgets.Layout(
            height='110px', 
            width='150px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_dig_cbox

"""
part 4 zoom
"""

def GUI_zoom_title():
    
    GUI_zoom_title = widgets.Label(
        value="Visualization:",
        layout = widgets.Layout(height='25px', width='100px'),
        align_items='flex-start'
    )
    return GUI_zoom_title

def GUI_Scale():
    
    GUI_Scale = widgets.IntSlider(
        value=10,
        min=1,
        max=100,
        step=1,
        description='Scale:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout = widgets.Layout(height='30px', width='278px'),
        style = {'description_width': '50px'},
    )
    return GUI_Scale

def GUI_delay():
    
    GUI_delay = widgets.IntSlider(
        value=-(2**(Dep_Mem - 1)),
        min=-(2**(Dep_Mem - 1)),
        max=(2**(Dep_Mem - 1))-1,
        step=1,
        description='Position:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout = widgets.Layout(height='30px', width='278px'),
        style = {'description_width': '50px'},
    )
    return GUI_delay

def GUI_zoom1(a, b):
    
    GUI_zoom1 = widgets.VBox(
        [
            GUI_zoom_title(),
            a, 
            b,
        ],
        layout = widgets.Layout(
            height='110px', 
            width='300px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_zoom1

"""
part 5 bandpass
"""

def GUI_bandpass_label():
    
    GUI_bandpass_label = widgets.Label(
        value="Passfilter:",
        layout = widgets.Layout(height='25px', width='70px'),
        align_items='flex-start'
    )
    return GUI_bandpass_label

#set the lower limit
def GUI_bandpass_low():
    
    GUI_bandpass_low = widgets.FloatText(
        value=0.0,
        disabled=False,
        layout = widgets.Layout(height='22px', width='60px'),
    )
    return GUI_bandpass_low

#set the higher limit
def GUI_bandpass_high():
    
    GUI_bandpass_high = widgets.FloatText(
        value=0.0,
        disabled=False,
        layout = widgets.Layout(height='22px', width='60px'),
    )
    return GUI_bandpass_high

def GUI_checkbox_low():
    
    GUI_checkbox_low = widgets.Checkbox(
        value=False,
        layout = widgets.Layout(height='22px', width='140px'),
        description='Lower bound (kHz):',
        disabled=False,
        indent=False
    )
    return GUI_checkbox_low

def GUI_checkbox_high():
    
    GUI_checkbox_high = widgets.Checkbox(
        value=False,
        layout = widgets.Layout(height='22px', width='140px'),
        description='Higher bound (kHz):',
        disabled=False,
        indent=False
    )
    return GUI_checkbox_high

def GUI_hbox_low(a, b):
    
    GUI_hbox_low = widgets.HBox(
        [
            a,
            b,
        ],
        layout = widgets.Layout(height='30px', width='210px'),
        align_items='flex-start'
    )
    return GUI_hbox_low

def GUI_hbox_high(a, b):
    
    GUI_hbox_high = widgets.HBox(
        [
            a,
            b,
        ],
        layout = widgets.Layout(height='30px', width='210px'),
        align_items='flex-start'
    )
    return GUI_hbox_high

def GUI_bandpass(a, b, c):
    
    GUI_bandpass = widgets.VBox(
        [
            a,
            b, 
            c, 
        ],
        layout = widgets.Layout(
            height='110px', 
            width='230px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_bandpass

"""
part 6 Enhancement
"""

def GUI_Dropdown_Enh_ch():
    
    GUI_Dropdown_Enh_ch = widgets.Dropdown(      
        options=[('0', 0), ('1', 1), ('2', 2), ('3', 3)],
        value=0,
        description='ch: ',
        disabled=False,
        style = {'description_width': '37px'},
        layout={'width': '128px'}, 
    )
    return GUI_Dropdown_Enh_ch

def GUI_blankline():
    
    GUI_blankline = widgets.Label(
        value="  ",
        layout = widgets.Layout(height='25px', width='20px'),
        align_items='top'
    )
    return GUI_blankline

def GUI_Enh_title():
    
    GUI_Enh_title = widgets.Label(
        value="Enhancement:",
        layout = widgets.Layout(height='25px', width='90px'), #min 90px
        align_items='top'
    )
    return GUI_Enh_title

def GUI_Enh_tau():
    
    GUI_Enh_tau = widgets.FloatText(
        value=1,
        description=r'$\tau$:',
        disabled=False,
        style = {'description_width': '37px'},
        layout={'width': '128px'}, 
    )
    return GUI_Enh_tau

def GUI_Enh_DC():
    
    GUI_Enh_DC = widgets.ToggleButton(
        value=False,
        description='Remove DC',
        disabled=False,
        button_style='',
        icon='',
        layout = widgets.Layout(height='30px', width='100px'), #min 100px
    )
    return GUI_Enh_DC

def GUI_Enh_sensitivity():
    
    GUI_Enh_sensitivity = widgets.ToggleButton(
        value=False,
        description='Sensitivity',
        disabled=False,
        button_style='',
        icon='',
        layout = widgets.Layout(height='30px', width='128px'),
    )
    return GUI_Enh_sensitivity

def GUI_Enh_Resolution():
    
    GUI_Enh_Resolution = widgets.ToggleButton(
        value=False,
        description='Resolution',
        disabled=False,
        button_style='',
        icon='',
        layout = widgets.Layout(height='30px', width='128px'),
    )
    return GUI_Enh_Resolution

def GUI_blankline_Enh():
    
    GUI_blankline_Enh = widgets.Label(
        value="  ",
        layout = widgets.Layout(height='20px', width='20px'),
        align_items='top'
    )
    return GUI_blankline_Enh

def GUI_Enh_2x2(a, b, c):
    
    GUI_Enh_2x2 = widgets.TwoByTwoLayout(
        top_left=a,
        bottom_left=b,
        top_right=c,
        merge=False
    )
    return GUI_Enh_2x2

def GUI_Enh1(a, b, c):
    
    GUI_Enh1 = widgets.VBox(
        [
            a,
            b, 
            c,
        ],
        layout = widgets.Layout(height='90px', width='162px'),
        align_items='top',
    )
    return GUI_Enh1

def GUI_Enh2(a, b, c):
    
    GUI_Enh2 = widgets.VBox(
        [
            a,
            b,
            c,
        ],
        layout = widgets.Layout(height='92px', width='150px'),
        align_items='top',
    )
    return GUI_Enh2

def GUI_Enh(a, b):
    
    GUI_Enh = widgets.HBox(
        [
            a,
            b,
        ],
        layout = widgets.Layout(
            height='110px', 
            width='300px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_Enh

"""
save file
"""

def GUI_save_label():
    
    GUI_save_label = widgets.Label(
        value="Save Data:",
        layout = widgets.Layout(height='25px', width='70px'),
        align_items='flex-start'
    )
    return GUI_save_label

def GUI_save_name():
    
    GUI_save_name = widgets.Text(
        description="File Name:",
        layout = widgets.Layout(height='30px', width='276px'),
        style = {'description_width': '70px'},
    )
    return GUI_save_name

def GUI_save_format():
    
    GUI_save_format = widgets.Dropdown(      
        options=[('.csv', 0), ('.txt', 1)],
        value=0,
        description='Save as:',
        disabled=False,
        style = {'description_width': '70px'},
        layout={
            'width': '180px',
            'height':'30px',
        }, 
    )
    return GUI_save_format

def GUI_save_button():
    
    GUI_save_button = widgets.Button(
    description='Save',
    layout = widgets.Layout(height='30px', width='94px'),
    )
    return GUI_save_button
   
def GUI_save_HBox(a, b):

    GUI_save_HBox = widgets.HBox(
        [
            a,
            b,
        ],
        layout = widgets.Layout(height='34px', width='280px'),
        align_items='flex-start'
    )
    return GUI_save_HBox
    
def GUI_save(a, b, c):
    
    GUI_save = widgets.VBox(
        [
            a,
            b, 
            c,
        ],
        layout = widgets.Layout(
            height='110px', 
            width='300px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_save

"""
FFT
"""

def GUI_FFT_label():
    
    GUI_FFT_label = widgets.Label(
        value="FFT: ",
        layout = widgets.Layout(height='25px', width='70px'),
        align_items='flex-start'
    )
    return GUI_FFT_label

def GUI_FFT_run_stop():
    
    GUI_TBtn_run_stop = widgets.ToggleButton(
        value=False,
        description='FFT Run/Stop',
        disabled=False,
        button_style='',
        tooltip='FFT Run/Stop',
        icon='',
        layout = widgets.Layout(height='30px', width='128px'),
    )
    return GUI_TBtn_run_stop

def GUI_FFT_ch():
    
    GUI_FFT_ch = widgets.Dropdown(      
        options=[('0', 0), ('1', 1), ('2', 2), ('3', 3)],
        value=0,
        description='Channel: ',
        style = {'description_width': '60px'},
        layout={'width': '128px'}, 
    )
    return GUI_FFT_ch

def GUI_FFT(a, b, c):
    
    GUI_FFT = widgets.VBox(
        [
            a,
            b,
            c,
        ],
        layout = widgets.Layout(
            height='110px', 
            width='150px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_FFT

"""
show real-time B0
"""
def GUI_B0_label():

    GUI_B0_label = widgets.Label(
        value = "B0 Control:",
        layout = widgets.Layout(height = '25px', width = '80px'),
        align_items='flex-start'
    )
    return GUI_B0_label

def GUI_B0_goal():
    
    GUI_B0_goal = widgets.Text(
        description="Goal B0[T]:",
        layout = widgets.Layout(height = '25px', width = '160px'),
        style = {'description_width': '63px'},
    )
    return GUI_B0_goal

def GUI_B0_now():
    
    GUI_B0_now = widgets.Text(
        description="Now B0[T]:",
        layout = widgets.Layout(height = '25px', width = '160px'),
        style = {'description_width': '63px'},
    )
    return GUI_B0_now

def GUI_B0(a, b, c):
    
    GUI_B0 = widgets.VBox(
        [
            a,
            b,
            c,
        ],
        layout = widgets.Layout(
            height='110px', 
            width='190px',
            border='solid 4px lightgreen',
            margin='0px 5px 0px 0px',
            padding='0px 5px 0px 5px'
        ),
        align_items='flex-start',
    )
    return GUI_B0


def GUI_head(a, b):
    
    GUI_head = widgets.HBox(
        [
            a,
            b,
        ],
        layout = widgets.Layout(height='80px', width='800px'),
        align_items='flex-start',
    )
    return GUI_head

def GUI_pulse_gen(a):
    
    GUI_pulse_gen = widgets.HBox(
        [
            a,
        ],
        layout = widgets.Layout(height='100px', width='1870px'),
        align_items='flex-start',
    )
    return GUI_pulse_gen

def GUI_head_blank():
    
    GUI_ana_label_blank = widgets.Label(
        value=" ",
        layout = widgets.Layout(height='22px', width='41px'),
        align_items='flex-start'
    )
    return GUI_ana_label_blank

def GUI_tracing(
    module1,
    module2,
    module3,
    module4,
    module5,
    module6,
    module7,
    module8, #sub GUI for B0 Control
):
    
    GUI_tracing = widgets.HBox(
        [
#             GUI_head_blank(),
            module1,
            module2,
            module3,
            module4,
            module5,
            module6,
            module7,
            module8, #sub GUI for B0 Control
        ],
        layout = widgets.Layout(height='115px', width='1890px'),
        align_items='flex-start',
    )
    return GUI_tracing

def GUI_total(a, b, c, d):
    
    GUI_total = widgets.VBox(
        [
            a,
            b,
            c,
            d,
        ],
        layout = widgets.Layout(height='auto', width='1890px'),
        align_items='flex-start',
    )
    return GUI_total

#NMR_CHIP_CFG
GUI_chip_cfg_ref_current = GUI_chip_cfg_ref_current()
GUI_chip_cfg_ref_current_box = GUI_chip_cfg_ref_current_box(GUI_chip_cfg_ref_current)
GUI_chip_cfg_vga_gain = GUI_chip_cfg_vga_gain()
GUI_chip_cfg_vga_gain_box = GUI_chip_cfg_vga_gain_box(GUI_chip_cfg_vga_gain)
GUI_chip_cfg_pll_mult = GUI_chip_cfg_pll_mult()
GUI_chip_cfg_pll_mult_box = GUI_chip_cfg_pll_mult_box(GUI_chip_cfg_pll_mult)
GUI_chip_cfg_box = GUI_chip_cfg_box(GUI_chip_cfg_ref_current_box, GUI_chip_cfg_vga_gain_box, GUI_chip_cfg_pll_mult_box)

# Tracing
#icons
GUI_logo = GUI_logo()
GUI_logo_iis = GUI_logo_iis()
ris_edge = ris_edge()
fal_edge = fal_edge()
GUI_blankline = GUI_blankline()

#onoff button
GUI_TBtn_arm = GUI_TBtn_arm()
GUI_TBtn_run_stop = GUI_TBtn_run_stop()
GUI_onoff = GUI_onoff(GUI_TBtn_run_stop, GUI_TBtn_arm)

#ana trigger cbox
GUI_ana_label_blank = GUI_ana_label_blank()
GUI_checkbox_ana_ris = GUI_checkbox_ana_ris()
GUI_checkbox_ana_fal = GUI_checkbox_ana_fal()
GUI_hbox_ana_ris = GUI_hbox_ana_ris(ris_edge, GUI_checkbox_ana_ris)
GUI_hbox_ana_fal = GUI_hbox_ana_fal(fal_edge, GUI_checkbox_ana_fal)
GUI_ana_cbox = GUI_ana_cbox(GUI_ana_label_blank, GUI_hbox_ana_ris, GUI_hbox_ana_fal)

#ana trigger ch tl
GUI_ana_label = GUI_ana_label()
GUI_Dropdown_analog_ch = GUI_Dropdown_analog_ch()
GUI_Analog_Level = GUI_Analog_Level()
GUI_ana_ch_tl = GUI_ana_ch_tl(GUI_ana_label, GUI_Dropdown_analog_ch, GUI_Analog_Level)
GUI_ana_all = GUI_ana_all(GUI_ana_ch_tl, GUI_ana_cbox)

#dig trigger cbox
GUI_dig_label = GUI_dig_label()
GUI_checkbox_dig_ris = GUI_checkbox_dig_ris()
GUI_checkbox_dig_fal = GUI_checkbox_dig_fal()
GUI_hbox_dig_ris = GUI_hbox_dig_ris(ris_edge, GUI_checkbox_dig_ris)
GUI_hbox_dig_fal = GUI_hbox_dig_fal(fal_edge, GUI_checkbox_dig_fal)
GUI_dig_cbox = GUI_dig_cbox(GUI_dig_label, GUI_hbox_dig_ris, GUI_hbox_dig_fal)

#zoom1
GUI_Scale = GUI_Scale()
GUI_delay = GUI_delay()
GUI_zoom1 = GUI_zoom1(GUI_Scale, GUI_delay)

#Enh1
GUI_Enh_title = GUI_Enh_title()
GUI_Dropdown_Enh_ch = GUI_Dropdown_Enh_ch()
GUI_Enh_tau = GUI_Enh_tau()
GUI_Enh1 = GUI_Enh1(GUI_Enh_title, GUI_Dropdown_Enh_ch, GUI_Enh_tau)
GUI_blankline_Enh = GUI_blankline_Enh()
#Enh2
GUI_Enh_sensitivity = GUI_Enh_sensitivity()
GUI_Enh_Resolution = GUI_Enh_Resolution()
GUI_Enh_DC = GUI_Enh_DC()
GUI_Enh_2x2 = GUI_Enh_2x2(GUI_Enh_sensitivity, GUI_Enh_Resolution, GUI_Enh_DC)
GUI_Enh2 = GUI_Enh2(GUI_blankline_Enh, GUI_Enh_sensitivity, GUI_Enh_Resolution)
#Enh
GUI_Enh = GUI_Enh(GUI_Enh1, GUI_Enh2)

#Save
GUI_save_label = GUI_save_label()
GUI_save_name = GUI_save_name()
GUI_save_format = GUI_save_format()
GUI_save_button = GUI_save_button()
GUI_save_HBox = GUI_save_HBox(GUI_save_format, GUI_save_button)
GUI_save = GUI_save(GUI_save_label, GUI_save_name, GUI_save_HBox)

#bandpass
GUI_bandpass_label = GUI_bandpass_label()
GUI_bandpass_low = GUI_bandpass_low()
GUI_bandpass_high = GUI_bandpass_high()
GUI_checkbox_low = GUI_checkbox_low()
GUI_checkbox_high = GUI_checkbox_high()
GUI_hbox_low = GUI_hbox_low(GUI_checkbox_low, GUI_bandpass_low)
GUI_hbox_high = GUI_hbox_high(GUI_checkbox_high, GUI_bandpass_high)
GUI_bandpass = GUI_bandpass(GUI_bandpass_label, GUI_hbox_low, GUI_hbox_high)

#FFT
GUI_FFT_label = GUI_FFT_label()
GUI_FFT_run_stop = GUI_FFT_run_stop()
GUI_FFT_ch = GUI_FFT_ch()
GUI_FFT = GUI_FFT(GUI_FFT_label, GUI_FFT_run_stop, GUI_FFT_ch)

#B0
GUI_B0_label = GUI_B0_label()
GUI_B0_goal = GUI_B0_goal()
GUI_B0_now = GUI_B0_now()
GUI_B0 = GUI_B0(GUI_B0_label, GUI_B0_goal, GUI_B0_now)

def GUI_prop_init():

    GUI_TBtn_run_stop.button_style = 'danger'
    GUI_TBtn_arm.button_style = 'danger'
    GUI_TBtn_arm.disabled = True
    GUI_Enh_sensitivity.button_style = 'danger'
    GUI_Enh_Resolution.button_style = 'danger'
    GUI_Enh_DC.button_style = 'danger'
    GUI_save_button.disabled = True
    GUI_FFT_run_stop.button_style = 'danger'

    return

def GUI_plot():

    GUI_plot = go.FigureWidget(layout={'hovermode' : 'closest',
                            'height'    : 450,
                            'width'     : 1430,
                            'margin'    : 
                            {
                                't':0, 'b':20, 'l':0, 'r':0
                            },
                            'showlegend' : True,
                            'xaxis_title': 'Time',
                            'yaxis_title': 'Value',
                            })

    Analog0_stream = [0]
    Analog1_stream = [0]
    Analog2_stream = [0]
    Analog3_stream = [0]

    GUI_plot.layout.yaxis.range = [-sample_value_half, sample_value_half]
    GUI_plot.layout.xaxis.range = [0, point_number_on_screen]

    GUI_plot.add_trace(go.Scattergl(
        y = Analog0_stream,
        name = 'Channel 0',
        showlegend = True,)
                    )

    GUI_plot.add_trace(go.Scattergl(
        y = Analog1_stream,
        name = 'Channel 1',
        showlegend = True,)
                    )

    GUI_plot.add_trace(go.Scattergl(
        y = Analog2_stream,
        name = 'Channel 2',
        showlegend = True,)
                    )

    GUI_plot.add_trace(go.Scattergl(
        y = Analog3_stream,
        name = 'Channel 3',
        showlegend = True,)
                    )

    GUI_plot.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))

    return GUI_plot

def GUI_plot_FFT():

    GUI_plot_FFT = go.FigureWidget(layout={'hovermode' : 'closest',
                            'height'    : 450,
                            'width'     : 400,
                            'margin'    : 
                            {
                                't':0, 'b':20, 'l':0, 'r':0
                            },
                            'showlegend' : False,
                            'xaxis_title': 'Frequency',
                            'yaxis_title': 'Amplitude',
                            })

    GUI_plot_FFT.layout.yaxis.range = [0, 1]
    GUI_plot_FFT.layout.xaxis.range = [0, point_number_on_screen/2]
    normalization_half_y = [0]

    GUI_plot_FFT.add_trace(go.Scattergl(
        y = normalization_half_y,
        name = 'FFT',
        showlegend = True,)
                    )
    return GUI_plot_FFT

def GUI_plot_3D():

    GUI_plot_3D = go.FigureWidget(data=go.Scatter3d(
    x=[0], y=[0], z=[0],
    marker=dict(
        size=4,
    #         color=z,
    #         colorscale='Viridis',
        ),
        line=dict(
            color='lightgreen',
            width=2
        )
    ))

    GUI_plot_3D.update_layout(
        width=1830,
        height=500,
        autosize=False,
        scene=dict(
            camera=dict(
                up=dict(
                    x=0,
                    y=0,
                    z=1
                ),
                eye=dict(
                    x=-0.2,
                    y=1,
                    z=0.2,
                )
            ),
            aspectmode = 'manual'
        ),
    )

    return GUI_plot_3D

"""
Functions for config Change
"""
#conf_dict['conf_token'] is an indicater for update the conf_paras.
#when this == 1, update all other Paras.
mmio = data_processing.mmio
conf_dict = all_of_the_parameters.conf_dict

# observe function for nmr_chip_cfg 
def on_value_change_GUI_chip_cfg_ref_current(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_nmr_chip_cfg_ref_curr'], change['new'])
        #config nmr chip
    ref_curr = mmio.read(conf_dict['conf_nmr_chip_cfg_ref_curr'])
    vga_gain = mmio.read(conf_dict['conf_nmr_chip_cfg_vga_gain'])
    pll_mult = mmio.read(conf_dict['conf_nmr_chip_cfg_pll_mult'])
    fpga_tracing_func.fpga_func_chip_cfg(ref_curr * 256 + vga_gain * 16 + pll_mult)

    return

def on_value_change_GUI_chip_cfg_vga_gain(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_nmr_chip_cfg_vga_gain'], change['new'])
        #config nmr chip
    ref_curr = mmio.read(conf_dict['conf_nmr_chip_cfg_ref_curr'])
    vga_gain = mmio.read(conf_dict['conf_nmr_chip_cfg_vga_gain'])
    pll_mult = mmio.read(conf_dict['conf_nmr_chip_cfg_pll_mult'])
    fpga_tracing_func.fpga_func_chip_cfg(ref_curr * 256 + vga_gain * 16 + pll_mult)

    return

def on_value_change_GUI_chip_cfg_pll_mult(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_nmr_chip_cfg_pll_mult'], change['new'])
        #config nmr chip
    ref_curr = mmio.read(conf_dict['conf_nmr_chip_cfg_ref_curr'])
    vga_gain = mmio.read(conf_dict['conf_nmr_chip_cfg_vga_gain'])
    pll_mult = mmio.read(conf_dict['conf_nmr_chip_cfg_pll_mult'])
    fpga_tracing_func.fpga_func_chip_cfg(ref_curr * 256 + vga_gain * 16 + pll_mult)

    return

# observe function for tracing 
def on_value_change_GUI_run_stop(change):
    
    trigger  = GUI_TBtn_arm.value #0 = triggered, 1 = not triggered
    mmio.write(conf_dict['conf_token'], 1)
    if trigger == 0: #not trigger
        if change['new'] == True:#0 = disable, 1 = enable
            mmio.write(conf_dict['conf_onoff'], 1)
            GUI_TBtn_run_stop.button_style = 'success'
            GUI_TBtn_run_stop.description='Run/Stop'
        elif change['new'] == False: 
            mmio.write(conf_dict['conf_onoff'], 0)
            GUI_TBtn_run_stop.button_style = 'danger'
            GUI_TBtn_run_stop.description='Run/Stop'    
    if trigger == 1: #trigger
        if change['new'] == True:#0 = disable, 1 = enable
            mmio.write(conf_dict['conf_onoff'], 1)
            GUI_TBtn_run_stop.button_style = 'warning'
            GUI_TBtn_run_stop.description='Single'
        elif change['new'] == False: 
            mmio.write(conf_dict['conf_onoff'], 0)
            GUI_TBtn_run_stop.button_style = 'warning'
            GUI_TBtn_run_stop.description='Single' 

    return

def on_value_change_Trigger_Activate(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:#0 = 'arm', 1 = 'singleshot'
        mmio.write(conf_dict['conf_trigger'], 0) #triggered
        GUI_TBtn_arm.button_style = 'success'
        GUI_TBtn_arm.description='Trigger Activated'
#         GUI_TBtn_run_stop.value = False
#         GUI_TBtn_run_stop.description='Single'
#         GUI_TBtn_run_stop.button_style = 'warning'
    elif change['new'] == False:
        mmio.write(conf_dict['conf_trigger'], 1) #not triggered
        GUI_TBtn_arm.button_style = 'danger'
        GUI_TBtn_arm.description='Trigger Activate'
#         GUI_TBtn_run_stop.description='Run/Stop'
#         GUI_TBtn_run_stop.button_style = 'danger'
#         GUI_TBtn_run_stop.value = False

    return

def on_value_change_ana_ris(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_ana_ris'], 1)
        GUI_TBtn_arm.disabled = False
        GUI_checkbox_dig_ris.value = False
        GUI_checkbox_dig_fal.value = False
    elif change['new'] == False:
        mmio.write(conf_dict['conf_ana_ris'], 0)
        if (
            GUI_checkbox_ana_ris.value == False and
            GUI_checkbox_ana_fal.value == False and
            GUI_checkbox_dig_ris.value == False and
            GUI_checkbox_dig_fal.value == False
        ):
            GUI_TBtn_arm.disabled = True
            GUI_TBtn_arm.value = False

    return

def on_value_change_ana_fal(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_ana_fal'], 1)
        GUI_TBtn_arm.disabled = False
        GUI_checkbox_dig_ris.value = False
        GUI_checkbox_dig_fal.value = False
    elif change['new'] == False:
        mmio.write(conf_dict['conf_ana_fal'], 0)
        if (
            GUI_checkbox_ana_ris.value == False and
            GUI_checkbox_ana_fal.value == False and
            GUI_checkbox_dig_ris.value == False and
            GUI_checkbox_dig_fal.value == False
        ):
            GUI_TBtn_arm.disabled = True
            GUI_TBtn_arm.value = False

    return

def on_value_change_ana_ch(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_ana_ch'], change['new'])

    return

def on_value_change_ana_TL(change):

    mmio.write(conf_dict['conf_token'], 1)
    trigger_level = int(change['new']) * sample_size
    mmio.write(conf_dict['conf_ana_tl'], trigger_level)

    return

def on_value_change_dig_ris(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_dig_ris'], 1)
        GUI_TBtn_arm.disabled = False
        GUI_checkbox_ana_ris.value = False
        GUI_checkbox_ana_fal.value = False
    elif change['new'] == False:
        mmio.write(conf_dict['conf_dig_ris'], 0)
        if (
            GUI_checkbox_ana_ris.value == False and
            GUI_checkbox_ana_fal.value == False and
            GUI_checkbox_dig_ris.value == False and
            GUI_checkbox_dig_fal.value == False
        ):
            GUI_TBtn_arm.disabled = True
            GUI_TBtn_arm.value = False

    return

def on_value_change_dig_fal(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_dig_fal'], 1)
        GUI_TBtn_arm.disabled = False
        GUI_checkbox_ana_ris.value = False
        GUI_checkbox_ana_fal.value = False
    elif change['new'] == False:
        mmio.write(conf_dict['conf_dig_fal'], 0)
        if (
            GUI_checkbox_ana_ris.value == False and
            GUI_checkbox_ana_fal.value == False and
            GUI_checkbox_dig_ris.value == False and
            GUI_checkbox_dig_fal.value == False
        ):
            GUI_TBtn_arm.disabled = True
            GUI_TBtn_arm.value = False

    return

def on_value_change_Scale(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_scale'], change['new'])

    return

def on_value_change_Position(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_position'], change['new'])

    return
    
def on_value_change_fft_ch(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_fft_ch'], change['new'])

    return

def on_value_change_fft_onoff(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_fft_onoff'], 1)
        GUI_FFT_run_stop.button_style = 'success'
    else: 
        mmio.write(conf_dict['conf_fft_onoff'], 0)
        GUI_FFT_run_stop.button_style = 'danger'

    return

def on_value_change_enh_ch(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_enh_ch'], change['new'])

    return

def on_value_change_enh_sen(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        GUI_Enh_sensitivity.button_style = 'success'
        mmio.write(conf_dict['conf_enh_sen'], 1)
    elif change['new'] == False:
        GUI_Enh_sensitivity.button_style = 'danger'
        mmio.write(conf_dict['conf_enh_sen'], 0)

    return

def on_value_change_enh_res(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        GUI_Enh_Resolution.button_style = 'success'
        mmio.write(conf_dict['conf_enh_res'], 1)
    elif change['new'] == False:
        GUI_Enh_Resolution.button_style = 'danger'
        mmio.write(conf_dict['conf_enh_res'], 0)

    return

def on_value_change_enh_tau(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_enh_tau'], change['new'])

    return

def on_value_change_enh_dc(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        GUI_Enh_DC.button_style = 'success'
        mmio.write(conf_dict['conf_enh_dc'], 1)
    elif change['new'] == False:
        GUI_Enh_DC.button_style = 'danger'
        mmio.write(conf_dict['conf_enh_dc'], 0)

    return

def on_value_change_bp_low_value(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_enh_bp_low_value'], change['new'])

    return

def on_value_change_bp_high_value(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_enh_bp_high_value'], change['new'])

    return

def on_value_change_bp_low_cb(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_enh_bp_low_cb'], 1)
    elif change['new'] == False:
        mmio.write(conf_dict['conf_enh_bp_low_cb'], 0)

    return

def on_value_change_bp_high_cb(change):

    mmio.write(conf_dict['conf_token'], 1)
    if change['new'] == True:
        mmio.write(conf_dict['conf_enh_bp_high_cb'], 1)
    elif change['new'] == False:
        mmio.write(conf_dict['conf_enh_bp_high_cb'], 0)

    return

def on_save_btn_click(self):    

    mmio.write(conf_dict['conf_save_file'], 1)

    return

def on_value_change_B0_goal(change):

    mmio.write(conf_dict['conf_token'], 1)
    mmio.write(conf_dict['conf_B0_goal'], change['new'])

    return

# observing nmr_chip_cfg GUI element
GUI_chip_cfg_ref_current.observe(on_value_change_GUI_chip_cfg_ref_current, names='value')
GUI_chip_cfg_vga_gain.observe(on_value_change_GUI_chip_cfg_vga_gain, names='value')
GUI_chip_cfg_pll_mult.observe(on_value_change_GUI_chip_cfg_pll_mult, names='value')

# observing tracing GUI element
GUI_TBtn_run_stop.observe(on_value_change_GUI_run_stop, names='value')
GUI_TBtn_arm.observe(on_value_change_Trigger_Activate, names='value')

GUI_checkbox_ana_ris.observe(on_value_change_ana_ris, names='value')
GUI_checkbox_ana_fal.observe(on_value_change_ana_fal, names='value')
GUI_Dropdown_analog_ch.observe(on_value_change_ana_ch, names='value')
GUI_Analog_Level.observe(on_value_change_ana_TL, names='value')

GUI_checkbox_dig_ris.observe(on_value_change_dig_ris, names='value')
GUI_checkbox_dig_fal.observe(on_value_change_dig_fal, names='value')

GUI_Dropdown_Enh_ch.observe(on_value_change_enh_ch, names='value')
GUI_Enh_tau.observe(on_value_change_enh_tau, names='value')
GUI_Enh_DC.observe(on_value_change_enh_dc, names='value')
GUI_Enh_sensitivity.observe(on_value_change_enh_sen, names='value')
GUI_Enh_Resolution.observe(on_value_change_enh_res, names='value')

GUI_bandpass_low.observe(on_value_change_bp_low_value, names='value')
GUI_bandpass_high.observe(on_value_change_bp_high_value, names='value')
GUI_checkbox_low.observe(on_value_change_bp_low_cb, names='value')
GUI_checkbox_high.observe(on_value_change_bp_high_cb, names='value')

GUI_Scale.observe(on_value_change_Scale, names='value')
GUI_delay.observe(on_value_change_Position, names='value')

GUI_FFT_ch.observe(on_value_change_fft_ch, names='value')
GUI_FFT_run_stop.observe(on_value_change_fft_onoff, names='value')

GUI_save_button.on_click(on_save_btn_click)

GUI_B0_goal.observe(on_value_change_B0_goal, names='value')