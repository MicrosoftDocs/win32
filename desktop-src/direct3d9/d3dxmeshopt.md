---
description: Specifies the type of mesh optimization to be performed.
ms.assetid: 32ef227a-b299-47c4-96b8-c0ea7bf549e1
title: D3DXMESHOPT enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _D3DXMESHOPT
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXMESHOPT enumeration

Specifies the type of mesh optimization to be performed.

## Syntax


```C++
enum _D3DXMESHOPT {
  D3DXMESHOPT_COMPACT            = 0x01000000, 
  D3DXMESHOPT_ATTRSORT           = 0x02000000, 
  D3DXMESHOPT_VERTEXCACHE        = 0x04000000, 
  D3DXMESHOPT_STRIPREORDER       = 0x08000000, 
  D3DXMESHOPT_IGNOREVERTS        = 0x10000000, 
  D3DXMESHOPT_DONOTSPLIT         = 0x20000000, 
  D3DXMESHOPT_DEVICEINDEPENDENT  = 0x40000000 

};
```



## Constants

<dl> <dt>

<span id="D3DXMESHOPT_COMPACT"></span><span id="d3dxmeshopt_compact"></span>**D3DXMESHOPT\_COMPACT**
</dt> <dd>

Reorders faces to remove unused vertices and faces.

</dd> <dt>

<span id="D3DXMESHOPT_ATTRSORT"></span><span id="d3dxmeshopt_attrsort"></span>**D3DXMESHOPT\_ATTRSORT**
</dt> <dd>

Reorders faces to optimize for fewer attribute bundle state changes and enhanced [**ID3DXBaseMesh::DrawSubset**](id3dxbasemesh--drawsubset.md) performance.

</dd> <dt>

<span id="D3DXMESHOPT_VERTEXCACHE"></span><span id="d3dxmeshopt_vertexcache"></span>**D3DXMESHOPT\_VERTEXCACHE**
</dt> <dd>

Reorders faces to increase the cache hit rate of vertex caches.

</dd> <dt>

<span id="D3DXMESHOPT_STRIPREORDER"></span><span id="d3dxmeshopt_stripreorder"></span>**D3DXMESHOPT\_STRIPREORDER**
</dt> <dd>

Reorders faces to maximize length of adjacent triangles.

</dd> <dt>

<span id="D3DXMESHOPT_IGNOREVERTS"></span><span id="d3dxmeshopt_ignoreverts"></span>**D3DXMESHOPT\_IGNOREVERTS**
</dt> <dd>

Optimize the faces only; do not optimize the vertices.

</dd> <dt>

<span id="D3DXMESHOPT_DONOTSPLIT"></span><span id="d3dxmeshopt_donotsplit"></span>**D3DXMESHOPT\_DONOTSPLIT**
</dt> <dd>

While attribute sorting, do not split vertices that are shared between attribute groups.

</dd> <dt>

<span id="D3DXMESHOPT_DEVICEINDEPENDENT"></span><span id="d3dxmeshopt_deviceindependent"></span>**D3DXMESHOPT\_DEVICEINDEPENDENT**
</dt> <dd>

Affects the vertex cache size. Using this flag specifies a default vertex cache size that works well on legacy hardware.

</dd> </dl>

## Remarks

The D3DXMESHOPT\_STRIPREORDER and D3DXMESHOPT\_VERTEXCACHE optimization flags are mutually exclusive.

The D3DXMESHOPT\_SHAREVB flag has been removed from this enumeration. Use D3DXMESH\_VB\_SHARE instead, in [**D3DXMESH**](./d3dxmesh.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 
