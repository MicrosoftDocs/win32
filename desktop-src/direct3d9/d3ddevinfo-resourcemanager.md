---
description: Resource usage statistics.
ms.assetid: e43de550-2025-4210-a420-e41d14620704
title: D3DDEVINFO_RESOURCEMANAGER structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DDEVINFO_RESOURCEMANAGER
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DDEVINFO\_RESOURCEMANAGER structure

Resource usage statistics.

## Syntax


```C++
typedef struct _D3DDEVINFO_RESOURCEMANAGER {
  D3DRESOURCESTATS stats[D3DRTYPECOUNT];
} D3DDEVINFO_RESOURCEMANAGER, *LPD3DDEVINFO_RESOURCEMANAGER;

```



## Members

<dl> <dt>

**stats**
</dt> <dd>

Type: **[**D3DRESOURCESTATS**](d3dresourcestats.md)**

</dd> <dd>

Array of resource statistics elements. See [**D3DRESOURCESTATS**](d3dresourcestats.md).

</dd> </dl>

## Remarks

D3DRTYPECOUNT refers to the number of enumerations in [**D3DRESOURCETYPE**](./d3dresourcetype.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
