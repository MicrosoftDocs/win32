---
description: Calculate per-triangle IMT's from per-texel data. This function is similar to D3DXComputeIMTFromTexture, but it uses a float array to pass in the data, and it can calculate higher dimensional values than 4.
ms.assetid: 4a151184-e67e-41e9-83c6-63da72f262fa
title: D3DXComputeIMTFromPerTexelSignal function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXComputeIMTFromPerTexelSignal
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXComputeIMTFromPerTexelSignal function

Calculate per-triangle IMT's from per-texel data. This function is similar to [**D3DXComputeIMTFromTexture**](d3dxcomputeimtfromtexture.md), but it uses a float array to pass in the data, and it can calculate higher dimensional values than 4.

## Syntax


```C++
HRESULT D3DXComputeIMTFromPerTexelSignal(
  _In_  LPD3DXMESH      pMesh,
  _In_  DWORD           dwTextureIndex,
  _In_  FLOAT           *pfTexelSignal,
  _In_  UINT            uWidth,
  _In_  UINT            uHeight,
  _In_  UINT            uSignalDimension,
  _In_  UINT            uComponents,
  _In_  DWORD           dwOptions,
        LPD3DXUVATLASCB pStatusCallback,
        LPVOID          pUserContext,
  _Out_ LPD3DXBUFFER    *ppIMTData
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

A pointer to an input mesh (see [**ID3DXMesh**](id3dxmesh.md)) which contains the object geometry for calculating the IMT.

</dd> <dt>

*dwTextureIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Zero-based texture coordinate index that identifies which set of texture coordinates to use.

</dd> <dt>

*pfTexelSignal* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

A pointer to an array of input texels from which IMT will be computed. The array size is uWidth\*uHeight\*uComponents.

</dd> <dt>

*uWidth* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Texture width in pixels.

</dd> <dt>

*uHeight* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Texture height in pixels.

</dd> <dt>

*uSignalDimension* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of floats per-component in each element of the signal array.

</dd> <dt>

*uComponents* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of components in each texel.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Texture wrap options. This is a combination of one or more [**D3DXIMT FLAGS**](./d3dximt-flags.md).

</dd> <dt>

*pStatusCallback* 
</dt> <dd>

Type: **[LPD3DXUVATLASCB](lpd3dxuvatlascb.md)**

A pointer to a callback function to monitor IMT computation progress.

</dd> <dt>

*pUserContext* 
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

A pointer to a user-defined variable which is passed to the status callback function. Typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

</dd> <dt>

*ppIMTData* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

A pointer to the buffer (see [**ID3DXBuffer**](id3dxbuffer.md)) containing the returned IMT array. This array can be provided as input to the D3DX [UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md) to prioritize texture-space allocation in the texture parameterization.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK; otherwise, the value is D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md)
</dt> <dt>

[Using UVAtlas (Direct3D 9)](using-uvatlas.md)
</dt> </dl>

 

 
