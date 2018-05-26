---
Description: Vertex cache optimization hints.
ms.assetid: 891624cd-03dd-4ddd-93f5-4899e1470325
title: D3DDEVINFO\_VCACHE structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DDEVINFO\_VCACHE structure

Vertex cache optimization hints.

## Syntax


```C++
typedef struct D3DDEVINFO_VCACHE {
  DWORD Pattern;
  DWORD OptMethod;
  DWORD CacheSize;
  DWORD MagicNumber;
} D3DDEVINFO_VCACHE, *LPD3DDEVINFO_VCACHE;
```



## Members

<dl> <dt>

**Pattern**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Bit pattern. Return value must be the FOURCC ('C', 'A', 'C', 'H').

</dd> <dt>

**OptMethod**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Optimizations method. Use 0 to get the longest strips. Use 1 to optimize the vertex cache usage.

</dd> <dt>

**CacheSize**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Cache size used as a target for optimization. This is required only if OptMethod is 1.

</dd> <dt>

**MagicNumber**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Used by internal optimization methods to determine when to restart strips. This cannot be set or modified by a user. This is required only if OptMethod is 1.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetData**](/windows/win32/d3d9helper/nf-d3d9-idirect3dquery9-getdata?branch=master)
</dt> </dl>

 

 




