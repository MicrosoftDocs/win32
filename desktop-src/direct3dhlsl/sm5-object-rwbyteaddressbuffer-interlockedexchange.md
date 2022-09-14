---
title: RWByteAddressBuffer::InterlockedExchange function
description: Exchanges a value, atomically.
ms.assetid: a50f4cba-a7a2-44b0-9de7-003b4c7a947f
keywords:
- InterlockedExchange function HLSL
topic_type:
- apiref
api_name:
- InterlockedExchange
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InterlockedExchange function

Exchanges a value, atomically.

## Syntax

``` syntax
void InterlockedExchange(
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

This operation can only be performed on scalar-typed resources and shared memory variables. There are three possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs the operation on the shared memory register referenced by dest. The second scenario is when R is a resource variable type. In this scenario, the function performs the operation on the resource location referenced by dest. Finally, the third scenario is when R is a local variable type. In this scenario, the function reduces to the operation performed using local operations. This operation is only available when R is readable and writable.

This function is supported in the following types of shaders:



| VS  | HS  | DS  | GS  | PS  | CS  |
|-----|-----|-----|-----|-----|-----|
|  x  |  x  |  x  |  x  | x   | x   |



 

## See also

<dl> <dt>

[RWByteAddressBuffer](sm5-object-rwbyteaddressbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 