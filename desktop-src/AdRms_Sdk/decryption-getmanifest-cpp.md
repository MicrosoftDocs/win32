---
Description: The following example shows how to retrieve the application manifest from the file specified on the command line.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dcf7aaae-97be-41a9-aff5-49f0beab6e7b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decryption\_GetManifest.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decryption\_GetManifest.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows how to retrieve the application manifest from the file specified on the command line. The manifest must be supplied to the [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master) function to create a secure environment. A secure environment handle is needed by the [**DRMCreateLicenseStorageSession**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreatelicensestoragesession?branch=master) function in [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md) to create a storage session used by the [**DRMAcquireLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmacquirelicense?branch=master) function when retrieving an end-user license.


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_GetManifest.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetManifest function retrieves a UNICODE string that contains
// the signed application manifest in the specified file.
//
HRESULT GetManifest(PWSTR pwszFileName, 
                    PWSTR *ppwszManifest)
{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //   hr....................Return value
  //   hFile.................Handle of encrypted content file
  //   dwBytesRead...........Number of bytes read
  //   bReturn...............Boolean return value
  //   fi....................BY_HANDLE_FILE_INFORMATION structure
  //
  HRESULT                     hr            = S_OK;
  HANDLE                      hFile         = INVALID_HANDLE_VALUE;
  DWORD                       dwBytesRead   = 0;
  BOOL                        bReturn       = false;
  BY_HANDLE_FILE_INFORMATION  fi;

  wprintf(L"\r\nEntering GetManifest.\r\n");

  // Get a handle to the manifest file.
  hFile = CreateFile(
              pwszFileName,     // File name
              GENERIC_READ,     // Access type
              0,                // Do not share
              NULL,             // Security attributes
              OPEN_EXISTING,    // Open the existing file
              0,                // No file attributes or flags
              NULL);            // No template
  if(INVALID_HANDLE_VALUE == hFile)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    return hr;
  }
  wprintf(L"CreateFile succeeded: hFile = %i\r\n", hFile);

  // Retrieve the file information structure to get the file size.
  bReturn = GetFileInformationByHandle(hFile, &amp;fi);
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }

  // Check for files that are too large and check for
  // integer overflow.
  if ((0 != fi.nFileSizeHigh) || 
      (fi.nFileSizeLow + sizeof( WCHAR ) < fi.nFileSizeLow))
  {
    hr = E_FAIL;
    goto e_Exit;
  }

  // Allocate memory for the manifest.
  *ppwszManifest = new WCHAR[fi.nFileSizeLow + sizeof(WCHAR)];
  if(NULL == *ppwszManifest)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }

  // Set the file contents into the manifest string.
  // The calling function must delete the memory.
  bReturn = ReadFile(
              hFile,                // Handle to the open file
              *ppwszManifest,       // Pointer to the buffer
              fi.nFileSizeLow,      // Length in bytes
              &amp;dwBytesRead,         // Number of bytes read
              NULL);                // Reserved.
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }
  wprintf(L"Readfile succeeded: Bytes read = %i\r\n", dwBytesRead);

e_Exit:
  if (INVALID_HANDLE_VALUE != hFile)CloseHandle(hFile);

  wprintf(L"Leaving GetManifest: hr = %i\r\n", hr); 
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

 

 



