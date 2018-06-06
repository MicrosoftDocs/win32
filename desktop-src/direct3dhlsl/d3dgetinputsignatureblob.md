---
title: D3DGetInputSignatureBlob function
description: Note D3DGetInputSignatureBlob may be altered or unavailable for releases after Windows 8.1. Instead use D3DGetBlobPart with the D3D\_BLOB\_INPUT\_SIGNATURE\_BLOB value. Gets the input signature from a compilation result.
ms.assetid: a3031513-ea13-434c-8379-2f3e11aae1a5
keywords:
- D3DGetInputSignatureBlob function HLSL
topic_type:
- apiref
api_name:
- D3DGetInputSignatureBlob
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DGetInputSignatureBlob function

> [!Note]  
> **D3DGetInputSignatureBlob** may be altered or unavailable for releases after Windows 8.1. Instead use [**D3DGetBlobPart**](d3dgetblobpart.md) with the [**D3D\_BLOB\_INPUT\_SIGNATURE\_BLOB**](d3d-blob-part.md#d3d-blob-input-signature-blob) value.

 

Gets the input signature from a compilation result.

## Syntax

``` syntax
HRESULT WINAPI D3DGetInputSignatureBlob(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  out ID3DBlob ppSignatureBlob
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to source data as compiled HLSL code.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of *pSrcData*.

</dd> <dt>

*ppSignatureBlob* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that contains a compiled shader.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3dcompiler\_47.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3dcompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





