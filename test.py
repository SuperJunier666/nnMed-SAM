import os
import torch
from nnunetv2.utilities.unet import SAMConvUNet
from torch import nn

device = 'cuda'

model = SAMConvUNet(1,
                    6,
                    (32, 64, 125, 256, 320, 320),
                    nn.Conv3d,
                    3,
                    (1, 2, 2, 2, 2, 2),
                    (2, 2, 2, 2, 2, 2),
                    1,
                    (2, 2, 2, 2, 2),
                    True,
                    nn.BatchNorm3d,
                    {'eps': 1e-5, 'affine': True},
                    None,
                    None,
                    nn.LeakyReLU,
                    {'inplace': True},
                    False
                    ).to(device)
data = torch.rand((1, 1, 128, 128, 128), dtype=torch.float32).to(device)
res = model(data)
print(res.shape)
# for r in res:
#     print(r.shape)
