---
title: dst function
description: Calculates a distance vector. | dst function
ms.assetid: 24d22743-5867-49db-8d0a-55cc3625c947
keywords:
- dst function HLSL
topic_type:
- apiref
api_name:
- dst
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# dst function

Calculates a distance vector.

## Syntax

``` syntax
fVector dst(
  in fVector src0,
  in fVector src1
);
```

## Parameters

<dl> <dt>

*src0* \[in\]
</dt> <dd>

Type: **[fVector](dx-graphics-hlsl-vector.md)**

The first vector.

</dd> <dt>

*src1* \[in\]
</dt> <dd>

Type: **[fVector](dx-graphics-hlsl-vector.md)**

The second vector.

</dd> </dl>

## Return value

Type: **[fVector](dx-graphics-hlsl-vector.md)**

The computed distance vector.

## Remarks

This intrinsic function provides the same functionality as the Vertex Shader instruction [dst](dst---vs.md).

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 




