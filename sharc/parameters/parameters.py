# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:35:52 2017

@author: edgar
"""

import configparser

from sharc.parameters.parameters_general import ParametersGeneral
from sharc.parameters.parameters_imt import ParametersImt
from sharc.parameters.parameters_hotspot import ParametersHotspot
from sharc.parameters.parameters_antenna_imt import ParametersAntennaImt
from sharc.parameters.parameters_fs import ParametersFs
from sharc.parameters.parameters_fss_ss import ParametersFssSs
from sharc.parameters.parameters_fss_es import ParametersFssEs
from sharc.parameters.parameters_ras import ParametersRas


class Parameters(object):
    """
    Reads parameters from input file.
    """

    def __init__(self):
        self.file_name = None

        self.general = ParametersGeneral()
        self.imt = ParametersImt()
        self.antenna_imt = ParametersAntennaImt()
        self.hotspot = ParametersHotspot()
        self.fs = ParametersFs()
        self.fss_ss = ParametersFssSs()
        self.fss_es = ParametersFssEs()
        self.ras = ParametersRas()


    def set_file_name(self, file_name: str):
        self.file_name = file_name


    def read_params(self):
        config = configparser.ConfigParser()
        config.read(self.file_name)

        #######################################################################
        # GENERAL
        #######################################################################
        self.general.num_snapshots   = config.getint("GENERAL", "num_snapshots")
        self.general.imt_link        = config.get("GENERAL", "imt_link")
        self.general.system          = config.get("GENERAL", "system")
        self.general.compatibility   = config.get("GENERAL", "compatibility")

        #######################################################################
        # IMT
        #######################################################################
        self.imt.topology                = config.get("IMT", "topology")
        self.imt.num_macrocell_sites     = config.getint("IMT", "num_macrocell_sites")
        self.imt.num_clusters            = config.getint("IMT", "num_clusters")
        self.imt.intersite_distance      = config.getfloat("IMT", "intersite_distance")
        self.imt.minimum_separation_distance_bs_ue = config.getfloat("IMT", "minimum_separation_distance_bs_ue")
        self.imt.interfered_with         = config.getboolean("IMT", "interfered_with")
        self.imt.frequency               = config.getfloat("IMT", "frequency")
        self.imt.bandwidth               = config.getfloat("IMT", "bandwidth")
        self.imt.rb_bandwidth            = config.getfloat("IMT", "rb_bandwidth")
        self.imt.guard_band_ratio        = config.getfloat("IMT", "guard_band_ratio")
        self.imt.bs_load_probability     = config.getfloat("IMT", "bs_load_probability")
        self.imt.bs_conducted_power      = config.getfloat("IMT", "bs_conducted_power")
        self.imt.bs_height               = config.getfloat("IMT", "bs_height")
        self.imt.bs_aclr                 = config.getfloat("IMT", "bs_aclr")
        self.imt.bs_acs                  = config.getfloat("IMT", "bs_acs")
        self.imt.bs_noise_figure         = config.getfloat("IMT", "bs_noise_figure")
        self.imt.bs_noise_temperature    = config.getfloat("IMT", "bs_noise_temperature")
        self.imt.bs_ohmic_loss           = config.getfloat("IMT", "bs_ohmic_loss")
        self.imt.ul_attenuation_factor   = config.getfloat("IMT", "ul_attenuation_factor")
        self.imt.ul_sinr_min             = config.getfloat("IMT", "ul_sinr_min")
        self.imt.ul_sinr_max             = config.getfloat("IMT", "ul_sinr_max")
        self.imt.ue_k                    = config.getint("IMT", "ue_k")
        self.imt.ue_k_m                  = config.getint("IMT", "ue_k_m")
        self.imt.ue_indoor_percent       = config.getfloat("IMT", "ue_indoor_percent")
        self.imt.ue_distribution_type    = config.get("IMT", "ue_distribution_type")
        self.imt.ue_distribution_distance = config.get("IMT", "ue_distribution_distance")
        self.imt.ue_distribution_azimuth = config.get("IMT", "ue_distribution_azimuth")
        self.imt.ue_tx_power_control     = config.get("IMT", "ue_tx_power_control")
        self.imt.ue_p_o_pusch            = config.getfloat("IMT", "ue_p_o_pusch")
        self.imt.ue_alfa                 = config.getfloat("IMT", "ue_alfa")
        self.imt.ue_p_cmax               = config.getfloat("IMT", "ue_p_cmax")
        self.imt.ue_conducted_power      = config.getfloat("IMT", "ue_conducted_power")
        self.imt.ue_height               = config.getfloat("IMT", "ue_height")
        self.imt.ue_aclr                 = config.getfloat("IMT", "ue_aclr")
        self.imt.ue_acs                  = config.getfloat("IMT", "ue_acs")
        self.imt.ue_noise_figure         = config.getfloat("IMT", "ue_noise_figure")
        self.imt.ue_feed_loss            = config.getfloat("IMT", "ue_feed_loss")
        self.imt.ue_body_loss            = config.getfloat("IMT", "ue_body_loss")
        self.imt.dl_attenuation_factor   = config.getfloat("IMT", "dl_attenuation_factor")
        self.imt.dl_sinr_min             = config.getfloat("IMT", "dl_sinr_min")
        self.imt.dl_sinr_max             = config.getfloat("IMT", "dl_sinr_max")
        self.imt.channel_model           = config.get("IMT", "channel_model")
        self.imt.line_of_sight_prob      = config.getfloat("IMT", "line_of_sight_prob")
        self.imt.shadowing               = config.getboolean("IMT", "shadowing")
        self.imt.noise_temperature       = config.getfloat("IMT", "noise_temperature")
        self.imt.BOLTZMANN_CONSTANT      = config.getfloat("IMT", "BOLTZMANN_CONSTANT")

        #######################################################################
        # IMT ANTENNA
        #######################################################################
        self.antenna_imt.bs_element_pattern          = config.get("IMT_ANTENNA", "bs_element_pattern")
        self.antenna_imt.ue_element_pattern          = config.get("IMT_ANTENNA", "ue_element_pattern")
        self.antenna_imt.bs_tx_element_max_g         = config.getfloat("IMT_ANTENNA", "bs_tx_element_max_g")
        self.antenna_imt.bs_tx_element_phi_deg_3db   = config.getfloat("IMT_ANTENNA", "bs_tx_element_phi_deg_3db")
        self.antenna_imt.bs_tx_element_theta_deg_3db = config.getfloat("IMT_ANTENNA", "bs_tx_element_theta_deg_3db")
        self.antenna_imt.bs_tx_element_am       = config.getfloat("IMT_ANTENNA", "bs_tx_element_am")
        self.antenna_imt.bs_tx_element_sla_v    = config.getfloat("IMT_ANTENNA", "bs_tx_element_sla_v")
        self.antenna_imt.bs_tx_n_rows           = config.getfloat("IMT_ANTENNA", "bs_tx_n_rows")
        self.antenna_imt.bs_tx_n_columns        = config.getfloat("IMT_ANTENNA", "bs_tx_n_columns")
        self.antenna_imt.bs_tx_element_horiz_spacing = config.getfloat("IMT_ANTENNA", "bs_tx_element_horiz_spacing")
        self.antenna_imt.bs_tx_element_vert_spacing = config.getfloat("IMT_ANTENNA", "bs_tx_element_vert_spacing")

        self.antenna_imt.bs_rx_element_max_g    = config.getfloat("IMT_ANTENNA", "bs_rx_element_max_g")
        self.antenna_imt.bs_rx_element_phi_deg_3db  = config.getfloat("IMT_ANTENNA", "bs_rx_element_phi_deg_3db")
        self.antenna_imt.bs_rx_element_theta_deg_3db = config.getfloat("IMT_ANTENNA", "bs_rx_element_theta_deg_3db")
        self.antenna_imt.bs_rx_element_am       = config.getfloat("IMT_ANTENNA", "bs_rx_element_am")
        self.antenna_imt.bs_rx_element_sla_v    = config.getfloat("IMT_ANTENNA", "bs_rx_element_sla_v")
        self.antenna_imt.bs_rx_n_rows           = config.getfloat("IMT_ANTENNA", "bs_rx_n_rows")
        self.antenna_imt.bs_rx_n_columns        = config.getfloat("IMT_ANTENNA", "bs_rx_n_columns")
        self.antenna_imt.bs_rx_element_horiz_spacing = config.getfloat("IMT_ANTENNA", "bs_rx_element_horiz_spacing")
        self.antenna_imt.bs_rx_element_vert_spacing = config.getfloat("IMT_ANTENNA", "bs_rx_element_vert_spacing")

        self.antenna_imt.ue_tx_element_max_g    = config.getfloat("IMT_ANTENNA", "ue_tx_element_max_g")
        self.antenna_imt.ue_tx_element_phi_deg_3db  = config.getfloat("IMT_ANTENNA", "ue_tx_element_phi_deg_3db")
        self.antenna_imt.ue_tx_element_theta_deg_3db = config.getfloat("IMT_ANTENNA", "ue_tx_element_theta_deg_3db")
        self.antenna_imt.ue_tx_element_am       = config.getfloat("IMT_ANTENNA", "ue_tx_element_am")
        self.antenna_imt.ue_tx_element_sla_v    = config.getfloat("IMT_ANTENNA", "ue_tx_element_sla_v")
        self.antenna_imt.ue_tx_n_rows           = config.getfloat("IMT_ANTENNA", "ue_tx_n_rows")
        self.antenna_imt.ue_tx_n_columns        = config.getfloat("IMT_ANTENNA", "ue_tx_n_columns")
        self.antenna_imt.ue_tx_element_horiz_spacing = config.getfloat("IMT_ANTENNA", "ue_tx_element_horiz_spacing")
        self.antenna_imt.ue_tx_element_vert_spacing = config.getfloat("IMT_ANTENNA", "ue_tx_element_vert_spacing")

        self.antenna_imt.ue_rx_element_max_g    = config.getfloat("IMT_ANTENNA", "ue_rx_element_max_g")
        self.antenna_imt.ue_rx_element_phi_deg_3db  = config.getfloat("IMT_ANTENNA", "ue_rx_element_phi_deg_3db")
        self.antenna_imt.ue_rx_element_theta_deg_3db = config.getfloat("IMT_ANTENNA", "ue_rx_element_theta_deg_3db")
        self.antenna_imt.ue_rx_element_am       = config.getfloat("IMT_ANTENNA", "ue_rx_element_am")
        self.antenna_imt.ue_rx_element_sla_v    = config.getfloat("IMT_ANTENNA", "ue_rx_element_sla_v")
        self.antenna_imt.ue_rx_n_rows           = config.getfloat("IMT_ANTENNA", "ue_rx_n_rows")
        self.antenna_imt.ue_rx_n_columns        = config.getfloat("IMT_ANTENNA", "ue_rx_n_columns")
        self.antenna_imt.ue_rx_element_horiz_spacing = config.getfloat("IMT_ANTENNA", "ue_rx_element_horiz_spacing")
        self.antenna_imt.ue_rx_element_vert_spacing = config.getfloat("IMT_ANTENNA", "ue_rx_element_vert_spacing")

        self.antenna_imt.bs_downtilt_deg = config.getfloat("IMT_ANTENNA", "bs_downtilt_deg")

        #######################################################################
        # HOTSPOT
        #######################################################################
        self.hotspot.num_hotspots_per_cell = config.getint("HOTSPOT", "num_hotspots_per_cell")
        self.hotspot.max_dist_hotspot_ue   = config.getfloat("HOTSPOT", "max_dist_hotspot_ue")
        self.hotspot.min_dist_bs_hotspot   = config.getfloat("HOTSPOT", "min_dist_bs_hotspot")
        self.hotspot.min_dist_hotspots     = config.getfloat("HOTSPOT", "min_dist_hotspots")

        #######################################################################
        # FSS space station
        #######################################################################
        self.fss_ss.frequency               = config.getfloat("FSS_SS", "frequency")
        self.fss_ss.bandwidth               = config.getfloat("FSS_SS", "bandwidth")
        self.fss_ss.tx_power_density        = config.getfloat("FSS_ES", "tx_power_density")
        self.fss_ss.altitude                = config.getfloat("FSS_SS", "altitude")
        self.fss_ss.lat_deg                 = config.getfloat("FSS_SS", "lat_deg")
        self.fss_ss.elevation               = config.getfloat("FSS_SS", "elevation")
        self.fss_ss.azimuth                 = config.getfloat("FSS_SS", "azimuth")
        self.fss_ss.noise_temperature       = config.getfloat("FSS_SS", "noise_temperature")
        self.fss_ss.inr_scaling             = config.getfloat("FSS_SS", "inr_scaling")
        self.fss_ss.antenna_gain            = config.getfloat("FSS_SS", "antenna_gain")
        self.fss_ss.antenna_pattern         = config.get("FSS_SS", "antenna_pattern")
        self.fss_ss.imt_altitude            = config.getfloat("FSS_SS", "imt_altitude")
        self.fss_ss.imt_lat_deg             = config.getfloat("FSS_SS", "imt_lat_deg")
        self.fss_ss.imt_long_diff_deg       = config.getfloat("FSS_SS", "imt_long_diff_deg")
        self.fss_ss.season                  = config.get("FSS_SS", "season")
        self.fss_ss.channel_model           = config.get("FSS_SS", "channel_model")
        self.fss_ss.antenna_l_s             = config.getfloat("FSS_SS", "antenna_l_s")
        self.fss_ss.antenna_3_dB            = config.getfloat("FSS_SS", "antenna_3_dB")
        self.fss_ss.BOLTZMANN_CONSTANT      = config.getfloat("FSS_SS", "BOLTZMANN_CONSTANT")
        self.fss_ss.EARTH_RADIUS            = config.getfloat("FSS_SS", "EARTH_RADIUS")

        #######################################################################
        # FSS earth station
        #######################################################################
        self.fss_es.location = config.get("FSS_ES", "location")
        self.fss_es.x = config.getfloat("FSS_ES", "x")
        self.fss_es.y = config.getfloat("FSS_ES", "y")
        self.fss_es.height = config.getfloat("FSS_ES", "height")
        self.fss_es.elevation = config.getfloat("FSS_ES", "elevation")
        self.fss_es.azimuth = config.getfloat("FSS_ES", "azimuth")
        self.fss_es.frequency = config.getfloat("FSS_ES", "frequency")
        self.fss_es.bandwidth = config.getfloat("FSS_ES", "bandwidth")
        self.fss_es.tx_power_density = config.getfloat("FSS_ES", "tx_power_density")
        self.fss_es.noise_temperature = config.getfloat("FSS_ES", "noise_temperature")
        self.fss_es.inr_scaling = config.getfloat("FSS_ES", "inr_scaling")
        self.fss_es.antenna_gain = config.getfloat("FSS_ES", "antenna_gain")
        self.fss_es.antenna_pattern = config.get("FSS_ES", "antenna_pattern")
        self.fss_es.diameter = config.getfloat("FSS_ES", "diameter")
        self.fss_es.channel_model = config.get("FSS_ES", "channel_model")
        self.fss_es.line_of_sight_prob = config.getfloat("FSS_ES", "line_of_sight_prob")
        self.fss_es.BOLTZMANN_CONSTANT = config.getfloat("FSS_ES", "BOLTZMANN_CONSTANT")
        self.fss_es.EARTH_RADIUS = config.getfloat("FSS_ES", "EARTH_RADIUS")

        # P452 parameters
        self.fss_es.atmospheric_pressure = config.getfloat("FSS_ES", "atmospheric_pressure")
        self.fss_es.air_temperature = config.getfloat("FSS_ES", "air_temperature")
        self.fss_es.water_vapour = config.getfloat("FSS_ES", "water_vapour")
        self.fss_es.theta_tx = config.getfloat("FSS_ES", "theta_tx")
        self.fss_es.theta_rx = config.getfloat("FSS_ES", "theta_rx")
        self.fss_es.N0 = config.getfloat("FSS_ES", "N0")
        self.fss_es.delta_N = config.getfloat("FSS_ES", "delta_N")
        self.fss_es.percentage_p = config.getfloat("FSS_ES", "percentage_p")
        self.fss_es.Dlt = config.getfloat("FSS_ES", "Dlt")
        self.fss_es.Dlr = config.getfloat("FSS_ES", "Dlr")
        self.fss_es.Dct = config.getfloat("FSS_ES", "Dct")
        self.fss_es.Dcr = config.getfloat("FSS_ES", "Dcr")
        self.fss_es.Hts = config.getfloat("FSS_ES", "Hts")
        self.fss_es.Hrs = config.getfloat("FSS_ES", "Hrs")
        self.fss_es.Hst = config.getfloat("FSS_ES", "Hst")
        self.fss_es.Hsr = config.getfloat("FSS_ES", "Hsr")
        self.fss_es.H0 = config.getfloat("FSS_ES", "H0")
        self.fss_es.Hn = config.getfloat("FSS_ES", "Hn")
        self.fss_es.Hte = config.getfloat("FSS_ES", "Hte")
        self.fss_es.Hre = config.getfloat("FSS_ES", "Hre")
        self.fss_es.omega = config.getfloat("FSS_ES", "omega")
        self.fss_es.phi = config.getfloat("FSS_ES", "phi")
        self.fss_es.dtm = config.getfloat("FSS_ES", "dtm")
        self.fss_es.dlm = config.getfloat("FSS_ES", "dlm")
        self.fss_es.epsilon = config.getfloat("FSS_ES", "epsilon")
        self.fss_es.hm = config.getfloat("FSS_ES", "hm")
        self.fss_es.elevation_angle_facade = config.getfloat("FSS_ES", "elevation_angle_facade")
        self.fss_es.probability_loss_notExceeded = config.getfloat("FSS_ES", "probability_loss_notExceeded")
        self.fss_es.thetaJ = config.getfloat("FSS_ES", "thetaJ")
        self.fss_es.par_ep = config.getfloat("FSS_ES", "par_ep")
        self.fss_es.Beta_0 = config.getfloat("FSS_ES", "Beta_0")
        self.fss_es.clutter_loss = config.getboolean("FSS_ES", "clutter_loss")

        #######################################################################
        # Fixed wireless service
        #######################################################################
        self.fs.x                       = config.getfloat("FS", "x")
        self.fs.y                       = config.getfloat("FS", "y")
        self.fs.height                  = config.getfloat("FS", "height")
        self.fs.elevation               = config.getfloat("FS", "elevation")
        self.fs.azimuth                 = config.getfloat("FS", "azimuth")
        self.fs.frequency               = config.getfloat("FS", "frequency")
        self.fs.bandwidth               = config.getfloat("FS", "bandwidth")
        self.fs.noise_temperature       = config.getfloat("FS", "noise_temperature")
        self.fs.tx_power_density        = config.getfloat("FS", "tx_power_density")
        self.fs.inr_scaling             = config.getfloat("FS", "inr_scaling")
        self.fs.antenna_gain            = config.getfloat("FS", "antenna_gain")
        self.fs.antenna_pattern         = config.get("FS", "antenna_pattern")
        self.fs.diameter                = config.getfloat("FS", "diameter")
        self.fs.channel_model           = config.get("FS", "channel_model")
        self.fs.line_of_sight_prob      = config.getfloat("FS", "line_of_sight_prob")
        self.fs.BOLTZMANN_CONSTANT      = config.getfloat("FS", "BOLTZMANN_CONSTANT")
        self.fs.EARTH_RADIUS            = config.getfloat("FS", "EARTH_RADIUS")
        
        #######################################################################
        # RAS station
        #######################################################################
        self.ras.x                          = config.getfloat("RAS", "x")
        self.ras.y                          = config.getfloat("RAS", "y")
        self.ras.height                     = config.getfloat("RAS", "height")
        self.ras.elevation                  = config.getfloat("RAS", "elevation")
        self.ras.azimuth                    = config.getfloat("RAS", "azimuth")
        self.ras.frequency                  = config.getfloat("RAS", "frequency")
        self.ras.bandwidth                  = config.getfloat("RAS", "bandwidth")
        self.ras.antenna_noise_temperature  = config.getfloat("RAS", "antenna_noise_temperature")
        self.ras.receiver_noise_temperature = config.getfloat("RAS", "receiver_noise_temperature")
        self.ras.inr_scaling                = config.getfloat("RAS", "inr_scaling")
        self.ras.antenna_efficiency         = config.getfloat("RAS", "antenna_efficiency")
        self.ras.antenna_gain               = config.getfloat("RAS", "antenna_gain")
        self.ras.antenna_pattern            = config.get("RAS", "antenna_pattern")
        self.ras.diameter                   = config.getfloat("RAS", "diameter")
        self.ras.channel_model              = config.get("RAS", "channel_model")
        self.ras.line_of_sight_prob         = config.getfloat("RAS", "line_of_sight_prob")
        self.ras.BOLTZMANN_CONSTANT         = config.getfloat("RAS", "BOLTZMANN_CONSTANT")
        self.ras.EARTH_RADIUS               = config.getfloat("RAS", "EARTH_RADIUS")
        self.ras.SPEED_OF_LIGHT             = config.getfloat("RAS", "SPEED_OF_LIGHT")
        
        # P452 parameters
        self.ras.atmospheric_pressure = config.getfloat("RAS", "atmospheric_pressure")
        self.ras.air_temperature = config.getfloat("RAS", "air_temperature")
        self.ras.water_vapour = config.getfloat("RAS", "water_vapour")
        self.ras.theta_tx = config.getfloat("RAS", "theta_tx")
        self.ras.theta_rx = config.getfloat("RAS", "theta_rx")
        self.ras.N0 = config.getfloat("RAS", "N0")
        self.ras.delta_N = config.getfloat("RAS", "delta_N")
        self.ras.percentage_p = config.getfloat("RAS", "percentage_p")
        self.ras.Dlt = config.getfloat("RAS", "Dlt")
        self.ras.Dlr = config.getfloat("RAS", "Dlr")
        self.ras.Dct = config.getfloat("RAS", "Dct")
        self.ras.Dcr = config.getfloat("RAS", "Dcr")
        self.ras.Hts = config.getfloat("RAS", "Hts")
        self.ras.Hrs = config.getfloat("RAS", "Hrs")
        self.ras.Hst = config.getfloat("RAS", "Hst")
        self.ras.Hsr = config.getfloat("RAS", "Hsr")
        self.ras.H0 = config.getfloat("RAS", "H0")
        self.ras.Hn = config.getfloat("RAS", "Hn")
        self.ras.Hte = config.getfloat("RAS", "Hte")
        self.ras.Hre = config.getfloat("RAS", "Hre")
        self.ras.omega = config.getfloat("RAS", "omega")
        self.ras.phi = config.getfloat("RAS", "phi")
        self.ras.dtm = config.getfloat("RAS", "dtm")
        self.ras.dlm = config.getfloat("RAS", "dlm")
        self.ras.epsilon = config.getfloat("RAS", "epsilon")
        self.ras.hm = config.getfloat("RAS", "hm")
        self.ras.elevation_angle_facade = config.getfloat("RAS", "elevation_angle_facade")
        self.ras.probability_loss_notExceeded = config.getfloat("RAS", "probability_loss_notExceeded")
        self.ras.thetaJ = config.getfloat("RAS", "thetaJ")
        self.ras.par_ep = config.getfloat("RAS", "par_ep")
        self.ras.Beta_0 = config.getfloat("RAS", "Beta_0")
        self.ras.clutter_loss = config.getboolean("RAS", "clutter_loss")

