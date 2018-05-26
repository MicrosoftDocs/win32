---
Description: The following code example reads encrypted content and a signed issuance license from a custom file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5612854c-bbf0-4e4f-b8e8-8d83f3a2f182
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decryption\_ReadEncryptedContent.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decryption\_ReadEncryptedContent.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example reads encrypted content and a signed issuance license from a custom file. The issuance license is used to create the end-user license needed to decrypt the content. The format of the file is:

-   A variable that specifies the length of the encrypted content (4 byte UINT value).
-   A variable that specifies the length of the issuance license (4 byte UINT value).
-   An array of bytes that contains the encrypted content (variable length).
-   An array of bytes that contains the issuance license (variable length).


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_ReadEncryptedContent.cpp

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
             PWSTR  pwszFileName,
             PWSTR* ppwszIL,
             UINT*  puiEncrypted,
             BYTE** ppbEncrypted)
{
  HRESULT   hr                  = S_OK;   // HRESULT return value
  BOOL      bReturn             = FALSE;  // Return from ReadFile
  DWORD     dwBytesRead         = 0;      // Number of bytes read
  UINT      uiILLength          = 0;      // Issuance license length

  wprintf(L"\r\nEntering ReadEncryptedContent.\r\n");

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
  wprintf(L"CreateFile succeeded: hFile = %i\r\n", hFile);

  // Retrieve the length, in bytes, of the encrypted data array.
  bReturn = ReadFile(
          hFile,                      // Handle of file to read
          puiEncrypted,               // Variable to read
          (DWORD)sizeof(UINT),        // Read 4 bytes
          &amp;dwBytesRead,               // Number of bytes read
          NULL);                      // Synchronous read only
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }
  wprintf(L"ReadFile: length of data = %i\r\n", *puiEncrypted);

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
  wprintf(L"ReadFile: length of IL = %i\r\n", uiILLength);


  // Allocate memory for the encrypted content and read it from
  // the file.
  *ppbEncrypted = new BYTE[*puiEncrypted];
  if(NULL == *ppbEncrypted)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }
  bReturn = ReadFile(
          hFile,                      // Handle of file to read 
          *ppbEncrypted,              // Buffer for encrypted data 
          (DWORD)*puiEncrypted,       // Number of bytes to read
          &amp;dwBytesRead,               // Number of bytes read
          NULL);                      // Synchronous read only
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }
  wprintf(L"Read encrypted data: bytes read = %i\r\n", dwBytesRead);

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
  if(!bReturn)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }
  wprintf(L"Read IL: bytes read = %i\r\n", dwBytesRead);

e_Exit:
  if (INVALID_HANDLE_VALUE != hFile)
  {
    CloseHandle(hFile);
    hFile = NULL;
  }

  wprintf(L"Leaving ReadEncryptedContent: hr = %x\r\n", hr);
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

 

 



