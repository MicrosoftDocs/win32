---
Description: The following example encrypts an item of content defined in the EncryptingContent.h header.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8549b7f5-fe6c-405f-be3f-e899707e3158
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encryption\_EncryptContent.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Encryption\_EncryptContent.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example encrypts an item of content defined in the [EncryptingContent.h](encryptingcontent-h.md) header.


```C++
// Content to encrypt.
#define PLAINTEXT L"This is the content to be encrypted."
```



The example performs the following actions:

-   Creates an enabling principal.
-   Creates an owner license.
-   Binds to the OWNER right in the license.
-   Creates an encrypting object.
-   Determines the size of the block that must be used when encrypting.
-   Allocates enough memory to make the plaintext buffer an even multiple of the block size and pads the additional space with zeros.
-   Encrypts the plaintext in block size chunks of memory.


```C++
#include "EncryptingContent.h"

/*===================================================================
File:      Encryption_EncryptContent.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The EncryptContent function encrypts content. In this example,
// the content to be encrypted is defined in the header file.
//   #define PLAINTEXT L"This is the content to be encrypted."
//
HRESULT EncryptContent(
          DRMENVHANDLE   hEnv,
          DRMHANDLE      hLib,
          PWSTR          pwszRAC,
          PWSTR          pwszGUID,
          DRMHANDLE      hIssuanceLic,
          PWSTR          pwszSignedIL,
          BYTE**         ppbEncrypted)

{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //   hr........................Return value                     
  //   pwszOwnerLicense..........License with OWNER right
  //   pwszOutFile...............Name of file for encrypted content
  //   pbEncrypted...............Buffer to hold encrypted content
  //   uiOwnerLicenseLength......Owner licensee length, in characters
  //   uiBlock...................Decryption block size (16 bytes)
  //   uiBytes...................Size, in bytes, of uiBlock
  //   uiPlainText...............Number of bytes in the plain text
  //   uiPadding.................Blank space added to plain text
  //   uiBuffer..................uiPlainText + uiPadding
  //   uiEncrypted...............Size, bytes, of encrypted content
  //   uiOffset..................Offset into encryption buffer
  //   pbPlainText...............Pointer to unencrypted content
  //   hBoundLicense.............Handle to license bound to OWNER
  //   hEP.......................Enabling principal for binding   
  //   hEBEncryptor..............Handle to encrypting object
  //   dwBytesWritten............WriteFile function bytes written 
  //   idNULL....................DRMID structure
  //   idContent.................Structure for binding a license
  //   idStandardEP..............Structure for enabling principal
  //   oParams...................Structure for binding a license
  //   eType.....................Structure for license encoding
  //   
  HRESULT       hr                     = E_FAIL;
  PWSTR         pwszOwnerLicense       = NULL;
  PWSTR         pwszOutFile            = L"EncryptedContent.bin";
  BYTE*         pbEncrypted            = NULL;
  UINT          uiOwnerLicenseLength   = 0;
  UINT          uiBlock                = 0;
  UINT          uiBytes                = 0;
  UINT          uiPlainText            = 0;
  UINT          uiBuffer               = 0;
  UINT          uiPadding              = 0;
  UINT          uiEncrypted            = 0;
  UINT          uiOffset               = 0;
  BYTE*         pbPlainText            = NULL;
  DRMHANDLE     hBoundLicense          = NULL; 
  DRMHANDLE     hEP                    = NULL; 
  DRMHANDLE     hEBEncryptor           = NULL;
  DWORD         dwBytesWritten         = 0;
  DRMID         idNULL;
  DRMID         idContent;
  DRMID         idStandardEP;
  DRMBOUNDLICENSEPARAMS oParams;
  DRMENCODINGTYPE eType;              

  wprintf(L"\r\nEntering EncryptContent.\r\n");
 
  // Validate the input parameters.
  if ( NULL==hEnv ||
       NULL==hLib ||
       NULL==pwszRAC ||
       NULL==pwszGUID ||
       NULL==hIssuanceLic ||
       NULL==pwszSignedIL ||
       NULL==ppbEncrypted)
       return E_INVALIDARG;

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
          pwszRAC,                  // Rights account certificate
          &amp;hEP);                    // enabling principal handle 
  if(FAILED(hr)) return hr;
  wprintf(L"DRMCreateEnablingPrincipal: hEP %i \r\n", hEP);

  // Call DRMGetOwnerLicense to get a license to bind to. An owner
  // license contains the OWNER right which allows the user to
  // exercise all rights regardless of whether they have been
  // explicitly granted.
  //   - Call DRMGetOwnerLicense once to retrieve the length, in
  //     characters, of the owner license.
  //   - Allocate memory for the license.
  //   - Call DRMGetOwnerLicense again to retrieve the license.
  //   - You must release the memory before leaving this function.
  hr = DRMGetOwnerLicense( 
           hIssuanceLic,               // Issuance license handle
           &amp;uiOwnerLicenseLength,      // License length
           NULL);                      // Not used
  if(FAILED(hr)) goto e_Exit;

  pwszOwnerLicense = new WCHAR[uiOwnerLicenseLength];
  if(NULL == pwszOwnerLicense)
  {
    hr = E_OUTOFMEMORY; 
    goto e_Exit; 
  }
  hr = DRMGetOwnerLicense( 
          hIssuanceLic, 
          &amp;uiOwnerLicenseLength, 
          pwszOwnerLicense);
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetOwnerLicense (pwszOwnerLicense) succeeded.\r\n");

  // Bind the owner license to the OWNER right.
  SecureZeroMemory(&amp;idContent, sizeof(idContent));
  idContent.wszIDType        = L"MS-GUID"; 
  idContent.wszID            = pwszGUID;

  SecureZeroMemory(&amp;oParams, sizeof(oParams));
  oParams.hEnablingPrincipal = hEP; 
  oParams.wszRightsRequested = L"OWNER";
  oParams.wszRightsGroup     = L"Main-Rights"; 
  oParams.idResource         = idContent; 

  hr = DRMCreateBoundLicense ( 
          hEnv,                     // Secure environment handle 
          &amp;oParams,                 // Additional license options 
          pwszOwnerLicense,         // Owner license 
          &amp;hBoundLicense,           // Handle to the bound license 
          NULL );                   // Reserved
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateBoundLicense: (hBoundLicense) succeeded.\r\n");

  // Create an encrypting object. 
  hr = DRMCreateEnablingBitsEncryptor( 
          hBoundLicense,              // Bound license handle
          oParams.wszRightsRequested, // Requested right
          NULL,                       // Reserved
          NULL,                       // Reserved
          &amp;hEBEncryptor);             // Encrypting object handle
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateEnablingBitsEncryptor succeeded.\r\n");

  // Retrieve the size, in bytes, of the memory block that must 
  // be passed to DRMEncrypt.
  uiBytes= sizeof(uiBlock);
  hr = DRMGetInfo(
          hEBEncryptor,               // Encrypting object handle
          g_wszQUERY_BLOCKSIZE,       // Attribute to query for
          &amp;eType,                     // Type of encoding to apply
          &amp;uiBytes,                   // Size of uiBlock variable
          (BYTE*)&amp;uiBlock);           // Size of memory block
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetInfo: uiBlock = %u\r\n", uiBlock);

  // Determine the size of the buffer needed to store the
  // encrypted content. The buffer must be an even multiple of 
  // the buffer size used during the [typically] iterative 
  // encryption process. In this example, the plain text
  // is 72 bytes long and the encryption buffer is 16 bytes. 
  // However 72 % 16 = 8. The plain text must therefore be padded
  // to 80 bytes (80 % 16 = 0).
  uiPlainText = (UINT)(sizeof(WCHAR) * wcslen(PLAINTEXT));
  uiPadding = uiBlock - (uiPlainText % uiBlock);
  uiBuffer = uiPlainText + uiPadding;

  pbPlainText = new BYTE[uiBuffer];
  *ppbEncrypted = new BYTE[uiBuffer];

  SecureZeroMemory(pbPlainText, sizeof(pbPlainText));
  memcpy_s(
          pbPlainText,
          uiBuffer,
          (BYTE*)PLAINTEXT,
          uiPlainText);

  // Encrypt the plain text.
  for ( int j = 0; (UINT)j * uiBlock < uiBuffer; j++ )
  {
    hr = DRMEncrypt( 
          hEBEncryptor,               // Encrypting object handle
          j * uiBlock,                // Position in buffer
          uiBlock,                    // Number of bytes to encrypt
          pbPlainText + (j*uiBlock),  // Bytes to encrypt
          &amp;uiEncrypted,               // Number of bytes encrypted
          NULL);                      // NULL on first call
    if(FAILED(hr)) goto e_Exit;

    hr = DRMEncrypt( 
          hEBEncryptor,               // Encrypting object handle 
          j * uiBlock,                // Position in buffer 
          uiBlock,                    // Number of bytes to encrypt
          pbPlainText + (j*uiBlock),  // Bytes to encrypt
          &amp;uiEncrypted,               // Number of bytes encrypted
          *ppbEncrypted + uiOffset);  // Encrypted content
    if(FAILED(hr)) goto e_Exit;

    uiOffset += uiEncrypted;          // Increment the buffer offset
  }

  // Create a new file to write the encrypted content and issuance
  // license to.
  HANDLE hFile = CreateFile(
          pwszOutFile,                // File name
          GENERIC_WRITE,              // Access type
          0,                          // Require exclusive access
          NULL,                       // Default security attributes
          CREATE_ALWAYS,              // Allow write-only access
          0,                          // No file attributes or flags
          NULL);                      // No open file as template
  if(INVALID_HANDLE_VALUE == hFile)
  {
    hr = HRESULT_FROM_WIN32(GetLastError());
    goto e_Exit;
  }
  wprintf(L"CreateFile: hFile = %i\r\n", hFile);

  // Write the encrypted content and relevant data to the file.
  if(!WriteFile(hFile, 
                &amp;uiBuffer, 
                sizeof(UINT), 
                &amp;dwBytesWritten, 
                NULL))
    goto e_Exit;
  size_t uiIssuanceLicenseLgth = (UINT)(sizeof(WCHAR) * 
                                 wcslen(pwszSignedIL));
  if(!WriteFile(hFile, 
                &amp;uiIssuanceLicenseLgth, 
                sizeof(size_t), 
                &amp;dwBytesWritten, 
                NULL))
    goto e_Exit;
  if(!WriteFile(hFile, 
                *ppbEncrypted, 
                uiBuffer, 
                &amp;dwBytesWritten, 
                NULL))
    goto e_Exit;
  if(!WriteFile(hFile, 
                pwszSignedIL, 
                uiIssuanceLicenseLgth, 
                &amp;dwBytesWritten, 
                NULL))
    goto e_Exit;
  wprintf(L"Writing to file succeeded.\r\n");

e_Exit:

  if (INVALID_HANDLE_VALUE != hFile)
  {
    CloseHandle(hFile);
  }
  if (NULL != hEP)
  {
    hr = DRMCloseHandle(hEP);
    hEP = NULL;
  }
  if (NULL != hBoundLicense)
  {
    hr = DRMCloseHandle(hBoundLicense);
    hBoundLicense = NULL;
  }
  if (NULL != hEBEncryptor)
  {
    hr = DRMCloseHandle(hEBEncryptor);
    hEBEncryptor = NULL;
  }
  if (NULL != pwszOwnerLicense)
  {
    delete [] pwszOwnerLicense;
    pwszOwnerLicense = NULL;
  }

  wprintf(L"Leaving EncryptContent: hr = %x \r\n", hr);
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

 

 



