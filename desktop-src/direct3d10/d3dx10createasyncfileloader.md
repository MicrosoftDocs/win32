---
description: Create an asynchronous-file loader.
ms.assetid: 1b79fba5-e7f0-4160-9cec-ffea94f84fde
title: D3DX10CreateAsyncFileLoader function (D3DX10Async.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10CreateAsyncFileLoader
api_type: 
- HeaderDef
api_location: 
- D3DX10Async.h
---

# D3DX10CreateAsyncFileLoader function

Create an asynchronous-file loader.

## Syntax


```C++
HRESULT D3DX10CreateAsyncFileLoader(
  _In_  LPCTSTR           pFileName,
  _Out_ ID3DX10DataLoader **ppDataLoader
);
```



## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

The name of the file to load. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> <dt>

*ppDataLoader* \[out\]
</dt> <dd>

Type: **[**ID3DX10DataLoader**](id3dx10dataloader.md)\*\***

Address of a pointer to the asynchronous-data loader (see [**ID3DX10DataLoader Interface**](id3dx10dataloader.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Async.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 
