---
description: Indicates whether the \_\_try block of a termination handler terminated normally. The function can be called only from within the \_\_finally block of a termination handler.
ms.assetid: 0ddaef1f-03f0-45fc-9c5e-8d6a26a73245
title: AbnormalTermination macro
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AbnormalTermination
api_type: 
- NA
api_location: 
---

# AbnormalTermination macro

Indicates whether the **\_\_try** block of a termination handler terminated normally. The function can be called only from within the **\_\_finally** block of a termination handler.

> [!Note]  
> The Microsoft C/C++ Optimizing Compiler interprets this function as a keyword, and its use outside the appropriate exception-handling syntax generates a compiler error.

 

## Syntax


```C++
BOOL AbnormalTermination(void);
```



## Parameters

This macro has no parameters.

## Return value

If the **\_\_try** block terminated abnormally, the return value is nonzero.

If the **\_\_try** block terminated normally, the return value is zero.

## Remarks

The **\_\_try** block terminates normally only if execution leaves the block sequentially after executing the last statement in the block. Statements (such as **return**, **goto**, **continue**, or **break**) that cause execution to leave the **\_\_try** block result in abnormal termination of the block. This is the case even if such a statement is the last statement in the **\_\_try** block.

Abnormal termination of a **\_\_try** block causes the system to search backward through all stack frames to determine whether any termination handlers must be called. This can result in the execution of hundreds of instructions, so it is important to avoid abnormal termination of a **\_\_try** block due to a **return**, **goto**, **continue**, or **break** statement. Note that these statements do not generate an exception, even though the termination is abnormal.

To avoid abnormal termination, execution should continue to the end of the block. You can also execute the **\_\_leave** statement. The **\_\_leave** statement allows for immediate termination of the **\_\_try** block without causing abnormal termination and its performance penalty. Check your compiler documentation to determine if the **\_\_leave** statement is supported.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Structured Exception Handling Functions](structured-exception-handling-functions.md)
</dt> <dt>

[Structured Exception Handling Overview](structured-exception-handling.md)
</dt> </dl>

 

 




