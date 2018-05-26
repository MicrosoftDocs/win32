---
Description: Creates an ID3DXTextureGutterHelper object from an input mesh and texture data.
ms.assetid: 1696fc3d-5b35-48cc-a79b-c0d4ed44e420
title: D3DXCreateTextureGutterHelper function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCreateTextureGutterHelper function

Creates an [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object from an input mesh and texture data.

## Syntax


```C++
HRESULT D3DXCreateTextureGutterHelper(
  _In_    UINT                      Width,
  _In_    UINT                      Height,
  _In_    LPD3DXMESH                pMesh,
  _In_    FLOAT                     GutterSize,
  _Inout_ LPD3DXTEXTUREGUTTERHELPER *ppBuffer
);
```



## Parameters

<dl> <dt>

*Width* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Width of the texture, in pixels.

</dd> <dt>

*Height* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Height of the texture, in pixels.

</dd> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an input [**ID3DXMesh**](id3dxmesh.md) mesh object.

</dd> <dt>

*GutterSize* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Number of texels by which to over-sample the texture and create the gutter region. Must be at least 1.

</dd> <dt>

*ppBuffer* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXTEXTUREGUTTERHELPER**](id3dxtexturegutterhelper.md)\***

Pointer to an [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object to be created.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of these: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Use [**D3DXConcatenateMeshes**](d3dxconcatenatemeshes.md) to transform a scene to new coordinates.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> </dl>

 

 




