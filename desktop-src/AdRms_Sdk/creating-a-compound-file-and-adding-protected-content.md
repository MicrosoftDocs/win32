---
Description: After you have encrypted content, saved it in a file, and obtained a signed issuance license, you can create a compound file container.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 54e961c8-13ac-4d48-99dd-939d970ed11b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating a Compound File and Adding Protected Content
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a Compound File and Adding Protected Content

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

After you have encrypted content, saved it in a file, and obtained a signed [*issuance license*](i-gly.md#-rm-issuance-license-gly), you can create a compound file container. The Active Directory Rights Management Add-on for Internet Explorer interprets the rights specified in the issuance license and allows permitted users to access the protected content.

It does not matter whether you first add the encrypted content or the signed issuance license to the compound file. The following example creates a compound file and adds the encrypted content first. The issuance license is added later. For more information, see [Adding an Issuance License to the Compound File](adding-an-issuance-license-to-the-compound-file.md).

Streams and storage objects hold header and data information in linear, binary form. Much of the following code that creates and adds information to a compound file is devoted to compiling long arrays of data in a specific order and copying that information into the header in specific locations.


```C++
HRESULT AddEncryptedContent(
                              WCHAR*wszRmhFilePath,
                              DWORD  cbUnpublishedFileLen,
                              BYTE*  pbEncryptedContent,
                              DWORD  cbEncryptedContent
                              )
{
   HRESULT hResult = S_OK;
   ULARGE_INTEGER ContentSize;
   DWORD bytesWritten = 0;

   // Insert ASCII characters into storage/stream names.
   short char_nine=9;
   memcpy(StreamName_DRMViewerContent,&amp;char_nine,2);

   // Storage and stream objects.
   IStorage *pStorage = NULL;
   IStream  *pStream = NULL;

   // Create the compound file.
   hResult = StgCreateStorageEx( 
              wszRmhFilePath,         // Compound file name
              STGM_READWRITE|
                STGM_SHARE_EXCLUSIVE|
                  STGM_CREATE, 
              STGFMT_STORAGE,         // Compound file
              0,                      // Required
              NULL,                   // Required
              0,                      // Required
              IID_IStorage,           // IStorage
              (void **)&amp;pStorage);    // IStorage pointer


   // Create a \009DRMViewerContent stream object 
   // to hold the content.
   hResult = pStorage->CreateStream( 
               StreamName_DRMViewerContent, // Name
               STGM_READWRITE | 
                  STGM_SHARE_EXCLUSIVE,     // Access
               0,                           // Required
               0,                           // Required
               &amp;pStream);                   // IStream pointer

   // Write the file to stream, starting with file 
   // size as a 64-bit UINT.
   ContentSize.QuadPart = cbUnpublishedFileLen; 
   hResult = pStream->Write(&amp;ContentSize,
                            8,
                            &amp;bytesWritten);
   hResult = pStream->Write(pbEncryptedContent, 
                            cbEncryptedContent, 
                            &amp;bytesWritten);

   // Save data.
   pStorage->Commit(STGC_DEFAULT);

e_Exit:
   // Clean up.
   if (pStream != NULL)
      pStream->Release();
   if (pStorage != NULL)
      pStorage->Release();

   return hResult;
}
```



## Related topics

<dl> <dt>

[Adding an Issuance License to the Compound File](adding-an-issuance-license-to-the-compound-file.md)
</dt> <dt>

[Adding a Use License to the Compound File](adding-a-use-license-to-the-compound-file.md)
</dt> <dt>

[Publishing Content](publishing-content.md)
</dt> <dt>

[Understanding Compound Files](understanding-compound-files.md)
</dt> </dl>

 

 



