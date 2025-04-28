---
description: The following examples demonstrate the use of an exception handler.
ms.assetid: c3b4e696-9f45-4616-ac6b-07ba29750bb2
title: Using an Exception Handler
ms.topic: concept-article
ms.date: 05/31/2018
---

# Using an Exception Handler

The following examples demonstrate the use of an exception handler.

Some of the examples use the [**GetExceptionCode**](getexceptioncode.md) function within the **\_\_except** filter expression to check the exception type before executing the handler. This enables the system to continue its search for an appropriate handler if some other type of exception occurs.

In general, only return EXCEPTION\_EXECUTE\_HANDLER from an exception filter when the exception type is expected and the faulting address is known. You should allow the default exception handler to process unexpected exception types and faulting addresses.

## Example 1

The following code fragment uses structured exception handling to check whether a division operation on two 32-bit integers will result in an division-by-zero error. If this occurs, the function returns **FALSE**— otherwise it returns **TRUE**.


```C++
BOOL SafeDiv(INT32 dividend, INT32 divisor, INT32 *pResult)
{
    __try 
    { 
        *pResult = dividend / divisor; 
    } 
    __except(GetExceptionCode() == EXCEPTION_INT_DIVIDE_BY_ZERO ? 
             EXCEPTION_EXECUTE_HANDLER : EXCEPTION_CONTINUE_SEARCH)
    { 
        return FALSE;
    }
    return TRUE;
} 
```



## Example 2

The following example function calls the [**DebugBreak**](/windows/win32/api/debugapi/nf-debugapi-debugbreak) function and uses structured exception handling to check for a breakpoint exception. If one occurs, that means that the exception was not handled by a debugger, and the function returns **FALSE**— otherwise it returns **TRUE**.


```C++
BOOL CheckForDebugger()
{
    __try 
    {
        DebugBreak();
    }
    __except(GetExceptionCode() == EXCEPTION_BREAKPOINT ? 
             EXCEPTION_EXECUTE_HANDLER : EXCEPTION_CONTINUE_SEARCH) 
    {
        // No debugger is attached, so return FALSE 
        // and continue.
        return FALSE;
    }
    return TRUE;
}
```



## Example 3

The following example shows the interaction of nested handlers. The [**RaiseException**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-raiseexception) function causes an exception in the guarded body of a termination handler that is inside the guarded body of an exception handler. The exception causes the system to evaluate the FilterFunction function, whose return value in turn causes the exception handler to be invoked. However, before the exception-handler block is executed, the **\_\_finally** block of the termination handler is executed because the flow of control has left the **\_\_try** block of the termination handler.


```C++
DWORD FilterFunction() 
{ 
    printf("1 ");                     // printed first 
    return EXCEPTION_EXECUTE_HANDLER; 
} 
 
VOID main(VOID) 
{ 
    __try 
    { 
        __try 
        { 
            RaiseException( 
                1,                    // exception code 
                0,                    // continuable exception 
                0, NULL);             // no arguments 
        } 
        __finally 
        { 
            printf("2 ");             // this is printed second 
        } 
    } 
    __except ( FilterFunction() ) 
    { 
        printf("3\n");                // this is printed last 
    } 
}
```



 

 
