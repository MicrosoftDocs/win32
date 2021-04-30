---
description: A frame-based exception handler allows you to deal with the possibility that an exception may occur in a certain sequence of code. A frame-based exception handler consists of the following elements.
ms.assetid: 07aac772-f917-48b7-91a9-3b5d4cb43600
title: Frame-based Exception Handling
ms.topic: article
ms.date: 05/31/2018
---

# Frame-based Exception Handling

A *frame-based exception handler* allows you to deal with the possibility that an exception may occur in a certain sequence of code. A frame-based exception handler consists of the following elements.

-   A guarded body of code
-   A filter expression
-   An exception-handler block

Frame-based exception handlers are declared in language-specific syntax. For example, in the Microsoft C/C++ Optimizing Compiler, they are implemented using **\_\_try** and **\_\_except**. For more information, see [Handler Syntax](handler-syntax.md).

The *guarded body of code* is a set of one or more statements for which the filter expression and the exception-handler block provide exception-handling protection. The guarded body can be a block of code, a set of nested blocks, or an entire procedure or function. Using the Microsoft C/C++ Optimizing Compiler, a guarded body is enclosed by braces ({}) following the **\_\_try** keyword.

The *filter expression* of a frame-based exception handler is an expression that is evaluated by the system when an exception occurs within the guarded body. This evaluation results in one of the following actions by the system.

-   The system stops its search for an exception handler, restores the machine state, and continues thread execution at the point at which the exception occurred.
-   The system continues its search for an exception handler.
-   The system transfers control to the exception handler, and thread execution continues sequentially in the stack frame in which the exception handler is found. If the handler is not in the stack frame in which the exception occurred, the system unwinds the stack, leaving the current stack frame and any other stack frames until it is back to the exception handler's stack frame. Before an exception handler is executed, termination handlers are executed for any guarded bodies of code that terminated as a result of the transfer of control to the exception handler. For more information about termination handlers, refer to [Termination Handling](termination-handling.md).

The filter expression can be a simple expression, or it can invoke a *filter function* that attempts to handle the exception. You can call the [**GetExceptionCode**](getexceptioncode.md) and [**GetExceptionInformation**](getexceptioninformation.md) functions from within a filter expression to get information about the exception being filtered. **GetExceptionCode** returns a code that identifies the type of exception, and **GetExceptionInformation** returns a pointer to an [**EXCEPTION\_POINTERS**](/windows/desktop/api/WinNT/ns-winnt-exception_pointers) structure that contains pointers to [**CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-arm64_nt_context) and [**EXCEPTION\_RECORD**](/windows/desktop/api/WinNT/ns-winnt-exception_record) structures.

These functions cannot be called from within a filter function, but their return values can be passed as parameters to a filter function. [**GetExceptionCode**](getexceptioncode.md) can be used within the exception-handler block, but [**GetExceptionInformation**](getexceptioninformation.md) cannot because the information it points to is typically on the stack and is destroyed when control is transferred to an exception handler. However, an application can copy the information to safe storage to make it available to the exception handler.

The advantage of a filter function is that it can handle an exception and return a value that causes the system to continue execution from the point at which the exception occurred. With an exception-handler block, in contrast, execution continues sequentially from the exception handler rather than from the point of the exception.

Handling an exception may be as simple as noting an error and setting a flag that will be examined later, printing a warning or error message, or taking some other limited action. If execution can be continued, it may also be necessary to change the machine state by modifying the context record. For an example of a filter function that handles a page fault exception, see [Using the Virtual Memory Functions](../memory/using-the-memory-management-functions.md).

The [**UnhandledExceptionFilter**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-unhandledexceptionfilter) function can be used as a filter function in a filter expression. It returns EXCEPTION\_EXECUTE\_HANDLER unless the process is being debugged, in which case it returns EXCEPTION\_CONTINUE\_SEARCH.

 

 
