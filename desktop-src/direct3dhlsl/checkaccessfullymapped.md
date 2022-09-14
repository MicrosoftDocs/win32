---
title: CheckAccessFullyMapped function
description: Determines whether all values from a Sample, Gather, or Load operation accessed mapped tiles in a tiled resource.
ms.assetid: 2CAB7770-143E-4E29-A57F-96C27021AC5F
keywords:
- CheckAccessFullyMapped function HLSL
topic_type:
- apiref
api_name:
- CheckAccessFullyMapped
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CheckAccessFullyMapped function

Determines whether all values from a **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features).

## Syntax

``` syntax
bool CheckAccessFullyMapped(
  in uint_only status
);
```

## Parameters

<dl> <dt>

*status* \[in\]
</dt> <dd>

Type: **uint\_only**

The status value that is returned from a **Sample**, **Gather**, or **Load** operation. Because you can't access this status value directly, you need to pass it to **CheckAccessFullyMapped**.

</dd> </dl>

## Return value

Type: **bool**

Returns a **Boolean** value that indicates whether all values from a **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). Returns **TRUE** if all values from the operation accessed mapped tiles; otherwise, returns **FALSE** if any values were taken from an unmapped tile.

## Remarks

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 