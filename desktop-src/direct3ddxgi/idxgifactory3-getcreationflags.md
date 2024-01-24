---
description: Gets the flags that were used when a Microsoft DirectX Graphics Infrastructure (DXGI) object was created.
ms.assetid: 1B4A5DC9-6853-4047-B64D-BD251352AC89
title: IDXGIFactory3::GetCreationFlags method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDXGIFactory3.GetCreationFlags
api_type: 
- COM
api_location: 
- dxgi1_3.h
---

# IDXGIFactory3::GetCreationFlags method

Gets the flags that were used when a Microsoft DirectX Graphics Infrastructure (DXGI) object was created.

## Syntax


```C++
UINT GetCreationFlags();
```



## Parameters

This method has no parameters.

## Return value

The creation flags.

## Remarks

The **GetCreationFlags** method returns flags that were passed to the [**CreateDXGIFactory2**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-createdxgifactory2) function, or were implicitly constructed by [**CreateDXGIFactory**](/windows/desktop/api/DXGI/nf-dxgi-createdxgifactory), [**CreateDXGIFactory1**](/windows/desktop/api/DXGI/nf-dxgi-createdxgifactory1), [**D3D11CreateDevice**](/windows/win32/api/d3d11/nf-d3d11-d3d11createdevice), or [**D3D11CreateDeviceAndSwapChain**](/windows/win32/api/d3d11/nf-d3d11-d3d11createdeviceandswapchain).

## See also

<dl> <dt>

[**IDXGIFactory3**](/windows/desktop/api/DXGI1_3/nn-dxgi1_3-idxgifactory3)
</dt> </dl>

 

 
