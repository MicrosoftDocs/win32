---
Description: The signed issuance license is added in a new stream to the compound file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 06cca54c-9de1-46fd-9502-5a650f0300ae
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Adding an Issuance License to the Compound File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding an Issuance License to the Compound File

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

In the following example, the signed [*issuance license*](i-gly.md#-rm-issuance-license-gly) is added in a new stream to the compound file. This stream must be called \\006Primary to enable the Microsoft Rights Management Add-on for Internet Explorer to read it.


```C++
// PaddingLength is a custom function that returns the number of 
// padding bytes required to bring a submitted number up to 
// a submitted block size. VERSIONSTAMP is a custom structure.

// CHECK_STG_ERROR is an error-handling macro.
#define CHECK_STG_ERROR(api,hresult) if(FAILED(hresult))           \
{                                                                  \
printf("Error (%s): %S [%d]\n",api,StorageError(hresult),hresult); \
goto e_Exit;                                                       \
}


WCHAR StorageName_DataSpaces[12]    =    L"*DataSpaces";
WCHAR StorageName_DataSpaceInfo[14] =    L"DataSpaceInfo";
WCHAR StorageName_TransformInfo[14] =    L"TransformInfo";
WCHAR StorageName_DRMTransform[14]  =    L"*DRMTransform";
WCHAR StreamName_DRMViewerContent[18] =  L"*DRMViewerContent";
WCHAR StreamName_Version[8]         =    L"Version";
WCHAR StreamName_DataSpaceMap[13]   =    L"DataSpaceMap";
WCHAR StreamName_DRMDataSpace[14]   =    L"*DRMDataSpace";
WCHAR StreamName_Primary[9]         =    L"*Primary";

...

CDOCLIB_API HRESULT __stdcall AddPublishingLicense(
                                 WCHAR* wcsPubLicense, 
                                 WCHAR* wcsRmhFilePath)
{
    int HeaderLen           = 0;
    int EntryCount          = 0;
    int EntryLength         = 0;
    int RefComponentCount   = 0;
    int RefComponentType    = 0;
    int RefComponentLen     = 0;
    int RefComponentPad     = 0;
    int DataSpaceNameLen    = 0;
    int DataSpaceNamePad    = 0;
    int TotalLength         = 0;

    LPWSTR RefComponent     = NULL;
    LPWSTR DataSpaceName    = NULL;

    // Storage and stream objects.
    IStorage *pStorage              = NULL;
    IStorage *pDataSpaceStorage     = NULL;
    IStorage *pDataSpaceInfoStorage = NULL;
    IStorage *pTransformInfoStorage = NULL;
    IStorage *pDRMTransformStorage  = NULL;
    IStream  *pStream               = NULL;

    HRESULT hResult     = NULL;
    ULONG bytesWritten  = 0;
    BYTE *dataspacemap  = NULL;
    LPSTR szB64Username = NULL;
    LPSTR szRightsLabel = NULL;
    BYTE *drm_transform = NULL;

    // Insert special characters into storage/stream names.
    short char_nine = 9;
    short char_six  = 6;
    memcpy(StorageName_DataSpaces, &amp;char_six, 2);
    memcpy(StorageName_DRMTransform, &amp;char_nine, 2);
    memcpy(StreamName_DRMDataSpace, &amp;char_nine, 2);
    memcpy(StreamName_Primary, &amp;char_six, 2);


    // Structure needed for the transform header.
    VERSIONSTAMP version;
    version.ReaderVersionMajor  = 1;
    version.ReaderVersionMinor  = 0;
    version.UpdaterVersionMajor = 1;
    version.UpdaterVersionMinor = 0;
    version.WriterVersionMajor  = 1;
    version.WriterVersionMinor  = 0;


    // Open the output compound file.
    hResult = StgOpenStorageEx( 
                 wcsRmhFilePath,         // File name
                 STGM_READWRITE|         // File access
                   STGM_SHARE_EXCLUSIVE, 
                 STGFMT_STORAGE,         // Compound file
                 0,              
                 NULL,           
                 0,              
                 IID_IStorage,           // IStorage IID
                 (void **)&amp;pStorage);    // IStorage pointer

    CHECK_STG_ERROR("StgCreateStorageEx", hResult);

    // Create \006DataSpaces storage.
    hResult = pStorage->CreateStorage(
                 StorageName_DataSpaces,
                 STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
                 0,
                 0,
                 &amp;pDataSpaceStorage);
    CHECK_STG_ERROR("IStorage::CreateStorage", hResult);

   // Create Version Stream.
   // Stream Format:
   // STAMP
   //   int32 FeatureIdentifierLength
   //   WCHAR FeatureIdentifier[]
   //   int16 ReaderVersionMajor
   //   int16 ReaderVersionMinor
   //   int16 UpdaterVersionMajor
   //   int16 UpdaterVersionMinor
   //   int16 WriterVersionMajor
   //   int16 WriterVersionMinor
   // END STAMP
    BYTE version_stamp[76];
    ZeroMemory(version_stamp, 76);
    version_stamp[0]=60;
    memcpy(version_stamp+4, L"Microsoft.Container.DataSpaces", 60);
    memcpy(version_stamp+64, &amp;version, 12);
    hResult = pDataSpaceStorage->CreateStream(
                StreamName_Version,    // Required name
                STGM_READWRITE |       // File access
                STGM_SHARE_EXCLUSIVE,
                0,                     
                0,                     
                &amp;pStream);             // IStream pointer
   CHECK_STG_ERROR("IStorage::CreateStream", hResult);
   hResult = pStream->Write(version_stamp, 76, &amp;bytesWritten);
   CHECK_STG_ERROR("IStream::Write", hResult);


   // Create DataSpaceMap stream.
   // Stream Format:
   // HEADER
   //   int32 HeaderLen
   //   int32 EntryCount
   // END HEADER
   // MAP ENTRY
   //   int32 EntryLength
   //   int32 RefComponentCount
   //   REFCOMPONENT
   //     int32 RefComponentType
   //     int32 RefComponentLen
   //     WCHAR RefComponent[]
   //   END REFCOMPONENT (DWORD ALIGN)
   //   int32 DataSpaceNameLen
   //   WCHAR DataSpaceName[] 
   // END MAP ENTRY (DWORD ALIGN)
   hResult = pDataSpaceStorage->CreateStream(
                StreamName_DataSpaceMap,   // Required name
                STGM_READWRITE |           // File access 
                    STGM_SHARE_EXCLUSIVE, 
                0,                     
                0,                     
                &amp;pStream);                 // IStream pointer
   CHECK_STG_ERROR("IStorage::CreateStream", hResult);

   // Calculate the size of the buffer needed to hold all
   // data for the DataSpaceMap stream.
   HeaderLen         = 8;
   EntryCount        = 1;
   RefComponentCount = 1;
   RefComponentType  = 0;
   RefComponentLen   = (int)wcslen(
                       StreamName_DRMViewerContent)*sizeof(WCHAR);
   RefComponentPad   = PaddingLength(RefComponentLen,sizeof(DWORD));
   RefComponent      = StreamName_DRMViewerContent;
   DataSpaceNameLen  = (int)wcslen(StreamName_DRMDataSpace)
                       *sizeof(WCHAR);
   DataSpaceNamePad  = PaddingLength(DataSpaceNameLen, 
                       sizeof(DWORD));
   DataSpaceName     = StreamName_DRMDataSpace;
   EntryLength       = sizeof(DWORD)*5+
                       RefComponentLen+RefComponentPad+
                       DataSpaceNameLen+DataSpaceNamePad;
   TotalLength       = sizeof(DWORD)*2+EntryLength;

   // Allocate buffer and copy headers and data to the buffer.
   dataspacemap = (BYTE *)HeapAlloc(
                            GetProcessHeap(), 
                            0, 
                            TotalLength);
   if (dataspacemap == NULL)
   {
       hResult = E_OUTOFMEMORY;
       goto e_Exit;
   }
   ZeroMemory(dataspacemap, TotalLength);
   memcpy(dataspacemap+0, &amp;HeaderLen, 4);
   memcpy(dataspacemap+4, &amp;EntryCount, 4);
   memcpy(dataspacemap+8, &amp;EntryLength, 4);
   memcpy(dataspacemap+12, &amp;RefComponentCount, 4);
   memcpy(dataspacemap+16, &amp;RefComponentType, 4);
   memcpy(dataspacemap+20, &amp;RefComponentType, 4);
   memcpy(dataspacemap+24, RefComponent, RefComponentLen);
   memcpy(dataspacemap+24+RefComponentLen+RefComponentPad, 
          &amp;DataSpaceNameLen, 4);
   memcpy(dataspacemap+28+RefComponentLen+RefComponentPad,
          DataSpaceName,DataSpaceNameLen);

   // Copy buffer to the new DataSpaceMap stream.
   hResult = pStream->Write(
                (void *)dataspacemap, 
                TotalLength, 
                &amp;bytesWritten); 
   CHECK_STG_ERROR("IStream::Write", hResult);

   // Release the stream. 
   if (pStream != NULL)
   {
        pStream->Release();
        pStream = NULL;
   }

   // Create DataSpaceInfo storage.
   hResult = pDataSpaceStorage->CreateStorage(
                 StorageName_DataSpaceInfo,
                 STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
                 0,
                 0,
                 &amp;pDataSpaceInfoStorage);
   CHECK_STG_ERROR("IStorage::CreateStorage[DataSpaceInfo]", 
                 hResult);

   // Create \009DRMDataSpace stream.
   // Stream Format:
   // HEADER
   //   int32 HeaderLen
   //   int32 TransformCount
   // END HEADER
   // TRANSFORM
   //   Int32 TransformNameLen
   //   WCHAR TransformName[]
   // END TRANSFORM
   hResult = pDataSpaceInfoStorage->CreateStream(
                  StreamName_DRMDataSpace,    // Required name
                  STGM_READWRITE |            // Eile access
                     STGM_SHARE_EXCLUSIVE, 
                  0,                          // Required
                  0,                          // Required 
                  &amp;pStream);                  // IStream pointer
   CHECK_STG_ERROR("IStorage::CreateStream", hResult);

   HeaderLen            = 8;
   int TransformCount   = 1;
   int TransformNameLen = 26;
   LPWSTR TransformName = StorageName_DRMTransform;

   // Copy data to buffer. 
   BYTE dataspace[40];
   ZeroMemory(dataspace, 40);
   memcpy(dataspace+0, &amp;HeaderLen, 4);
   memcpy(dataspace+4, &amp;TransformCount, 4);
   memcpy(dataspace+8, &amp;TransformNameLen, 4);
   memcpy(dataspace+12, TransformName, TransformNameLen+2);

   // Write \009DRMDataSpace stream.
   hResult = pStream->Write(
                  (void *)dataspace, 
                  40, 
                  &amp;bytesWritten); 
   CHECK_STG_ERROR("IStream::Write", hResult);

   // Create TransformInfo storage.
   hResult = pDataSpaceStorage->CreateStorage(
                  StorageName_TransformInfo,
                  STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
                  0,
                  0,
                  &amp;pTransformInfoStorage);
   CHECK_STG_ERROR("IStorage::CreateStorage[TransformInfo]", 
                  hResult);

   // Create \009DRMTransform storage.
   memcpy(StorageName_DRMTransform, &amp;char_nine, 2);
   hResult = pTransformInfoStorage->CreateStorage( 
                  StorageName_DRMTransform,
                  STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
                  0,
                  0,
                  &amp;pDRMTransformStorage);
   CHECK_STG_ERROR("IStorage::CreateStorage[DRMTransform]", 
                  hResult);

   // Create \006Primary stream.
   hResult = pDRMTransformStorage->CreateStream(
                  StreamName_Primary,      // Required name
                  STGM_READWRITE |         // File access
                     STGM_SHARE_EXCLUSIVE, 
                  0,                       // Required value
                  0,                       // Required value
                  &amp;pStream);               // IStream pointer
   CHECK_STG_ERROR("IStorage::CreateStream", hResult);

   LPWSTR ClassID  = L"{C73DFACD-061F-43B0-8B64-0C620D2A8B50}";
   LPWSTR FeatureIdentifier = L"Microsoft.Metadata.DRMTransform";
   LPWSTR wszSignedIL  = wcsPubLicense;
   int IndexOfFeatureIdentifierLength   = 88;
   int TheNumberOne  = 1;
   int ClassIDLength  = (int)wcslen(ClassID)*sizeof(WCHAR);
   int FeatureIdentifierLength = (int)wcslen(FeatureIdentifier)
                                 *sizeof(WCHAR);
   int TheNumberFour  = 4;
   short TheNumberZero  = 0;
   szRightsLabel = (CHAR *)HeapAlloc(GetProcessHeap(),
                   0, 
                   wcslen(wszSignedIL)+1);
   if ( NULL == szRightsLabel )
   {
       printf("Error (%s): E_OUTOFMEMORY\n", "HeapAlloc");
       goto e_Exit;
   }
   StringCchPrintf(szRightsLabel, 
                   wcslen(wszSignedIL)+1, 
                   "%S", 
                   wszSignedIL);
   int RightsLabelLength  = (int)strlen(szRightsLabel);
   int TransformLength    = 38 + ClassIDLength + 
                            FeatureIdentifierLength + 
                            RightsLabelLength +     
                            PaddingLength(
                               RightsLabelLength, 
                               sizeof(DWORD));
   
   // Allocate buffer to hold \006Primary stream data.
   drm_transform = (BYTE *)HeapAlloc(GetProcessHeap(),
                  0, 
                  TransformLength);
   if ( NULL == drm_transform )
   {
       printf("Error (%s): E_OUTOFMEMORY\n", "HeapAlloc");
       goto e_Exit;
   }
   ZeroMemory(drm_transform, TransformLength);

   // Copy headers and issuance license to buffer.
   memcpy(drm_transform+0, &amp;IndexOfFeatureIdentifierLength, 4);
   memcpy(drm_transform+4, &amp;TheNumberOne, 4);
   memcpy(drm_transform+8, &amp;ClassIDLength, 4);
   memcpy(drm_transform+12, ClassID, ClassIDLength);
   memcpy(drm_transform+12+ClassIDLength,
          &amp;FeatureIdentifierLength, 
          4);
   memcpy(drm_transform+16+ClassIDLength, 
          FeatureIdentifier, 
          FeatureIdentifierLength);
   memcpy(drm_transform+16+ClassIDLength+FeatureIdentifierLength,
          &amp;TheNumberZero, 
          2);
   memcpy(drm_transform+18+ClassIDLength+FeatureIdentifierLength,
          &amp;version,
          12);
   memcpy(drm_transform+30+ClassIDLength+FeatureIdentifierLength, 
          &amp;TheNumberFour,
          4);
   memcpy(drm_transform+34+ClassIDLength+FeatureIdentifierLength,
          &amp;RightsLabelLength,
          4);
   memcpy(drm_transform+38+ClassIDLength+FeatureIdentifierLength,
          szRightsLabel,
          RightsLabelLength);

   // Copy buffer to \006Primary stream.
   hResult = pStream->Write(
                 (void *)drm_transform, 
                 TransformLength, 
                 &amp;bytesWritten); 
   CHECK_STG_ERROR("IStream::Write", hResult);
   
   // Commit changes to root storage.
   pStorage->Commit(STGC_DEFAULT);

e_Exit:
   // Clean up.
   if (NULL != dataspacemap) HeapFree(GetProcessHeap(),
                  0, 
                  dataspacemap);
   if (NULL != szB64Username) HeapFree(GetProcessHeap(),
                  0, 
                  szB64Username);
   if (NULL != szRightsLabel) HeapFree(GetProcessHeap(),
                  0, 
                  szRightsLabel);
   if (NULL != drm_transform) HeapFree(GetProcessHeap(), 
                  0, 
                  drm_transform);

   if (pStorage != NULL)
       pStorage->Release();
   if (pDataSpaceStorage != NULL)
       pDataSpaceStorage->Release();
   if (pDataSpaceInfoStorage != NULL)
       pDataSpaceInfoStorage->Release();
   if (pTransformInfoStorage != NULL)
       pTransformInfoStorage->Release();
   if (pDRMTransformStorage != NULL)
       pDRMTransformStorage->Release();
   if (pStream != NULL)
       pStream->Release();
    
   return hResult;
}
```



## Related topics

<dl> <dt>

[Adding a Use License to the Compound File](adding-a-use-license-to-the-compound-file.md)
</dt> <dt>

[Creating a Compound File and Adding Protected Content](creating-a-compound-file-and-adding-protected-content.md)
</dt> <dt>

[Understanding Compound Files](understanding-compound-files.md)
</dt> </dl>

 

 



