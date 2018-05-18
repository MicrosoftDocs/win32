---
Description: 'Create the best Direct3D device and a swap chain.'
ms.assetid: 'c320a6c4-fa68-47fc-b2cb-0dc53c2767e7'
title: D3DX10CreateDeviceAndSwapChain function
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

Type: **[**IDXGIAdapter**](direct3ddxgi.idxgiadapter)\***

Pointer to a [**IDXGIAdapter**](direct3ddxgi.idxgiadapter).

</dd> <dt>

*DriverType* \[in\]
</dt> <dd>

Type: **[**D3D10\_DRIVER\_TYPE**](d3d10-driver-type.md)**

The type of driver for the device. See [**D3D10\_DRIVER\_TYPE**](d3d10-driver-type.md).

</dd> <dt>

*Software* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

A handle to the DLL that implements a software rasterizer. Must be **NULL** if DriverType is non-software. The HMODULE of a DLL can be obtained with [LoadLibrary](http://msdn2.microsoft.com/en-us/library/ms684175.aspx), [LoadLibraryEx](http://msdn2.microsoft.com/en-us/library/ms684179.aspx), or [GetModuleHandle](http://msdn.microsoft.com/en-us/library/ms683199.aspx).

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Optional. Device creation flags (see [**D3D10\_CREATE\_DEVICE\_FLAG**](d3d10-create-device-flag.md)) that enable [API layers](d3d10-graphics-programming-guide-api-features-layers.md). These flags can be bitwise OR'd together.

</dd> <dt>

*pSwapChainDesc* \[in\]
</dt> <dd>

Type: **[**DXGI\_SWAP\_CHAIN\_DESC**](direct3ddxgi.dxgi_swap_chain_desc)\***

Description of the swap chain. See [**DXGI\_SWAP\_CHAIN\_DESC**](direct3ddxgi.dxgi_swap_chain_desc).

</dd> <dt>

*ppSwapChain* \[out\]
</dt> <dd>

Type: **[**IDXGISwapChain**](direct3ddxgi.idxgiswapchain)\*\***

Address of a pointer to an [**IDXGISwapChain**](direct3ddxgi.idxgiswapchain).

</dd> <dt>

*ppDevice* \[out\]
</dt> <dd>

Type: **[**ID3D10Device**](id3d10device.md)\*\***

Address of a pointer to an [**ID3D10Device Interface**](id3d10device.md) that will receive the newly created device.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

This method returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

To create the best device, this method implements more than one device creation option. First, the method attempts to create a 10.1 device (and swap chain). If that fails, the method attempts to create a 10.0 device. If that fails, the method will fail. If your application needs to create only a 10.1 device, or a 10.0 device only, use these APIs instead:

-   Use [**D3D10CreateDeviceAndSwapChain**](d3d10createdeviceandswapchain.md) to create a Direct3D 10.0 (only) device and swap chain.
-   Use [**D3D10CreateDeviceAndSwapChain1**](d3d10createdeviceandswapchain1.md) to create a Direct3D 10.1 (only) device and swap chain.

This method requires Windows Vista Service Pack 1.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Core.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




