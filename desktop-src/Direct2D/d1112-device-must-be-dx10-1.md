---
title: D1112 Device Must Be DX11
ms.assetid: 39dcccaf-db56-402d-b62f-704ad4daf151
description: The device associated with the DXGI surface must be a D3D11 device.
keywords:
- D1112 Device Must Be DX11 Direct2D
topic_type:
- apiref
api_name:
- D1112 Device Must Be DX11
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1112: Device Must Be DX11

The device associated with the DXGI surface must be a D3D11 device.



| &nbsp;      |  &nbsp; |
|-------------|---------|
| Error Level | Warning |



 

## Possible Causes

There was an attempt to use the [**CreateDxgiSurfaceRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdxgisurfacerendertarget(idxgisurface_constd2d1_render_target_properties__id2d1rendertarget)) with a DXGI surface created by a non-Direct3D11 device.

 

 




