---
title: Hindering Filter Deletion
description: Following example code demonstrates how to make a filter difficult to delete by setting a DACL.
ms.assetid: 83c336fa-983e-4e17-86b3-3a42f4824c74
ms.topic: article
ms.date: 05/31/2018
---

# Hindering Filter Deletion

The following example code demonstrates how to make a filter difficult to delete by setting a DACL.


```C++
#include <windows.h>
#include <accctrl.h>
#include <aclapi.h>
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

DWORD HinderFilterDeletion(
         __in HANDLE engine,
         __in const GUID* filterKey
         )
{
   DWORD result = ERROR_SUCCESS;
   EXPLICIT_ACCESS_W access;
   SID worldSid =
   {
      SID_REVISION,
      1,
      SECURITY_WORLD_SID_AUTHORITY,
      { SECURITY_WORLD_RID }
   };
   PACL acl = NULL;

   // Deny certain access rights to the world:
   //    DELETE - prevents the object from being deleted.
   //    WRITE_DAC - prevents someone from granting themselves DELETE access.
   //       Note that the owner always has WRITE_DAC access.
   //    WRITE_OWNER - prevents someone from taking ownership. Note that anyone
   //       with the TakeOwnership privilege enabled always has WRITE_OWNER
   //       access.
   access.grfAccessPermissions = ( DELETE | WRITE_DAC | WRITE_OWNER );
   access.grfAccessMode = DENY_ACCESS;
   access.grfInheritance = 0;
   BuildTrusteeWithSid(&(access.Trustee), &worldSid);

   result = SetEntriesInAcl(1, &access, NULL, &acl);
   EXIT_ON_ERROR(SetEntriesInAcl);

   // We don't protect the new DACL because we still want the default ACEs to
   // be inherited. The deny ACE we're setting will come before (and thus
   // override) the inherited ACEs.
   result = FwpmFilterSetSecurityInfoByKey0(
               engine,
               filterKey,
               DACL_SECURITY_INFORMATION,
               NULL,
               NULL,
               acl,
               NULL
               );
   EXIT_ON_ERROR(FwpmFilterSetSecurityInfo0);

CLEANUP:
   LocalFree(acl);
   return result;
}

DWORD wmain(int argc,
            wchar_t* argv[])
{
   UNREFERENCED_PARAMETER(argc);
   UNREFERENCED_PARAMETER(argv);
   static const GUID guid = 
    { 0x836a4ff0, 0x7c26, 0x47d2, { 0xb9, 0x6d, 0x68, 0x70, 0xa, 0x98, 0x31, 0x18 } };
   
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
   
   // Add a filter
   FWPM_FILTER0 filter;
   memset(&filter, 0, sizeof(filter));
   filter.filterKey = guid;
   filter.displayData.name = L"MihaelaTestFilter";
   filter.action.type = FWP_ACTION_BLOCK;
   filter.layerKey = FWPM_LAYER_INBOUND_IPPACKET_V4;
   result = FwpmFilterAdd0(engineHandle, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);   

   // Block the removal of the filter    
   result = HinderFilterDeletion(engineHandle, &guid);

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



 

 




