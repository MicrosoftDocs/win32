---
title: Register For Change Notification
description: The following sample code shows how to register for change notifications in the routing table. The topic \ 0034;Use the Event Notification Callback \ 0034; demonstrates how to utilize those change notifications.
ms.assetid: a311759a-e337-4297-af3d-55e969162b0f
ms.topic: article
ms.date: 05/31/2018
---

# Register For Change Notification

The following sample code shows how to register for change notifications in the routing table. The topic "[Use the Event Notification Callback](use-the-event-notification-callback.md)" demonstrates how to utilize those change notifications.


```C++
#include <windows.h>
#include <stdio.h>
#include "Rtmv2.h"
#include "nldef.h"
#include <tchar.h>

// The following #defines are from routprot.h in the Platform Software Development Kit (SDK)
#define PROTO_TYPE_UCAST        0
#define PROTOCOL_ID(Type, VendorId, ProtocolId) (((Type & 0x03)<<30)|((VendorId & 0x3FFF)<<16)|(ProtocolId & 0xFFFF))
#define PROTO_VENDOR_ID        0xFFFF

// This is a simple callback method used by the new client registering for change notifications
void WINAPI Method(RTM_ENTITY_HANDLE CallerHandle, RTM_ENTITY_HANDLE CalleeHandle, RTM_ENTITY_METHOD_INPUT *Input, RTM_ENTITY_METHOD_OUTPUT *Output){
   
    UNREFERENCED_PARAMETER(CallerHandle);
    UNREFERENCED_PARAMETER(CalleeHandle);
    UNREFERENCED_PARAMETER(Input);
    UNREFERENCED_PARAMETER(Output);
 
    wprintf(L"Hello World!");
    return;
}

int __cdecl main(){

    RTM_ENTITY_HANDLE ThisClientHandle, OtherClientHandle;
    RTM_ENTITY_INFO EntityInfo;
    RTM_REGN_PROFILE RegnProfile;
    UINT NumMethods = 0;
    DWORD dwRet = ERROR_SUCCESS;
    RTM_ENTITY_EXPORT_METHODS Methods;
    PRTM_NOTIFY_HANDLE NotifyHandle = NULL;

    //------------------------------------------------------
    // Register a new client with an export method (callback)
    //------------------------------------------------------
    
    // Set the callback Method() as the exported client function
    Methods.NumMethods = 1;
    Methods.Methods[0] = (RTM_ENTITY_EXPORT_METHOD) Method;
    
    // Set the new client's properties
    EntityInfo.RtmInstanceId = 0;
    EntityInfo.AddressFamily = AF_INET;
    EntityInfo.EntityId.EntityProtocolId = PROTO_IP_RIP;
    EntityInfo.EntityId.EntityInstanceId = PROTOCOL_ID(PROTO_TYPE_UCAST, PROTO_VENDOR_ID, PROTO_IP_RIP);

    // Register the new client in the routing table manager
    dwRet = RtmRegisterEntity(&EntityInfo, &Methods, NULL, FALSE, &RegnProfile, &ThisClientHandle);
    if (dwRet != ERROR_SUCCESS){
        // RtmRegisterEntity failed
        // Do something here
        // clean-up
        return 0;
    }
    
    //------------------------------------------------------
    //  Register the new client for change notifications
    //------------------------------------------------------

    // Register for change notifications to the best routes to all destinations in the unicast view of the routing table.
    // For simplicity in this example, set the caller client handle to be the same as the callee client handle
    OtherClientHandle = ThisClientHandle;
    NotifyHandle = (PRTM_NOTIFY_HANDLE) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, sizeof(RTM_NOTIFY_HANDLE));
    dwRet = RtmRegisterForChangeNotification(ThisClientHandle, RTM_VIEW_MASK_UCAST, RTM_CHANGE_TYPE_BEST, OtherClientHandle, NotifyHandle);
    
    if (dwRet != ERROR_SUCCESS){
        // RtmRegisterForChangeNotification failed
        // Do something here
        // clean-up
        return 0;
    }

    // Clean-up: Deregister the new entity and free heap memory
    dwRet = RtmDeregisterFromChangeNotification(ThisClientHandle, *NotifyHandle);
    dwRet |= RtmDeregisterEntity(ThisClientHandle);
    if (dwRet != ERROR_SUCCESS){
        // Deregistration failed
        // Do something here
    }
    HeapFree(GetProcessHeap(), 0, NotifyHandle);

    return 0;
}
```



 

 




