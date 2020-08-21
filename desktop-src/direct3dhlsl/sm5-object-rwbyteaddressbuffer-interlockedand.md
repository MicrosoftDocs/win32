---
title: RWByteAddressBuffer::InterlockedAnd function
description: Ands the value, atomically.
ms.assetid: c4024be0-3884-4af9-8075-76774c7c6178
keywords:
- InterlockedAnd function HLSL
topic_type:
- apiref
api_name:
- InterlockedAnd
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InterlockedAnd function

Ands the value, atomically.

## Syntax

``` syntax
void InterlockedAnd(
  in  UINT dest,
  in  UINT value,
  out UINT original_value
);
```

## Parameters

<dl> <dt>

*dest* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The destination address.

</dd> <dt>

*value* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The input value.

</dd> <dt>

*original\_value* \[out\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The original value.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This operation can only be performed on int or uint typed resources and shared memory variables. There are three possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs an atomic and of value to the shared memory register referenced by dest. The second scenario is when R is a resource variable type. In this scenario, the function performs an atomic and of value to the resource location referenced by dest. Finally, the third scenario is when R is a local variable type. In this scenario, the function reduces to an and of the value of dest and value, stored in dest. The overloaded function has an additional output variable which will be set to the original value of dest. This overloaded operation is only available when R is readable and writable.

This function is supported in the following types of shaders:



| VS  | HS  | DS  | GS  | PS  | CS  |
|-----|-----|-----|-----|-----|-----|
| x   | x   |  x  | x   | x   | x   |



 

## See also

<dl> <dt>

[RWByteAddressBuffer](sm5-object-rwbyteaddressbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 