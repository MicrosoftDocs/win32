---
title: InterlockedOr function
description: Performs an atomic OR on the value.
ms.assetid: 3a05619b-db97-4cf1-af3c-12c376e605a6
keywords:
- InterlockedOr function HLSL
topic_type:
- apiref
api_name:
- InterlockedOr
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# InterlockedOr function

Performs an atomic **OR** on the value.

## Syntax

``` syntax
void InterlockedOr(
  in  UINT dest,
  in  UINT value,
  out UINT original_value
);
```

## Parameters

<dl> <dt>

*dest* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The destination address.

</dd> <dt>

*value* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The input value.

</dd> <dt>

*original\_value* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The original value.

</dd> </dl>

## Return value

Nothing

## Remarks

This operation can be performed only on **INT** or **UINT** typed resources and shared memory variables. There are three possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs an atomic **OR** with the value of the shared memory register referenced by *dest*. The second scenario is when R is a resource variable type. In this scenario, the function performs an atomic **OR** with the value of the resource location referenced by *dest*. Finally, the third scenario is when R is a local variable type. In this scenario, the function reduces to an **OR** with the values of *dest* and *value*. The result of the operation replaces the value of *dest*. The overloaded function has an additional output variable, which will be set to the original value of *dest*. This overloaded operation is available only when R is readable and writable.

This function is supported in the following types of shaders:



| VS  | HS  | DS  | GS  | PS  | CS  |
|-----|-----|-----|-----|-----|-----|
|     |     |     |     | x   | x   |



 

## See also

<dl> <dt>

[RWByteAddressBuffer](sm5-object-rwbyteaddressbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




