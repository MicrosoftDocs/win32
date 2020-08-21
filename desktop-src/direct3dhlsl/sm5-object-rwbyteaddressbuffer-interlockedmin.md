---
title: RWByteAddressBuffer::InterlockedMin function
description: Finds the minimum value, atomically.
ms.assetid: bf650b2e-9c6c-4458-9565-1e9ec76a1472
keywords:
- InterlockedMin function HLSL
topic_type:
- apiref
api_name:
- InterlockedMin
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InterlockedMin function

Finds the minimum value, atomically.

## Syntax

``` syntax
void InterlockedMin(
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

Nothing

## Remarks

This operation can only be performed on int and uint typed resources and shared memory variables. There are three possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs an atomic minimum of the value to the shared memory register referenced by dest. The second scenario is when R is a resource variable type. In this scenario, the function performs an atomic minimum of the value to the resource location referenced by dest. Finally, the third scenario is when R is a local variable type. In this scenario, the function reduces to a minimum of the value of dest and value, stored in dest. The overloaded function has an additional output variable which will be set to the original value of dest. This overloaded operation is only available when R is readable and writable.

This function is supported in the following types of shaders:



| VS  | HS  | DS  | GS  | PS  | CS  |
|-----|-----|-----|-----|-----|-----|
| x   |  x  | x   | x   | x   | x   |



 

## See also

<dl> <dt>

[RWByteAddressBuffer](sm5-object-rwbyteaddressbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 