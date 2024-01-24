---
description: Describes a vertex buffer.
ms.assetid: 0ae8f976-d0ca-4d55-b6db-5be85fa3c799
title: D3DVERTEXBUFFER_DESC structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DVERTEXBUFFER_DESC
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DVERTEXBUFFER\_DESC structure

Describes a vertex buffer.

## Syntax


```C++
typedef struct D3DVERTEXBUFFER_DESC {
  D3DFORMAT       Format;
  D3DRESOURCETYPE Type;
  DWORD           Usage;
  D3DPOOL         Pool;
  UINT            Size;
  DWORD           FVF;
} D3DVERTEXBUFFER_DESC, *LPD3DVERTEXBUFFER_DESC;
```



## Members

<dl> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

Member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the surface format of the vertex buffer data.

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3DRESOURCETYPE**](./d3dresourcetype.md)**

</dd> <dd>

Member of the [**D3DRESOURCETYPE**](./d3dresourcetype.md) enumerated type, identifying this resource as a vertex buffer.

</dd> <dt>

**Usage**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Combination of one or more [**D3DUSAGE**](d3dusage.md) flags.

</dd> <dt>

**Pool**
</dt> <dd>

Type: **[**D3DPOOL**](./d3dpool.md)**

</dd> <dd>

Member of the [**D3DPOOL**](./d3dpool.md) enumerated type, specifying the class of memory allocated for this vertex buffer.

</dd> <dt>

**Size**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Size of the vertex buffer, in bytes.

</dd> <dt>

**FVF**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Combination of [D3DFVF](d3dfvf.md) that describes the vertex format of the vertices in this buffer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetDesc**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvertexbuffer9-getdesc)
</dt> <dt>

[Vertex Buffers (Direct3D 9)](vertex-buffers.md)
</dt> </dl>

 

 
