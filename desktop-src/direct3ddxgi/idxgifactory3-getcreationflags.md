---
Description: Gets the flags that were used when a Microsoft DirectX Graphics Infrastructure (DXGI) object was created.
ms.assetid: 1B4A5DC9-6853-4047-B64D-BD251352AC89
title: IDXGIFactory3GetCreationFlags method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

The **GetCreationFlags** method returns flags that were passed to the [**CreateDXGIFactory2**](/windows/win32/dxgi1_3/nf-dxgi1_3-createdxgifactory2?branch=master) function, or were implicitly constructed by [**CreateDXGIFactory**](/windows/win32/DXGI/nf-dxgi-createdxgifactory?branch=master), [**CreateDXGIFactory1**](/windows/win32/DXGI/nf-dxgi-createdxgifactory1?branch=master), [**D3D11CreateDevice**](direct3d11.d3d11createdevice), or [**D3D11CreateDeviceAndSwapChain**](direct3d11.d3d11createdeviceandswapchain).

## See also

<dl> <dt>

[**IDXGIFactory3**](/windows/win32/DXGI1_3/nn-dxgi1_3-idxgifactory3?branch=master)
</dt> </dl>

 

 



