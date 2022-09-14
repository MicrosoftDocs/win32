---
title: Forcing Filter Deletion
description: Following sample code demonstrates how to make a user with the TakeOwnership privilege capable of deleting a filter.
ms.assetid: f0a3de8e-6d3f-45d3-af42-b8ae62278667
ms.topic: article
ms.date: 05/31/2018
---

# Forcing Filter Deletion

The following sample code demonstrates how to make a user with the TakeOwnership privilege capable of deleting a filter.

> [!Note]  
> A setup application might use this feature during an uninstall to ensure that all objects are successfully deleted.

 


```C++
#include <windows.h>
#include <stdio.h>
#include <accctrl.h>
#include <aclapi.h>
#include <fwpmu.h>

#pragma comment(lib, "fwpuclnt.lib")
#pragma comment(lib, "advapi32.lib")

#define EXIT_ON_ERROR(err) if((err) != ERROR_SUCCESS) {goto CLEANUP;}

#define EXIT_ON_LAST_ERROR(success, fnName) \
   if (!(success)) \
   { \
      result = GetLastError(); \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

#define EXIT_ON_ALLOC_FAILURE(ptr, fnName) \
   if ((ptr) == NULL) \
   { \
      result = ERROR_NOT_ENOUGH_MEMORY; \
      printf(#fnName " = ERROR_NOT_ENOUGH_MEMORY\n"); \
      goto CLEANUP; \
   }


DWORD ForceFilterDeletion(__in const GUID* filterKey)
{
   DWORD result = ERROR_SUCCESS;
   BOOL success;
   HANDLE token = NULL;
   DWORD userLen, oldPrivLen;
   TOKEN_USER* user = NULL;
   TOKEN_PRIVILEGES oldPriv, newPriv;
   BOOL takeOwnershipEnabled = FALSE;
   HANDLE engine = NULL;
   EXPLICIT_ACCESS_W access;
   PACL acl = NULL;

   // This assumes that the current thread is not impersonating. If it is
   // impersonating, you need to call OpenThreadToken instead.
   success = OpenProcessToken(
                GetCurrentProcess(),
                ( TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY ),
                &token
                );
   EXIT_ON_LAST_ERROR(success, OpenProcessToken);

   // Get our SID -- we'll use this to make ourselves owner.
   success = GetTokenInformation(
                token,
                TokenUser,
                NULL,
                0,
                &userLen
                );
   result = success ? ERROR_INVALID_DATA : GetLastError();
   if (result != ERROR_INSUFFICIENT_BUFFER)
   {
      EXIT_ON_ERROR(result);
   }

   user = (TOKEN_USER*)HeapAlloc(GetProcessHeap(), 0, userLen);
   EXIT_ON_ALLOC_FAILURE(user, HeapAlloc);

   success = GetTokenInformation(
                token,
                TokenUser,
                user,
                userLen,
                &userLen
                );
   EXIT_ON_LAST_ERROR(success, GetTokenInformation);

   newPriv.PrivilegeCount = 1;
   success = LookupPrivilegeValueW(
                NULL,
                SE_TAKE_OWNERSHIP_NAME,
                &(newPriv.Privileges[0].Luid)
                );
   EXIT_ON_LAST_ERROR(success, LookupPrivilegeValueW);
   newPriv.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;

   // Enable the TakeOwnership privilege. This must be done before the call to
   // FwpmEngineOpen0. The token used for authentication during the call to
   // FwpmEngineOpen0 is used for all future access checks as well.
   success = AdjustTokenPrivileges(
                token,
                FALSE,
                &newPriv,
                sizeof(oldPriv),
                &oldPriv,
                &oldPrivLen
                );
   EXIT_ON_LAST_ERROR(success, AdjustTokenPrivileges);

   // Check if anything changed, so we can restore the privilege to its
   // previous state.
   if (oldPriv.PrivilegeCount == 1)
   {
      takeOwnershipEnabled = TRUE;
   }

   // The authentication service should always be RPC_C_AUTHN_DEFAULT.
   result = FwpmEngineOpen0(
               NULL,
               RPC_C_AUTHN_DEFAULT,
               NULL,
               NULL,
               &engine
               );
   EXIT_ON_ERROR(result);

   // Make ourselves owner. This will succeed since anyone with the
   // TakeOwnership privilege enabled automatically has WRITE_OWNER access.
   result = FwpmFilterSetSecurityInfoByKey0(
               engine,
               filterKey,
               OWNER_SECURITY_INFORMATION,
               (const SID*)user->User.Sid,
               NULL,
               NULL,
               NULL
               );
   EXIT_ON_ERROR(result);

   access.grfAccessPermissions = DELETE;
   access.grfAccessMode = GRANT_ACCESS;
   access.grfInheritance = 0;
   BuildTrusteeWithSid(&(access.Trustee), user->User.Sid);

   result = SetEntriesInAcl(1, &access, NULL, &acl);
   EXIT_ON_ERROR(result);

   // Grant ourselves delete access. This will succeed since the owner
   // automatically has WRITE_DAC access.
   result = FwpmFilterSetSecurityInfoByKey0(
               engine,
               filterKey,
               DACL_SECURITY_INFORMATION,
               NULL,
               NULL,
               acl,
               NULL
               );
   EXIT_ON_ERROR(result);

   // Delete the filter. This will succeed since we just granted ourselves
   // delete access.
   result = FwpmFilterDeleteByKey0(engine, filterKey);
   EXIT_ON_ERROR(result);

CLEANUP:
   LocalFree(acl);
   // FwpmEngineClose0 accepts null engine handles, so we needn't precheck for
   // null.
   FwpmEngineClose0(engine);
   if (takeOwnershipEnabled)
   {
      newPriv.Privileges[0].Attributes = 0;
      AdjustTokenPrivileges(
         token,
         FALSE,
         &newPriv,
         0,
         NULL,
         0
         );
   }
   HeapFree(GetProcessHeap(), 0, user);
   if (token != NULL)
   {
      CloseHandle(token);
   }
   return result;
}

DWORD wmain(int argc,
            wchar_t* argv[])
{
   UNREFERENCED_PARAMETER(argc);
   UNREFERENCED_PARAMETER(argv);
   
   static const GUID guid = { 0x836a4ff0, 0x7c26, 0x47d2, { 0xb9, 0x6d, 0x68, 0x70, 0xa, 0x98, 0x31, 0x18 } };
   
   // Open a session to the filter engine
   HANDLE engineHandle = 0;

   // Use dynamic sessions for efficiency and safety:
   //  - All objects associated with the dynamic session are deleted with one call.
   //  - Filtering policy objects are deleted even when the application crashes. 
   FWPM_SESSION0 session;
   memset(&session, 0, sizeof(session));
   session.flags = FWPM_SESSION_FLAG_DYNAMIC;
   session.sessionKey = guid;

   DWORD result = FwpmEngineOpen0(NULL, RPC_C_AUTHN_WINNT, NULL, &session, &engineHandle);
   EXIT_ON_ERROR(result);   
   
   // Add a filter
   FWPM_FILTER0 filter;
   memset(&filter, 0, sizeof(filter));
   filter.filterKey = guid;
   filter.displayData.name = L"MihaelaTestFilter";
   filter.action.type = FWP_ACTION_BLOCK;
   filter.layerKey = FWPM_LAYER_INBOUND_IPPACKET_V4;
   
   result = FwpmFilterAdd0(engineHandle, &filter, NULL, NULL);
   EXIT_ON_ERROR(result);   

   // Delete the newly added filter
   result = ForceFilterDeletion(&guid);
   EXIT_ON_ERROR(result);

   printf("Success.\n");
   
CLEANUP:
   FwpmEngineClose0(engineHandle);

   return result;
}
```



 

 




