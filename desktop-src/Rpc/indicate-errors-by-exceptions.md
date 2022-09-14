---
title: Indicate Errors by Exceptions
description: For traditional C programmers, errors are commonly returned through return values, or a special \ out\ parameter that returns the error code.
ms.assetid: 85ee217d-6e0b-4160-9cec-a652c1daa9a0
ms.topic: article
ms.date: 05/31/2018
---

# Indicate Errors by Exceptions

For traditional C programmers, errors are commonly returned through return values, or a special \[out\] parameter that returns the error code. This leads to interfaces implemented the following way:

``` syntax
long sample(...)
{
    ...
    p = new Cbar(...);
    if (p == NULL)
    {
        // cleanup
        ...
        return ERROR_OUTOFMEMORY;
    }
}
```

The problem with this approach is that RPC return values are simply long integers. They have no special meaning as errors (note that [**error\_status\_t**](/windows/desktop/Midl/error-status-t) has no special semantics on the server side), which carries important implications.

First, RPC is not alerted that the operation failed; it attempts to unmarshal all \[in, out\] and \[out\] arguments. The failure semantics of context handles are also different. The packet returned to the client is essentially a success packet, with the error code buried deep in the packet. This also means RPC does not use extended error information, so client software often is unable to discern where the call failed.

Indicating errors in RPC server routines by throwing Structured Exception Handling (SEH) exceptions (not C++) is a much better approach. When an SEH exception is thrown, control goes directly to the RPC run time. An error sometimes occurs deep in a routine that cannot properly clean up, and it needs to indicate an error to its caller. The routine should return an error to its caller, which in turn can return an error to its caller and so on. However, the last server routine on the stack should throw an exception before it returns to RPC to indicate to RPC that an error occurred.

## Related topics

<dl> <dt>

[Exception Handling](exception-handling.md)
</dt> </dl>

 

 