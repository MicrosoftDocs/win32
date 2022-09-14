---
description: Verifies that the calling process has read access to a memory block. If not, the macro calls the DbgBreak macro.
ms.assetid: 1a70e4e5-e144-4cfe-b6be-c0a70aac9ada
title: ValidateReadPtr macro (Wxdebug.h)
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

# ValidateReadPtr macro

Verifies that the calling process has read access to a memory block. If not, the macro calls the [**DbgBreak**](dbgbreak.md) macro.

> [!Note]  
> This macro is deprecated. In the Windows SDK for Windows Vista (and later) this macro does not do anything.

 

## Syntax


```C++
void ValidateReadPtr(
   const void *p,
         UINT cb
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Pointer to a memory block.

</dd> <dt>

*cb* 
</dt> <dd>

Size of the memory block, in bytes.

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

 

 




