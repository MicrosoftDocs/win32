---
title: Reserving Ports
description: Following sample code demonstrates how to use the resource assignment layers to reserve a range of ports for administrators.
ms.assetid: 415aa0c9-40d6-4dc9-9ce9-352f52ef7a76
ms.topic: article
ms.date: 05/31/2018
---

# Reserving Ports

The following sample code demonstrates how to use the resource assignment layers to reserve a range of ports for administrators.


```C++
#include <windows.h>
#include <sddl.h>
#include <fwpmu.h>
#include <stdio.h>

#pragma comment(lib, "fwpuclnt.lib")
#pragma comment(lib, "advapi32.lib")

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

#define EXIT_ON_LAST_ERROR(success, fnName) \
   if (!(success)) \
   { \
      result = GetLastError(); \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

DWORD ReservePortRangeForAdmins(
         __in HANDLE engine,
         __in PCWSTR filterName,
         __in_opt const GUID* providerKey,
         __in_opt const GUID* subLayerKey,
         __in UINT16 loPort,
         __in UINT16 hiPort
         )
{
   DWORD result = ERROR_SUCCESS;
   FWPM_FILTER_CONDITION0 conds[2];
   FWP_RANGE0 portRange;
   BOOL success;
   PSECURITY_DESCRIPTOR sd = NULL;
   FWP_BYTE_BLOB sdBlob;
   FWPM_FILTER0 filter;
   BOOL txnInProgress = FALSE;

   //////////
   // The first condition matches any local port in the desired range.
   //////////

   portRange.valueLow.type = FWP_UINT16;
   portRange.valueLow.uint16 = loPort;
   portRange.valueHigh.type = FWP_UINT16;
   portRange.valueHigh.uint16 = hiPort;

   conds[0].fieldKey = FWPM_CONDITION_IP_LOCAL_PORT;
   conds[0].matchType = FWP_MATCH_RANGE;
   conds[0].conditionValue.type = FWP_RANGE_TYPE;
   conds[0].conditionValue.rangeValue = &portRange;

   //////////
   // The second condition matches any user who is a member of the built-in
   // Administrators group.
   //////////

   // For well-known security descriptors, it's easiest to build them in one
   // shot from an SDDL string, rather than constructing them programmatically
   // using lower-level APIs.
   success = ConvertStringSecurityDescriptorToSecurityDescriptorW(
                L"D:(A;;0x1;;;BA)",
                SDDL_REVISION_1,
                &sd,
                NULL
                );
   EXIT_ON_LAST_ERROR(
      success,
      ConvertStringSecurityDescriptorToSecurityDescriptorW
      );

   // Security descriptors must be in self-relative form (i.e., contiguous).
   // The security descriptor returned by
   // ConvertStringSecurityDescriptorToSecurityDescriptorW is already
   // self-relative, but if you're using another mechanism to build the
   // descriptor, you may have to convert it. See MakeSelfRelativeSD for
   // details.
   sdBlob.size = GetSecurityDescriptorLength(sd);
   sdBlob.data = (UINT8*)sd;

   conds[1].fieldKey = FWPM_CONDITION_ALE_USER_ID;
   conds[1].matchType = FWP_MATCH_EQUAL;
   conds[1].conditionValue.type = FWP_SECURITY_DESCRIPTOR_TYPE;
   conds[1].conditionValue.sd = &sdBlob;

   // Fill in the common fields shared by all our filters.
   memset(&filter, 0, sizeof(filter));
   // For MUI compatibility, object names should be indirect strings. See
   // SHLoadIndirectString for details.
   filter.displayData.name = (PWSTR)filterName;
   // Link all objects to our provider. When multiple providers are installed
   // on a computer, this makes it easy to determine who added what.
   filter.providerKey = (GUID*)providerKey;
   // Generally, it's best to add filters to our own sublayer, so we don't have
   // to worry about being overridden by filters added by another provider.
   if (subLayerKey != NULL)
   {
      filter.subLayerKey = *subLayerKey;
   }
   filter.filterCondition = conds;

   // We add all the filters from within a single transaction to make it easy
   // to clean up partial results in error paths.
   result = FwpmTransactionBegin0(engine, 0);
   EXIT_ON_ERROR(FwpmTransactionBegin0);
   txnInProgress = TRUE;

   // Add the filters for IPv4.
   filter.layerKey = FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V4;

   // This filter just has the port range condition, so it blocks all users for
   // the desired port range.
   filter.numFilterConditions = 1;
   filter.action.type = FWP_ACTION_BLOCK;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // This filter permits Administrators for the port range. Since we're using
   // auto-weighting and this filter is more specific than the previous, it
   // will have a higher weight. When an admin tries to bind to a port in the
   // range, this filter will match first, permitting the bind. When a
   // non-admin tries, this filter won't match and the previous filter will
   // block the bind.
   filter.numFilterConditions = 2;
   filter.action.type = FWP_ACTION_PERMIT;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Add the same filters for IPv6.
   filter.layerKey = FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_V6;

   filter.numFilterConditions = 1;
   filter.action.type = FWP_ACTION_BLOCK;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.numFilterConditions = 2;
   filter.action.type = FWP_ACTION_PERMIT;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Once all the adds have succeeded, we commit the transaction to atomically
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
   LocalFree(sd);
   return result;
}
```



## Related topics

<dl> <dt>

[**Filtering Conditions Available at Each Filtering Layer**](filtering-conditions-available-at-each-filtering-layer.md)
</dt> </dl>

 

 




