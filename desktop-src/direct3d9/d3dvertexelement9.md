---
Description: 'Defines the vertex data layout. Each vertex can contain one or more data types, and each data type is described by a vertex element.'
ms.assetid: '6f3c40a0-b28e-48d6-acad-ef80a919c5d7'
title: D3DVERTEXELEMENT9 structure
---

# D3DVERTEXELEMENT9 structure

Defines the vertex data layout. Each vertex can contain one or more data types, and each data type is described by a vertex element.

## Syntax


```C++
typedef struct D3DVERTEXELEMENT9 {
  WORD Stream;
  WORD Offset;
  BYTE Type;
  BYTE Method;
  BYTE Usage;
  BYTE UsageIndex;
} D3DVERTEXELEMENT9, *LPD3DVERTEXELEMENT9;
```



## Members

<dl> <dt>

**Stream**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

Stream number.

</dd> <dt>

**Offset**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

Offset from the beginning of the vertex data to the data associated with the particular data type.

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**BYTE**](winprog.windows_data_types)**

</dd> <dd>

The data type, specified as a [**D3DDECLTYPE**](direct3d9.d3ddecltype). One of several predefined types that define the data size. Some methods have an implied type.

</dd> <dt>

**Method**
</dt> <dd>

Type: **[**BYTE**](winprog.windows_data_types)**

</dd> <dd>

The method specifies the tessellator processing, which determines how the tessellator interprets (or operates on) the vertex data. For more information, see [**D3DDECLMETHOD**](direct3d9.d3ddeclmethod).

</dd> <dt>

**Usage**
</dt> <dd>

Type: **[**BYTE**](winprog.windows_data_types)**

</dd> <dd>

Defines what the data will be used for; that is, the interoperability between vertex data layouts and vertex shaders. Each usage acts to bind a vertex declaration to a vertex shader. In some cases, they have a special interpretation. For example, an element that specifies D3DDECLUSAGE\_NORMAL or D3DDECLUSAGE\_POSITION is used by the N-patch tessellator to set up tessellation. See [**D3DDECLUSAGE**](direct3d9.d3ddeclusage) for a list of the available semantics. D3DDECLUSAGE\_TEXCOORD can be used for user-defined fields (which don't have an existing usage defined).

</dd> <dt>

**UsageIndex**
</dt> <dd>

Type: **[**BYTE**](winprog.windows_data_types)**

</dd> <dd>

Modifies the usage data to allow the user to specify multiple usage types.

</dd> </dl>

## Remarks

Vertex data is defined using an array of **D3DVERTEXELEMENT9** structures. Use [**D3DDECL\_END**](d3ddecl-end.md) to declare the last element in the declaration.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[Vertex Declaration (Direct3D 9)](vertex-declaration.md)
</dt> </dl>

 

 




