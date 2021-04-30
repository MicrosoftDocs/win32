---
description: This section describes the syntax and usage of structured exception handling as implemented in the Microsoft C/C++ Optimizing Compiler. The following keywords are interpreted by the compiler as part of the structured exception-handling mechanism.
ms.assetid: '22190b75-417c-49d3-83fe-546018fb61ea'
title: Handler Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Handler Syntax

This section describes the syntax and usage of structured exception handling as implemented in the Microsoft C/C++ Optimizing Compiler. The following keywords are interpreted by the compiler as part of the structured exception-handling mechanism.



| Keyword         | Description                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\_\_try**     | Begins a guarded body of code. Used with the **\_\_except** keyword to construct an [exception handler](exception-handler-syntax.md), or with the **\_\_finally** keyword to construct a [termination handler](termination-handler-syntax.md). |
| **\_\_except**  | Begins a block of code that is executed only when an exception occurs within its associated **\_\_try** block.                                                                                                                                   |
| **\_\_finally** | Begins a block of code that is executed whenever the flow of control leaves its associated **\_\_try** block.                                                                                                                                    |
| **\_\_leave**   | Allows for immediate termination of the **\_\_try** block without causing abnormal termination and its performance penalty.                                                                                                                      |



 

The compiler also interprets the [**GetExceptionCode**](getexceptioncode.md), [**GetExceptionInformation**](getexceptioninformation.md), and [**AbnormalTermination**](abnormaltermination.md) functions as keywords, and their use outside the appropriate exception-handling syntax generates a compiler error. The following are brief descriptions of these functions.



| Function                                                   | Description                                                                                                                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetExceptionCode**](getexceptioncode.md)               | Returns a code that identifies the type of exception. This function can be called only from within the filter expression or the exception-handler block.                                                                                                |
| [**GetExceptionInformation**](getexceptioninformation.md) | Returns a pointer to an [**EXCEPTION\_POINTERS**](/windows/desktop/api/WinNT/ns-winnt-exception_pointers) structure containing pointers to the context record and the exception record. This function can be called only from within the filter expression of an exception handler. |
| [**AbnormalTermination**](abnormaltermination.md)         | Indicates whether the flow of control left the associated **\_\_try** block sequentially after executing the last statement in the block. This function can be called only from within the **\_\_finally** block of a termination handler.              |



 

 

 



