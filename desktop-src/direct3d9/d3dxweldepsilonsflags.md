---
description: Options for welding together vertices.
ms.assetid: e73af63d-ed02-4fbc-8386-e8a40b0465ea
title: D3DXWELDEPSILONSFLAGS enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _D3DXWELDEPSILONSFLAGS
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXWELDEPSILONSFLAGS enumeration

Options for welding together vertices.

## Syntax


```C++
enum _D3DXWELDEPSILONSFLAGS {
  D3DXWELDEPSILONS_WELDALL              = 1, 
  D3DXWELDEPSILONS_WELDPARTIALMATCHES   = 2, 
  D3DXWELDEPSILONS_DONOTREMOVEVERTICES  = 4, 
  D3DXWELDEPSILONS_DONOTSPLIT           = 8 

};
```



## Constants

<dl> <dt>

<span id="D3DXWELDEPSILONS_WELDALL"></span><span id="d3dxweldepsilons_weldall"></span>**D3DXWELDEPSILONS\_WELDALL**
</dt> <dd>

Weld together all vertices that are at the same location. Using this flag avoids an epsilon comparison between vertex components.

</dd> <dt>

<span id="D3DXWELDEPSILONS_WELDPARTIALMATCHES"></span><span id="d3dxweldepsilons_weldpartialmatches"></span>**D3DXWELDEPSILONS\_WELDPARTIALMATCHES**
</dt> <dd>

If a given vertex component is within epsilon, modify partially matched vertices so that both components are identical. If all components are equal, remove one of the vertices.

</dd> <dt>

<span id="D3DXWELDEPSILONS_DONOTREMOVEVERTICES"></span><span id="d3dxweldepsilons_donotremovevertices"></span>**D3DXWELDEPSILONS\_DONOTREMOVEVERTICES**
</dt> <dd>

Instructs the weld to allow only modifications to vertices and not removal. This flag is valid only if D3DXWELDEPSILONS\_WELDPARTIALMATCHES is set. It is useful to modify vertices to be equal, but not to allow vertices to be removed.

</dd> <dt>

<span id="D3DXWELDEPSILONS_DONOTSPLIT"></span><span id="d3dxweldepsilons_donotsplit"></span>**D3DXWELDEPSILONS\_DONOTSPLIT**
</dt> <dd>

Instructs the weld not to split vertices that are in separate attribute groups. When the [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) method is called with the D3DXMESHOPT\_ATTRSORT flag, then the D3DXMESHOPT\_DONOTSPLIT flag will also be set. Setting this flag can slow down software vertex processing.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> <dt>

[**D3DXWeldVertices**](d3dxweldvertices.md)
</dt> </dl>

 

 




