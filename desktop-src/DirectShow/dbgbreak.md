---
description: Displays a message box with the specified string, the name of the source file, and the line number. The user can ignore the message, enter the debugger, or quit the application. Ignored in retail builds.
ms.assetid: ac4da7da-f9d0-44ae-9ad1-9a5908b288fb
title: DbgBreak macro (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgBreak
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
---

# DbgBreak macro

Displays a message box with the specified string, the name of the source file, and the line number. The user can ignore the message, enter the debugger, or quit the application. Ignored in retail builds.

## Syntax


```C++
void DbgBreak(
    strLiteral
);
```



## Parameters

<dl> <dt>

*strLiteral* 
</dt> <dd>

Text string.

</dd> </dl>

## Return value

This macro does not return a value.

## Examples


```C++
DbgBreak("Unrecoverable error occurred.");
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




