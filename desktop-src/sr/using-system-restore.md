---
title: Using System Restore
description: The following examples demonstrate how to create and cancel restore points using the SRSetRestorePoint function.
ms.assetid: 98c79305-3659-4d1a-8165-bb6e451e2d1e
keywords:
- System Restore, using
ms.topic: article
ms.date: 05/31/2018
---

# Using System Restore

The following examples demonstrate how to create and cancel restore points using the [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) function.

The first step to using using System Restore is setting up the COM calls to [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity). This is required for any process that uses the [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) function. The NetworkService, LocalService, and System must be allowed make calls to the process. The following **InitializeCOMSecurity** function is an example of how to initialize COM security. You may need to modify the parameters to the **CoInitializeSecurity** function for your application.


```C++
#include <stdio.h>
#include <windows.h>
#include <accctrl.h>
#include <aclapi.h>
#include <objbase.h>
#include <strsafe.h>
#include <srrestoreptapi.h>

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "advapi32.lib")

typedef BOOL (WINAPI *PFN_SETRESTOREPTW) (PRESTOREPOINTINFOW, PSTATEMGRSTATUS);

BOOL InitializeCOMSecurity()
{   
    // Create the security descriptor explicitly as follows because
    // CoInitializeSecurity() will not accept the relative security descriptors  
    // returned by ConvertStringSecurityDescriptorToSecurityDescriptor().

    SECURITY_DESCRIPTOR securityDesc = {0};
    EXPLICIT_ACCESS   ea[5] = {0};
    ACL        *pAcl = NULL;
    ULONGLONG  rgSidBA[(SECURITY_MAX_SID_SIZE+sizeof(ULONGLONG)-1)/sizeof(ULONGLONG)]={0};
    ULONGLONG  rgSidLS[(SECURITY_MAX_SID_SIZE+sizeof(ULONGLONG)-1)/sizeof(ULONGLONG)]={0};
    ULONGLONG  rgSidNS[(SECURITY_MAX_SID_SIZE+sizeof(ULONGLONG)-1)/sizeof(ULONGLONG)]={0};
    ULONGLONG  rgSidPS[(SECURITY_MAX_SID_SIZE+sizeof(ULONGLONG)-1)/sizeof(ULONGLONG)]={0};
    ULONGLONG  rgSidSY[(SECURITY_MAX_SID_SIZE+sizeof(ULONGLONG)-1)/sizeof(ULONGLONG)]={0};
    DWORD      cbSid = 0;
    BOOL       fRet = FALSE;
    DWORD      dwRet = ERROR_SUCCESS;
    HRESULT    hrRet = S_OK;

    //
    // This creates a security descriptor that is equivalent to the following 
    // security descriptor definition language (SDDL) string:
    //
    //   O:BAG:BAD:(A;;0x1;;;LS)(A;;0x1;;;NS)(A;;0x1;;;PS)(A;;0x1;;;SY)(A;;0x1;;;BA)
    //
 
    // Initialize the security descriptor.
    fRet = ::InitializeSecurityDescriptor( &securityDesc, SECURITY_DESCRIPTOR_REVISION );
    if( !fRet )
    {
        goto exit;
    }

    // Create an administrator group security identifier (SID).
    cbSid = sizeof( rgSidBA );
    fRet = ::CreateWellKnownSid( WinBuiltinAdministratorsSid, NULL, rgSidBA, &cbSid );
    if( !fRet )
    {
        goto exit;
    }

    // Create a local service security identifier (SID).
    cbSid = sizeof( rgSidLS );
    fRet = ::CreateWellKnownSid( WinLocalServiceSid, NULL, rgSidLS, &cbSid );
    if( !fRet )
    {
        goto exit;
    }

    // Create a network service security identifier (SID).
    cbSid = sizeof( rgSidNS );
    fRet = ::CreateWellKnownSid( WinNetworkServiceSid, NULL, rgSidNS, &cbSid );
    if( !fRet )
    {
        goto exit;
    }

    // Create a personal account security identifier (SID).
    cbSid = sizeof( rgSidPS );
    fRet = ::CreateWellKnownSid( WinSelfSid, NULL, rgSidPS, &cbSid );
    if( !fRet )
    {
        goto exit;
    }

    // Create a local service security identifier (SID).
    cbSid = sizeof( rgSidSY );
    fRet = ::CreateWellKnownSid( WinLocalSystemSid, NULL, rgSidSY, &cbSid );
    if( !fRet )
    {
        goto exit;
    }

    // Setup the access control entries (ACE) for COM. You may need to modify 
    // the access permissions for your application. COM_RIGHTS_EXECUTE and
    // COM_RIGHTS_EXECUTE_LOCAL are the minimum access rights required.

    ea[0].grfAccessPermissions = COM_RIGHTS_EXECUTE | COM_RIGHTS_EXECUTE_LOCAL;
    ea[0].grfAccessMode = SET_ACCESS;
    ea[0].grfInheritance = NO_INHERITANCE;
    ea[0].Trustee.pMultipleTrustee = NULL;
    ea[0].Trustee.MultipleTrusteeOperation = NO_MULTIPLE_TRUSTEE;
    ea[0].Trustee.TrusteeForm = TRUSTEE_IS_SID;
    ea[0].Trustee.TrusteeType = TRUSTEE_IS_GROUP;
    ea[0].Trustee.ptstrName = (LPTSTR)rgSidBA;

    ea[1].grfAccessPermissions = COM_RIGHTS_EXECUTE | COM_RIGHTS_EXECUTE_LOCAL;
    ea[1].grfAccessMode = SET_ACCESS;
    ea[1].grfInheritance = NO_INHERITANCE;
    ea[1].Trustee.pMultipleTrustee = NULL;
    ea[1].Trustee.MultipleTrusteeOperation = NO_MULTIPLE_TRUSTEE;
    ea[1].Trustee.TrusteeForm = TRUSTEE_IS_SID;
    ea[1].Trustee.TrusteeType = TRUSTEE_IS_GROUP;
    ea[1].Trustee.ptstrName = (LPTSTR)rgSidLS;

    ea[2].grfAccessPermissions = COM_RIGHTS_EXECUTE | COM_RIGHTS_EXECUTE_LOCAL;
    ea[2].grfAccessMode = SET_ACCESS;
    ea[2].grfInheritance = NO_INHERITANCE;
    ea[2].Trustee.pMultipleTrustee = NULL;
    ea[2].Trustee.MultipleTrusteeOperation = NO_MULTIPLE_TRUSTEE;
    ea[2].Trustee.TrusteeForm = TRUSTEE_IS_SID;
    ea[2].Trustee.TrusteeType = TRUSTEE_IS_GROUP;
    ea[2].Trustee.ptstrName = (LPTSTR)rgSidNS;

    ea[3].grfAccessPermissions = COM_RIGHTS_EXECUTE | COM_RIGHTS_EXECUTE_LOCAL;
    ea[3].grfAccessMode = SET_ACCESS;
    ea[3].grfInheritance = NO_INHERITANCE;
    ea[3].Trustee.pMultipleTrustee = NULL;
    ea[3].Trustee.MultipleTrusteeOperation = NO_MULTIPLE_TRUSTEE;
    ea[3].Trustee.TrusteeForm = TRUSTEE_IS_SID;
    ea[3].Trustee.TrusteeType = TRUSTEE_IS_GROUP;
    ea[3].Trustee.ptstrName = (LPTSTR)rgSidPS;

    ea[4].grfAccessPermissions = COM_RIGHTS_EXECUTE | COM_RIGHTS_EXECUTE_LOCAL;
    ea[4].grfAccessMode = SET_ACCESS;
    ea[4].grfInheritance = NO_INHERITANCE;
    ea[4].Trustee.pMultipleTrustee = NULL;
    ea[4].Trustee.MultipleTrusteeOperation = NO_MULTIPLE_TRUSTEE;
    ea[4].Trustee.TrusteeForm = TRUSTEE_IS_SID;
    ea[4].Trustee.TrusteeType = TRUSTEE_IS_GROUP;
    ea[4].Trustee.ptstrName = (LPTSTR)rgSidSY;

    // Create an access control list (ACL) using this ACE list.
    dwRet = ::SetEntriesInAcl( ARRAYSIZE( ea ), ea, NULL, &pAcl );
    if( dwRet != ERROR_SUCCESS || pAcl == NULL )
    {
        fRet = FALSE;
        goto exit;
    }

    // Set the security descriptor owner to Administrators.
    fRet = ::SetSecurityDescriptorOwner( &securityDesc, rgSidBA, FALSE );
    if( !fRet )
    {
        goto exit;
    }

    // Set the security descriptor group to Administrators.
    fRet = ::SetSecurityDescriptorGroup( &securityDesc, rgSidBA, FALSE );
    if( !fRet )
    {
        goto exit;
    }

    // Set the discretionary access control list (DACL) to the ACL.
    fRet = ::SetSecurityDescriptorDacl( &securityDesc, TRUE, pAcl, FALSE );
    if( !fRet )
    {
        goto exit;
    }

    // Initialize COM. You may need to modify the parameters of
    // CoInitializeSecurity() for your application. Note that an
    // explicit security descriptor is being passed down.
 
    hrRet = ::CoInitializeSecurity( &securityDesc,
                                    -1,
                                    NULL,
                                    NULL,
                                    RPC_C_AUTHN_LEVEL_PKT_PRIVACY,
                                    RPC_C_IMP_LEVEL_IDENTIFY,
                                    NULL,
                                    EOAC_DISABLE_AAA | EOAC_NO_CUSTOM_MARSHAL,
                                    NULL );
    if( FAILED( hrRet ) )
    {
        fRet = FALSE;
        goto exit;
    }

    fRet = TRUE;

 exit:

    ::LocalFree( pAcl );

    return fRet;
}
    
```



