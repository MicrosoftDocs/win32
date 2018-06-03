---
Description: The following example shows how to decrypt a byte array that contains encrypted content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3804216c-6698-43f0-9077-35149704375a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decryption\_DecryptContent.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Decryption\_DecryptContent.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows how to decrypt a byte array that contains encrypted content. The content was encrypted by using the [Encrypting Content Code Example](encrypting-content-code-example.md) and saved in a custom file. The encrypted content is retrieved from the file in [Decryption\_ReadEncryptedContent.cpp](decryption-readencryptedcontent-cpp.md). This example performs the following actions:

-   Creates a decrypting object.
-   Determines the size of the block that must be used when decrypting.
-   Allocates memory for a buffer to hold the decrypted content.
-   Decrypts the content in block size chunks of memory.


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_DecryptContent.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The DecryptContent function decrypts content. The content to be 
// decrypted was created by the EncryptingContent example shown 
// earlier in this documentation.
//
HRESULT DecryptContent(
          DRMHANDLE      hBoundLic,
          UINT           uiEncrypted,
          BYTE*          pbEncrypted,
          BYTE**         ppbDecrypted)
{
  HRESULT hr = S_OK;                  // HRESULT return code
  UINT uiBlock = 0;                   // Decryption block size (16)
  UINT uiBytes = 0;                   // Size of uiBlock variable (4)
  UINT uiDecrypted = 0;               // Number of decrypted bytes
  UINT uiOffset = 0;                  // Decryption buffer offset
  DRMHANDLE hEBDecryptor = NULL;      // Decrypting object handle
  DRMENCODINGTYPE eType;

  wprintf(L"\r\nEntering DecryptContent.\r\n");

  // Validate the input parameters.
  if ( NULL==hBoundLic ||
       NULL==pbEncrypted ||
       NULL==ppbDecrypted)
       return E_INVALIDARG;

  // Create a decrypting object.
  hr = DRMCreateEnablingBitsDecryptor( 
          hBoundLic,                // Bound license handle
          L"EDIT",                  // Requested right
          NULL,                     // Reserved
          NULL,                     // Reserved
          &amp;hEBDecryptor);           // Decrypting object pointer
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"DRMCreateEnablingBitsDecryptor: hEBDecryptor = %i\r\n",
          hEBDecryptor);

  // Retrieve the size, in bytes, of the memory block that must 
  // be passed to DRMDecrypt.
  uiBytes= sizeof(uiBlock);
  hr = DRMGetInfo(
          hEBDecryptor,               // Decrypting object handle
          g_wszQUERY_BLOCKSIZE,       // Attribute to query for
          &amp;eType,                     // Type of encoding to apply
          &amp;uiBytes,                   // Size of uiBlock variable
          (BYTE*)&amp;uiBlock);           // Size of memory block
  if(FAILED(hr)) goto e_Exit;
  wprintf(L"DRMGetInfo: uiBlock = %u\r\n", uiBlock);

  // Allocate memory for the decrypted content.
  // Note: This example uses a buffer of known size to store the
  //       decrypted content.  Typically, however, the buffer to 
  //       store the content should be allocated based on the size
  //       returned by the first call to DRMDecrypt.
  *ppbDecrypted = new BYTE[uiEncrypted];
  if (NULL == *ppbDecrypted)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }

  // Decrypt the content.
  for ( int j = 0; (UINT)j * uiBlock < uiEncrypted; j++ )
  {
    hr = DRMDecrypt( 
          hEBDecryptor,               // Decrypting object handle
          j * uiBlock,                // Position in the buffer
          uiBlock,                    // Number of bytes to decrypt
          pbEncrypted + (j*uiBlock),  // Bytes to decrypt
          &amp;uiDecrypted,               // Number of decrypted bytes
          NULL);                      // Set to NULL on first call
    if(FAILED(hr)) goto e_Exit;

    hr = DRMDecrypt( 
          hEBDecryptor,               // Decrypting object handle
          j * uiBlock,                // Position in the buffer 
          uiBlock,                    // Number of bytes to decrypt
          pbEncrypted + (j*uiBlock),  // Bytes to decrypt
          &amp;uiDecrypted,               // Number of decrypted bytes
          *ppbDecrypted + uiOffset);  // Decrypted data
    if(FAILED(hr)) goto e_Exit;

    uiOffset += uiDecrypted;          // Increment the buffer offset
  }

e_Exit:

  if (NULL != hEBDecryptor)
  {
    hr = DRMCloseHandle(hEBDecryptor);
    hEBDecryptor = NULL;
  }
  
  wprintf(L"Leaving DecryptContent: hr = %x\r\n", hr);
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

 

 



