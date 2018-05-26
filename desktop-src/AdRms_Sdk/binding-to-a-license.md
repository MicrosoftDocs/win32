---
Description: Binding to a license is the key to exercising the rights that the license grants.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9f7ef9be-6cad-42ab-be9b-a1492f251f8c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Binding to a License
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Binding to a License

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Binding to a license is the key to exercising the rights that the license grants. To bind to a license, call [**DRMCreateBoundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateboundlicense?branch=master) and specify the following items. Specifying **NULL** for the principal or the rights group causes the license to bind to the first item of each type in the license.

-   The principal (user)
-   The content ID
-   The rights group (currently only one is available)
-   The rights requested

When an application calls [**DRMCreateBoundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateboundlicense?branch=master), the rights management system verifies that the user can exercise the right or rights requested (in the environment supplied), and returns a handle to the license. The license contains only the rights that the user has requested and information pertaining to that user and those rights. If any of the requested rights are not granted, the call fails.

The following code example, from [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md), retrieves an end-user license chain from the certificate store, acquires the end-user license from the chain, and binds the license to the EDIT right.


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_GetBoundLicense.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetBoundLicense function binds an end user license to the
// EDIT right and returns a pointer to the license handle.
//
HRESULT GetBoundLicense (
          DRMHSESSION       hClient, 
          DRMENVHANDLE      hEnv,
          DRMHANDLE         hLib,
          PWSTR             pwszRAC,
          PWSTR             pwszSignedIL,
          DRMHANDLE*        phBoundLic)
{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //   hr........................Return value                     
  //   pwszEULChain..............End user license chain
  //   pwszEUL...................End user license
  //   pwszContentID.............Content ID string
  //   uiEUL.....................Number of characters in the EUL
  //   hEnablingPrin.............Enabling principal used for binding
  //   hLicenseStorage...........Handle to license storage session
  //   DW_WAIT_TIME..............Maximum time to wait for signal
  //   dwWaitResult..............Actual time of wait for signal
  //   idNULL....................DRMID structure
  //   idContent.................Structure for binding a license
  //   oParams...................Structure for binding a license
  //   idStandardEP..............Structure for enabling principal
  //   context...................Callback context
  HRESULT       hr               = S_OK;
  PWSTR         pwszEULChain     = NULL;
  PWSTR         pwszEUL          = NULL;
  PWSTR         pwszContentID    = NULL;
  UINT          uiEUL            = 0;
  DRMHANDLE     hEnablingPrin    = NULL;
  DRMHSESSION   hLicenseStorage  = NULL;
  const DWORD   DW_WAIT_TIME     = 60000;
  DWORD         dwWaitResult     = 0;
  DRMID         idContent;
  DRMID         idStandardEP;
  DRMID         idNULL;
  DRM_CONTEXT   context;
  DRMBOUNDLICENSEPARAMS oParams;

  wprintf(L"\r\nEntering GetBoundLicense.\r\n");

  // Create a license storage session.
  hr = DRMCreateLicenseStorageSession( 
          hEnv,                       // Environment handle
          hLib,                       // Library handle
          hClient,                    // Client session handle
          0,                          // Reserved
          pwszSignedIL,               // Signed issuance license
          &amp;hLicenseStorage );         // License storage handle
  if(FAILED(hr)) goto e_Exit; 
  wprintf(L"DRMCreateLicenseStorageSession: hLicenseStorage=%i\r\n",
          hLicenseStorage);

  // Initialize the callback context.
  context.hEvent   = NULL;            // Event handle
  context.pwszData = NULL;            // Signed license

  // Create an event to signal when the license has been acquired.
  context.hEvent = CreateEvent(
          NULL,                       // No attributes
          FALSE,                      // Automatic reset
          FALSE,                      // Initial state not signaled
          NULL);                      // Event object not named
  if(NULL == context.hEvent) goto e_Exit;

  // Call DRMAcquireLicense, which will put the end-user license 
  // into the permanent license store for you by default, or specify 
  // DRM_AL_NOPERSIST if you want to put the license into the  
  // temporary store and handle storage and management yourself. 
 hr = DRMAcquireLicense( 
          hLicenseStorage,            // Storage session handle
          0,                          // No flags set
          NULL,                       // No RAC specified
          NULL,                       // Reserved
          NULL,                       // Custom data
          NULL,                       // Optional license URL
          (VOID*)&amp;context);           // Callback context
 if(FAILED(hr)) goto e_Exit;

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
  if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) goto e_Exit;

  // Enumerate the end user license chain from the license store.
  // Note:  This example assumes that there is only one EUL in the 
  //        license  store. If others exist, you can increment the  
  //        index of the DRMEnumerateLicense function until you  
  //        receive an E_DRM_NO_MORE_DATA error to ensure that you 
  //        have tried all of the possible EULs for this content.
  hr = GetCertificate(
          hLicenseStorage,            // License storage session
          DRM_EL_EUL,                 // Certificate type
          &amp;pwszEULChain);             // EUL chain
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszEULChain) succeeded.\r\n");

  // Retrieve the EUL from the EUL chain.
  //    - Call DRMDeconstructCertificateChain once to retrieve the
  //      length of the license.
  //    - Allocate memory for the license.
  //    - Call DRMDeconstructCertificateChain again to retrieve the
  //      license.
  hr = DRMDeconstructCertificateChain( 
          pwszEULChain,               // The EUL certificate chain
          0,                          // Index of certificate
          &amp;uiEUL,                     // Certificate length
          NULL);
  if (FAILED(hr)) goto e_Exit;

  // Allocate memory for the end user license.
  pwszEUL = new WCHAR[uiEUL];
  if (NULL == pwszEUL)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }

  hr = DRMDeconstructCertificateChain( 
          pwszEULChain,               // The EUL certificate chain
          0,                          // Item 0 is the EUL
          &amp;uiEUL,                     // Certificate length
          pwszEUL);                   // End user license
 if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMDeconstructCertificateChain succeeded.\r\n");


  // Retrieve the content ID from the end user license.
  hr = GetContentID(
          pwszEUL,                    // End user license
          &amp;pwszContentID);            // Content ID string
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetContentID: pwszContentID = \r\n", pwszContentID);

  // Create an enabling principal.
  SecureZeroMemory(&amp;idNULL, sizeof(idNULL));
  SecureZeroMemory(&amp;idStandardEP, sizeof(idStandardEP));
 idStandardEP.wszIDType = L"ASCII Tag"; 
 idStandardEP.wszID     = L"UDStdPlg Enabling Principal";

  hr = DRMCreateEnablingPrincipal ( 
          hEnv,                     // Secure environment handle 
          hLib,                     // Library handle 
          idStandardEP.wszID,       // Enabling principal type 
          &amp;idNULL,                  // DRMID structure 
          pwszRAC,                  // Current RAC 
          &amp;hEnablingPrin);          // Enabling principal handle 
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateEnablingPrincipal succeeded.\r\n");

  // Bind the end user license to the EDIT right. The content ID 
  // defined by the pwszContentID parameter is the same as that 
  // defined when creating the issuance license.
  SecureZeroMemory(&amp;idContent, sizeof(idContent));
 idContent.wszIDType         = L"MS-GUID"; 
 idContent.wszID             = pwszContentID;

  SecureZeroMemory(&amp;oParams, sizeof(oParams));
 oParams.hEnablingPrincipal = hEnablingPrin; 
 oParams.wszRightsRequested = L"EDIT";
 oParams.wszRightsGroup     = L"Main-Rights"; 
 oParams.idResource         = idContent; 

  // Create a bound license.
  hr = DRMCreateBoundLicense ( 
          hEnv,                    // Secure environment handle 
          &amp;oParams,                // Additional license options 
          pwszEULChain,            // EUL chain
          phBoundLic,              // Handle to bound license 
          NULL);                   // Reserved 
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateBoundLicense: hBoundLic = %i\r\n", *phBoundLic);

