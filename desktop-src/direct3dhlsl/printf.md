---
title: printf function
description: Submits a custom shader message to the information queue.
ms.assetid: 0c6c15fc-1da5-4a26-ade0-5a0489e4f564
keywords:
- printf function HLSL
topic_type:
- apiref
api_name:
- printf
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# printf function

Submits a custom shader message to the information queue.

## Syntax

``` syntax
void printf(
   string format,
    argument ...
);
```

## Parameters

<dl> <dt>

*format* 
</dt> <dd>

The format string.

</dd> <dt>

*argument ...* 
</dt> <dd>

Optional arguments.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This operation does nothing on devices that do not support it.

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                        | Supported |
|---------------------------------------------------------------------|-----------|
| [Shader Model 4 (DirectX HLSL) or later.](dx-graphics-hlsl-sm3.md) | yes       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 




