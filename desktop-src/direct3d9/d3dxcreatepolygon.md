---
Description: Uses a left-handed coordinate system to create a mesh containing an n-sided polygon.
ms.assetid: f3313f55-3e60-4440-8bea-d2886b636c9a
title: D3DXCreatePolygon function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCreatePolygon function

Uses a left-handed coordinate system to create a mesh containing an n-sided polygon.

## Syntax


```C++
HRESULT D3DXCreatePolygon(
  _In_  LPDIRECT3DDEVICE9 pDevice,
  _In_  FLOAT             Length,
  _In_  UINT              Sides,
  _Out_ LPD3DXMESH        *ppMesh,
  _Out_ LPD3DXBUFFER      *ppAdjacency
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) interface, representing the device associated with the created polygon mesh.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Length of each side.

</dd> <dt>

*Sides* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of sides for the polygon. Value must be greater than or equal to 3.

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

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

The created polygon is centered at the origin.

This function creates a mesh with the D3DXMESH\_MANAGED creation option and [D3DFVF\_XYZ \| D3DFVF\_NORMAL](d3dfvf.md) flexible vertex format (FVF).

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9shape.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>    |



## See also

<dl> <dt>

[Shape Drawing Functions](dx9-graphics-reference-d3dx-functions-shape.md)
</dt> </dl>

 

 




