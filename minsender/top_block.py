#!/usr/bin/env python2
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Nov 10 16:24:02 2010
##################################################

from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
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
		self.tunefreq = tunefreq = 0
		self.samp_rate = samp_rate = 1000000

		##################################################
		# Notebooks
		##################################################
		self.n0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "t1")
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "t2")
		self.n0.AddPage(grc_wxgui.Panel(self.n0), "t3")
		self.Add(self.n0)

		##################################################
		# Controls
		##################################################
		_tunefreq_sizer = wx.BoxSizer(wx.VERTICAL)
		self._tunefreq_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_tunefreq_sizer,
			value=self.tunefreq,
			callback=self.set_tunefreq,
			label="tunefreq",
			converter=forms.int_converter(),
			proportion=0,
		)
		self._tunefreq_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_tunefreq_sizer,
			value=self.tunefreq,
			callback=self.set_tunefreq,
			minimum=-100,
			maximum=100,
			num_steps=200,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.Add(_tunefreq_sizer)

		##################################################
		# Blocks
		##################################################
		self.blks2_dxpsk_demod_0 = blks2.dbpsk_demod(
			samples_per_symbol=2,
			excess_bw=0.35,
			costas_alpha=0.175,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			gray_code=True,
			verbose=False,
			log=False,
		)
		self.blks2_dxpsk_mod_0 = blks2.dbpsk_mod(
			samples_per_symbol=4,
			excess_bw=0.35,
			gray_code=True,
			verbose=False,
			log=False,
		)
		self.blks2_packet_decoder_0 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
			),
		)
		self.blks2_packet_encoder_0 = grc_blks2.packet_mod_f(grc_blks2.packet_encoder(
				samples_per_symbol=2,
				bits_per_symbol=1,
				access_code="",
				pad_for_usrp=False,
			),
			payload_length=0,
		)
		self.gr_char_to_float_1 = gr.char_to_float()
		self.gr_sig_source_x_0 = gr.sig_source_f(samp_rate/2/2, gr.GR_SAW_WAVE, 1000, 127, 0)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_char*1, samp_rate/2)
		self.gr_throttle_0_0 = gr.throttle(gr.sizeof_char*1, samp_rate/2)
		self.gr_throttle_2 = gr.throttle(gr.sizeof_float*1, samp_rate/4/4)
		self.gr_throttle_2_0 = gr.throttle(gr.sizeof_float*1, samp_rate/4/4)
		self.wxgui_constellationsink2_1 = constsink_gl.const_sink_c(
			self.GetWin(),
			title="Constellation Plot",
			sample_rate=samp_rate/2*2*8,
			frame_rate=5,
			const_size=2048,
			M=4,
			theta=0,
			alpha=0.005,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=samp_rate/2*2*8/4,
			omega_limit=0.005,
		)
		self.Add(self.wxgui_constellationsink2_1.win)
		self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
			self.n0.GetPage(1).GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate/2/2,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
		)
		self.n0.GetPage(1).Add(self.wxgui_scopesink2_1.win)
		self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
			self.n0.GetPage(0).GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
		)
		self.n0.GetPage(0).Add(self.wxgui_scopesink2_2.win)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_throttle_0, 0), (self.blks2_dxpsk_mod_0, 0))
		self.connect((self.blks2_dxpsk_demod_0, 0), (self.gr_throttle_0_0, 0))
		self.connect((self.blks2_packet_encoder_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_throttle_0_0, 0), (self.blks2_packet_decoder_0, 0))
		self.connect((self.blks2_packet_decoder_0, 0), (self.gr_throttle_2, 0))
		self.connect((self.gr_throttle_2, 0), (self.wxgui_scopesink2_1, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_throttle_2_0, 0))
		self.connect((self.gr_throttle_2_0, 0), (self.blks2_packet_encoder_0, 0))
		self.connect((self.blks2_dxpsk_mod_0, 0), (self.blks2_dxpsk_demod_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.gr_char_to_float_1, 0))
		self.connect((self.gr_char_to_float_1, 0), (self.wxgui_scopesink2_2, 0))
		self.connect((self.blks2_dxpsk_mod_0, 0), (self.wxgui_constellationsink2_1, 0))

	def set_tunefreq(self, tunefreq):
		self.tunefreq = tunefreq
		self._tunefreq_slider.set_value(self.tunefreq)
		self._tunefreq_text_box.set_value(self.tunefreq)

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate/2/2)
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate/2/2)
		self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
		self.wxgui_constellationsink2_1.set_sample_rate(self.samp_rate/2*2*8)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

