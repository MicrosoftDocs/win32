---
Description: 'Gets the flags that were used when a Microsoft DirectX Graphics Infrastructure (DXGI) object was created.'
ms.assetid: '1B4A5DC9-6853-4047-B64D-BD251352AC89'
title: 'IDXGIFactory3::GetCreationFlags method'
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

The **GetCreationFlags** method returns flags that were passed to the [**CreateDXGIFactory2**](createdxgifactory2.md) function, or were implicitly constructed by [**CreateDXGIFactory**](createdxgifactory.md), [**CreateDXGIFactory1**](createdxgifactory1.md), [**D3D11CreateDevice**](direct3d11.d3d11createdevice), or [**D3D11CreateDeviceAndSwapChain**](direct3d11.d3d11createdeviceandswapchain).

## See also

<dl> <dt>

[**IDXGIFactory3**](idxgifactory3.md)
</dt> </dl>

 

 



