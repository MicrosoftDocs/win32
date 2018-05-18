---
Description: 'Structure that contains the attributes of a patch mesh.'
ms.assetid: 'aaea69c9-2d33-46e8-bc26-95daf65abf50'
title: D3DXPATCHINFO structure
---

# D3DXPATCHINFO structure

Structure that contains the attributes of a patch mesh.

## Syntax


```C++
typedef struct D3DXPATCHINFO {
  D3DXPATCHMESHTYPE PatchType;
  D3DDEGREETYPE     Degree;
  D3DBASISTYPE      Basis;
} D3DXPATCHINFO, *LPD3DXPATCHINFO;
```



## Members

<dl> <dt>

**PatchType**
</dt> <dd>

Type: **[**D3DXPATCHMESHTYPE**](direct3d9.d3dxpatchmeshtype)**

</dd> <dd>

The patch type. For information about patch types, see [**D3DXPATCHMESHTYPE**](direct3d9.d3dxpatchmeshtype).

</dd> <dt>

**Degree**
</dt> <dd>

Type: **[**D3DDEGREETYPE**](direct3d9.d3ddegreetype)**

</dd> <dd>

Degree of the curves used to construct the patch. For information about the degrees supported, see [**D3DDEGREETYPE**](direct3d9.d3ddegreetype).

</dd> <dt>

**Basis**
</dt> <dd>

Type: **[**D3DBASISTYPE**](direct3d9.d3dbasistype)**

</dd> <dd>

Type of curve used to construct the patch. For information about the basis types supported, see [**D3DBASISTYPE**](direct3d9.d3dbasistype).

</dd> </dl>

## Remarks

A mesh is a set of faces, each of which is described by a simple polygon. Objects can be created by connecting several meshes together. A patch mesh is constructed from patches. A patch is a four-sided piece of geometry constructed from curves. The type of curve used and the order of the curve can be varied so that the patch surface will fit almost any surface shape.

The following types of patch combinations are supported:



| Patch Type | Basis       | Degree |
|------------|-------------|--------|
| Rectangle  | Bezier      | 2,3,5  |
| Rectangle  | B-Spline    | 2,3,5  |
| Rectangle  | Catmull-Rom | 3      |
| Triangle   | Bezier      | 2,3,5  |
| N-patch    | N/A         | 3      |



 

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DRECTPATCH\_INFO**](d3drectpatch-info.md)
</dt> <dt>

[**D3DTRIPATCH\_INFO**](d3dtripatch-info.md)
</dt> <dt>

[**D3DXCreatePatchMesh**](d3dxcreatepatchmesh.md)
</dt> </dl>

 

 




