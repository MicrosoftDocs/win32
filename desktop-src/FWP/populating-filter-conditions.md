---
title: Populating Filter Conditions
description: Following sample code demonstrates how to populate filter conditions used by a server application to find filters and events that affect it.
ms.assetid: 6c7c8d55-2cd4-45fe-ad6b-e568941d6765
ms.topic: article
ms.date: 05/31/2018
---

# Populating Filter Conditions

The following sample code demonstrates how to populate filter conditions used by a server application to find filters and events that affect it.

> [!Note]  
> These conditions are the same as those supported by the downlevel **IsPortAllowed** API.

 


```C++
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
   DWORD result = NO_ERROR;
   UINT32 numConds = 0;
   UINT16 port;
   void* addr;

   *numCondsOut = 0;

   if (localAddr != NULL)
   {
      port = INETADDR_PORT(localAddr);
      if (port != 0)
      {
         if (numConds >= numCondsIn)
         {
            result = ERROR_INSUFFICIENT_BUFFER;
            goto CLEANUP;
         }

         conds[numConds].fieldKey = FWPM_CONDITION_IP_LOCAL_PORT;
         conds[numConds].matchType = FWP_MATCH_EQUAL;
         conds[numConds].conditionValue.type = FWP_UINT16;
         // The SOCKADDR struct has the port in network order, but the
         // filtering engine expects it in host order.
         conds[numConds].conditionValue.uint16 = ntohs(port);
         ++numConds;
      }

      if (!INETADDR_ISANY(localAddr))
      {
         if (numConds > numCondsIn)
         {
            result = ERROR_INSUFFICIENT_BUFFER;
            goto CLEANUP;
         }

         addr = INETADDR_ADDRESS(localAddr);

         conds[numConds].fieldKey = FWPM_CONDITION_IP_LOCAL_ADDRESS;
         conds[numConds].matchType = FWP_MATCH_EQUAL;

         if (localAddr->sa_family == AF_INET)
         {
            conds[numConds].conditionValue.type = FWP_UINT32;
            // The SOCKADDR struct has the port in network order, but the
            // filtering engine expects it in host order.
            conds[numConds].conditionValue.uint32 = ntohl(*(ULONG*)addr);
         }
         else
         {
            conds[numConds].conditionValue.type = FWP_BYTE_ARRAY16_TYPE;
            conds[numConds].conditionValue.byteArray16 =
               (FWP_BYTE_ARRAY16*)addr;
         }

         ++numConds;
      }
   }

   if (ipProtocol != 0)
   {
      if (numConds >= numCondsIn)
      {
         result = ERROR_INSUFFICIENT_BUFFER;
         goto CLEANUP;
      }

      conds[numConds].fieldKey = FWPM_CONDITION_IP_PROTOCOL;
      conds[numConds].matchType = FWP_MATCH_EQUAL;
      conds[numConds].conditionValue.type = FWP_UINT8;
      conds[numConds].conditionValue.uint8 = ipProtocol;
      ++numConds;
   }

   if (appPath != NULL)
   {
      if (numConds >= numCondsIn)
      {
         result = ERROR_INSUFFICIENT_BUFFER;
         goto CLEANUP;
      }

      // appPath must be a fully-qualified file name, and the file must
      // exist on the local machine.
      result = FwpmGetAppIdFromFileName0(appPath, appId);
      BAIL_ON_ERROR(FwpmGetAppIdFromFileName0);

      conds[numConds].fieldKey = FWPM_CONDITION_ALE_APP_ID;
      conds[numConds].matchType = FWP_MATCH_EQUAL;
      conds[numConds].conditionValue.type = FWP_BYTE_BLOB_TYPE;
      conds[numConds].conditionValue.byteBlob = *appId;
      ++numConds;
   }

   *numCondsOut = numConds;

CLEANUP:
   return result;
}
```



 

 




