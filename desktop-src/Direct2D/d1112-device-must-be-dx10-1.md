---
title: D1112 Device Must Be DX11
ms.assetid: '39dcccaf-db56-402d-b62f-704ad4daf151'
description: 
keywords: ["D1112 Device Must Be DX11 Direct2D"]
topic_type:
- apiref
api_name:
- D1112 Device Must Be DX11
api_type:
- NA
---

# D1112: Device Must Be DX11

The device associated with the DXGI surface must be a D3D11 device.



|             |         |
|-------------|---------|
| Error Level | Warning |



 

## Possible Causes

There was an attempt to use the [**CreateDxgiSurfaceRenderTarget**](id2d1factory-createdxgisurfacerendertarget.md) with a DXGI surface created by a non-Direct3D11 device.

 

 




