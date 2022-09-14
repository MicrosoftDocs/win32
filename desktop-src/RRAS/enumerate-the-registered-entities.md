---
title: Enumerate the Registered Entities
description: The following sample code shows how to create an enumeration of registered clients and obtain the client information from the routing table manager.
ms.assetid: a96a4089-6a7c-4565-baeb-5d5fa7b84b35
ms.topic: article
ms.date: 05/31/2018
---

# Enumerate the Registered Entities

The following sample code shows how to create an enumeration of registered clients and obtain the client information from the routing table manager.


```C++
#include <windows.h>
#include <stdio.h>
#include "Rtmv2.h"
#include "nldef.h"

// The following #defines are from routprot.h in the Platform Software Development Kit (SDK)
#define PROTO_TYPE_UCAST            0
#define PROTOCOL_ID(Type, VendorId, ProtocolId) (((Type & 0x03)<<30)|((VendorId & 0x3FFF)<<16)|(ProtocolId & 0xFFFF))
#define PROTO_VENDOR_ID            0xFFFF

int __cdecl main(){
 
    RTM_ENTITY_HANDLE RtmRegHandle;
    RTM_ENTITY_INFO EntityInfo;
    RTM_ENTITY_HANDLE EntityHandle;
    RTM_REGN_PROFILE RegnProfile;
    UINT NumEntities = 0;
    DWORD dwRet = ERROR_SUCCESS;
    
    PRTM_ENTITY_INFO EntityInfoArray;
    PRTM_ENTITY_HANDLE EntityHandleArray;

    EntityInfo.RtmInstanceId = 0;
    EntityInfo.AddressFamily = AF_INET;
    EntityInfo.EntityId.EntityProtocolId = PROTO_IP_RIP;
    EntityInfo.EntityId.EntityInstanceId = PROTOCOL_ID(PROTO_TYPE_UCAST, PROTO_VENDOR_ID, PROTO_IP_RIP);

    // Register the new entity.
    dwRet = RtmRegisterEntity(&EntityInfo, NULL, NULL, FALSE, &RegnProfile, &RtmRegHandle);
    if (dwRet != ERROR_SUCCESS){
        // Registration failed
        // Do something here
        // Clean-up
        return 0;
    }

    // This call will return the number of entities in NumEntities for use in the next call to this function.
    dwRet = RtmGetRegisteredEntities(RtmRegHandle, &NumEntities, &EntityHandle, NULL);

    if (dwRet == ERROR_INSUFFICIENT_BUFFER){
        
        EntityInfoArray = (PRTM_ENTITY_INFO) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, NumEntities * sizeof(RTM_ENTITY_INFO));
        EntityHandleArray = (PRTM_ENTITY_HANDLE) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, NumEntities * sizeof(PRTM_ENTITY_HANDLE));

        if (EntityInfoArray == NULL || EntityHandleArray == NULL){
            wprintf(L"HeapAlloc failed");
            HeapFree(GetProcessHeap(), 0, EntityInfoArray);
            HeapFree(GetProcessHeap(), 0, EntityHandleArray);
            return 0;
        }
              
        // Call RtmGetRegisteredEntities in order to receive the list of registered entities into EntityInfoArray
        dwRet = RtmGetRegisteredEntities(RtmRegHandle, &NumEntities, EntityHandleArray, EntityInfoArray);
        
        // Loop through each of the registered entities and depending upon its protocol ID, do something
        for (UINT i = 0; i <= NumEntities; i++){
            if (EntityInfoArray[i].EntityId.EntityProtocolId == PROTO_IP_OSPF){
                // Do something here
            }else if (EntityInfoArray[i].EntityId.EntityProtocolId == PROTO_IP_RIP){
                // Do something here
            }
        }
        
        // Clean up: Release handles and free memory
        RtmReleaseEntities(RtmRegHandle, NumEntities, EntityHandleArray);
        HeapFree(GetProcessHeap(), 0, EntityInfoArray);
        HeapFree(GetProcessHeap(), 0, EntityHandleArray);
    }

    // Clean-up: Deregister the new entity
    dwRet = RtmDeregisterEntity(RtmRegHandle);
    if (dwRet != ERROR_SUCCESS){
        // Deregistration failed
        // Do something here
    }
    
    return 0;
}
```



 

 




