---
title: Using Classify Options
description: Following code samples demonstrate how to use filter classify options in order to alter the filtering process.
ms.assetid: 02d57ea2-066b-4cb9-81f1-2ff9ee55f22f
ms.topic: article
ms.date: 05/31/2018
---

# Using Classify Options

The following code samples demonstrate how to use filter classify options in order to alter the filtering process.

## Enable Loose Source Mapping for a Remote UDP Port


```C++
#include <windows.h>
#include <fwpmu.h>
#include <stdio.h>

#pragma comment(lib, "fwpuclnt.lib")
#pragma comment(lib, "rpcrt4.lib")

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

DWORD EnableLooseSourceMapping(
         __in HANDLE engine,
         __in PCWSTR provCtxtName,
         __in PCWSTR filterName,
         __in_opt const GUID* providerKey,
         __in_opt const GUID* subLayerKey,
         __in UINT16 port
         )
{
   DWORD result = ERROR_SUCCESS;
   FWPM_CLASSIFY_OPTION0 option;
   FWPM_CLASSIFY_OPTIONS0 options;
   FWPM_PROVIDER_CONTEXT0 provCtxt;
   FWPM_FILTER_CONDITION0 conds[2];
   FWPM_FILTER0 filter;
   BOOL txnInProgress = FALSE;

   //////////
   // Loose source mapping is controlled through classify options, so first
   // you add a provider context with the desired option value.
   //////////

   option.type = FWP_CLASSIFY_OPTION_LOOSE_SOURCE_MAPPING;
   option.value.type = FWP_UINT32;
   option.value.uint32 = FWP_OPTION_VALUE_ENABLE_LOOSE_SOURCE;

   options.numOptions = 1;
   options.options = &option;

   memset(&provCtxt, 0, sizeof(provCtxt));
   // You have to assign the key yourself since you'll need it when adding 
   // the filters that reference this provider context.
   result = UuidCreate(&(provCtxt.providerContextKey));
   EXIT_ON_ERROR(UuidCreate);
   // For MUI compatibility, object names should be indirect strings. See
   // SHLoadIndirectString for details.
   provCtxt.displayData.name = (PWSTR)provCtxtName;
   // Link all objects to your provider. When multiple providers are
   // installed on a computer, this makes it easy to determine who added what.
   provCtxt.providerKey = (GUID*)providerKey;
   provCtxt.type = FWPM_CLASSIFY_OPTIONS_CONTEXT;
   provCtxt.classifyOptions = &options;

   // Add all the objects from within a single transaction to make it easy
   // to clean up partial results in error paths.
   result = FwpmTransactionBegin0(engine, 0);
   EXIT_ON_ERROR(FwpmTransactionBegin0);
   txnInProgress = TRUE;

   result = FwpmProviderContextAdd0(engine, &provCtxt, NULL, NULL);
   EXIT_ON_ERROR(FwpmProviderContextAdd0);

   //////////
   // Next, add filters at the ALE_AUTH_CONNECT layers that reference the
   // provider context.
   //////////

   // First condition matches UDP traffic only.
   conds[0].fieldKey = FWPM_CONDITION_IP_PROTOCOL;
   conds[0].matchType = FWP_MATCH_EQUAL;
   conds[0].conditionValue.type = FWP_UINT8;
   conds[0].conditionValue.uint16 = IPPROTO_UDP;

   // Second condition matches the remote port.
   conds[1].fieldKey = FWPM_CONDITION_IP_REMOTE_PORT;
   conds[1].matchType = FWP_MATCH_EQUAL;
   conds[1].conditionValue.type = FWP_UINT16;
   conds[1].conditionValue.uint16 = port;

   // Fill in the common fields shared by all filters.
   memset(&filter, 0, sizeof(filter));
   filter.displayData.name = (PWSTR)filterName;
   // Filters can have either a raw context (which is a UINT64) or a
   // provider context. If using the latter, you have to set the
   // appropriate flag.
   filter.flags = FWPM_FILTER_FLAG_HAS_PROVIDER_CONTEXT;
   filter.providerKey = (GUID*)providerKey;
   // Generally, it's best to add filters to your own sublayer, so you don't have
   // to worry about being overridden by filters added by another provider.
   if (subLayerKey != NULL)
   {
      filter.subLayerKey = *subLayerKey;
   }
   filter.numFilterConditions = 2;
   filter.filterCondition = conds;
   // The set options callouts never return permit or block, so they're
   // inspection callouts.
   filter.action.type = FWP_ACTION_CALLOUT_INSPECTION;
   // Link the filter to the provider context we just added. Note that multiple
   // filters can reference a single provider context, so once you've added a
   // provider context to enable LSM, you can use it over and over again.
   filter.providerContextKey = provCtxt.providerContextKey;

   // Add the IPv4 filter.
   filter.layerKey = FWPM_LAYER_ALE_AUTH_CONNECT_V4;
   filter.action.calloutKey = FWPM_CALLOUT_SET_OPTIONS_AUTH_CONNECT_LAYER_V4;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Add the IPv6 filter.
   filter.layerKey = FWPM_LAYER_ALE_AUTH_CONNECT_V6;
   filter.action.calloutKey = FWPM_CALLOUT_SET_OPTIONS_AUTH_CONNECT_LAYER_V6;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Once all the adds have succeeded, commit the transaction to atomically
   // add all the new objects.
   result = FwpmTransactionCommit0(engine);
   EXIT_ON_ERROR(FwpmTransactionCommit0);
   txnInProgress = FALSE;

CLEANUP:
   if (txnInProgress)
   {
      // Abort any transaction still in progress to clean up partial results.
      FwpmTransactionAbort0(engine);
   }
   return result;
}
```



