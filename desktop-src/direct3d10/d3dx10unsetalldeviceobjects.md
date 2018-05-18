---
Description: 'Removes all resources from the device by setting their pointers to NULL. This should be called during shutdown of your application. It helps ensure that when one is releasing all of their resources that none of them are bound to the device.'
ms.assetid: 'f41ce97e-5a81-43a4-a8c7-7411b43c0d61'
title: D3DX10UnsetAllDeviceObjects function
---

# D3DX10UnsetAllDeviceObjects function

Removes all resources from the device by setting their pointers to **NULL**. This should be called during shutdown of your application. It helps ensure that when one is releasing all of their resources that none of them are bound to the device.

## Syntax


```C++
HRESULT D3DX10UnsetAllDeviceObjects(
  _In_ ID3D10Device *pDevice
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](id3d10device.md)\***

Pointer to the device. See [**ID3D10Device Interface**](id3d10device.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




