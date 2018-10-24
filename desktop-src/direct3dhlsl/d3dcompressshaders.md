---
title: D3DCompressShaders function
description: Compresses a set of shaders into a more compact form.
ms.assetid: e53a0d36-3cd4-4327-8969-6a864b38a15b
keywords:
- D3DCompressShaders function HLSL
topic_type:
- apiref
api_name:
- D3DCompressShaders
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DCompressShaders function

> [!Note]  
> You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.

 

Compresses a set of shaders into a more compact form.

## Syntax

``` syntax
HRESULT WINAPI D3DCompressShaders(
  in  UINT uNumShaders,
  in  D3D_SHADER_DATA pShaderData,
  in  UINT uFlags,
  out ID3DBlob ppCompressedData
);
```

## Parameters

<dl> <dt>

*uNumShaders* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of shaders to compress.

</dd> <dt>

*pShaderData* \[in\]
</dt> <dd>

Type: **[**D3D\_SHADER\_DATA**](d3d-shader-data.md)\***

An array of [**D3D\_SHADER\_DATA**](d3d-shader-data.md) structures that describe the set of shaders to compress.

</dd> <dt>

*uFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags that indicate how to compress the shaders. Currently, only the D3D\_COMPRESS\_SHADER\_KEEP\_ALL\_PARTS (0x00000001) flag is defined.

</dd> <dt>

*ppCompressedData* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

The address of a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that is used to retrieve the compressed shader data.

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

 

 





