#!/usr/bin/env python2
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov  9 18:33:29 2010
##################################################

from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import scopesink2
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
		self.samp_rate = samp_rate = 10000

		##################################################
		# Notebooks
		##################################################
		self.n0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "tab1")
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "tab2")
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "tab3")
		self.Add(self.n0)

		##################################################
		# Blocks
		##################################################
		self.blks2_dxpsk2_mod_0 = blks2.dqpsk2_mod(
			samples_per_symbol=2,
			excess_bw=0.10,
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
		self.gr_char_to_float_0 = gr.char_to_float()
		self.gr_cma_equalizer_cc_0 = gr.cma_equalizer_cc(64, 2, 1.0*10**-9)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vff((1/85., ))
		self.gr_multiply_const_vxx_1 = gr.multiply_const_vcc((1./100, ))
		self.gr_repeat_0 = gr.repeat(gr.sizeof_char*1, 2*8)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_char*1, samp_rate)
		self.gr_throttle_0_0 = gr.throttle(gr.sizeof_char*1, samp_rate)
		self.gr_throttle_1 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate*2*8/2)
		self.gr_throttle_1_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate*2*8)
		self.gr_vector_source_x_0 = gr.vector_source_b((0, 85,0,0,0,0,0,0,0,0,000,0,0,0,0), True, 1)
		self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
			self.n0.GetPage(0).GetWin(),
			title="Constellation Plot",
			sample_rate=samp_rate*2*8,
			frame_rate=5,
			const_size=512,
			M=4,
			theta=0,
			alpha=0.005,
			fmax=0.5,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=samp_rate*2*8/2.,
			omega_limit=0.005,
		)
		self.n0.GetPage(0).Add(self.wxgui_constellationsink2_0.win)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.n0.GetPage(1).GetWin(),
			title="Scope Plot",
			sample_rate=8*20,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
		)
		self.n0.GetPage(1).Add(self.wxgui_scopesink2_0.win)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_vector_source_x_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.blks2_packet_encoder_0, 0))
		self.connect((self.blks2_packet_encoder_0, 0), (self.gr_throttle_0_0, 0))
		self.connect((self.gr_throttle_0_0, 0), (self.gr_repeat_0, 0))
		self.connect((self.gr_throttle_0_0, 0), (self.blks2_dxpsk2_mod_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.wxgui_scopesink2_0, 1))
		self.connect((self.gr_char_to_float_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_repeat_0, 0), (self.gr_char_to_float_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.gr_throttle_1_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.gr_throttle_1_0, 0), (self.wxgui_constellationsink2_0, 0))
		self.connect((self.gr_cma_equalizer_cc_0, 0), (self.gr_throttle_1_0, 0))
		self.connect((self.blks2_dxpsk2_mod_0, 0), (self.gr_throttle_1, 0))
		self.connect((self.gr_agc2_xx_0, 0), (self.gr_cma_equalizer_cc_0, 0))
		self.connect((self.gr_throttle_1, 0), (self.gr_multiply_const_vxx_1, 0))
		self.connect((self.gr_multiply_const_vxx_1, 0), (self.gr_agc2_xx_0, 0))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate*2*8)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

