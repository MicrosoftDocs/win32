---
description: Specifies the instruction set D3DX is currently optimized for.
ms.assetid: 5fc97028-4a9d-4bc7-9c90-236a70e570e1
title: D3DX_CPU_OPTIMIZATION enumeration (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX_CPU_OPTIMIZATION
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DX\_CPU\_OPTIMIZATION enumeration

Specifies the instruction set D3DX is currently optimized for.

## Syntax


```C++
typedef enum _D3DX_CPU_OPTIMIZATION { 
  D3DX_NOT_OPTIMIZED    = 0,
  D3DX_3DNOW_OPTIMIZED  = 1,
  D3DX_SSE2_OPTIMIZED   = 2,
  D3DX_SSE_OPTIMIZED    = 3
} D3DX_CPU_OPTIMIZATION;
```



## Constants

<dl> <dt>

<span id="D3DX_NOT_OPTIMIZED"></span><span id="d3dx_not_optimized"></span>**D3DX\_NOT\_OPTIMIZED**
</dt> <dd>

Do not optimize.

</dd> <dt>

<span id="D3DX_3DNOW_OPTIMIZED"></span><span id="d3dx_3dnow_optimized"></span>**D3DX\_3DNOW\_OPTIMIZED**
</dt> <dd>

Optimize for a 3DNow! instruction set.

</dd> <dt>

<span id="D3DX_SSE2_OPTIMIZED"></span><span id="d3dx_sse2_optimized"></span>**D3DX\_SSE2\_OPTIMIZED**
</dt> <dd>

Optimize for an SSE2 instruction set.

</dd> <dt>

<span id="D3DX_SSE_OPTIMIZED"></span><span id="d3dx_sse_optimized"></span>**D3DX\_SSE\_OPTIMIZED**
</dt> <dd>

Optimize for an SSE instruction set.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](d3d10-graphics-reference-d3dx10-enums.md)
</dt> </dl>

 

 




