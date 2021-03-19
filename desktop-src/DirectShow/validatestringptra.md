---
description: Verifies that the calling process has read access to an ANSI string. If not, the macro calls the DbgBreak macro.
ms.assetid: 44be67f8-9896-4360-82de-083a5f28a3d0
title: ValidateStringPtrA macro (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ValidateStringPtrA
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
---

# ValidateStringPtrA macro

Verifies that the calling process has read access to an ANSI string. If not, the macro calls the [**DbgBreak**](dbgbreak.md) macro.

> [!Note]  
> This macro is deprecated. In the Windows SDK for Windows Vista (and later) this macro does not do anything.

 

## Syntax


```C++
void ValidateStringPtrA(
   LPCSTR p
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Pointer to a NULL-terminated ANSI string.

</dd> </dl>

## Return value

This macro does not return a value.

## Remarks

This macro is ignored unless DEBUG, \_DEBUG, or VFWROBUST is defined when the DirectShow base-class header file is included.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Pointer Validation Macros](pointer-validation-macros.md)
</dt> </dl>

 

 




