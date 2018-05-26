---
Description: The following code example shows how to create and configure a new unsigned issuance license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 19387d86-6dbc-436f-8772-b9f25458460e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineSigning\_GetUnsignedIL.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnlineSigning\_GetUnsignedIL.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows how to create and configure a new unsigned issuance license. The function performs the following actions:

-   Calls [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) to create an empty issuance license.
-   Creates a user object from the user account specified on the command line.
-   Creates an EDIT right for the user and associates the right and the user with the new license.
-   Creates a GUID and assigns it to the license as a content ID.


```C++
#include "OnlineILSigning.h"

/*===================================================================
File:      OnlineSigning_GetUnsignedIL.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetUnsignedIL function performs the following:
//    - Creates an unsigned issuance license from scratch
//    - Associates an EDIT right with a user
//    - Adds the user and the right to the license
//    - Creates a GUID string to use as a content ID
//    - Adds the content ID to the license
//    - Returns the unsigned issuance license
//
HRESULT GetUnsignedIL(
                PWSTR         pwszUserId, 
                DRMPUBHANDLE* phIssuanceLic)
{
  HRESULT         hr              = S_OK;     // HRESULT return code
  UINT            uiGUIDLength    = 0;        // GUID length
  const UINT      GUID_LENGTH     = 128;      // GUID string length
  PWSTR           pwszGUID        = NULL;     // Content ID string
  DRMPUBHANDLE    hUser           = NULL;     // User handle
  DRMPUBHANDLE    hRight          = NULL;     // Right handle
  SYSTEMTIME      stTimeFrom;                 // Validity start
  SYSTEMTIME      stTimeUntil;                // Validity end
  GUID            guid;                       // Content ID

  // Retrieve the system time to use for the validity
  // period in the issuance license.
  GetSystemTime(&amp;stTimeFrom);
  GetSystemTime(&amp;stTimeUntil);
  stTimeUntil.wYear++;

  // Create an issuance license.
  hr = DRMCreateIssuanceLicense( 
          &amp;stTimeFrom,            // Validity period start
          &amp;stTimeUntil,           // Validity period end
          NULL,                   // Not used
          NULL,                   // Not used
          NULL,                   // Owner handle
          NULL,                   // Template
          NULL,                   // Bound license
          phIssuanceLic);         // Unsigned issuance license
  if (FAILED(hr)) return hr;

  // Create a user object.
  hr = DRMCreateUser( 
            pwszUserId,           // User name (SMTP address)
            NULL,                 // User ID
            L"Unspecified",       // User ID type
            &amp;hUser );             // Handle to the user object
  if (FAILED(hr)) return hr;

  // Create an EDIT right.
  hr = DRMCreateRight( 
            L"EDIT",              // Name of the right
            &amp;stTimeFrom,          // Validity period start
            &amp;stTimeUntil,         // Validity period end
            0,                    // Extended information length
            NULL,                 // Extended information name
            NULL,                 // Extended information value
            &amp;hRight);             // Handle to the right
  if (FAILED(hr)) goto e_Exit;

  // Associate the EDIT right with the user in the issuance license.
  hr = DRMAddRightWithUser( 
            *phIssuanceLic,       // Handle to the issuance license
            hRight,               // Handle to the right
            hUser);               // Handle to the user
  if (FAILED(hr)) goto e_Exit;

  // Create a GUID to use as a unique content ID in the license.
  hr = CoCreateGuid(&amp;guid);
  if (FAILED(hr)) goto e_Exit;

  pwszGUID = new WCHAR[GUID_LENGTH];
  if(NULL == pwszGUID)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }

  uiGUIDLength = StringFromGUID2(guid, pwszGUID, GUID_LENGTH);
  if (0 == uiGUIDLength)
  {
    delete[] pwszGUID;
    hr = E_FAIL;
    goto e_Exit;
  }

  // Set the metadata in the issuance license.
  hr = DRMSetMetaData( 
            *phIssuanceLic,       // Handle to the issuance license
            pwszGUID,             // Content ID
            L"MS-GUID",           // Content ID type
            NULL,                 // SKU ID
            NULL,                 // SKU ID type
            NULL,                 // Type of content
            NULL);                // Content display name
 
e_Exit:

  if(NULL != pwszGUID)
  {
    delete [] pwszGUID;
    pwszGUID = NULL;
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

  return hr;
}
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



