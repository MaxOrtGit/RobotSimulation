#!/bin/bash

# Run the training workflow with specific arguments for headless video capture
./isaaclab.sh -p source/ChargeProject/workflows/train.py -- \
  --task "Chargeproject-Direct-v0" \
  --headless \
  --video \
  --video_interval 500 \
  --video_length 500