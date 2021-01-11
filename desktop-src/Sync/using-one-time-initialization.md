---
description: The following examples demonstrate the use of the one-time initialization functions.
ms.assetid: 47e68fbb-29f8-4930-beba-01d44263eb1e
title: Using One-Time Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Using One-Time Initialization

The following examples demonstrate the use of the one-time initialization functions.

## Synchronous Example

In this example, the `g_InitOnce` global variable is the one-time initialization structure. It is initialized statically using **INIT\_ONCE\_STATIC\_INIT**.

The `OpenEventHandleSync` function returns a handle to an event that is created only once. It calls the [**InitOnceExecuteOnce**](/windows/win32/api/synchapi/nf-synchapi-initonceexecuteonce) function to execute the initialization code contained in the `InitHandleFunction` callback function. If the callback function succeeds, `OpenEventHandleSync` returns the event handle returned in *lpContext*; otherwise, it returns **INVALID\_HANDLE\_VALUE**.

The `InitHandleFunction` function is the [one-time initialization callback function](/windows/win32/api/synchapi/nc-synchapi-pinit_once_fn). `InitHandleFunction` calls the [**CreateEvent**](/windows/win32/api/synchapi/nf-synchapi-createeventa) function to create the event and returns the event handle in the *lpContext* parameter.


```C++
#define _WIN32_WINNT 0x0600
#include <windows.h>

// Global variable for one-time initialization structure
INIT_ONCE g_InitOnce = INIT_ONCE_STATIC_INIT; // Static initialization

// Initialization callback function 
BOOL CALLBACK InitHandleFunction (
    PINIT_ONCE InitOnce,        
    PVOID Parameter,            
    PVOID *lpContext);           

// Returns a handle to an event object that is created only once
HANDLE OpenEventHandleSync()
{
  PVOID lpContext;
  BOOL  bStatus;
  
  // Execute the initialization callback function 
  bStatus = InitOnceExecuteOnce(&g_InitOnce,          // One-time initialization structure
                                InitHandleFunction,   // Pointer to initialization callback function
                                NULL,                 // Optional parameter to callback function (not used)
                                &lpContext);          // Receives pointer to event object stored in g_InitOnce

  // InitOnceExecuteOnce function succeeded. Return event object.
  if (bStatus)
  {
    return (HANDLE)lpContext;
  }
  else
  {
    return (INVALID_HANDLE_VALUE);
  }
}

// Initialization callback function that creates the event object 
BOOL CALLBACK InitHandleFunction (
    PINIT_ONCE InitOnce,        // Pointer to one-time initialization structure        
    PVOID Parameter,            // Optional parameter passed by InitOnceExecuteOnce            
    PVOID *lpContext)           // Receives pointer to event object           
{
  HANDLE hEvent;

  // Create event object
  hEvent = CreateEvent(NULL,    // Default security descriptor
                       TRUE,    // Manual-reset event object
                       TRUE,    // Initial state of object is signaled 
                       NULL);   // Object is unnamed

  // Event object creation failed.
  if (NULL == hEvent)
  {
    return FALSE;
  }
  // Event object creation succeeded.
  else
  {
    *lpContext = hEvent;
    return TRUE;
  }
}
```



## Asynchronous Example

In this example, the `g_InitOnce` global variable is the one-time initialization structure. It is initialized statically using **INIT\_ONCE\_STATIC\_INIT**.

The `OpenEventHandleAsync` function returns a handle to an event that is created only once. `OpenEventHandleAsync` calls the [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) function to enter the initializing state.

If the call succeeds, the code checks the value of the *fPending* parameter to determine whether to create the event or simply return a handle to the event created by another thread. If *fPending* is **FALSE**, initialization has already completed so `OpenEventHandleAsync` returns the event handle returned in the *lpContext* parameter. Otherwise, it calls the [**CreateEvent**](/windows/win32/api/synchapi/nf-synchapi-createeventa) function to create the event and the [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) function to complete the initialization.

If the call to [**InitOnceComplete**](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) succeeds, `OpenEventHandleAsync` returns the new event handle. Otherwise, it closes the event handle and calls [**InitOnceBeginInitialize**](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) with **INIT\_ONCE\_CHECK\_ONLY** to determine whether initialization failed or was completed by another thread.

If the initialization was completed by another thread, `OpenEventHandleAsync` returns the event handle returned in *lpContext*. Otherwise, it returns **INVALID\_HANDLE\_VALUE**.


```C++
#define _WIN32_WINNT 0x0600
#include <windows.h>

// Global variable for one-time initialization structure
INIT_ONCE g_InitOnce = INIT_ONCE_STATIC_INIT; // Static initialization

// Returns a handle to an event object that is created only once
HANDLE OpenEventHandleAsync()
{
  PVOID  lpContext;
  BOOL   fStatus;
  BOOL   fPending;
  HANDLE hEvent;
  
  // Begin one-time initialization
  fStatus = InitOnceBeginInitialize(&g_InitOnce,       // Pointer to one-time initialization structure
                                    INIT_ONCE_ASYNC,   // Asynchronous one-time initialization
                                    &fPending,         // Receives initialization status
                                    &lpContext);       // Receives pointer to data in g_InitOnce  

  // InitOnceBeginInitialize function failed.
  if (!fStatus)
  {
    return (INVALID_HANDLE_VALUE);
  }

  // Initialization has already completed and lpContext contains event object.
  if (!fPending)
  {
    return (HANDLE)lpContext;
  }

  // Create event object for one-time initialization.
  hEvent = CreateEvent(NULL,    // Default security descriptor
                       TRUE,    // Manual-reset event object
                       TRUE,    // Initial state of object is signaled 
                       NULL);   // Object is unnamed

  // Event object creation failed.
  if (NULL == hEvent)
  {
    return (INVALID_HANDLE_VALUE);
  }

  // Complete one-time initialization.
  fStatus = InitOnceComplete(&g_InitOnce,             // Pointer to one-time initialization structure
                             INIT_ONCE_ASYNC,         // Asynchronous initialization
                             (PVOID)hEvent);          // Pointer to event object to be stored in g_InitOnce

  // InitOnceComplete function succeeded. Return event object.
  if (fStatus)
  {
    return hEvent;
  }
  
  // Initialization has already completed. Free the local event.
  CloseHandle(hEvent);


  // Retrieve the final context data.
  fStatus = InitOnceBeginInitialize(&g_InitOnce,            // Pointer to one-time initialization structure
                                    INIT_ONCE_CHECK_ONLY,   // Check whether initialization is complete
                                    &fPending,              // Receives initialization status
                                    &lpContext);            // Receives pointer to event object in g_InitOnce
  
  // Initialization is complete. Return handle.
  if (fStatus && !fPending)
  {
    return (HANDLE)lpContext;
  }
  else
  {
    return INVALID_HANDLE_VALUE;
  }
}
```



## Related topics

<dl> <dt>

[One-Time Initialization](one-time-initialization.md)
</dt> </dl>

 

 