## Example 1: Create a restore point.


```C++
#include <windows.h>
#include <accctrl.h>
#include <aclapi.h>
#include <objbase.h>
#include <strsafe.h>
#include <srrestoreptapi.h>

typedef BOOL (WINAPI *PFN_SETRESTOREPTW) (PRESTOREPOINTINFOW, PSTATEMGRSTATUS);

extern "C" int __cdecl wmain(int argc, WCHAR **argv)
{
   RESTOREPOINTINFOW RestorePtInfo;
   STATEMGRSTATUS SMgrStatus;
   PFN_SETRESTOREPTW fnSRSetRestorePointW=NULL;
   DWORD dwErr = ERROR_SUCCESS;
   HMODULE hSrClient = NULL;
   BOOL fRet = FALSE;
   HRESULT hr = S_OK;

   UNREFERENCED_PARAMETER(argc);
   UNREFERENCED_PARAMETER(argv);
   
   hr = CoInitializeEx( NULL, COINIT_MULTITHREADED );
   if( FAILED( hr ) )
   {
       wprintf( L"Unexpected error: CoInitializeEx() failed with 0x%08x\n", hr );
       goto exit;
   }

   // Initialize COM security to enable NetworkService,
   // LocalService and System to make callbacks to the process 
   // calling  System Restore. This is required for any process
   // that calls SRSetRestorePoint.
    
   fRet = InitializeCOMSecurity();
   if( !fRet )
   {
       wprintf( L"Unexpected error: failed to initialize COM security\n" );
       goto exit;
   }
    
   // Initialize the RESTOREPOINTINFO structure
   RestorePtInfo.dwEventType = BEGIN_SYSTEM_CHANGE;

   // Notify the system that changes are about to be made.
   // An application is to be installed.
   RestorePtInfo.dwRestorePtType = APPLICATION_INSTALL;

   // RestPtInfo.llSequenceNumber must be 0 when creating a restore point.
   RestorePtInfo.llSequenceNumber = 0;

   // String to be displayed by System Restore for this restore point.
   StringCbCopyW(RestorePtInfo.szDescription, 
            sizeof(RestorePtInfo.szDescription), 
            L"First Restore Point");
   
   // Load the DLL, which may not exist on Windows server
   hSrClient = LoadLibraryW(L"srclient.dll");
   if(NULL == hSrClient)
   {
      wprintf(L"System Restore is not present.\n");
      goto exit;
   }

   // If the library is loaded, find the entry point
   fnSRSetRestorePointW = (PFN_SETRESTOREPTW) GetProcAddress(
      hSrClient, "SRSetRestorePointW");
   if (NULL == fnSRSetRestorePointW)
   {
      wprintf(L"Failed to find SRSetRestorePointW.\n");
      goto exit;
   }

   fRet = fnSRSetRestorePointW(&RestorePtInfo, &SMgrStatus);
   if(!fRet)
   {
      dwErr = SMgrStatus.nStatus;
      if(dwErr == ERROR_SERVICE_DISABLED)
      {
         wprintf(L"System Restore is turned off.\n");
         goto exit;
      }
      wprintf(L"Failure to create the restore point; error=%u.\n", dwErr);
      goto exit;
   }

   wprintf(L"Restore point created; number=%I64d.\n", SMgrStatus.llSequenceNumber);

   // The application performs some installation operations here.

   // It is not necessary to call SrSetRestorePoint to indicate that the 
   // installation is complete except in the case of ending a nested 
   // restore point. Every BEGIN_NESTED_SYSTEM_CHANGE must have a 
   // corresponding END_NESTED_SYSTEM_CHANGE or the application cannot 
   // create new restore points.

   // Update the RESTOREPOINTINFO structure to notify the 
   // system that the operation is finished.
   RestorePtInfo.dwEventType = END_SYSTEM_CHANGE;

   // End the system change by using the sequence number 
   // received from the first call to SRSetRestorePoint.
   RestorePtInfo.llSequenceNumber = SMgrStatus.llSequenceNumber;

   // Notify the system that the operation is done and that this
   // is the end of the restore point.
   fRet = fnSRSetRestorePointW(&RestorePtInfo, &SMgrStatus);
   if(!fRet) 
   {
      dwErr = SMgrStatus.nStatus;
      wprintf(L"Failure to end the restore point; error=%u.\n", dwErr);
      goto exit;
   }

exit:

   if(hSrClient != NULL)
   {
      FreeLibrary(hSrClient);
      hSrClient = NULL;
   }

   return 0;
}
```



