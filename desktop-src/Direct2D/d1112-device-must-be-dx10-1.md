---
title: D1112 Device Must Be DX11
ms.assetid: 39dcccaf-db56-402d-b62f-704ad4daf151
description: 
keywords:
- D1112 Device Must Be DX11 Direct2D
topic_type:
- apiref
api_name:
- D1112 Device Must Be DX11
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D1112: Device Must Be DX11

The device associated with the DXGI surface must be a D3D11 device.



|             |         |
|-------------|---------|
| Error Level | Warning |



 

## Possible Causes

There was an attempt to use the [**CreateDxgiSurfaceRenderTarget**](/windows/desktop/api/d2d1/nf-d2d1-createdxgisurfacerendertarget) with a DXGI surface created by a non-Direct3D11 device.

 

 




