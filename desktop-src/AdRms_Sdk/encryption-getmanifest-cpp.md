---
Description: The following example shows how to retrieve the application manifest from the file specified on the command line.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: edabc3e7-21cd-4704-b571-94a79497dd00
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encryption\_GetManifest.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Encryption\_GetManifest.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows how to retrieve the application manifest from the file specified on the command line. The manifest must be supplied to the [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment) function to create a secure environment. A secure environment handle is needed when using the [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense) function to sign a license offline.


```C++
#include "EncryptingContent.h"

/*===================================================================
File:      Encryption_GetManifest.cpp

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
  // Declare and define variables.
  HRESULT                     hr            = S_OK;
  HANDLE                      hFile         = INVALID_HANDLE_VALUE;
  DWORD                       dwBytesRead   = 0;
  BOOL                        bReturn       = false;
  BY_HANDLE_FILE_INFORMATION  fi;

  wprintf(L"\r\nEntering GetManifest.\r\n");
  wprintf(L"Manifest file name = %s\r\n", pwszFileName);

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
  wprintf(L"CreateFile: hFile = %i\r\n", hFile);

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
  wprintf(L"ReadFile (*ppwszManifest) succeeded.\r\n");
  wprintf(L"Number of bytes read = %i\r\n", dwBytesRead);


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

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Encrypting Content Code Example](encrypting-content-code-example.md)
</dt> </dl>

 

 



