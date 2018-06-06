---
Description: Gets the flags that were used when a Microsoft DirectX Graphics Infrastructure (DXGI) object was created.
ms.assetid: 1B4A5DC9-6853-4047-B64D-BD251352AC89
title: IDXGIFactory3::GetCreationFlags method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

The **GetCreationFlags** method returns flags that were passed to the [**CreateDXGIFactory2**](/windows/desktop/api/dxgi1_3/nf-dxgi1_3-createdxgifactory2) function, or were implicitly constructed by [**CreateDXGIFactory**](/windows/desktop/api/DXGI/nf-dxgi-createdxgifactory), [**CreateDXGIFactory1**](/windows/desktop/api/DXGI/nf-dxgi-createdxgifactory1), [**D3D11CreateDevice**](https://msdn.microsoft.com/d1c85ec0-84a8-41ff-9cbe-f47bbaa5863b), or [**D3D11CreateDeviceAndSwapChain**](https://msdn.microsoft.com/84d73e8c-f13c-4343-91de-57f9f8a0ad96).

## See also

<dl> <dt>

[**IDXGIFactory3**](/windows/desktop/api/DXGI1_3/nn-dxgi1_3-idxgifactory3)
</dt> </dl>

 

 



