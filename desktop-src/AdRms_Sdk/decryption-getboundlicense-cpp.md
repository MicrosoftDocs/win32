---
Description: The following code example retrieves an end-user license chain from the certificate store, acquires the end-user license from the chain, and binds the license to the EDIT right.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cc2b6faf-d768-4e6e-98e0-8d9022460582
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decryption\_GetBoundLicense.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Decryption\_GetBoundLicense.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example retrieves an end-user license chain from the certificate store, acquires the end-user license from the chain, and binds the license to the EDIT right.


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
  // temporarystore and handle storage and management yourself. 
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



## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Decrypting Content Code Example](decrypting-content-code-example.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> </dl>

 

 