e_Exit:

  if (NULL != hLicenseStorage)
  {
    hr = DRMCloseSession(hLicenseStorage);
    hLicenseStorage = NULL;
  }
  if (NULL != pwszEULChain)
  {
    delete [] pwszEULChain;
    pwszEULChain = NULL;
  }
  if (NULL != pwszEUL)
  {
    delete [] pwszEUL;
    pwszEUL = NULL;
  }

  wprintf(L"Leaving GetBoundLicense: hr = %x\r\n", hr);
  return hr;
}
```



When binding to a license, it is possible that you will encounter the following complications:

-   If a requested right is denied, binding will fail. When at least one of the rights you request is denied, [**DRMCreateBoundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateboundlicense?branch=master) returns **E\_DRM\_BIND\_RIGHT\_NOT\_GRANTED**. It is recommended that you call [**DRMParseUnboundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmparseunboundlicense?branch=master) to parse the unbound license to determine what rights can be granted. For more information, see [Querying Licenses](querying-licenses.md).
-   Information about rights not granted is removed from the bound license.
-   The same right can be granted in multiple rights groups.
-   XrML allows a symmetric content key to be associated with a license, a work, a rights group, or an individual right. If your application determines that the granted rights are not all associated with the same file, you must handle the differences appropriately.
-   You must determine what additional rights to request when requesting the EDIT right. For example, if your application grants the EDIT right to another application, you must identify the additional rights to grant so that the content can be edited. With the EDIT right, the PLAY and VIEW rights are assumed, but you must also decide whether you will allow the user to print, copy, or perform other actions. For more information, see [Understanding XrML Rights](understanding-xrml-rights.md)
-   The rights you want to request can be distributed among more than one end-user license. If the desired rights are distributed across several licenses, you can bind to each license.
-   Any certificate in a license might require updated revocation lists. If an application calls [**DRMAcquireLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmacquirelicense?branch=master) to obtain a license, revocation lists will automatically be acquired (but must still be registered with [**DRMRegisterRevocationList**](/windows/previous-versions/Msdrm/nf-msdrm-drmregisterrevocationlist?branch=master)).

## Related topics

<dl> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



