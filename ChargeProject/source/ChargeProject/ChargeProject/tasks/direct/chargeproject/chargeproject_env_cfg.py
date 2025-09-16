# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from isaaclab_assets.robots.anymal import ANYMAL_C_CFG  # isort: skip
from isaaclab_assets.robots.spot import SPOT_CFG
from isaaclab_assets.robots.unitree import UNITREE_GO2_CFG

from isaaclab.assets import ArticulationCfg
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sensors import ContactSensorCfg
from isaaclab.sim import SimulationCfg
from isaaclab.utils import configclass


@configclass
class ChargeprojectEnvCfg(DirectRLEnvCfg):
    # env
    decimation = 4
    episode_length_s = 35.0
    # - spaces definition
    action_scale = 0.5
    action_space = 12
    observation_space = 51 
    state_space = 0
    # simulation
    sim: SimulationCfg = SimulationCfg(dt=1 / 120, render_interval=decimation)
    # robot(s)
    #robot: ArticulationCfg = UNITREE_GO2_CFG.replace(prim_path="/World/envs/env_.*/Robot")
    robot: ArticulationCfg = ANYMAL_C_CFG.replace(prim_path="/World/envs/env_.*/Robot")
    
    # Unitree Go2
    #base_name = "base"
    #foot_names = ".*_foot"
    #undesired_contact_body_names = ".*_thigh"

    # Spot
    #base_name = "body"
    #foot_names = ".*_foot"
    #undesired_contact_body_names = ".*_uleg"

    # Anymal
    base_name = "base"
    foot_names = ".*FOOT"
    undesired_contact_body_names = ".*THIGH"

    contact_sensor: ContactSensorCfg = ContactSensorCfg(
        prim_path="/World/envs/env_.*/Robot/.*", history_length=3, update_period=0.005, track_air_time=True
    )
    # scene
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=1024, env_spacing=4.0, replicate_physics=True)


    point_max_distance = 6.0
    point_min_distance = 4.0
    success_tolerance = 0.25  # meters
    time_out_per_target = 12.0  # seconds

    marker_colors = 50
    
    # reward scales
    #lin_vel_reward_scale = 3.0
    #yaw_rate_reward_scale = 0.5
    
    progress_reward_scale = 6.0
    velocity_alignment_reward_scale = 6.0
    reach_target_reward = 2500.0
    z_vel_reward_scale = -2.0
    z_vel_reward_scale = -2.0
    ang_vel_reward_scale = -0.05
    joint_torque_reward_scale = -2.5e-5
    joint_accel_reward_scale = -2.5e-7
    action_rate_reward_scale = -0.01
    feet_air_time_reward_scale = 0.5
    undesired_contact_reward_scale = 0 # -1.0
    flat_orientation_reward_scale = -4.0 #-5.0

