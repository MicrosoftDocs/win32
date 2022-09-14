---
title: abort function (Corecrt\_terminate.h)
description: Submits an error message to the information queue and terminates the current draw or dispatch call being executed.
ms.assetid: b8ce153b-0d1c-4294-b88e-b7e50e708ab9
keywords:
- abort function HLSL
topic_type:
- apiref
api_name:
- abort
api_location:
- corecrt_terminate.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# abort function

Submits an error message to the information queue and terminates the current draw or dispatch call being executed.

## Syntax

``` syntax
void abort(
    
);
```

## Parameters

<dl> <dt>

 
</dt> <dd>

None

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This operation does nothing on rasterizers that do not support it.

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                        | Supported |
|---------------------------------------------------------------------|-----------|
| [Shader Model 4 (DirectX HLSL) or later.](dx-graphics-hlsl-sm3.md) | yes       |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Corecrt\_terminate.h</dt> </dl> |



## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





