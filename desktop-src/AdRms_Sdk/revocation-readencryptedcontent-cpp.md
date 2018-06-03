---
Description: The following code example reads encrypted content and a signed issuance license from a custom file that was created by the Encrypting Content Code Example.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 56a69743-4f3c-4e0f-a69e-e151fb0d87dc
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation\_ReadEncryptedContent.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revocation\_ReadEncryptedContent.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example reads encrypted content and a signed issuance license from a custom file that was created by the [Encrypting Content Code Example](encrypting-content-code-example.md). The encrypted content is not used in this example. Only the issuance license is used to create a license storage session. The file consists of:

-   A variable that specifies the length of the encrypted content (4 byte UINT value).
-   A variable that specifies the length of the issuance license (4 byte UINT value).
-   An array of bytes that contains the encrypted content (variable length).
-   An array of bytes that contains the issuance license (variable length).


```C++
#include "RevocationList.h"

/*===================================================================
File:      Revocation_ReadEncryptedContent.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The ReadEncryptedContent function reads encrypted content and
// an issuance license from a binary file. The file is created by
// the EncryptingContent example. The format is:
//    Encrypted data length   - 4 bytes
//    Issuance license length - 4 bytes
//    Encrypted data          - variable number of bytes
//    Issuance license        - variable number of bytes
//
HRESULT ReadEncryptedContent(
             PWSTR pwszFileName,
             PWSTR* ppwszIL,
             BYTE** ppbEncrypted)
{
  HRESULT   hr                  = S_OK;   // HRESULT return value
  BOOL      bReturn             = FALSE;  // Return from ReadFile
  DWORD     dwBytesRead         = 0;      // Number of bytes read
  UINT      uiEncryptedLength   = 0;      // Number encrypted bytes
  BYTE*     pbEncrypted         = NULL;   // Encrypted content buffer
  UINT      uiILLength          = 0;      // Issuance license length

  // Open the file that contains the encrypted content.
  HANDLE hFile = CreateFile(
          pwszFileName,               // File name
          GENERIC_READ,               // Read-only
          0,                          // Require exclusive access
          NULL,                       // Default security attributes
          OPEN_EXISTING,              // Open only if file exists
          0,                          // No file attributes or flags
          NULL);                      // No open file as template
  if(INVALID_HANDLE_VALUE == hFile)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    return hr;
  }

  // Retrieve the length, in bytes, of the encrypted data array.
  bReturn = ReadFile(
          hFile,                      // Handle of file to read
          &amp;uiEncryptedLength,         // Variable to read
          (DWORD)sizeof(UINT),        // Read 4 bytes
          &amp;dwBytesRead,               // Number of bytes read
          NULL);                      // Synchronous read only
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }

  // Retrieve the length, in bytes, of the issuance license.
  bReturn = ReadFile(
          hFile,                      // Handle of file to read
          &amp;uiILLength,                // Variable to read
          (DWORD)sizeof(UINT),        // Read 4 bytes
          &amp;dwBytesRead,               // Number of bytes read 
          NULL);                      // Synchronous read only
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }

  // Allocate memory for the encrypted content and read it from
  // the file.
  *ppbEncrypted = new BYTE[uiEncryptedLength * sizeof(WCHAR)];
  if(NULL == *ppbEncrypted)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }
  bReturn = ReadFile(
          hFile,                      // Handle of file to read 
          *ppbEncrypted,              // Buffer for encrypted data 
          (DWORD)uiEncryptedLength,   // Number of bytes to read
          &amp;dwBytesRead,               // Number of bytes read
          NULL);                      // Synchronous read only
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }

  // Allocate memory for the issuance license and read it from
  // the file.
  *ppwszIL = new WCHAR[uiILLength];
  if(NULL == *ppwszIL)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }
  bReturn = ReadFile(
          hFile,                      // Handle of file to read 
          *ppwszIL,                   // Buffer for issuance license
          (DWORD)uiILLength,          // Number of bytes to read
          &amp;dwBytesRead,               // Number of bytes read
          NULL);                      // Synchronous read only
  if(!bReturn) hr = HRESULT_FROM_WIN32(GetLastError());

e_Exit:
  if (INVALID_HANDLE_VALUE != hFile)CloseHandle(hFile);

  return hr;
}
```



## Related topics

<dl> <dt>

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



