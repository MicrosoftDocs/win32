---
description: Contains data for memory pressure reporting.
ms.assetid: bdf65d35-281f-4795-a2c1-0d4e91bfa7bc
title: D3DMEMORYPRESSURE structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DMEMORYPRESSURE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DMEMORYPRESSURE structure (D3d9types.h)

Contains data for memory pressure reporting.

## Syntax


```C++
typedef struct _D3DMEMORYPRESSURE {
  UINT64 BytesEvictedFromProcess;
  UINT64 SizeOfInefficientAllocation;
  DWORD  LevelOfEfficiency;
} D3DMEMORYPRESSURE;
```



## Members

<dl> <dt>

**BytesEvictedFromProcess**
</dt> <dd>

Type: **[**UINT64**](../winprog/windows-data-types.md)**

</dd> <dd>

The number of bytes that were evicted by the process during the duration of the query.

</dd> <dt>

**SizeOfInefficientAllocation**
</dt> <dd>

Type: **[**UINT64**](../winprog/windows-data-types.md)**

</dd> <dd>

The total number of bytes placed in nonoptimal memory segments, due to inadequate space within the preferred memory segments.

</dd> <dt>

**LevelOfEfficiency**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

The overall efficiency of the memory allocations that were placed in nonoptimal memory. The value is expressed as a percentage. For example, the value 95 indicates that the allocations placed in nonpreferred memory segments are 95% efficient. This number should not be considered an exact measurement.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