## Example 2: Create and cancel a restore point.


```C++
#include <stdio.h>
#include <windows.h>
#include <accctrl.h>
#include <aclapi.h>
#include <objbase.h>
#include <strsafe.h>
#include <srrestoreptapi.h>

typedef BOOL (WINAPI *PFN_SETRESTOREPTW) (PRESTOREPOINTINFOW, PSTATEMGRSTATUS);

extern "C" int __cdecl wmain(int argc, WCHAR** argv)
{
   RESTOREPOINTINFOW RestorePtInfo;
   STATEMGRSTATUS SMgrStatus;
   PFN_SETRESTOREPTW fnSRSetRestorePointW = NULL;
   DWORD dwErr = ERROR_SUCCESS;
   HMODULE hSrClient = NULL;
   BOOL fRet = FALSE;
   HRESULT hr = S_OK;    

   UNREFERENCED_PARAMETER(argc);
   UNREFERENCED_PARAMETER(argv);
   
   hr = CoInitializeEx( NULL, COINIT_MULTITHREADED );
   if( FAILED( hr ) )
   {
       wprintf( L"Unexpected error: CoInitializeEx() failed with 0x%08x\n", hr );
       goto exit;
   }

   // Initialize COM security to enable NetworkService,
   // LocalService and System to make callbacks to the process 
   // calling  System Restore. This is required for any process
   // that calls SRSetRestorePoint.
    
   fRet = InitializeCOMSecurity();
   if( !fRet )
   {
       wprintf( L"Unexpected error: failed to initialize COM security\n" );
       goto exit;
   }
    
   // Initialize the RESTOREPOINTINFO structure.
   RestorePtInfo.dwEventType=BEGIN_SYSTEM_CHANGE;
   RestorePtInfo.dwRestorePtType=APPLICATION_INSTALL; 
   RestorePtInfo.llSequenceNumber=0;
   StringCbCopyW(RestorePtInfo.szDescription, 
            sizeof(RestorePtInfo.szDescription), 
            L"Sample Restore Point");

   // Load the DLL, which may not exist on Windows server
   hSrClient = LoadLibraryW(L"srclient.dll");
   if(NULL == hSrClient)
   {
      wprintf(L"System Restore is not present.\n");
      goto exit;
   }

   // If the library is loaded, find the entry point
   fnSRSetRestorePointW = (PFN_SETRESTOREPTW) GetProcAddress(
      hSrClient, "SRSetRestorePointW");
   if (NULL == fnSRSetRestorePointW)
   {
      wprintf(L"Failed to find SRSetRestorePointW.\n");
      goto exit;
   }

   fRet = fnSRSetRestorePointW(&RestorePtInfo, &SMgrStatus);
   if(!fRet)
   {
      dwErr = SMgrStatus.nStatus;
      if(dwErr == ERROR_SERVICE_DISABLED)
      {
         wprintf(L"System Restore is turned off.\n");
         goto exit;
      }
      wprintf(L"Failure to create the restore point; error=%u.\n", dwErr);
      goto exit;
   }

   wprintf(L"Restore point set. Restore point data:\n");
   wprintf(L"\tSequence Number=%I64d\n",SMgrStatus.llSequenceNumber);
   wprintf(L"\tStatus=%u\n",SMgrStatus.nStatus);

   // Update the structure to cancel the previous restore point.
   RestorePtInfo.dwEventType=END_SYSTEM_CHANGE;
   RestorePtInfo.dwRestorePtType=CANCELLED_OPERATION;
   // This is the sequence number returned by the previous call.
   RestorePtInfo.llSequenceNumber=SMgrStatus.llSequenceNumber; 

   // Cancel the previous restore point
   fRet = fnSRSetRestorePointW(&RestorePtInfo, &SMgrStatus);
   if(!fRet) 
   {
      dwErr = SMgrStatus.nStatus;
      wprintf(L"Failure to cancel the restore point; error=%u.\n", dwErr);
      goto exit;
   }

   wprintf(L"Restore point canceled. Restore point data:\n");
   wprintf(L"\tSequence Number=%I64d\n",SMgrStatus.llSequenceNumber);
   wprintf(L"\tStatus=%u\n",SMgrStatus.nStatus);

exit: 

   if(hSrClient != NULL)
   {
      FreeLibrary(hSrClient);
      hSrClient = NULL;
   }

   return 0;
}
```



 

 