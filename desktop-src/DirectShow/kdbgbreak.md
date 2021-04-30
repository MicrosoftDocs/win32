---
description: Causes a breakpoint exception, and logs the specified string using the DbgLog macro. Ignored in retail builds.
ms.assetid: 475810db-692b-4727-9ef1-ece74e9618d0
title: KDbgBreak macro (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KDbgBreak
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
---

# KDbgBreak macro

Causes a breakpoint exception, and logs the specified string using the [**DbgLog**](dbglog.md) macro. Ignored in retail builds.

## Syntax


```C++
void KDbgBreak(
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

## Remarks

Unlike the [**DbgBreak**](dbgbreak.md) macro, this macro does not display a message box prompting the user. In debug builds, it automatically causes a breakpoint exception to occur.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




