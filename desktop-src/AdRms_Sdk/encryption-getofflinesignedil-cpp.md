---
Description: The following code example shows how to create, configure, and sign an issuance license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f5874c07-21b5-4b1e-a756-15c1bee3e55c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encryption\_GetOfflineSignedIL.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Encryption\_GetOfflineSignedIL.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows how to create, configure, and sign an issuance license. The license is signed offline by using the client licensor certificate. Signing requires a secure environment, created by the GetSecureEnvironment function in the [Encryption\_GetSecureEnvironment.cpp](encryption-getsecureenvironment-cpp.md) file. The GetOfflineSignedIL function shown here performs the following actions:

-   Calls [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) to create an empty issuance license.
-   Creates a GUID and assigns it to the license as a content ID.
-   Creates an example name/value pair.
-   Creates an example use policy.
-   Creates a user object from the user account specified on the command line.
-   Creates an EDIT right for the user and associates the right and the user with the new license.
-   Calls [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master) to sign the license offline.


```C++
#include "EncryptingContent.h"

/*===================================================================
File:      Encryption_GetOfflineSignedIL.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetOfflineSignedIL function creates an unsigned issuance
// license, specifies a user and associated right, and signs the
// license offline by using the client licensor certificate.
//
HRESULT GetOfflineSignedIL(DRMENVHANDLE hEnv,
                           DRMHANDLE hLib,
                           PWSTR pwszUserID, 
                           PWSTR pwszMachineCert,
                           PWSTR pwszCLC,
                           PWSTR pwszManifest,
                           PWSTR* ppwszGUID,
                           DRMPUBHANDLE* phIssuanceLic,
                           PWSTR *ppwszSignedIL)
{
  HRESULT       hr               = S_OK;  // HRESULT return code
  DRMPUBHANDLE  hIssuanceLicense = NULL;  // Issuance license handle
  DRMPUBHANDLE  hUser            = NULL;  // User handle
  DRMPUBHANDLE  hRight           = NULL;  // Right handle
  const UINT    GUID_LENGTH      = 128;   // GUID string length
  PWSTR         pwszGUID         = NULL;  // Unique content ID
  UINT          uiGUIDLength     = 0;     // GUID length
  GUID          guid;                     // Unique identifier
  const DWORD   DW_WAIT_TIME     = 60000; // Wait for 60 seconds
  DWORD         dwWaitResult     = 0;     // Event signal duration
  SYSTEMTIME    stTimeFrom;               // Validity period start
  SYSTEMTIME    stTimeUntil;              // Validity period end
  DRM_CONTEXT   context;                  // Callback context

  wprintf(L"\r\nEntering GetOfflineSignedIL.\r\n");

  // Get the system time for the starting and ending times that
  // specify the validity period of the unsigned issuance license.
  // Add one year to the ending time.
  GetSystemTime( &amp;stTimeFrom );
  GetSystemTime( &amp;stTimeUntil );
  stTimeUntil.wYear++;

  // Create an unsigned issuance license from scratch.
  hr = DRMCreateIssuanceLicense( 
          &amp;stTimeFrom,                // Starting validity time
          &amp;stTimeUntil,               // Ending validity time
          NULL,                       // Not supported
          NULL,                       // Not supported
          NULL,                       // Handle to license owner
          NULL,                       // Template or existing license
          NULL,                       // Bound license handle
          &amp;hIssuanceLicense);         // Handle to the license
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateIssuanceLicense: hIssuanceLicense = %i\r\n",\
          hIssuanceLicense);

  // Create a GUID to use as the unique content ID.
  hr = CoCreateGuid(&amp;guid);
  if(FAILED(hr)) goto e_Exit;

  pwszGUID = new WCHAR[GUID_LENGTH];
  if (NULL == pwszGUID)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }

  uiGUIDLength = StringFromGUID2(guid, pwszGUID, GUID_LENGTH);
  if (0 == uiGUIDLength)
  {
    hr = E_FAIL;
    goto e_Exit;
  }
  wprintf(L"StringFromGUID2: pwszGUID = %s\r\n", pwszGUID); 

  // Set your metadata in the unsigned issuance license.
  hr = DRMSetMetaData(
          hIssuanceLicense,           // Issuance license handle
          pwszGUID,                   // Unique content ID
          L"MS-GUID",                 // Type of content ID
          L"SKUId",                   // SKU ID
          L"SKUIdType",               // SKU ID type
          L"ContentType",             // Content type
          L"ContentName");            // Content name
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMSetMetaData succeeded.\r\n");

  // Set an application specific name/value pair in the license.
  hr = DRMSetApplicationSpecificData( 
          hIssuanceLicense,           // Issuance license handle
          false,                      // Add the name/value pair
          L"SomeName",                // Name portion of pair
          L"SomeValue" );             // Value portion of pair
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMSetApplicationSpecificData succeeded.\r\n");

  // Set the interval time in the license.
  hr = DRMSetIntervalTime( 
          hIssuanceLicense,           // Issuance license handle
          30);                        // Interval period in days
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMSetIntervalTime succeeded.\r\n");

  // Set the usage policy
  hr = DRMSetUsagePolicy( 
          hIssuanceLicense,               // Issuance license handle
          DRM_USAGEPOLICY_TYPE_BYNAME,    // Policy type
          false,                          // Add the policy
          true,                           // Rights are prohibited
          L"ApplicationName",             // Application name
          L"1.0.0.0",                     // Minimum version number
          L"3.0.0.0",                     // Maximum version number
          NULL,                           // Public key not required
          NULL,                           // Digest algorithm
          NULL,                           // Pointer to the digest
          NULL );                         // Digest length
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMSetUsagePolicy succeeded.\r\n");

  // Create a user handle.
  hr = DRMCreateUser(
          pwszUserID,                 // User ID or name
          NULL,                       // Verified ID
          L"Windows",                 // Type of user ID
          &amp;hUser );                   // Handle to the user
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateUser succeeded.\r\n");

  // Create a right.
  hr = DRMCreateRight( 
          L"EDIT",                    // Name of the right to create
          &amp;stTimeFrom,                // Starting validity time
          &amp;stTimeUntil,               // Ending validity time
          0,                          // No extended information
          NULL,                       // Extended information name
          NULL,                       // Extended information value
          &amp;hRight );                  // Handle to the created right
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateRight succeeded.\r\n");

  // Associate the right with the user and add both to the 
  // unsigned issuance license
  hr = DRMAddRightWithUser( 
          hIssuanceLicense,           // Issuance license handle
          hRight,                     // Right from DRMCreateRight
          hUser );                    // User from DRMCreateUser
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMAddRightWithUser succeeded.\r\n");

  // Initialize the callback context.
  context.hEvent   = NULL;            // Event handle
  context.pwszData = NULL;            // Signed license

  // Create an event to signal when the license has been signed.
  context.hEvent = CreateEvent(
          NULL,                       // No attributes
          FALSE,                      // Automatic reset
          FALSE,                      // Initial state not signaled
          NULL);                      // Event object not named
  if(NULL == context.hEvent) goto e_Exit;

  // Sign the issuance license offline by using the client
  // licensor certificate
  hr = DRMGetSignedIssuanceLicense( 
          hEnv,                       // Environment handle
          hIssuanceLicense,           // Issuance license handle
          DRM_SIGN_OFFLINE |          // Sign offline with a CLC
            DRM_AUTO_GENERATE_KEY,    // Generate a content key
          NULL,                       // No symmetric key specified
          0,                          // No length specified
          L"AES",                     // Encryption key type
          pwszCLC,                    // Client licensor certificate
          &amp;StatusCallback,            // Callback function
          NULL,                       // No licensing URL specified
          (void*)&amp;context);           // Callback context parameter
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetSignedIssuanceLicense succeeded.\r\n");

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
  if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) goto e_Exit;

  // Assign the output parameters.
  *ppwszGUID = pwszGUID;
  *phIssuanceLic = hIssuanceLicense;
  *ppwszSignedIL = context.pwszData;

e_Exit:
  pwszGUID = NULL;
  hIssuanceLicense = NULL;
  context.pwszData = NULL;
  if(NULL != context.hEvent)
  {
    CloseHandle(context.hEvent);
    context.hEvent = NULL;
  }
  if(NULL != hIssuanceLicense)
  {
    hr = DRMClosePubHandle(hIssuanceLicense);
    hIssuanceLicense = NULL;
  }
  if(NULL != hUser)
  {
    hr = DRMClosePubHandle(hUser);
    hUser = NULL;
  }
  if(NULL != hRight)
  {
    hr = DRMClosePubHandle(hRight);
    hRight = NULL;
  }

  wprintf(L"Leaving GetOfflineSignedIL: hr = %x\r\n", hr);
  return hr;
}
```



## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Encrypting Content Code Example](encrypting-content-code-example.md)
</dt> </dl>

 

 



