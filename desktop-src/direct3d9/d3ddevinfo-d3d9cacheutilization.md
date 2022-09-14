---
description: Measure the cache hit rate performance for textures and indexed vertices.
ms.assetid: 70bc4e93-0a34-485b-bdcc-028c24b52f62
title: D3DDEVINFO_D3D9CACHEUTILIZATION structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DDEVINFO_D3D9CACHEUTILIZATION
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DDEVINFO\_D3D9CACHEUTILIZATION structure

Measure the cache hit rate performance for textures and indexed vertices.

## Syntax


```C++
typedef struct D3DDEVINFO_D3D9CACHEUTILIZATION {
  FLOAT TextureCacheHitRate;
  FLOAT PostTransformVertexCacheHitRate;
} D3DDEVINFO_D3D9CACHEUTILIZATION, *LPD3DDEVINFO_D3D9CACHEUTILIZATION;
```



## Members

<dl> <dt>

**TextureCacheHitRate**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The hit rate for finding a texture in the texture cache. This assumes there is a texture cache. Increasing the level-of-detail bias to use the most detailed texture, using many large textures, or producing a near random texture access pattern on large textures with custom shader code can dramatically affect the texture cache hit rate.

</dd> <dt>

**PostTransformVertexCacheHitRate**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The hit rate for finding transformed vertices in the vertex cache. The GPU is designed to transform indexed vertices and may store them in a vertex cache. If you are using meshes, [**D3DXOptimizeFaces**](d3dxoptimizefaces.md) or [**D3DXOptimizeVertices**](d3dxoptimizevertices.md) may result in better vertex cache utilization.

</dd> </dl>

## Remarks

An efficient cache is typically closer to a 90 percent hit rate, and an inefficient cache is typically closer to a 10 percent hit rate (although a low percentage is not necessarily a problem).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetData**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-getdata)
</dt> </dl>

 

 
