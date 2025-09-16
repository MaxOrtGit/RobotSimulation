# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##


gym.register(
    id="Chargeproject-Direct-v0",
    #entry_point=f"{__name__}.old_chargeproject_env:OldChargeprojectEnv",
    entry_point=f"{__name__}.chargeproject_env:ChargeprojectEnv",
    disable_env_checker=True,
    kwargs={
        #"env_cfg_entry_point": f"{__name__}.old_chargeproject_env_cfg:OldChargeprojectEnvCfg",
        "env_cfg_entry_point": f"{__name__}.chargeproject_env_cfg:ChargeprojectEnvCfg",
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:PPORunnerCfg",
        "skrl_amp_cfg_entry_point": f"{agents.__name__}:skrl_amp_cfg.yaml",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_ppo_cfg.yaml",
        "sb3_cfg_entry_point": f"{agents.__name__}:sb3_ppo_cfg.yaml",
    },
)