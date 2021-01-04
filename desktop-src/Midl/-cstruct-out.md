---
title: /cstruct_out switch
description: The /cstruct_out switch modifies the C definition of a COM interface which returns structures to match the ABI a C++ implementer would provide.
keywords:
- /cstruct_out switch MIDL
topic_type:
- apiref
api_name:
- /cstruct_out
api_type:
- NA
ms.topic: reference
ms.date: 12/10/2020
---

# /cstruct\_out switch

This switch modifies the C definition of a COM interface which returns structures to match the ABI a C++ implementer would provide.

``` syntax
midl /cstruct_out
```

## Switch Options

This switch has no parameters.

## Remarks

Some interface definitions (notably those in `d3d12.idl`) contain `__stdcall` methods that return structures. The C and C++ ABIs from MSVC differ in how they implement such functions:

* C treats them as plain functions that take a hidden `this` pointer as the first parameter. The complier applies a small struct optimization that allows structs smaller than 8 bytes (or larger if all values are floating point) to be returned in registers. Only larger structures are promoted to use a hidden parameter and caller-allocated return value.
* C++ treats them as member functions. The compiler *always* does so by inserting a hidden parameter (a pointer to a caller-allocated return value) as the second parameter, after the `this` pointer. It also returns that same pointer as its return value.

This switch forces the C definition of interfaces in the resulting header to assume that the implementer was using C++, and that the C code should instead explicitly use the C++ ABI. This implies that the function includes a hidden parameter for the return value pointer and returns that pointer instead of the structure directly.

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>
