---
Description: 'Check the access rights that a security descriptor allows for a client.'
ms.assetid: 'de21968e-4590-4798-9152-43204d55521f'
title: Verifying Client Access with ACLs in C++
---

# Verifying Client Access with ACLs in C++

The following example shows how a server could check the access rights that a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) allows for a client. The example uses the [**ImpersonateNamedPipeClient**](impersonatenamedpipeclient.md) function; however, it would work the same using any of the other impersonation functions. After impersonating the client, the example calls the [**OpenThreadToken**](openthreadtoken.md) function to get the [*impersonation token*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly). Then, it calls the [**MapGenericMask**](mapgenericmask.md) function to convert any generic access rights to the corresponding specific and standard rights according to the mapping specified in the [**GENERIC\_MAPPING**](generic-mapping.md) structure.

The [**AccessCheck**](accesscheck.md) function checks the requested access rights against the rights allowed for the client in the DACL of the security descriptor. To check access and generate an entry in the security event log, use the [**AccessCheckAndAuditAlarm**](accesscheckandauditalarm.md) function.


```C++
#include <windows.h>
#pragma comment(lib, "advapi32.lib")

BOOL ImpersonateAndCheckAccess(
  HANDLE hNamedPipe,               // handle of pipe to impersonate
  PSECURITY_DESCRIPTOR pSD,        // security descriptor to check
  DWORD dwAccessDesired,           // access rights to check
  PGENERIC_MAPPING pGeneric,       // generic mapping for object
  PDWORD pdwAccessAllowed          // returns allowed access rights
) 
{
   HANDLE hToken;
   PRIVILEGE_SET PrivilegeSet;
   DWORD dwPrivSetSize = sizeof( PRIVILEGE_SET );
   BOOL fAccessGranted=FALSE;

// Impersonate the client.

   if (! ImpersonateNamedPipeClient(hNamedPipe) ) 
      return FALSE;

// Get an impersonation token with the client's security context.

   if (! OpenThreadToken( GetCurrentThread(), TOKEN_ALL_ACCESS,
         TRUE, &amp;hToken ))
   {
      goto Cleanup;
   }

// Use the GENERIC_MAPPING structure to convert any 
// generic access rights to object-specific access rights.

   MapGenericMask( &amp;dwAccessDesired, pGeneric );

// Check the client's access rights.

   if( !AccessCheck( 
      pSD,                 // security descriptor to check
      hToken,              // impersonation token
      dwAccessDesired,     // requested access rights
      pGeneric,            // pointer to GENERIC_MAPPING
      &amp;PrivilegeSet,       // receives privileges used in check
      &amp;dwPrivSetSize,      // size of PrivilegeSet buffer
      pdwAccessAllowed,    // receives mask of allowed access rights
      &amp;fAccessGranted ))   // receives results of access check
   {
      goto Cleanup;
   }

Cleanup:

   RevertToSelf();

   if (hToken != INVALID_HANDLE_VALUE)
      CloseHandle(hToken);  

   return fAccessGranted;
}
```



 

 



