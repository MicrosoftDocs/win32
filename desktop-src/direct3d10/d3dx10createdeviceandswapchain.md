---
Description: Create the best Direct3D device and a swap chain.
ms.assetid: c320a6c4-fa68-47fc-b2cb-0dc53c2767e7
title: D3DX10CreateDeviceAndSwapChain function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DX10CreateDeviceAndSwapChain function

Create the best Direct3D device and a swap chain.

## Syntax


```C++
HRESULT D3DX10CreateDeviceAndSwapChain(
  _In_  IDXGIAdapter         *pAdapter,
  _In_  D3D10_DRIVER_TYPE    DriverType,
  _In_  HMODULE              Software,
  _In_  UINT                 Flags,
  _In_  DXGI_SWAP_CHAIN_DESC *pSwapChainDesc,
  _Out_ IDXGISwapChain       **ppSwapChain,
  _Out_ ID3D10Device         **ppDevice
);
```



## Parameters

<dl> <dt>

*pAdapter* \[in\]
</dt> <dd>

Type: **[**IDXGIAdapter**](https://msdn.microsoft.com/VS|directx_sdk|~\idxgiadapter.htm)\***

Pointer to a [**IDXGIAdapter**](https://msdn.microsoft.com/VS|directx_sdk|~\idxgiadapter.htm).

</dd> <dt>

*DriverType* \[in\]
</dt> <dd>

Type: **[**D3D10\_DRIVER\_TYPE**](/windows/desktop/api/D3D10misc/ne-d3d10misc-d3d10_driver_type)**

The type of driver for the device. See [**D3D10\_DRIVER\_TYPE**](/windows/desktop/api/D3D10misc/ne-d3d10misc-d3d10_driver_type).

</dd> <dt>

*Software* \[in\]
</dt> <dd>

Type: **[**HMODULE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

A handle to the DLL that implements a software rasterizer. Must be **NULL** if DriverType is non-software. The HMODULE of a DLL can be obtained with [LoadLibrary](http://msdn2.microsoft.com/en-us/library/ms684175.aspx), [LoadLibraryEx](http://msdn2.microsoft.com/en-us/library/ms684179.aspx), or [GetModuleHandle](http://msdn.microsoft.com/en-us/library/ms683199.aspx).

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Optional. Device creation flags (see [**D3D10\_CREATE\_DEVICE\_FLAG**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_create_device_flag)) that enable [API layers](d3d10-graphics-programming-guide-api-features-layers.md). These flags can be bitwise OR'd together.

</dd> <dt>

*pSwapChainDesc* \[in\]
</dt> <dd>

Type: **[**DXGI\_SWAP\_CHAIN\_DESC**](https://msdn.microsoft.com/VS|directx_sdk|~\dxgi_swap_chain_desc.htm)\***

Description of the swap chain. See [**DXGI\_SWAP\_CHAIN\_DESC**](https://msdn.microsoft.com/VS|directx_sdk|~\dxgi_swap_chain_desc.htm).

</dd> <dt>

*ppSwapChain* \[out\]
</dt> <dd>

Type: **[**IDXGISwapChain**](https://msdn.microsoft.com/VS|directx_sdk|~\idxgiswapchain.htm)\*\***

Address of a pointer to an [**IDXGISwapChain**](https://msdn.microsoft.com/VS|directx_sdk|~\idxgiswapchain.htm).

</dd> <dt>

*ppDevice* \[out\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\*\***

Address of a pointer to an [**ID3D10Device Interface**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device) that will receive the newly created device.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

This method returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

To create the best device, this method implements more than one device creation option. First, the method attempts to create a 10.1 device (and swap chain). If that fails, the method attempts to create a 10.0 device. If that fails, the method will fail. If your application needs to create only a 10.1 device, or a 10.0 device only, use these APIs instead:

-   Use [**D3D10CreateDeviceAndSwapChain**](/windows/desktop/api/D3D10Misc/nf-d3d10misc-d3d10createdeviceandswapchain) to create a Direct3D 10.0 (only) device and swap chain.
-   Use [**D3D10CreateDeviceAndSwapChain1**](/windows/desktop/api/D3D10_1/nf-d3d10_1-d3d10createdeviceandswapchain1) to create a Direct3D 10.1 (only) device and swap chain.

This method requires Windows Vista Service Pack 1.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Core.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




