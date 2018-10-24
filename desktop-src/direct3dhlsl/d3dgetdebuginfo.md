---
title: D3DGetDebugInfo function
description: Note You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store. Gets shader debug information.
ms.assetid: e3cf2fe8-3052-4602-b712-a0ebd13ef3d2
keywords:
- D3DGetDebugInfo function HLSL
topic_type:
- apiref
api_name:
- D3DGetDebugInfo
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DGetDebugInfo function

> [!Note]  
> You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.

 

Gets shader debug information.

## Syntax

``` syntax
HRESULT WINAPI D3DGetDebugInfo(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  out ID3DBlob ppDebugInfo
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to source data; either uncompiled or compiled HLSL code.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of *pSrcData*.

</dd> <dt>

*ppDebugInfo* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that contains debug information.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

Debug information is embedded in the body of the shader after calling [**D3DCompile**](d3dcompile.md).

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

 

 





