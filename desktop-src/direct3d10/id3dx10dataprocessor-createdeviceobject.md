---
description: Create a device object.
ms.assetid: 5b9b00de-c744-43c7-b383-1d3358c80741
title: ID3DX10DataProcessor::CreateDeviceObject method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10DataProcessor.CreateDeviceObject
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10DataProcessor::CreateDeviceObject method

Create a device object.

## Syntax


```C++
HRESULT CreateDeviceObject(
  [out] void **ppDataObject
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

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10DataProcessor](id3dx10dataprocessor.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




