---
description: Uses a left-handed coordinate system to create a mesh containing a torus.
ms.assetid: 68df7650-8a87-4762-8b57-5704c419b0d7
title: D3DXCreateTorus function (D3dx9shape.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXCreateTorus
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreateTorus function

Uses a left-handed coordinate system to create a mesh containing a torus.

## Syntax


```C++
HRESULT D3DXCreateTorus(
  _In_  LPDIRECT3DDEVICE9 pDevice,
  _In_  FLOAT             InnerRadius,
  _In_  FLOAT             OuterRadius,
  _In_  UINT              Sides,
  _In_  UINT              Rings,
  _Out_ LPD3DXMESH        *ppMesh,
  _Out_ LPD3DXBUFFER      *ppAdjacency
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) interface, representing the device associated with the created torus mesh.

</dd> <dt>

*InnerRadius* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Inner-radius of the torus. Value should be greater than or equal to 0.0f.

</dd> <dt>

*OuterRadius* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Outer-radius of the torus. Value should be greater than or equal to 0.0f.

</dd> <dt>

*Sides* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of sides in a cross-section. Value must be greater than or equal to 3.

</dd> <dt>

*Rings* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of rings making up the torus. Value must be greater than or equal to 3.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Address of a pointer to the output shape, an [**ID3DXMesh**](id3dxmesh.md) interface.

</dd> <dt>

*ppAdjacency* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) interface. When the method returns, this parameter is filled with an array of three DWORDs per face that specify the three neighbors for each face in the mesh. **NULL** can be specified.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The created torus is centered at the origin, and its axis is aligned with the z-axis. The inner radius of the torus is the radius of the cross-section (the minor radius), and the outer radius of the torus is the radius of the central hole.

This function returns a mesh that can be used later for drawing or manipulation by the application.

This function creates a mesh with the D3DXMESH\_MANAGED creation option and [D3DFVF\_XYZ \| D3DFVF\_NORMAL](d3dfvf.md) flexible vertex format (FVF).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9shape.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>    |



## See also

<dl> <dt>

[Shape Drawing Functions](dx9-graphics-reference-d3dx-functions-shape.md)
</dt> </dl>

 

 
