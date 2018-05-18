---
Description: 'Generates mipmap chain using a particular texture filter.'
ms.assetid: '19e651dd-dc34-405b-8769-00d91c097a1f'
title: D3DX10FilterTexture function
---

# D3DX10FilterTexture function

Generates mipmap chain using a particular texture filter.

## Syntax


```C++
HRESULT D3DX10FilterTexture(
   ID3D10Resource *pTexture,
   UINT           SrcLevel,
   UINT           MipFilter
);
```



## Parameters

<dl> <dt>

*pTexture* 
</dt> <dd>

Type: **[**ID3D10Resource**](id3d10resource.md)\***

The texture object to be filtered. See [**ID3D10Resource**](id3d10resource.md).

</dd> <dt>

*SrcLevel* 
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The mipmap level whose data is used to generate the rest of the mipmap chain.

</dd> <dt>

*MipFilter* 
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Flags controlling how each miplevel is filtered (or D3DX10\_DEFAULT for D3DX10\_FILTER\_BOX). See [**D3DX10\_FILTER\_FLAG**](d3dx10-filter-flag.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Tex.h</dt> </dl> |



## See also

<dl> <dt>

[Texture Functions in D3DX 10](d3d10-graphics-reference-d3dx10-functions-texturing.md)
</dt> </dl>

 

 




