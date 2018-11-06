---
title: Monitoring Filter Changes
description: Following sample code demonstrates how to monitor the addition and deletion of filters that might affect a server application.
ms.assetid: 7ca527e1-217a-4e97-86e9-23b484ffc25d
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Filter Changes

The following sample code demonstrates how to monitor the addition and deletion of filters that might affect a server application.

> [!Note]  
> The filter conditions are the same as those supported by the downlevel **IsPortAllowed** API.

 


```C++
#include <windows.h>
#include <fwpmu.h>
#include <stdio.h>

#pragma comment(lib, "fwpuclnt.lib")

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

void FilterChangeCallback(IN void* context,
                          IN const FWPM_FILTER_CHANGE0* change)
{
   PCSTR changeType;
   wchar_t guidString[sizeof("{eaea82e6-6747-4321-ab51-44ba5509b812}")];

   switch (change->changeType)
   {
      case FWPM_CHANGE_ADD:
      {
         changeType = "FWPM_CHANGE_ADD";
         break;
      }
      case FWPM_CHANGE_DELETE:
      {
         changeType = "FWPM_CHANGE_DELETE";
         break;
      }

      default:
      {
         changeType = "<unknown>";
         break;
      }
   }

   printf(
      "   changeType = %s\n"
      "   filterId = %I64u\n"
      "\n",
      changeType,
      change->filterId
      );
}

DWORD InitFilterConditions(
         __in_opt PCWSTR appPath,
         __in_opt const SOCKADDR* localAddr,
         __in_opt UINT8 ipProtocol,
         __in UINT32 numCondsIn,
         __out_ecount_part(numCondsIn, *numCondsOut)
            FWPM_FILTER_CONDITION0* conds,
         __out UINT32* numCondsOut,
         __deref_out FWP_BYTE_BLOB** appId
         )
{
    *numCondsOut = 0;
    return 0;
}

DWORD MonitorMatchingFilters(
         __in HANDLE engine,
         __in const GUID* layerKey,
         __in_opt PCWSTR appPath,
         __in_opt const SOCKADDR* localAddr,
         __in_opt UINT8 ipProtocol,
         __in FWPM_FILTER_CHANGE_CALLBACK0 callback,
         __in_opt void* context,
         __out HANDLE* changeHandle
         )
{
   DWORD result = ERROR_SUCCESS;
   FWPM_FILTER_CONDITION0 conds[4];
   UINT32 numConds;
   FWP_BYTE_BLOB* appBlob = NULL;
   FWPM_FILTER_ENUM_TEMPLATE0 enumTempl;
   FWPM_FILTER_SUBSCRIPTION0 sub;

   // InitFilterConditions is presented in the 
   // Populating Filter Conditions example code 
   result = InitFilterConditions(
               appPath,
               localAddr,
               ipProtocol,
               ARRAYSIZE(conds),
               conds,
               &numConds,
               &appBlob
               );
   EXIT_ON_ERROR(InitFilterConditions);

   memset(&enumTempl, 0, sizeof(enumTempl));
   enumTempl.layerKey = *layerKey;
   enumTempl.numFilterConditions = numConds;
   if (numConds > 0)
   {
      enumTempl.filterCondition = conds;
   }
   // We want to see all filters regardless of action.
   enumTempl.actionMask = 0xFFFFFFFF;

   memset(&sub, 0, sizeof(sub));
   sub.enumTemplate = &enumTempl;
   // We want to see both adds and deletes.
   sub.flags = ( FWPM_SUBSCRIPTION_FLAG_NOTIFY_ON_ADD |
                 FWPM_SUBSCRIPTION_FLAG_NOTIFY_ON_DELETE );

   // Once we have successfully subscribed, our callback will be invoked for
   // every matching add and delete until we call FwpmFilterUnsubscribeChanges0.
   result = FwpmFilterSubscribeChanges0(
               engine,
               &sub,
               callback,
               context,
               changeHandle
               );
   EXIT_ON_ERROR(result);

CLEANUP:
   FwpmFreeMemory0((void**)&appBlob);
   return result;
}



DWORD wmain(int argc,
            wchar_t* argv[])
{
   UNREFERENCED_PARAMETER(argc);
   UNREFERENCED_PARAMETER(argv);
 
   // Open a session to the filter engine
   HANDLE engineHandle = 0;

   // Use dynamic sessions for efficiency and safety:
   //  - All objects associated with the dynamic session are deleted with one call.
   //  - Filtering policy objects are deleted even when the application crashes. 
   FWPM_SESSION0 session;
   memset(&session, 0, sizeof(session));
   session.flags = FWPM_SESSION_FLAG_DYNAMIC;

   DWORD result = FwpmEngineOpen0(NULL, RPC_C_AUTHN_WINNT, NULL, &session, &engineHandle);
   EXIT_ON_ERROR(FwpmEngineOpen0);      
 
   HANDLE changeHandle = 0;
   FWPM_FILTER_CHANGE_CALLBACK0 callback = (FWPM_FILTER_CHANGE_CALLBACK0)FilterChangeCallback;
   result = MonitorMatchingFilters(
         engineHandle,
         &FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4,
         0,
         0,
         0,
         callback,
         0,
         &changeHandle
         );

CLEANUP:  
   if (result != ERROR_SUCCESS)
   {
       printf("Error: %x\n", result);
   }
   else
   {
       printf("Success");
   }

   return result;
}
```



 

 




