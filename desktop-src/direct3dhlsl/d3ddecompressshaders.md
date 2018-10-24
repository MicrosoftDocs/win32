---
title: D3DDecompressShaders function
description: Decompresses one or more shaders from a compressed set.
ms.assetid: 9b62026f-0658-405c-8f45-ee921213148a
keywords:
- D3DDecompressShaders function HLSL
topic_type:
- apiref
api_name:
- D3DDecompressShaders
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DDecompressShaders function

> [!Note]  
> You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.

 

Decompresses one or more shaders from a compressed set.

## Syntax

``` syntax
HRESULT WINAPI D3DDecompressShaders(
  in      LPCVOID pSrcData,
  in      SIZE_T SrcDataSize,
  in      UINT uNumShaders,
  in      UINT uStartIndex,
  in_opt  UINT pIndices,
  in      UINT uFlags,
  out     ID3DBlob ppShaders,
  out_opt UINT pTotalShaders
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

*uNumShaders* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of shaders to decompress.

</dd> <dt>

*uStartIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The index of the first shader to decompress.

</dd> <dt>

*pIndices* \[in, optional\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

An array of indexes that represent the shaders to decompress.

</dd> <dt>

*uFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags that indicate how to decompress. Currently, no flags are defined.

</dd> <dt>

*ppShaders* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

The address of a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that is used to retrieve the decompressed shader data.

</dd> <dt>

*pTotalShaders* \[out, optional\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

A pointer to a variable that receives the total number of shaders that **D3DDecompressShaders** decompressed.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

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

 

 





