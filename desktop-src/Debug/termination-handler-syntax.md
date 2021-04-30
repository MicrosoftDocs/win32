---
description: The \_\_try and \_\_finally keywords are used to construct a termination handler. The following example shows the structure of a termination handler.
ms.assetid: fbaf8890-2516-4b60-be57-464f91f2a38a
title: Termination-Handler Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Termination-Handler Syntax

The **\_\_try** and **\_\_finally** keywords are used to construct a termination handler. The following example shows the structure of a termination handler.


```C++
__try 
{ 
    // guarded body of code 
 
} 
__finally 
{ 
    // __finally block 
 
}
```



For examples, see [Using a Termination Handler](using-a-termination-handler.md).

As with the exception handler, both the **\_\_try** block and the **\_\_finally** block require braces ({}), and using a **goto** statement to jump into either block is not permitted.

The **\_\_try** block contains the guarded body of code that is protected by the termination handler. A function can have any number of termination handlers, and these termination-handling blocks can be nested within the same function or in different functions.

The **\_\_finally** block is executed whenever the flow of control leaves the **\_\_try** block. However, the **\_\_finally** block is not executed if you call any of the following functions within the **\_\_try** block: [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess), [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread), or **abort**.

The **\_\_finally** block is executed in the context of the function in which the termination handler is located. This means that the **\_\_finally** block can access that function's local variables. Execution of the **\_\_finally** block can terminate by any of the following means.

-   Execution of the last statement in the block and continuation to the next instruction
-   Use of a control statement (**return**, **break**, **continue**, or **goto**)
-   Use of **longjmp** or a jump to an exception handler

If execution of the **\_\_try** block terminates because of an exception that invokes the exception-handling block of a frame-based exception handler, the **\_\_finally** block is executed before the exception-handling block is executed. Similarly, a call to the **longjmp** C run-time library function from the **\_\_try** block causes execution of the **\_\_finally** block before execution resumes at the target of the **longjmp** operation. If **\_\_try** block execution terminates due to a control statement (**return**, **break**, **continue**, or **goto**), the **\_\_finally** block is executed.

The [**AbnormalTermination**](abnormaltermination.md) function can be used within the **\_\_finally** block to determine whether the **\_\_try** block terminated sequentially — that is, whether it reached the closing brace (}). Leaving the **\_\_try** block because of a call to **longjmp**, a jump to an exception handler, or a **return**, **break**, **continue**, or **goto** statement, is considered an abnormal termination. Note that failure to terminate sequentially causes the system to search through all stack frames in reverse order to determine whether any termination handlers must be called. This can result in performance degradation due to the execution of hundreds of instructions.

To avoid abnormal termination of the termination handler, execution should continue to the end of the block. You can also execute the **\_\_leave** statement. The **\_\_leave** statement allows for immediate termination of the **\_\_try** block without causing abnormal termination and its performance penalty. Check your compiler documentation to determine if the **\_\_leave** statement is supported.

If execution of the **\_\_finally** block terminates because of the **return** control statement, it is equivalent to a **goto** to the closing brace in the enclosing function. Therefore, the enclosing function will return.

 

 
