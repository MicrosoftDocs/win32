---
description: Percent of time processing shader data.
ms.assetid: 388bb943-c25f-4b50-b7e4-d6259f1186c2
title: D3DDEVINFO_D3D9STAGETIMINGS structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DDEVINFO_D3D9STAGETIMINGS
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DDEVINFO\_D3D9STAGETIMINGS structure

Percent of time processing shader data.

## Syntax


```C++
typedef struct D3DDEVINFO_D3D9STAGETIMINGS {
  FLOAT MemoryProcessingPercent;
  FLOAT ComputationProcessingPercent;
} D3DDEVINFO_D3D9STAGETIMINGS, *LPD3DDEVINFO_D3D9STAGETIMINGS;
```



## Members

<dl> <dt>

**MemoryProcessingPercent**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Percent of time in shader spent on memory accesses.

</dd> <dt>

**ComputationProcessingPercent**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Percent of time processing (moving data around in registers or doing mathematical operations).

</dd> </dl>

## Remarks

For best performance, a balanced load is recommended.

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

 

 