## Modify the Idle Lifetimes for ALE Flows


```C++
#include <windows.h>
#include <stdio.h>
#include <fwpmu.h>
#define INITGUID
#include <guiddef.h>

#pragma comment(lib, "fwpuclnt.lib")

// a4124528-12d6-4da5-a9ee-897a46966dfa
DEFINE_GUID(
   CONFIGURE_TIMEOUT_PROVIDER_CONTEXT,
   0xa4124528,
   0x12d6,
   0x4da5,
   0xa9, 0xee, 0x89, 0x7a, 0x46, 0x96, 0x6d, 0xfa
);

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

DWORD ConfigureALEFlowTimeouts(
        __in HANDLE engineHandle)
{
   DWORD result = ERROR_SUCCESS;
   FWPM_PROVIDER_CONTEXT0 configureTimeouts;
   FWPM_CLASSIFY_OPTIONS0 options;
   FWPM_CLASSIFY_OPTION0 option[2];
   FWPM_FILTER0 filter;
   FWPM_FILTER_CONDITION0 filterConditions[1];

   // Start Transaction.
   result = FwpmTransactionBegin0(engineHandle, 0);
   EXIT_ON_ERROR(FwpmTransactionBegin0);
   
   RtlZeroMemory(&option, sizeof(option));
   
   option[0].type = FWP_CLASSIFY_OPTION_MCAST_BCAST_LIFETIME;
   option[0].value.type = FWP_UINT32;
   option[0].value.uint32 = 10; // 10 seconds

   option[1].type = FWP_CLASSIFY_OPTION_UNICAST_LIFETIME;
   option[1].value.type = FWP_UINT32;
   option[1].value.uint32 = 90; // 1.5 minutes
   
   RtlZeroMemory(&options, sizeof(FWPM_CLASSIFY_OPTIONS0));
   options.numOptions = 2;
   options.options = option;
   
   RtlZeroMemory(&configureTimeouts, sizeof(FWPM_PROVIDER_CONTEXT0));
   
   configureTimeouts.providerContextKey = CONFIGURE_TIMEOUT_PROVIDER_CONTEXT;
   configureTimeouts.type = FWPM_CLASSIFY_OPTIONS_CONTEXT;
   configureTimeouts.displayData.name = L"Classify Options";
   configureTimeouts.displayData.description = L"Sets options ALE connect layers";
   configureTimeouts.classifyOptions = &options;

   // Add Provider Context for V4 connections.
   result = FwpmProviderContextAdd0(engineHandle, &configureTimeouts, NULL, NULL);
   EXIT_ON_ERROR(FwpmProviderContextAdd0);
   
   RtlZeroMemory(&filter, sizeof(FWPM_FILTER0));

   filter.layerKey = FWPM_LAYER_ALE_AUTH_CONNECT_V4;
   filter.displayData.name = L"Implement Configure Timeouts for V4";
   filter.displayData.description = L"Sets up flow for traffic that we are interested in.";
   filter.action.type = FWP_ACTION_CALLOUT_INSPECTION;
   filter.action.calloutKey = FWPM_CALLOUT_SET_OPTIONS_AUTH_CONNECT_LAYER_V4;
   filter.subLayerKey = FWPM_SUBLAYER_INSPECTION;
   filter.weight.type = FWP_EMPTY; // auto-weight
   filter.flags = FWPM_FILTER_FLAG_HAS_PROVIDER_CONTEXT;

   filter.providerContextKey = CONFIGURE_TIMEOUT_PROVIDER_CONTEXT;
   filter.filterCondition = filterConditions;
   filter.numFilterConditions = 1;

   RtlZeroMemory(filterConditions, sizeof(filterConditions));

   // Enable filter for UDP traffic.
   filterConditions[0].fieldKey = FWPM_CONDITION_IP_PROTOCOL;
   filterConditions[0].matchType = FWP_MATCH_EQUAL;
   filterConditions[0].conditionValue.type = FWP_UINT8;
   filterConditions[0].conditionValue.uint8 = IPPROTO_UDP;

   // Add Connect V4 Configure Timeouts filter.
   result = FwpmFilterAdd0(engineHandle, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Commit transaction.
   result = FwpmTransactionCommit0(engineHandle);
   if (ERROR_SUCCESS == result)
   {
      printf("Successfully Committed Transaction\n");
   }
   goto CLEANUP;

CLEANUP:
   return result;
}


DWORD wmain(int argc,
            wchar_t* argv[])
{
   UNREFERENCED_PARAMETER(argc);
   UNREFERENCED_PARAMETER(argv);
   
   HANDLE engineHandle = 0;

   // Use dynamic sessions for efficiency and safety:
   //  - All objects associated with the dynamic session are deleted with one call.
   //  - Filtering policy objects are deleted even when the application crashes. 
   FWPM_SESSION0 session;
   memset(&session, 0, sizeof(session));
   session.flags = FWPM_SESSION_FLAG_DYNAMIC;

   DWORD result = FwpmEngineOpen0(NULL, RPC_C_AUTHN_WINNT, NULL, &session, &engineHandle);
   if (ERROR_SUCCESS == result)
   {
        result = ConfigureALEFlowTimeouts(engineHandle);
   }

   if (result != ERROR_SUCCESS)
   {

       printf("Error: %x\n", result);
   }

   return result;
}
```



## Related topics

<dl> <dt>

[**Filtering Conditions Available at Each Filtering Layer**](filtering-conditions-available-at-each-filtering-layer.md)
</dt> </dl>

 

 




