#!/usr/bin/env python2
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov  9 13:50:36 2010
##################################################

from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 1000

		##################################################
		# Blocks
		##################################################
		self.blks2_ofdm_mod_0 = grc_blks2.packet_mod_b(blks2.ofdm_mod(
				options=grc_blks2.options(
					modulation="bpsk",
					fft_length=1024,
					occupied_tones=256,
					cp_length=512,
					pad_for_usrp=True,
					log=None,
					verbose=None,
				),
			),
			payload_length=0,
		)
		self.gr_float_to_char_0 = gr.float_to_char()
		self.gr_sig_source_x_0 = gr.sig_source_f(samp_rate, gr.GR_SIN_WAVE, 100, 127, 0)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_char*1, samp_rate)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=50,
			ref_scale=2.0,
			sample_rate=samp_rate*1000,
			fft_size=1024,
			fft_rate=30,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_throttle_0, 0), (self.blks2_ofdm_mod_0, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_float_to_char_0, 0))
		self.connect((self.gr_float_to_char_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.blks2_ofdm_mod_0, 0), (self.wxgui_fftsink2_0, 0))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate*1000)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

