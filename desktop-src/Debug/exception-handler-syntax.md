---
description: The \_\_try and \_\_except keywords are used to construct a frame-based exception handler. The following example shows the structure of an exception handler.
ms.assetid: 1ea2c7f7-f920-4c72-bc62-4eb5e8d70790
title: Exception-Handler Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Exception-Handler Syntax

The **\_\_try** and **\_\_except** keywords are used to construct a frame-based exception handler. The following example shows the structure of an exception handler.


```C++
__try 
{
    // guarded body of code 
 
} 
__except (filter-expression) 
{ 
    // exception-handler block 
 
}
```



Note that the **\_\_try** block and the exception-handler block require braces ({}). Using a **goto** statement to jump into the body of a **\_\_try** block or into an exception-handler block is not permitted. This rule applies to both exception handlers and termination handlers.

The **\_\_try** block contains the guarded body of code that the exception handler protects. A function can have any number of exception handlers, and these exception-handling statements can be nested within the same function or in different functions. If an exception occurs within the **\_\_try** block, the system takes control and begins the search for an exception handler. For a detailed description of this search, see [Exception Handling](exception-handling.md).

The exception handler receives only exceptions that occur within a single thread. This means that if a **\_\_try** block contains a call to the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) or [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread) function, exceptions that occur within the new process or thread are not dispatched to this handler.

The system evaluates the filter expression of each exception handler guarding the code in which the exception occurred until either the exception is handled or there are no more handlers. A filter expression must be evaluated as one of the three following values.



| Value                              | Meaning                                                                                                                                                                                                                |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EXCEPTION\_EXECUTE\_HANDLER**    | The system transfers control to the exception handler, and execution continues in the stack frame in which the handler is found.                                                                                       |
| **EXCEPTION\_CONTINUE\_SEARCH**    | The system continues to search for a handler.                                                                                                                                                                          |
| **EXCEPTION\_CONTINUE\_EXECUTION** | The system stops its search for a handler and returns control to the point at which the exception occurred. If the exception is noncontinuable, this results in an **EXCEPTION\_NONCONTINUABLE\_EXCEPTION** exception. |



 

The filter expression is evaluated in the context of the function in which the exception handler is located, even though the exception may have occurred in a different function. This means that the filter expression can access the function's local variables. Similarly, the exception-handler block can access the local variables of the function in which it is located.

For more examples, see [Using an Exception Handler](using-an-exception-handler.md).

For more information about filter expressions and filter functions, see [Frame-based Exception Handling](frame-based-exception-handling.md).

 

 
