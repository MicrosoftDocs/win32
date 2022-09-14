---
title: Preventing Unwanted NULL Pixel Shader SRVs
description: This topic discusses how to work around the driver receiving NULL shader-resource views (SRVs) even when non-NULL SRVs are bound to the pixel shader stage.
ms.assetid: c832c199-59b8-4079-a159-45490a2f6a94
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Unwanted NULL Pixel Shader SRVs

Direct3D 11 applications that run on Direct3D 9 graphics hardware could inadvertently cause the driver to receive **NULL** shader-resource views (SRVs) even when the applications bind non-**NULL** SRVs to the pixel shader stage. This situation can occur only if the applications destroy SRVs while they execute. This topic discusses how to work around the driver receiving **NULL** shader-resource views (SRVs) even when non-**NULL** SRVs are bound to the pixel shader stage.

To prevent the driver from receiving unwanted **NULL** SRVs, the applications must call [**ID3D11DeviceContext::PSSetShaderResources**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-pssetshaderresources) to unset all SRVs before each call to [**ID3D11DeviceContext::PSSetShader**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-pssetshader). However, if the applications do not destroy SRVs until the end of their code execution, they do not need to unset the SRVs.

The [10Level9 Reference](d3d11-graphics-reference-10level9.md) section lists the differences between how various [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) methods behave at various 10Level9 feature levels.

## Related topics

<dl> <dt>

[Direct3D 11 on Downlevel Hardware](overviews-direct3d-11-devices-downlevel.md)
</dt> </dl>

 

 




