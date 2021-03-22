---
description: Evaluates an expression, and causes a breakpoint exception if the expression is FALSE. The text of the expression, the name of the source file, and the line number are logged using the DbgLog macro. Ignored in retail builds.
ms.assetid: fd116403-df23-490f-b3a8-b2a8bf2b4a5f
title: KASSERT macro (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KASSERT
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
---

# KASSERT macro

Evaluates an expression, and causes a breakpoint exception if the expression is **FALSE**. The text of the expression, the name of the source file, and the line number are logged using the [**DbgLog**](dbglog.md) macro. Ignored in retail builds.

## Syntax


```C++
void KASSERT(
    cond
);
```



## Parameters

<dl> <dt>

*cond* 
</dt> <dd>

Expression to evaluate.

</dd> </dl>

## Return value

This macro does not return a value.

## Remarks

Unlike the [**ASSERT**](assert.md) and [**EXECUTE\_ASSERT**](execute-assert.md) macros, this macro does not display a message box prompting the user. In debug builds, if the expression is **FALSE**, the macro automatically causes a breakpoint exception to occur.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




