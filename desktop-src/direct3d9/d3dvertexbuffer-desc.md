---
Description: Describes a vertex buffer.
ms.assetid: 0ae8f976-d0ca-4d55-b6db-5be85fa3c799
title: D3DVERTEXBUFFER\_DESC structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

Type: **[**D3DRESOURCETYPE**](https://msdn.microsoft.com/en-us/library/Bb172601(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DRESOURCETYPE**](https://msdn.microsoft.com/en-us/library/Bb172601(v=VS.85).aspx) enumerated type, identifying this resource as a vertex buffer.

</dd> <dt>

**Usage**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Combination of one or more [**D3DUSAGE**](d3dusage.md) flags.

</dd> <dt>

**Pool**
</dt> <dd>

Type: **[**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DPOOL**](https://msdn.microsoft.com/en-us/library/Bb172584(v=VS.85).aspx) enumerated type, specifying the class of memory allocated for this vertex buffer.

</dd> <dt>

**Size**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Size of the vertex buffer, in bytes.

</dd> <dt>

**FVF**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Combination of [D3DFVF](d3dfvf.md) that describes the vertex format of the vertices in this buffer.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetDesc**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dvertexbuffer9-getdesc)
</dt> <dt>

[Vertex Buffers (Direct3D 9)](vertex-buffers.md)
</dt> </dl>

 

 




