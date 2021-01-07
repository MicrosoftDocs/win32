---
description: The interactive nature of telephony requires TAPI to be a real-time operating environment.
ms.assetid: b8512588-ec28-4fbe-b47f-b900e2dba1f2
title: Synchronous/Asynchronous Model
ms.topic: article
ms.date: 05/31/2018
---

# Synchronous/Asynchronous Model

The interactive nature of telephony requires TAPI to be a real-time operating environment. Many of the TAPI functions are required to complete quickly and return their results to the application synchronously. Other functions (such as dialing) may not be able to complete as quickly and therefore operate asynchronously.

Telephony operations complete either synchronously or asynchronously. These two models differ as follows. *Synchronous functions* execute the entire request before the caller's thread is allowed to return from the function call. *Asynchronous functions* return before the request has executed in its entirety. When the asynchronous request later completes, the service provider reports the completion by calling a callback procedure that TAPI originally supplied to it early in the initialization sequence.

-   Asynchronous operations have a parameter named *dwRequestID* of the defined type [DRV\_REQUESTID](./drv-requestid.md) as their first parameter. Such an operation performs part of its processing in the function call and the remainder of its processing in an independent execution thread after the function call has returned. When the function returns, it returns either a negative error result or the (positive) *dwRequestID* that was passed in the function call. The negative error result indicates that the operation is complete (and failed). The positive *dwRequestID* returned indicates that the operation continues in the independent thread. In such a case, the service provider eventually calls the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) procedure, passing the *dwRequestID* and a result code to indicate the outcome of the operation. The result code is zero for success or one of the same set of (negative) error results. In any case, the service provider must never return zero or any positive value other than *dwRequestID* from a function designated as asynchronous because doing so can produce unexpected results. Service providers should always copy input data from application memory into service provider memory before returning from an asynchronous function.
-   Synchronous operations do not have *dwRequestID* as their first parameter. Such an operation performs all of its processing in the caller's execution thread, returning the final result when it returns. The result is zero for success or a negative error code for failure. The service provider does not call [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) for synchronous operations.

It is interesting to consider the timing of a "completion" callback relative to when the original request returns. A typical asynchronous request would be implemented by the service provider as in the following pseudocode:

``` syntax
Some_request(Request_ID, ...) {
  check parameters for validity
  check device state for validity
  store Request_ID for Completion Interrupt Handler's use
  manipulate device registers to start physical operation
  return Request_ID  // to indicate asynch operation
}
Operation Completion Interrupt Handler: {
  if operation was successful then
    call "completion" callback passing Request_ID and "success"
  else
    call "completion" callback passing Request_ID and "error num"
  endif
}
```

If the operation completes very rapidly (or the original request returns very slowly), it is possible that the interrupt handler that runs when a physical operation completes may be triggered before the original request returns to the application or even to TAPI. This behavior is allowed. TAPI guarantees that the eventual completion notification to the application is delivered after the original request returns.

**TAPI 2.x:** Lists which state whether each function completes synchronously or asynchronously appear in [TAPI Quick Function Reference](./tapi-quick-function-reference.md).

 

 
