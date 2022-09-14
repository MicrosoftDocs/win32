---
description: Assert and Breakpoint Macros
ms.assetid: c34db182-1f65-4a2f-9534-268638c2502d
title: Assert and Breakpoint Macros
ms.topic: article
ms.date: 05/31/2018
---

# Assert and Breakpoint Macros

The [DirectShow Base Classes](directshow-base-classes.md) provide several macros that perform asserts or cause breakpoints.



| Macro                                        | Description                                                                                                                        |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**ASSERT**](assert.md)                     | Evaluates an expression, and displays a diagnostic message if the expression is **FALSE**.                                         |
| [**DbgAssertAligned**](dbgassertaligned.md) | Tests whether a pointer is aligned to a specified boundary.                                                                        |
| [**DbgBreak**](dbgbreak.md)                 | Displays a message box with the specified string, the name of the source file, and the line number.                                |
| [**EXECUTE\_ASSERT**](execute-assert.md)    | Evaluates an expression in debug and retail builds. In debug builds, displays a diagnostic message if the expression is **FALSE**. |
| [**KASSERT**](kassert.md)                   | Evaluates an expression, and causes a breakpoint exception if the expression is **FALSE**.                                         |
| [**KDbgBreak**](kdbgbreak.md)               | Causes a breakpoint exception, and logs the specified string.                                                                      |



 

## Related topics

<dl> <dt>

[Debugging Utilities](debugging-utilities.md)
</dt> </dl>

 

 



