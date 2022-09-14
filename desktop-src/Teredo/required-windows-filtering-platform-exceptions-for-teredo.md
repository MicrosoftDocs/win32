---
title: Windows Filtering Platform exceptions for Teredo
description: Exceptions that allow applications to receive unsolicited traffic over Teredo through a firewall must be created using Windows Filtering Platform APIs.
ms.assetid: 8e562757-cd31-4c83-bf4a-92c2e0d3f2ed
ms.topic: article
ms.date: 05/31/2018
---

# Windows Filtering Platform exceptions for Teredo

Exceptions that allow applications to receive unsolicited traffic over [Teredo](about-teredo.md) through a firewall must be created using [Windows Filtering Platform](/windows/desktop/FWP/windows-filtering-platform-start-page) APIs. This is accomplished by opening incoming and outgoing application-based exceptions (Application \<app name\>) at the Teredo Sublayer of ALE for IPv6 traffic. This ensures that only applications with the Teredo exception can use Teredo. Caution should be exercised in the creation of these exceptions. The use of the general " \* " (all) option could allow programs not registered with the Teredo sublayer or tunnel traffic to pass the firewall and pose a threat to security.

In any situation at least one blocked application is required, but there can be zero or more allowed applications added by a firewall depending on how many applications need to be permitted.

The following sample demonstrates the use of one allow and one block.


```C++
/*--
Routine Description:

    Adds the necessary filters to permit specific applications and block all other
    via the Windows Filtering Platform (WFP).

Arguments:
   
   [in] HANDLE engineHandle - Handle to the base firewall engine.
   [in] FWP_BYTE_BLOB* applicationId - Identifier for this application.

Return Value:

    NO_ERROR or a specific Result

--*/
   DWORD Result = NO_ERROR;
   FWPM_FILTER0 Filter;
   FWPM_FILTER_CONDITION0 FilterConditions[3]; // We only need three.
   DWORD TempResult;
   FWP_BYTE_BLOB* applicationId;

   printf("Starting Transaction\n");

   Result = FwpmTransactionBegin0(engineHandle, 0);
   if (NO_ERROR != Result)
   {
      goto abort;
   }
   
   printf("Successfully Started Transaction\n");

   RtlZeroMemory(&Filter, sizeof(FWPM_FILTER0));

   Filter.layerKey = FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6;
   Filter.displayData.name = L"Teredo Filter for Application Specific Permit";
   Filter.displayData.description = L"Implement Teredo Filter for Application Specific Permit at the Recv Accept layer";
   Filter.action.type = FWP_ACTION_PERMIT;
   Filter.subLayerKey = FWPM_SUBLAYER_TEREDO;
   Filter.weight.type = FWP_EMPTY; // auto-weight
   Filter.filterCondition = FilterConditions;
   Filter.numFilterConditions = 3;

   RtlZeroMemory(FilterConditions, sizeof(FilterConditions));

   //
   // Enable this for IfType == Tunnel, TunnelType == Teredo.
   //
   FilterConditions[0].fieldKey = FWPM_CONDITION_INTERFACE_TYPE;
   FilterConditions[0].matchType = FWP_MATCH_EQUAL;
   FilterConditions[0].conditionValue.type = FWP_UINT32;
   FilterConditions[0].conditionValue.uint32 = IF_TYPE_TUNNEL;

   //
   // Enable this for IfType == Tunnel, TunnelType == Teredo.
   //
   FilterConditions[1].fieldKey = FWPM_CONDITION_TUNNEL_TYPE;
   FilterConditions[1].matchType = FWP_MATCH_EQUAL;
   FilterConditions[1].conditionValue.type = FWP_UINT32;
   FilterConditions[1].conditionValue.uint32 = TUNNEL_TYPE_TEREDO;

   //
   // Add a permitted application.
   //
   FilterConditions[2].fieldKey = FWPM_CONDITION_ALE_APP_ID;
   FilterConditions[2].matchType = FWP_MATCH_EQUAL;
   FilterConditions[2].conditionValue.type = FWP_BYTE_BLOB_TYPE;
   FilterConditions[2].conditionValue.byteBlob = applicationId;

   printf("Adding Recv Accept Application specific V6 Teredo Filter.\n");

   Result = FwpmFilterAdd0(engineHandle,
                           &Filter,
                           NULL,
                           NULL);

   if (NO_ERROR != Result)
   {
      goto abort;
   }
   
   printf("Successfully added Recv Accept Application specific V6 Teredo Filter.\n");

   Filter.layerKey = FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6;
   Filter.displayData.name = L"Teredo Filter for Blocking other applications";
   Filter.displayData.description = L"This blocks any other traffic coming in over the Teredo interface that hasn't explicitly been permitted.";
   Filter.action.type = FWP_ACTION_BLOCK;
   Filter.subLayerKey = FWPM_SUBLAYER_TEREDO;
   Filter.weight.type = FWP_EMPTY; // auto-weight
   Filter.filterCondition = FilterConditions;
   Filter.numFilterConditions = 2;

   RtlZeroMemory(FilterConditions, sizeof(FilterConditions));

   //
   // Enable this for IfType == Tunnel, TunnelType == Teredo.
   //
   FilterConditions[0].fieldKey = FWPM_CONDITION_INTERFACE_TYPE;
   FilterConditions[0].matchType = FWP_MATCH_EQUAL;
   FilterConditions[0].conditionValue.type = FWP_UINT32;
   FilterConditions[0].conditionValue.uint32 = IF_TYPE_TUNNEL;

   //
   // Enable this for IfType == Tunnel, TunnelType == Teredo.
   //
   FilterConditions[1].fieldKey = FWPM_CONDITION_TUNNEL_TYPE;
   FilterConditions[1].matchType = FWP_MATCH_EQUAL;
   FilterConditions[1].conditionValue.type = FWP_UINT32;
   FilterConditions[1].conditionValue.uint32 = TUNNEL_TYPE_TEREDO;

   printf("Adding Recv Accept block all non-permitted V6 Teredo Filter.\n");

   Result = FwpmFilterAdd0(engineHandle,
                           &Filter,
                           NULL,
                           NULL);

   if (NO_ERROR != Result)
   {
      goto abort;
   }
   
   printf("Successfully added Recv Accept block all non-permitted V6 Teredo Filter.\n");

   printf("Committing Transaction\n");
   Result = FwpmTransactionCommit0(engineHandle);
   if (NO_ERROR == Result)
   {
      printf("Successfully Committed Transaction\n");
   }
   goto cleanup;

abort:
   printf("Aborting Transaction\n");
   TempResult = FwpmTransactionAbort0(engineHandle);
   if (NO_ERROR == TempResult)
   {
      printf("Successfully Aborted Transaction\n");
   }

cleanup:
   
   return Result;

```



 

 