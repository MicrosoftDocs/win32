---
title: D3DSetBlobPart function
description: Sets information in a compilation result.
ms.assetid: 244B094D-408A-4EC3-BC56-A7EE41D695E4
keywords:
- D3DSetBlobPart function HLSL
topic_type:
- apiref
api_name:
- D3DSetBlobPart
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

# D3DSetBlobPart function

Sets information in a compilation result.

## Syntax

``` syntax
HRESULT WINAPI D3DSetBlobPart(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  in  D3D_BLOB_PART Part,
  in  UINT Flags,
  in  LPCVOID pPart,
  in  SIZE_T PartSize,
  out ID3DBlob ppNewShader
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to compiled shader data.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The length of the compiled shader data that *pSrcData* points to.

</dd> <dt>

*Part* \[in\]
</dt> <dd>

Type: **[**D3D\_BLOB\_PART**](d3d-blob-part.md)**

A [**D3D\_BLOB\_PART**](d3d-blob-part.md)-typed value that specifies the part to set. Currently, you can update only private data; that is, **D3DSetBlobPart** currently only supports the [**D3D\_BLOB\_PRIVATE\_DATA**](d3d-blob-part.md#d3d-blob-private-data) value.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags that indicate how to set the blob part. Currently, no flags are defined; therefore, set to zero.

</dd> <dt>

*pPart* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to data to set in the compilation result.

</dd> <dt>

*PartSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The length of the data that *pPart* points to.

</dd> <dt>

*ppNewShader* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface for the new shader in which the new part data is set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

**D3DSetBlobPart** modifies data in a compiled shader. Currently, **D3DSetBlobPart** can update only the private data in a compiled shader. You can use **D3DSetBlobPart** to attach arbitrary uninterpreted data to a compiled shader.

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DSetBlobPart** compiler function.

 

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

 

 





