---
description: Get a Direct3D 10.1 device interface pointer from a Direct3D 10.0 interface pointer.
ms.assetid: cf31a67f-0493-4e79-8e73-0297ab93bbae
title: D3DX10GetFeatureLevel1 function (D3DX10Core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10GetFeatureLevel1
api_type: 
- HeaderDef
api_location: 
- D3DX10Core.h
---

# D3DX10GetFeatureLevel1 function

Get a Direct3D 10.1 device interface pointer from a Direct3D 10.0 interface pointer.

## Syntax


```C++
HRESULT D3DX10GetFeatureLevel1(
  _In_  ID3D10Device  *pDevice,
  _Out_ ID3D10Device1 **ppDevice
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\***

Pointer to the Direct3D 10.0 device (see the [**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device) interface).

</dd> <dt>

*ppDevice* \[out\]
</dt> <dd>

Type: **[**ID3D10Device1**](/windows/desktop/api/D3D10_1/nn-d3d10_1-id3d10device1)\*\***

Pointer to the Direct3D 10.1 device (see the [**ID3D10Device1**](/windows/desktop/api/D3D10_1/nn-d3d10_1-id3d10device1) interface).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

This function returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md). If a Direct3D 10.1 device interface can be acquired, this function succeeds and passes a pointer to the 10.1 interface using the *ppDevice* parameter. If a Direct3D 10.1 device interface cannot be acquired, this function returns E\_FAIL, and will not return anything for the *ppDevice* parameter.

## Remarks

For this function to succeed, you must have acquired the supplied [**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device) pointer using a call to the [**D3DX10CreateDevice**](d3dx10createdevice.md) function, the [**D3DX10CreateDeviceAndSwapChain**](d3dx10createdeviceandswapchain.md) function, the [**D3D10CreateDevice1**](/windows/desktop/api/D3D10_1/nf-d3d10_1-d3d10createdevice1) function, or the [**D3D10CreateDeviceAndSwapChain1**](/windows/desktop/api/D3D10_1/nf-d3d10_1-d3d10createdeviceandswapchain1) function.

You can only create a Direct3D 10.1 device on computers running Windows Vista Service Pack 1 or later, and with Direct3D 10.1-compatible hardware installed. This function will return E\_FAIL on any computer not meeting these requirements. However, you can call this function on any version of Windows that has the D3DX10 DLL installed.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Core.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




