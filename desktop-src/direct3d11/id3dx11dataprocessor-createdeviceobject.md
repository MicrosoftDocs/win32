---
title: ID3DX11DataProcessor CreateDeviceObject method (D3DX11core.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Creates a device object.
ms.assetid: 797d216b-2f54-4d24-aa97-04be0c71f909
keywords:
- CreateDeviceObject method Direct3D 11
- CreateDeviceObject method Direct3D 11 , ID3DX11DataProcessor interface
- ID3DX11DataProcessor interface Direct3D 11 , CreateDeviceObject method
topic_type:
- apiref
api_name:
- ID3DX11DataProcessor.CreateDeviceObject
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11DataProcessor::CreateDeviceObject method

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

Creates a device object.

## Syntax


```C++
HRESULT CreateDeviceObject(
  [out] void **ppDataObject
);
```



## Parameters

<dl> <dt>

*ppDataObject* \[out\]
</dt> <dd>

Type: **void\*\***

Address of a pointer to the created device object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

This method is used by an [**ID3DX11ThreadPump Interface**](id3dx11threadpump.md).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DX11DataProcessor](id3dx11dataprocessor.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

 





