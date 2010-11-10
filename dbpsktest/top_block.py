#!/usr/bin/env python2
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Nov 10 16:39:31 2010
##################################################

from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 8*2**10
		self.nsps_mod = nsps_mod = 4
		self.noise = noise = .1
		self.freq_off = freq_off = 0
		self.ebw_mod = ebw_mod = 0.35

		##################################################
		# Notebooks
		##################################################
		self.n0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "tab1")
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "tab2")
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "tab3")
		self.Add(self.n0)

		##################################################
		# Controls
		##################################################
		_nsps_mod_sizer = wx.BoxSizer(wx.VERTICAL)
		self._nsps_mod_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_nsps_mod_sizer,
			value=self.nsps_mod,
			callback=self.set_nsps_mod,
			label="Samples per symbol for DPSK modulator",
			converter=forms.int_converter(),
			proportion=0,
		)
		self._nsps_mod_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_nsps_mod_sizer,
			value=self.nsps_mod,
			callback=self.set_nsps_mod,
			minimum=2,
			maximum=32,
			num_steps=31,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.Add(_nsps_mod_sizer)
		_noise_sizer = wx.BoxSizer(wx.VERTICAL)
		self._noise_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_noise_sizer,
			value=self.noise,
			callback=self.set_noise,
			label="Noise",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._noise_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_noise_sizer,
			value=self.noise,
			callback=self.set_noise,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_noise_sizer)
		_freq_off_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq_off_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq_off_sizer,
			value=self.freq_off,
			callback=self.set_freq_off,
			label="Freq Offset",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq_off_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq_off_sizer,
			value=self.freq_off,
			callback=self.set_freq_off,
			minimum=-.5,
			maximum=.5,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_freq_off_sizer)
		_ebw_mod_sizer = wx.BoxSizer(wx.VERTICAL)
		self._ebw_mod_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_ebw_mod_sizer,
			value=self.ebw_mod,
			callback=self.set_ebw_mod,
			label="Excess BW for DPSK modulator",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._ebw_mod_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_ebw_mod_sizer,
			value=self.ebw_mod,
			callback=self.set_ebw_mod,
			minimum=00.01,
			maximum=10.00,
			num_steps=10*100-1,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_ebw_mod_sizer)

		##################################################
		# Blocks
		##################################################
		self.blks2_dxpsk2_mod_0 = blks2.dqpsk2_mod(
			samples_per_symbol=nsps_mod,
			excess_bw=ebw_mod,
			gray_code=True,
			verbose=False,
			log=False,
		)
		self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
				samples_per_symbol=1,
				bits_per_symbol=1,
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.gr_agc2_xx_0 = gr.agc2_cc(1e-1, 1e-2, 1.0, 1.0, 1e3)
		self.gr_channel_model_0 = gr.channel_model(
			noise_voltage=noise,
			frequency_offset=freq_off,
			epsilon=1.0,
			taps=(16.0, ),
			noise_seed=42,
		)
		self.gr_throttle_1_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate*nsps_mod*8)
		self.random_source_x_0 = gr.vector_source_b(map(int, numpy.random.randint(0, 2, 1000)), True)
		self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
			self.n0.GetPage(1).GetWin(),
			title="Constellation Plot",
			sample_rate=samp_rate*8*nsps_mod/2,
			frame_rate=5,
			const_size=512,
			M=4,
			theta=0,
			alpha=0.005,
			fmax=0.5,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=samp_rate*8/2,
			omega_limit=0.005,
		)
		self.n0.GetPage(1).Add(self.wxgui_constellationsink2_0.win)

		##################################################
		# Connections
		##################################################
		self.connect((self.blks2_packet_encoder_0, 0), (self.blks2_dxpsk2_mod_0, 0))
		self.connect((self.random_source_x_0, 0), (self.blks2_packet_encoder_0, 0))
		self.connect((self.gr_channel_model_0, 0), (self.gr_agc2_xx_0, 0))
		self.connect((self.gr_throttle_1_0, 0), (self.wxgui_constellationsink2_0, 0))
		self.connect((self.blks2_dxpsk2_mod_0, 0), (self.gr_channel_model_0, 0))
		self.connect((self.gr_agc2_xx_0, 0), (self.gr_throttle_1_0, 0))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate*8*self.nsps_mod/2)

	def set_nsps_mod(self, nsps_mod):
		self.nsps_mod = nsps_mod
		self._nsps_mod_slider.set_value(self.nsps_mod)
		self._nsps_mod_text_box.set_value(self.nsps_mod)
		self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate*8*self.nsps_mod/2)

	def set_noise(self, noise):
		self.noise = noise
		self._noise_slider.set_value(self.noise)
		self._noise_text_box.set_value(self.noise)
		self.gr_channel_model_0.set_noise_voltage(self.noise)

	def set_freq_off(self, freq_off):
		self.freq_off = freq_off
		self._freq_off_slider.set_value(self.freq_off)
		self._freq_off_text_box.set_value(self.freq_off)
		self.gr_channel_model_0.set_frequency_offset(self.freq_off)

	def set_ebw_mod(self, ebw_mod):
		self.ebw_mod = ebw_mod
		self._ebw_mod_slider.set_value(self.ebw_mod)
		self._ebw_mod_text_box.set_value(self.ebw_mod)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

