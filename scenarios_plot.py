
from plot import *


names_basic = ['1000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_1000_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_',
               '1000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_',
               '1000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_1_',
               '1000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_2_',
               '1000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_']
names_2000d = ['2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_1000_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_',
               '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_',
               '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_1_',
               '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_2_',
               '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_']

names_tb_k3 = [#'2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_0__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_0.2__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_0.4__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_0.6__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_0.8__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1__v1']

names_tb_k0 = [#'2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_0__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_0.2__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_0.4__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_0.6__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_0.8__v1',
             '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_1__v1']

names_q = ['2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1_0.5_0__v1',
           '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1_0.5_500__v1',
           '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1_0.5_1000__v1',
           '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1_0.5_2000__v1',
           '2000_16_16_16_16_16_16_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1_0.5_4000__v1']

names_Erl1 = ['1000_1_1_1_1_1_1_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_1000_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_1_0.5_10000__v1',
              '1000_1_1_1_1_1_1_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_0_1_0.5_10000__v1',
              '1000_1_1_1_1_1_1_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_1_1_0.5_10000__v1',
              '1000_1_1_1_1_1_1_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_2_1_0.5_10000__v1',
              '1000_1_1_1_1_1_1_10000_7_5.5_5_1.5_9_0.7_0.5_0.3_2_0.6_0.9_0.8_1_1_250_0.5_0.5_[0.5, 0.5, 0.3, 0.1]_[0.3, 0.1, 0.1, 0.1]_3_1_0.5_10000__v1']


#plotEbola(names= names_basic, savename='basic', type = 'mix')
#plotEbola(names= names_2000d, savename='2000d', type = 'mix')
#plotEbola(names= names_tb_k3, savename='tb_k3', type = 'all', lab = ['0.2', '0.4', '0.6', '0.8', '1.0'])
#plotEbola(names= names_tb_k0, savename='tb_k0', type = 'all', lab = ['0.2', '0.4', '0.6', '0.8', '1.0'])
#plotEbola(names= names_q, savename='q', type = 'all', lab = ['0', '500', '1000', '2000', '4000'])
plotEbola(names= names_Erl1, savename='Erl1', type = 'all', lab = ['0.0', '0.2', '0.4', '0.6', '0.8'], Nerls=[1,1,1,1,1])



