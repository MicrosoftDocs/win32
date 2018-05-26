---
title: Operator\ \ function
description: Returns a resource variable.
ms.assetid: 59e5e4ec-ff0d-43aa-805a-04b79f5ab57f
keywords:
- Operator function HLSL
topic_type:
- apiref
api_name:
- Operator
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Operator\[\] function

Returns a resource variable.

## Syntax

``` syntax
R Operator[](
  in uint pos
);
```

## Parameters

<dl> <dt>

*pos* \[in\]
</dt> <dd>

Type: **uint**

The index position.

</dd> </dl>

## Return value

Type: **R**

A resource variable.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[RWBuffer](sm5-object-rwbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




