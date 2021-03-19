---
description: Verifies that the calling process has read access to a string. If not, the macro calls the DbgBreak macro.
ms.assetid: 749a8c22-7a4a-49c2-a214-fc64dc5a0202
title: ValidateStringPtr macro (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ValidateReadPtr
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
---

# ValidateStringPtr macro

Verifies that the calling process has read access to a string. If not, the macro calls the [**DbgBreak**](dbgbreak.md) macro.

> [!Note]  
> This macro is deprecated. In the Windows SDK for Windows Vista (and later) this macro does not do anything.

 

## Syntax


```C++
void ValidateReadPtr(
   LPCTSTR p
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Pointer to a NULL-terminated **TCHAR** string.

</dd> </dl>

## Return value

This macro does not return a value.

## Remarks

This macro is ignored unless DEBUG, \_DEBUG, or VFWROBUST is defined when the DirectShow base-class header file is included. This macro can have a significant performance cost.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Pointer Validation Macros](pointer-validation-macros.md)
</dt> </dl>

 

 




