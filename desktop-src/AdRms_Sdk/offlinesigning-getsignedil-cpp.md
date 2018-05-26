---
Description: The following code example shows how to create, configure, and sign an issuance license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ef473013-e0ed-4e41-90b1-93e501b9ce14
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OfflineSigning\_GetSignedIL.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OfflineSigning\_GetSignedIL.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows how to create, configure, and sign an issuance license. The function performs the following actions:

-   Retrieves the lockbox path.
-   Initializes a secure environment.
-   Calls [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) to create an empty issuance license.
-   Creates a GUID and assigns it to the license as a content ID.
-   Creates an example name/value pair.
-   Creates an example use policy.
-   Creates a user object from the user account specified on the command line.
-   Creates an EDIT right for the user and associates the right and the user with the new license.


```C++
#include "OfflineILSigning.h"

/*===================================================================
File:      OfflineSigning_GetSignedIL.cpp

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
HRESULT GetOfflineSignedIL(PWSTR pwszUserID, 
                           PWSTR pwszMachineCert,
                           PWSTR pwszCLC,
                           PWSTR pwszManifest,
                           PWSTR *ppwszSignedIL)
{
  HRESULT       hr               = S_OK;  // HRESULT return code
  PWSTR         pwszSecProvType  = NULL;  // Secure provider type
  UINT          uiProvTypeLgth   = 0;     // Provider type length
  PWSTR         pwszSecProvPath  = NULL;  // Secure provider path
  UINT          uiProvPathLgth   = 0;     // Provider path length
  DRMPUBHANDLE  hIssuanceLicense = NULL;  // Issuance license handle
  DRMENVHANDLE  hEnv             = NULL;  // Environment handle
  DRMHANDLE     hLib             = NULL;  // Library handle
  DRMPUBHANDLE  hUser            = NULL;  // User handle
  DRMPUBHANDLE  hRight           = NULL;  // Right handle
  const UINT    GUID_LENGTH      = 128;   // GUID string length
  PWSTR         pwszGUID         = NULL;  // Unique content ID
  UINT          uiGUIDLength     = 0;     // GUID length
  GUID          guid;                     // Raw unique content ID
  const DWORD   DW_WAIT_TIME     = 60000; // Maximum signal duration
  DWORD         dwWaitResult     = 0;     // Actual signal duration
  SYSTEMTIME    stTimeFrom;               // Validity period start
  SYSTEMTIME    stTimeUntil;              // Validity period end
  DRM_CONTEXT   context;                  // Callback context

  wprintf(L"\r\nEntering GetOfflineSignedIL. \r\n");

  // Initialize the callback context.
  SecureZeroMemory(&amp;context, sizeof(context));

  // Retrieve the client lockbox:
  //   - Call DRMGetSecurityProvider once to retrieve the number of
  //     characters for the provider type and provider path.
  //   - Allocate memory for the type and path strings.
  //   - Call DRMGetSecurityProvider again to retrieve the secure
  //     provider type and path information.
  hr = DRMGetSecurityProvider( 
            0,                      // Reserved
            &amp;uiProvTypeLgth,        // Length of the type string
            NULL,                   // Type string - NULL on input
            &amp;uiProvPathLgth,        // Length of the path string
            NULL);                  // Path string - NULL on input
  if(FAILED(hr)) return hr;

  pwszSecProvType = new WCHAR[uiProvTypeLgth];
  pwszSecProvPath = new WCHAR[uiProvPathLgth];
  if(NULL==pwszSecProvType || NULL==pwszSecProvPath)
  {
    hr = E_OUTOFMEMORY;
    return hr;
  }

  hr = DRMGetSecurityProvider( 
            0,                        // Reserved
            &amp;uiProvTypeLgth,          // Length of the type string
            pwszSecProvType,          // Return type string
            &amp;uiProvPathLgth,          // Length of the path string
            pwszSecProvPath );        // Path string
  if(FAILED(hr)) return hr;
  wprintf(L"DRMGetSecurityProvider: pwszSecProvType %s \r\n",
          pwszSecProvType);
  wprintf(L"DRMGetSecurityProvider: pwszSecProvPath %s \r\n",
          pwszSecProvPath);

  // Initialize a secure environment. This requires a lockbox,
  // a signed manifest, and the machine certificate associated
  // with the user.
  hr = DRMInitEnvironment( 
          DRMSECURITYPROVIDERTYPE_SOFTWARESECREP, 
          DRMSPECTYPE_FILENAME,       // Provider is in a file
          pwszSecProvPath,            // Path to the provider
          pwszManifest,               // Application manifest
          pwszMachineCert,            // Machine certificate
          &amp;hEnv,                      // Return environment handle
          &amp;hLib);                     // Return library
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMInitEnvironment: hEnv = %i \r\n", hEnv);
  wprintf(L"DRMInitEnvironment: hLib = %i \r\n", hLib);
  wprintf(L"Attach debugger here, set a breakpoint,");
  wprintf(L"and enter any key to continue: \r\n");
  _getch();

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
  wprintf(L"DRMCreateIssuanceLicense: hIssuanceLicense = %i \r\n",
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

  uiGUIDLength = StringFromGUID2( guid, pwszGUID, GUID_LENGTH );
  if (0 == uiGUIDLength)
  {
    hr = E_FAIL;
    goto e_Exit;
  }
  wprintf(L"StringFromGUID2: pwszGUID = %s \r\n", pwszGUID);

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
  wprintf(L"DRMSetMetaData succeeded. \r\n");

  // Set an application specific name/value pair in the license.
  hr = DRMSetApplicationSpecificData( 
          hIssuanceLicense,           // Issuance license handle
          false,                      // Add the name/value pair
          L"SomeName",                // Name portion of pair
          L"SomeValue" );             // Value portion of pair
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMSetApplicationSpecificData succeeded. \r\n");

  // Set the interval time in the license.
  hr = DRMSetIntervalTime( 
          hIssuanceLicense,           // Issuance license handle
          30);                        // Interval period in days
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMSetIntervalTime succeeded. \r\n");

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
  wprintf(L"DRMSetUsagePolicy succeeded. \r\n");

  // Create a user handle.
  hr = DRMCreateUser(
          pwszUserID,                 // User ID or name
          NULL,                       // Verified ID
          L"Windows",                 // Type of user ID
          &amp;hUser );                   // Handle to the user
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateUser:  hUser = %i \r\n", hUser);

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
  wprintf(L"DRMCreateRight:  hRight = %i \r\n", hRight);

  // Associate the right with the user and add both to the 
  // unsigned issuance license.
  hr = DRMAddRightWithUser( 
          hIssuanceLicense,           // Issuance license handle
          hRight,                     // Right from DRMCreateRight
          hUser );                    // User from DRMCreateUser
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMAddRightWithUser succeeded. \r\n");

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
          (void*)&amp;context);         // Callback context parameter
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetSignedIssuanceLicense succeeded. \r\n");

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
  if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) goto e_Exit;

  // Assign the license pointer to the output parameter. 
  *ppwszSignedIL = context.pwszData;

e_Exit:

  if(NULL != context.hEvent)
  {
    CloseHandle(context.hEvent);
    context.hEvent = NULL;
  }
  if(NULL != hIssuanceLicense)
  {
    DRMClosePubHandle(hIssuanceLicense);
    hIssuanceLicense = NULL;
  }
  if(NULL != hUser)
  {
    DRMClosePubHandle(hUser);
    hUser = NULL;
  }
  if(NULL != hRight)
  {
    DRMClosePubHandle(hRight);
    hRight = NULL;
  }
  if(NULL != hLib)
  {
    DRMCloseHandle(hLib);
    hLib = NULL;
  }
  if(NULL != pwszGUID)
  {
    delete [] pwszGUID;
    pwszGUID = NULL;
  }
  if(NULL != pwszSecProvType)
  {
    delete [] pwszSecProvType;
    pwszSecProvType = NULL;
  }
  if(NULL != pwszSecProvPath)
  {
    delete [] pwszSecProvPath;
    pwszSecProvPath = NULL;
  }
  if(NULL != hEnv)
  {
    DRMCloseEnvironmentHandle(hEnv);
    hEnv = NULL;
  }

  wprintf(L"Leaving GetOfflineSignedIL: hr = %x \r\n", hr);
  return hr;
}
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> </dl>

 

 



