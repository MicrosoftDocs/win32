---
title: Obtain and Call the Exported Methods for a Client
description: The following sample code shows how to obtain a list of methods a client has exported, and how to invoke a method for that client.
ms.assetid: 55b2a03f-498c-4321-891b-747f4baea10d
ms.topic: article
ms.date: 05/31/2018
---

# Obtain and Call the Exported Methods for a Client

The following sample code shows how to obtain a list of methods a client has exported, and how to invoke a method for that client.


```C++
#include <windows.h>
#include <stdio.h>
#include "Rtmv2.h"
#include "nldef.h"
#include "strsafe.h"

// The following #defines are from routprot.h in the Platform Software Development Kit (SDK)
#define PROTO_TYPE_UCAST       0
#define PROTOCOL_ID(Type, VendorId, ProtocolId) (((Type & 0x03)<<30)|((VendorId & 0x3FFF)<<16)|(ProtocolId & 0xFFFF))
#define PROTO_VENDOR_ID                    0xFFFF

// This is the simple callback method the entity (client) first registers and then exports via RtmGetEntityMethods()
void WINAPI Method(RTM_ENTITY_HANDLE CallerHandle, RTM_ENTITY_HANDLE CalleeHandle, RTM_ENTITY_METHOD_INPUT *Input, RTM_ENTITY_METHOD_OUTPUT *Output){

    UNREFERENCED_PARAMETER(CallerHandle);
    UNREFERENCED_PARAMETER(CalleeHandle);

    if(Input != NULL){
        wprintf(L"%s\n", Input->InputData);
        FillMemory(Output->OutputData,sizeof(ERROR_SUCCESS),ERROR_SUCCESS);
        return;
    }

    FillMemory(Output->OutputData,sizeof(ERROR_INVALID_DATA),ERROR_INVALID_DATA);
    return;
}

int __cdecl main(){

    RTM_ENTITY_HANDLE ThisClientHandle, OtherClientHandle;
    RTM_ENTITY_INFO EntityInfo;
    RTM_REGN_PROFILE RegnProfile;
    UINT NumMethods = 0;
    DWORD dwRet = ERROR_SUCCESS;
    PRTM_ENTITY_EXPORT_METHOD ExportMethods = NULL;
    RTM_ENTITY_EXPORT_METHODS Methods;

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
        // Registration failed
        // Do something here
        // clean-up
        return 0;
    }
    
    //------------------------------------------------------
    // Determine the number of exported methods
    //------------------------------------------------------

    // Calling RtmGetEntityMethods with NumMethods = 0 returns the number of registered methods for the client
    // For simplicity in this example, set the caller client handle to be the same as the callee client handle
    OtherClientHandle = ThisClientHandle;
    dwRet = RtmGetEntityMethods(ThisClientHandle, OtherClientHandle, &NumMethods, ExportMethods);
    if (dwRet != ERROR_SUCCESS){
        // RtmGetEntityMethods failed
        // Do something here
        // clean-up
        return 0;
    }

    // If the client registered any methods proceed, otherwise quit
    if (NumMethods > 0){

        //----------------------------------------------
        // Get function pointers to the exported methods
        //----------------------------------------------

        // Allocate memory from the heap for the number of callback methods registered by the client
        ExportMethods = (PRTM_ENTITY_EXPORT_METHOD) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, NumMethods * sizeof(PRTM_ENTITY_EXPORT_METHOD));    
        
        if (ExportMethods == NULL){
            // HeapAlloc failed
            // Do something here
            // clean-up
            return 0;
        }

        // Calling RtmGetEntityMethods in order to receive the callback pointers into ExportMethods
        dwRet = RtmGetEntityMethods(ThisClientHandle, OtherClientHandle, &NumMethods, ExportMethods);
        if (dwRet != ERROR_SUCCESS){
            // RtmGetEntityMethods failed
            // Do something here
            // clean-up
            return 0;
        }

        //--------------------------
        // Call the exported methods using RtmInvokeMethod(). You cannot call the methods directly.
        //--------------------------

        // Initialize the exported method's input and output data
        PRTM_ENTITY_METHOD_INPUT Input;
        PRTM_ENTITY_METHOD_OUTPUT Output;
        LPWSTR InputString = L"Hello world from the exported method!";
        UINT InputSize = sizeof(L"Hello world from the exported method!");

        // Allocated heap memory for the method's input data
        Input = (PRTM_ENTITY_METHOD_INPUT) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, InputSize + FIELD_OFFSET(RTM_ENTITY_METHOD_INPUT, InputData));

        if (Input == NULL){
            // HeapAlloc failed
            // Do something here
            // clean-up
            return 0;
        }
        Input->MethodType = METHOD_TYPE_ALL_METHODS;
        Input->InputSize = InputSize;    
        dwRet = StringCchCopyN((STRSAFE_LPWSTR)Input->InputData, InputSize, InputString, InputSize);
        if (dwRet != ERROR_SUCCESS){
            // String copy failed
            // Do something here
            // clean-up
        }
        
        // Assume there is no output data for the function other than an error code 
        // For more than one method, multiply sizeof(DWORD) by the number of exported methods 
        UINT OutputHdrSize = FIELD_OFFSET(RTM_ENTITY_METHOD_OUTPUT, OutputData);            
        UINT OutputSize = OutputHdrSize + sizeof(DWORD); 
        Output = (PRTM_ENTITY_METHOD_OUTPUT) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, OutputSize);    
        if (Output == NULL){
            // HeapAlloc failed
            // Do something here
            // clean-up
            return 0;
        }

        // Calling RtmInvokeMethod with arbitray input data and output size for the method exported by OtherClientHandle
        dwRet = RtmInvokeMethod(ThisClientHandle, OtherClientHandle, Input, &OutputSize, Output);
        if (dwRet == NO_ERROR){
            // Parse the output from the method
            printf("Exported method completed with error code: %d\n", (DWORD) *Output->OutputData);
        }    

        // Clean up: Release handles and free memory
        HeapFree(GetProcessHeap(), 0, ExportMethods);
        HeapFree(GetProcessHeap(), 0, Output);
        HeapFree(GetProcessHeap(), 0, Input);
    }

    // Clean-up: Deregister the new entity
    dwRet = RtmDeregisterEntity(ThisClientHandle);
    if (dwRet != ERROR_SUCCESS){
        // Deregistration failed
        // Do something here
    }

    return 0;
}
```



 

 




