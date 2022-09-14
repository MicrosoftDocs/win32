---
description: A helper structure containing member structure information.
ms.assetid: 2fbe5e97-047e-48bf-9413-dd297632288a
title: D3DXSHADER_STRUCTMEMBERINFO structure (D3dx9shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHADER_STRUCTMEMBERINFO
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
---

# D3DXSHADER\_STRUCTMEMBERINFO structure

A helper structure containing member structure information.

## Syntax


```C++
typedef struct D3DXSHADER_STRUCTMEMBERINFO {
  DWORD Name;
  DWORD TypeInfo;
} D3DXSHADER_STRUCTMEMBERINFO, *LPD3DXSHADER_STRUCTMEMBERINFO;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Offset from the beginning of this structure, in bytes, to the string that contains the structure member name.

</dd> <dt>

**TypeInfo**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Offset from the beginning of this structure, in bytes, to the string that contains the type information. See [**D3DXSHADER\_TYPEINFO**](d3dxshader-typeinfo.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXSHADER\_TYPEINFO**](d3dxshader-typeinfo.md)
</dt> </dl>

 

 
