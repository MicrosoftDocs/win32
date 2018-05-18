---
Description: 'Evaluates an expression, and displays a diagnostic message if the expression is FALSE. Ignored in retail builds.'
ms.assetid: '8c3815bb-3164-4066-a947-974e791af5cd'
title: ASSERT macro
---

# ASSERT macro

Evaluates an expression, and displays a diagnostic message if the expression is **FALSE**. Ignored in retail builds.

## Syntax


```C++
void ASSERT(
   BOOL cond
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

In debug builds, if the expression is **FALSE**, this macro displays a message box with the text of the expression, the name of the source file, and the line number. The user can ignore the assertion, enter the debugger, or quit the application.

## Examples


```
ASSERT(rtStartTime <= rtEndTime);
```



## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




