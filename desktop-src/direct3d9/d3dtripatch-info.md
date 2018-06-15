---
Description: Describes a triangular high-order patch.
ms.assetid: 3f97120b-3b32-4f95-8614-7b263ff330db
title: D3DTRIPATCH\_INFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DTRIPATCH\_INFO structure

Describes a triangular high-order patch.

## Syntax


```C++
typedef struct D3DTRIPATCH_INFO {
  UINT          StartVertexOffset;
  UINT          NumVertices;
  D3DBASISTYPE  Basis;
  D3DDEGREETYPE Degree;
} D3DTRIPATCH_INFO, *LPD3DTRIPATCH_INFO;
```



## Members

<dl> <dt>

**StartVertexOffset**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Starting vertex offset, in number of vertices.

</dd> <dt>

**NumVertices**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of vertices.

</dd> <dt>

**Basis**
</dt> <dd>

Type: **[**D3DBASISTYPE**](https://msdn.microsoft.com/en-us/library/Bb172507(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DBASISTYPE**](https://msdn.microsoft.com/en-us/library/Bb172507(v=VS.85).aspx) enumerated type, which defines the basis type for the triangular high-order patch. The only valid value for this member is D3DBASIS\_BEZIER.

</dd> <dt>

**Degree**
</dt> <dd>

Type: **[**D3DDEGREETYPE**](https://msdn.microsoft.com/en-us/library/Bb172536(v=VS.85).aspx)**

</dd> <dd>

Member of the [**D3DDEGREETYPE**](https://msdn.microsoft.com/en-us/library/Bb172536(v=VS.85).aspx) enumerated type, defining the degree type for the triangular high-order patch.



| Value                | Number of vertices |
|----------------------|--------------------|
| D3DDEGREE\_CUBIC     | 10                 |
| D3DDEGREE\_LINEAR    | 3                  |
| D3DDEGREE\_QUADRATIC | N/A                |
| D3DDEGREE\_QUINTIC   | 21                 |



 

N/A - Not available. Not supported.

</dd> </dl>

## Remarks

For example, the following diagram identifies the vertex order and segment numbers for a cubic Bézier triangle patch. The vertex order determines the segment numbers used by [**DrawTriPatch**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-drawtripatch). The offset is the number of bytes to the first triangle patch vertex in the vertex buffer.

![diagram of a triangular high-order patch with nine vertices](images/hop-tripatch-info.png)

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**DrawTriPatch**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-drawtripatch)
</dt> <dt>

[**D3DXTessellateTriPatch**](d3dxtessellatetripatch.md)
</dt> </dl>

 

 




