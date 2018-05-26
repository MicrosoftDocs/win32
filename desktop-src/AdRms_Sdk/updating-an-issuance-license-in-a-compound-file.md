---
Description: If a compound file is stored for any length of time, it is possible that the users and rights specified in the issuance license are out of date.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e1223f2f-61e7-4fa4-b74d-8d52fa7b7875
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Updating an Issuance License in a Compound File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Updating an Issuance License in a Compound File

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

If a compound file is stored for any length of time, it is possible that the users and rights specified in the [*issuance license*](i-gly.md#-rm-issuance-license-gly) are out of date. You may need to add more users, for example, or remove a right from an existing user. To do this, you must rebuild the issuance license and use the latest template or specifications, republish the existing license, and then replace the old issuance license with the new one in the compound file.

You can use the [**EditIssuanceLicense**](-editissuancelicense.md) SOAP web method to republish a license. **EditIssuanceLicense** accepts an existing signed issuance license and an unsigned new issuance license, copies the encrypted content key from the existing license into the new issuance license, and signs the new license. You cannot merely create a new signed issuance license and use it to replace the old one because you will lose the key used to encrypt the content, thereby making it impossible to decrypt the content. Also, you cannot create a new signed issuance license and swap out the content keys by hand because the signature in the new issuance license will not be correct and the consuming application will not therefore accept the license.

> \[!Important\]  
> For [**EditIssuanceLicense**](-editissuancelicense.md) to work, you must specify the application-specific data pair "Allow\_Server\_Editing"/"True" in the original issuance license. Also note that the access control list (ACL) on the EditIssuanceLicense.asmx AD RMS webpage is set to "System" by default. Therefore, if you want to use the **EditIssuanceLicense** method, you must change the ACL for EditIssuanceLicense.asmx to a more appropriate value. It is important to understand that only approved computers or (occasionally) users should have access to this function because anyone with access to this function can gain full rights to any license issued by this service that has the "Allow\_Server\_Editing"/"True" pair.

 

**To republish an issuance license**

1.  Obtain the existing issuance license from the compound file.
2.  Create a new, unsigned issuance license for the content.
3.  Call [**EditIssuanceLicense**](-editissuancelicense.md), passing in both certificates, and retrieve the returned issuance license chain.
4.  Replace the existing issuance license in the compound file. This is shown by the following code example.
    ```C++
    // PaddingLength is a custom function that returns the number of 
    // padding bytes required to bring a submitted number up to 
    // a submitted block size. VERSIONSTAMP is a custom structure.

    // Error handling macro used in the function.
    #define CHECK_STG_ERROR(api, hresult) if(FAILED(hresult))            \
    {                                                                    \
    printf("Error (%s): %S [%d]\n", api, StorageError(hresult), hresult);\
    goto e_Exit;                                                         \
    }

    CDOCLIB_API HRESULT __stdcall UpdatePublishingLicense(
                  WCHAR* wcsRmhFilePath, 
                  WCHAR* wcsEditedLicense)
    {
        // Storages and streams.
        IStorage    *pStorage               = NULL;
        IStorage    *pDataSpaceStorage      = NULL;
        IStorage    *pTransformInfoStorage  = NULL;
        IStorage    *pDRMTransformStorage   = NULL;
        IStream     *pStream                = NULL;
        HRESULT     hResult                 = NULL;
        ULONG       bytesWritten            = 0;
        LPSTR       szRightsLabel           = NULL;
        BYTE        *drm_transform          = NULL;
        LPWSTR      ClassID                 = 
                    L"{C73DFACD-061F-43B0-8B64-0C620D2A8B50}";
        LPWSTR      FeatureIdentifier       = 
                    L"Microsoft.Metadata.DRMTransform";
        LPWSTR      wszSignedIL             = wcsEditedLicense;
        int         IndexOfFeatureIdentifierLength = 88;
        int         TheNumberOne            = 1;
        int         ClassIDLength           = 
                    (int)wcslen(ClassID)*sizeof(WCHAR);
        int         FeatureIdentifierLength = 
                    (int)wcslen(FeatureIdentifier)*sizeof(WCHAR);
        int         TheNumberFour           = 4;
        short       TheNumberZero           = 0;

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

        // Specifies the new stream size.
        ULARGE_INTEGER ui = {0,0};


        // Open the output compound file.
        hResult = StgOpenStorageEx(
                    wcsRmhFilePath,         // File name
                    STGM_READWRITE|         // File access
                      STGM_SHARE_EXCLUSIVE, 
                    STGFMT_STORAGE,         // Compound file
                    0,                      // Required
                    NULL,                   // Required
                    0,                      // Required
                    IID_IStorage,           // IStorage IID
                    (void **)&amp;pStorage);    // IStorage pointer
        CHECK_STG_ERROR("StgOpenStorageEx", hResult);

        // Now navigate down to \006Primary stream, where 
        // the issuance license is stored.
        // \006DataSpaces->TransformInfo->\009DRMTransform->\006Primary.
        
        // \006DataSpaces storage.
        memcpy(StorageName_DataSpaces, &amp;char_six, 2);
        hResult = pStorage->OpenStorage(
                                StorageName_DataSpaces,
                                NULL,
                                STGM_READWRITE|STGM_SHARE_EXCLUSIVE,
                                NULL,
                                0,
                                &amp;pDataSpaceStorage);
        CHECK_STG_ERROR("OpenStorage", hResult);
        
        // TransformInfo storage.
        hResult = pDataSpaceStorage->OpenStorage(
                                StorageName_TransformInfo,
                                NULL,
                                STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
                                NULL,
                                0,
                                &amp;pTransformInfoStorage);
        CHECK_STG_ERROR("OpenStorage[TransformInfo]", hResult);
        
        // \009DRMTransform storage.
        memcpy(StorageName_DRMTransform, &amp;char_nine, 2);
        hResult = pTransformInfoStorage->OpenStorage(
                                StorageName_DRMTransform,
                                NULL,
                                STGM_READWRITE|STGM_SHARE_EXCLUSIVE,
                                NULL,
                                0,
                                &amp;pDRMTransformStorage);
        CHECK_STG_ERROR("OpenStorage[DRMTransform]:", hResult);

        // \006Primary stream.
        hResult = pDRMTransformStorage->OpenStream(
                                StreamName_Primary,
                                NULL,
                                STGM_READWRITE|STGM_SHARE_EXCLUSIVE,
                                0,
                                &amp;pStream);
        CHECK_STG_ERROR("OpenStream[StreamName_Primary]:", hResult);

        // Remove existing issuance license.
        hResult = pStream->SetSize(ui);
        CHECK_STG_ERROR("SetSize:", hResult);

        // Allocate new buffer to hold new issuance license.
        szRightsLabel = (CHAR *)HeapAlloc(
                                GetProcessHeap(),
                                0, 
                                wcslen(wszSignedIL)+1);
        if ( NULL == szRightsLabel )
        {
            printf("Error (%s): E_OUTOFMEMORY\n", "HeapAlloc");
            goto e_Exit;
        }

        // Copy new issuance license into buffer.
        StringCchPrintf(szRightsLabel, 
                        wcslen(wszSignedIL)+1, 
                        "%S", 
                        wszSignedIL);

        // Calculate size of new buffer needed to hold new 
        // stream and allocate memory.
        int RightsLabelLength = (int)strlen(szRightsLabel);
        int TransformLength = 38 + ClassIDLength + 
                              FeatureIdentifierLength + 
                              RightsLabelLength +      
                              PaddingLength(RightsLabelLength,
                                            sizeof(DWORD));
        drm_transform = (BYTE *)HeapAlloc(
                                GetProcessHeap(), 
                                0, 
                                TransformLength);
        if ( NULL == drm_transform )
        {
            printf("Error (%s): E_OUTOFMEMORY\n", "HeapAlloc");
            goto e_Exit;
        }
        ZeroMemory(drm_transform, TransformLength);

        // Copy headers and new issuance license into buffer.
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
               &amp;TheNumberZero, 2);
        memcpy(drm_transform+18+ClassIDLength+FeatureIdentifierLength,
               &amp;version, 12);
        memcpy(drm_transform+30+ClassIDLength+FeatureIdentifierLength,
               &amp;TheNumberFour, 4);
        memcpy(drm_transform+34+ClassIDLength+FeatureIdentifierLength,
               &amp;RightsLabelLength, 4);
        memcpy(drm_transform+38+ClassIDLength+FeatureIdentifierLength,
               szRightsLabel, RightsLabelLength);

        //Write buffer to stream.
        hResult = pStream->Write(
                                (void *)drm_transform, 
                                TransformLength, 
                                &amp;bytesWritten); 
        CHECK_STG_ERROR("IStream::Write", hResult);

        // Commit changes to root storage.
        pStorage->Commit(STGC_DEFAULT);

    e_Exit:
        // Clean up.
        if (pStorage != NULL)
            pStorage->Release();
        if (pDataSpaceStorage != NULL)
            pDataSpaceStorage->Release();
        if (pTransformInfoStorage != NULL)
            pTransformInfoStorage->Release();
        if (pDRMTransformStorage != NULL)
            pDRMTransformStorage->Release();
        if (pStream != NULL)
            pStream->Release();
        if (drm_transform != NULL)
            HeapFree(GetProcessHeap(), NULL, drm_transform);
        if (szRightsLabel != NULL)
            HeapFree(GetProcessHeap(), NULL, szRightsLabel);
        
        return hResult;
    }
    ```

    

## Related topics

<dl> <dt>

[Creating a Compound File and Adding Protected Content](creating-a-compound-file-and-adding-protected-content.md)
</dt> <dt>

[Adding an Issuance License to the Compound File](adding-an-issuance-license-to-the-compound-file.md)
</dt> <dt>

[Adding a Use License to the Compound File](adding-a-use-license-to-the-compound-file.md)
</dt> <dt>

[Publishing Content](publishing-content.md)
</dt> <dt>

[Understanding Compound Files](understanding-compound-files.md)
</dt> </dl>

 

 



