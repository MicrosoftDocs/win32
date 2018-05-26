---
title: D3DGetBlobPart function
description: Retrieves a specific part from a compilation result.
ms.assetid: cf9cea53-e7a3-4473-bfdf-0cdeb8370974
keywords:
- D3DGetBlobPart function HLSL
topic_type:
- apiref
api_name:
- D3DGetBlobPart
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

# D3DGetBlobPart function

Retrieves a specific part from a compilation result.

## Syntax

``` syntax
HRESULT WINAPI D3DGetBlobPart(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  in  D3D_BLOB_PART Part,
  in  UINT Flags,
  out ID3DBlob ppPart
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to uncompiled shader data; either ASCII HLSL code or a compiled effect.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of uncompiled shader data that *pSrcData* points to.

</dd> <dt>

*Part* \[in\]
</dt> <dd>

Type: **[**D3D\_BLOB\_PART**](d3d-blob-part.md)**

A [**D3D\_BLOB\_PART**](d3d-blob-part.md)-typed value that specifies the part of the buffer to retrieve.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags that indicate how to retrieve the blob part. Currently, no flags are defined.

</dd> <dt>

*ppPart* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

The address of a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that is used to retrieve the specified part of the buffer.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

**D3DGetBlobPart** retrieves the part of a blob (arbitrary length data buffer) that contains the type of data that the *Part* parameter specifies.

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

 

 





