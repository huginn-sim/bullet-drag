# -*- coding: utf-8 -*-
"""
.. module:: sample_data

.. moduleauthor:: Huginn
"""

from numpy import array

samples = {}
samples['50 ATV BT'] = \
	{
	#	Key		X - Horizontal Displacement						Y - Values 
		'v':	array(zip([0  , 100, 200, 300, 400, 500], 		[3300, 2889, 2514, 2168, 1851])),
		'E':	array(zip([0  , 100, 200, 300, 400, 500], 		[1209, 927, 701, 522, 380, 273])),
		'st':	array(zip([50 , 100, 150, 200, 250, 300], 		[0., 0.5, 0., -1.7, -4.8, -9.4])),
		'lt':	array(zip([100, 150, 200, 250, 300, 400, 500], 	[-.1, 1.3, 0., -2.6, -6.9, -21.2, -45.8]))
	}