---
description: Process some data.
ms.assetid: c64f6a2d-4512-4028-8ed9-bfc5e9e86758
title: ID3DX10DataProcessor::Process method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10DataProcessor.Process
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10DataProcessor::Process method

Process some data.

## Syntax


```C++
HRESULT Process(
  [in] void   *pData,
  [in] SIZE_T cBytes
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **void\***

Pointer to the data to be processed.

</dd> <dt>

*cBytes* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](../winprog/windows-data-types.md)**

Size of the data to be processed.

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

 

 
