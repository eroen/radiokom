#!/usr/bin/env python2
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov  9 11:57:58 2010
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import scopesink2
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
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0)
		self.gr_descrambler_bb_0 = gr.descrambler_bb(0x8A, 0x7F, 7)
		self.gr_float_to_complex_0 = gr.float_to_complex(1)
		self.gr_packed_to_unpacked_xx_0 = gr.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
		self.gr_scrambler_bb_0 = gr.scrambler_bb(0x8A, 0x7F, 7)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_throttle_0_0 = gr.throttle(gr.sizeof_char*1, samp_rate)
		self.gr_throttle_0_0_0 = gr.throttle(gr.sizeof_char*1, samp_rate*8)
		self.gr_throttle_0_0_0_0 = gr.throttle(gr.sizeof_char*1, samp_rate*8*8)
		self.gr_uchar_to_float_0 = gr.uchar_to_float()
		self.gr_unpacked_to_packed_xx_0 = gr.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
		self.gr_vector_source_x_0 = gr.vector_source_b((0, 1, 3,7,255,3,1,0), True, 1)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate*32,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
		)
		self.Add(self.wxgui_scopesink2_0.win)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_float_to_complex_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.const_source_x_0, 0), (self.gr_float_to_complex_0, 1))
		self.connect((self.gr_throttle_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.gr_vector_source_x_0, 0), (self.gr_throttle_0_0, 0))
		self.connect((self.gr_throttle_0_0, 0), (self.gr_packed_to_unpacked_xx_0, 0))
		self.connect((self.gr_descrambler_bb_0, 0), (self.gr_unpacked_to_packed_xx_0, 0))
		self.connect((self.gr_packed_to_unpacked_xx_0, 0), (self.gr_throttle_0_0_0, 0))
		self.connect((self.gr_throttle_0_0_0, 0), (self.gr_scrambler_bb_0, 0))
		self.connect((self.gr_scrambler_bb_0, 0), (self.gr_throttle_0_0_0_0, 0))
		self.connect((self.gr_throttle_0_0_0_0, 0), (self.gr_descrambler_bb_0, 0))
		self.connect((self.gr_uchar_to_float_0, 0), (self.gr_float_to_complex_0, 0))
		self.connect((self.gr_unpacked_to_packed_xx_0, 0), (self.gr_uchar_to_float_0, 0))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate*32)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

