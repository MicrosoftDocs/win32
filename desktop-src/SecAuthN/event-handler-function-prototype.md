---
description: Event Handler Prototype functions are used for all functions that handle Winlogon notification events.
ms.assetid: 99b91e80-5e4e-4119-89aa-c0a80fce69e3
title: Event Handler Function Prototype callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Event_Handler_Function_Name
api_type: 
- UserDefined
api_location: 
---

# Event Handler Function Prototype callback function

\[Event Handler Prototype functions are no longer available for use as of Windows Server 2008 and Windows Vista. \]

Event Handler Prototype functions are used for all functions that handle [*Winlogon*](/windows/desktop/SecGloss/w-gly) notification events. The name of the function, represented below by the place holder *Event\_Handler\_Function\_Name*, typically reflects the name of the event that the function handles. For example, the function that handles logon events might be named: **WLEventLogon**.

## Syntax


```C++
void Event_Handler_Function_Name(
  _In_ PWLX_NOTIFICATION_INFO pInfo
);
```



## Parameters

<dl> <dt>

*pInfo* \[in\]
</dt> <dd>

A pointer to a [**WLX\_NOTIFICATION\_INFO**](/windows/desktop/api/Winwlx/ns-winwlx-wlx_notification_info) structure that contains the details of the event.

</dd> </dl>

## Return value

This callback function does not return a value.

## Remarks

If your event handler needs to create child processes, it should call the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function. Otherwise, the new process will be created on the Winlogon desktop, not the user's desktop.

## Examples

The following sample shows how to implement event handlers for Winlogon events. For simplicity, only the implementations of the Logon and Logoff event handlers are shown. You can implement handlers for the rest of the events in exactly the same manner.


```C++
// Copyright (C) Microsoft. All rights reserved. 
#include <windows.h>

// Here is the entrance function for the DLL.
BOOL WINAPI LibMain(HINSTANCE hInstance, DWORD dwReason, LPVOID lpReserved)
{
    switch (dwReason)
    {
        case DLL_PROCESS_ATTACH:
            {

             // Disable DLL_THREAD_ATTACH & DLL_THREAD_DETACH
             // notification calls. This is a performance optimization
             // for multithreaded applications that do not need 
             // thread-level notifications of attachment or
             // detachment.

            DisableThreadLibraryCalls (hInstance);
            }
            break;
    }

    return TRUE;
}

// Here is the event handler for the Winlogon Logon event.
void WLEventLogon (PWLX_NOTIFICATION_INFO pInfo)
{

    // Print the name of the handler to debug output.
    // You can replace this with more useful functionality.
    OutputDebugString (TEXT("NOTIFY:  Entering WLEventLogon.\r\n"));
}

// Here is the event handler for the Winlogon Logoff event.
void WLEventLogoff (PWLX_NOTIFICATION_INFO pInfo)
{

    // Print the name of the handler to debug output.
    // You can replace this with more useful functionality.
    OutputDebugString (TEXT("NOTIFY:  Entering WLEventLogff.\r\n"));
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



 

