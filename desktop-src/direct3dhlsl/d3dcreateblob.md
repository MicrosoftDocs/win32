---
title: D3DCreateBlob function
description: Creates a buffer.
ms.assetid: 9cad9bff-1641-4fb1-a7c9-c3e31089d7f7
keywords:
- D3DCreateBlob function HLSL
topic_type:
- apiref
api_name:
- D3DCreateBlob
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DCreateBlob function

Creates a buffer.

## Syntax

``` syntax
HRESULT WINAPI D3DCreateBlob(
  in  SIZE_T Size,
  out ID3DBlob ppBlob
);
```

## Parameters

<dl> <dt>

*Size* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Number of bytes in the blob.

</dd> <dt>

*ppBlob* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

The address of a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that is used to retrieve the buffer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

The latest D3dcompiler\_nn.dll contains the **D3DCreateBlob** compiler function. Therefore, you are no longer required to create and use an arbitrary length data buffer by using the [**D3D10CreateBlob**](https://msdn.microsoft.com/library/windows/desktop/bb205085) function that is contained in D3d10.dll.

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3DCompiler.lib</dt> </dl>     |
| DLL<br/>     | <dl> <dt>D3DCompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





