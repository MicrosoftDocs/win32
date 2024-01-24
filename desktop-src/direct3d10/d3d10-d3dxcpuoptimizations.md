---
description: Enables or disables CPU optimizations.
ms.assetid: 6f73df12-f2fc-4651-b0f7-f7a55e534d3d
title: D3DXCpuOptimizations function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCpuOptimizations
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXCpuOptimizations function

Enables or disables CPU optimizations.

## Syntax


```C++
D3DX_CPU_OPTIMIZATION D3DXCpuOptimizations(
  _In_ BOOL Enable
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

**TRUE** to enable CPU optimizations; otherwise **FALSE**.

</dd> </dl>

## Return value

Type: **[**D3DX\_CPU\_OPTIMIZATION**](d3dx-cpu-optimization.md)**

Returns the type of CPU detected, and for which optimizations exist (see [**D3DX\_CPU\_OPTIMIZATION**](d3dx-cpu-optimization.md)).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
