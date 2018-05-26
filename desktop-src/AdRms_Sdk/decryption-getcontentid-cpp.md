---
Description: The following example shows how to retrieve a content ID value from the end-user license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5bad4ec5-61e1-44d0-9fa8-1fca1a480844
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decryption\_GetContentID.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decryption\_GetContentID.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows how to retrieve a content ID value from the end-user license. This is the same content ID added to the issuance license in [Encryption\_GetOfflineSignedIL.cpp](encryption-getofflinesignedil-cpp.md). When an end-user license is created for decryption, the content ID embedded in the issuance license is added to the end-user license. The GetContentID function shown here is called in [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md).


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_GetContentID.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetContentID function returns the address of a pointer to a
// string that contains the ID for the content to be decrypted. The
// content ID is in the end user license.
//
HRESULT GetContentID(
              PWSTR pwszEUL,
              PWSTR* ppwszContentID)
{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //   hr.....................Return value      
  //   hQueryHandle...........The work [content] object in the EUL
  //   hSubQueryHandle........The content ID in the EUL (and the IL)
  //   pwszContentID..........The content ID in the EUL (and the IL)
  //   uiIdValue..............Number of characters in the content ID
  //   encodingType...........Encoding type of item queried for
  //
  HRESULT           hr                  = S_OK;
  DRMQUERYHANDLE    hQueryHandle        = NULL;
  DRMQUERYHANDLE    hSubQueryHandle     = NULL;
  PWSTR             pwszContentID       = NULL;
  UINT              uiIdValue           = 0;
  DRMENCODINGTYPE   encodingType;

  wprintf(L"\r\nEntering GetContentID.\r\n");

  // Parse the unbound end user license (EUL) to retrieve the 
 // EUL handle.
 hr = DRMParseUnboundLicense(
            pwszEUL,                  // End user license
            &amp;hQueryHandle );          // EUL handle
 if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMParseUnboundLicense: hQueryHandle = %i\r\n", 
          hQueryHandle);

 // Retrieve the handle of the WORK object.
 hr = DRMGetUnboundLicenseObject(
            hQueryHandle,             // EUL handle
            L"work",                  // Object to find
            0,                        // Object index
            &amp;hSubQueryHandle);        // Handle to the WORK object
 if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetUnboundLicenseObject: hSubQueryHandle = %i\r\n", 
          hSubQueryHandle);

  // Retrieve the content ID value
  //   - Call DRMGetUnboundLicenseAttribute to retrieve the
  //     length of the content ID, including the terminating
  //     null character.
  //   - Allocate memory for the content ID.
  //   - Call DRMGetUnboundLicenseAttribute again to retrieve
  //     the content ID.
  hr = DRMGetUnboundLicenseAttribute( 
            hSubQueryHandle,          // WORK object handle
            L"id-value",              // Attribute to retrieve
            0,                        // Attribute index
            &amp;encodingType,            // Encoding type of return
            &amp;uiIdValue,               // Return value length
            NULL);
 if (FAILED(hr)) goto e_Exit;

  // Allocate memory for the content ID.
  pwszContentID = new WCHAR[uiIdValue];
 if (NULL == pwszContentID)
 {
  hr = E_OUTOFMEMORY;
  goto e_Exit;
 }

 hr = DRMGetUnboundLicenseAttribute( 
            hSubQueryHandle, 
            L"id-value", 
            0, 
            &amp;encodingType, 
            &amp;uiIdValue, 
            (BYTE*)pwszContentID);
 if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetUnboundLicenseAttribute: pwszContentID = %s\r\n", 
          pwszContentID);  

  // Return value.
  *ppwszContentID = pwszContentID;

e_Exit:
  if (NULL != pwszContentID)
  {
    pwszContentID = NULL;
  }
 if (NULL != hQueryHandle)
 {
  hr = DRMCloseQueryHandle(hQueryHandle);
    hQueryHandle = NULL;
 }
 if (NULL != hSubQueryHandle)
 {
  hr = DRMCloseQueryHandle(hSubQueryHandle);
    hSubQueryHandle = NULL;
 }

  wprintf(L"Leaving GetContentID: hr = %x\r\n", hr);
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

 

 



