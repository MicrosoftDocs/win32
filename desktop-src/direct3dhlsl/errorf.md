---
title: errorf function
description: Submits an error message to the information queue.
ms.assetid: bf4dc6dc-b36e-4b71-ad61-b7a5ba332879
keywords:
- errorf function HLSL
topic_type:
- apiref
api_name:
- errorf
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# errorf function

Submits an error message to the information queue.

## Syntax

``` syntax
void errorf(
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

 

 




