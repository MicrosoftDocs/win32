---
description: Components are often designed to perform initialization tasks when they are first called, rather than when they are loaded.
ms.assetid: 404c083c-7bee-44c2-b8e7-da1901b6ab2f
title: One-Time Initialization
ms.topic: article
ms.date: 05/31/2018
---

# One-Time Initialization

Components are often designed to perform initialization tasks when they are first called, rather than when they are loaded. The one-time initialization functions ensure that this initialization occurs only once, even when multiple threads may attempt the initialization.

**Windows Server 2003 and Windows XP:** Applications must provide their own synchronization for one-time initialization by using the [interlocked functions](interlocked-variable-access.md) or other synchronization mechanism. The one-time initialization functions are available starting with Windows Vista and Windows Server 2008.

The one-time initialization functions provide significant advantages to ensure that only one thread performs the initialization:

-   They are optimized for speed.
-   They create the appropriate barriers on processor architectures that require them.
-   They support both locked and parallel initialization.
-   They avoid internal locking so the code can operate asynchronously or synchronously.

The system manages the initialization process through an opaque **INIT\_ONCE** structure that contains data and state information. The caller allocates this structure and initializes it by either calling [**InitOnceInitialize**](/windows/win32/api/synchapi/nf-synchapi-initonceinitialize) (to initialize the structure dynamically) or assigning the constant **INIT\_ONCE\_STATIC\_INIT** to the structure variable (to initialize the structure statically). Initially, the data stored in the one-time initialization structure is NULL and its state is uninitialized.

One-time initialization structures cannot be shared across processes.

The thread that performs the initialization can optionally set a context that is available to the caller after initialization is complete. The context can be a synchronization object or it can be a value or data structure. If the context is a value, its low-order **INIT\_ONCE\_CTX\_RESERVED\_BITS** must be zero. If the context is a data structure, the data structure must be **DWORD**-aligned. The context is returned to the caller in the *lpContext* output parameter of the [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) or [**InitOnceExecuteOnce**](/windows/win32/api/synchapi/nf-synchapi-initonceexecuteonce) function.

One-time initialization can be performed synchronously or asynchronously. An optional callback function can be used for synchronous one-time initialization.

## Synchronous One-time Initialization

The following steps describe synchronous one-time initialization that does not use a callback function.

1.  The first thread to call the [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) function successfully causes one-time initialization to begin. For synchronous one-time initialization, **InitOnceBeginInitialize** must be called without the **INIT\_ONCE\_ASYNC** flag.
2.  Subsequent threads that attempt initialization are blocked until the first thread either completes initialization or fails. If the first thread fails, the next thread is allowed to attempt the initialization, and so on.
3.  When initialization is finished, the thread calls the [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) function. The thread can optionally create a synchronization object (or other context data) and specify it in the *lpContext* parameter of the **InitOnceComplete** function.
4.  If the initialization succeeds, the state of the one-time initialization structure is changed to initialized and the *lpContext* handle (if any) is stored in the initialization structure. Subsequent initialization attempts return this context data. If the initialization fails, the data is **NULL**.

The following steps describe synchronous one-time initialization that uses a callback function.

1.  The first thread to successfully call the [**InitOnceExecuteOnce**](/windows/win32/api/synchapi/nf-synchapi-initonceexecuteonce) function passes a pointer to an application-defined [*InitOnceCallback*](/windows/win32/api/synchapi/nc-synchapi-pinit_once_fn) callback function and any data required by the callback function. If the call succeeds, the *InitOnceCallback* callback function executes.
2.  Subsequent threads that attempt initialization are blocked until the first thread either completes initialization or fails. If the first thread fails, the next thread is allowed to attempt the initialization, and so on.
3.  When initialization is finished, the callback function returns. The callback function can optionally create a synchronization object (or other context data) and specify it in its *Context* output parameter.
4.  If the initialization succeeds, the state of the one-time initialization structure is changed to initialized and the *Context* handle (if any) is stored in the initialization structure. Subsequent initialization attempts return this context data. If the initialization fails, the data is **NULL**.

## Asynchronous One-time Initialization

The following steps describe asynchronous one-time initialization.

1.  If multiple threads simultaneously attempt to begin initialization by calling [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) with **INIT\_ONCE\_ASYNC**, the function succeeds for all of the threads with the *fPending* parameter set to **TRUE**. Only one thread will actually succeed at initialization; other concurrent attempts do not change the initialization state.
2.  When [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) returns, the *fPending* parameter indicates the initialization status:
    -   If *fPending* is **FALSE**, one thread has succeeded at initialization. Other threads should clean up any context data they have created and use the context data in the *lpContext* output parameter of [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize).
    -   If *fPending* is **TRUE**, initialization has not yet completed and other threads should continue.
3.  Each thread calls the [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) function. The thread can optionally create a synchronization object (or other context data) and specify it in the *lpContext* parameter of **InitOnceComplete**.
4.  When [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) returns, its return value indicates whether the calling thread succeeded at initialization.
    -   If [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) succeeds, the calling thread has succeeded at initialization. The state of the one-time initialization structure is changed to initialized and the *lpContext* handle (if any) is stored in the initialization structure.
    -   If [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) fails, another thread has succeeded at initialization. The calling thread should clean up any context data it has created and call [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) with **INIT\_ONCE\_CHECK\_ONLY** to retrieve any context data stored in the one-time initialization structure.

## Calling One-Time Initialization from multiple sites

One-time initialization guarded by a single **INIT\_ONCE** structure may be performed from mutiple sites; different callback may be passed from each site, and synchronization with and without callback may be mixed. Initialization is still guaranted to perform sucesfully just once.

However, asynchronous and synchronous initialization cannot be mixed: once asynchronous initialization is attempted, attempts to start synchronous initialization would fail.

## Related topics

<dl> <dt>

[Using One-Time Initialization](using-one-time-initialization.md)
</dt> </dl>

 

 
