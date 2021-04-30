---
description: Defines a range.
ms.assetid: 28e8c478-f6ce-4f75-95c6-ea2d08424238
title: D3DRANGE structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DRANGE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DRANGE structure

Defines a range.

## Syntax


```C++
typedef struct D3DRANGE {
  UINT Offset;
  UINT Size;
} D3DRANGE, *LPD3DRANGE;
```



## Members

<dl> <dt>

**Offset**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Offset, in bytes.

</dd> <dt>

**Size**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Size, in bytes.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
