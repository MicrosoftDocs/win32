---
title: How-to enable document tracking and revocation
description: This topic covers the basic guidance for implementing document tracking of content as well as example code for metadata updates and for creating a Track Usage button for your app.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'F5089765-9D94-452B-85E0-00D22675D847'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# How-to: enable document tracking and revocation

This topic covers the basic guidance for implementing document tracking of content as well as example code for metadata updates and for creating a **Track Usage** button for your app.

> [!Note]  
> Document tracking only works only with Azure RMS and does not currently work with AD RMS.

 

## Steps to implement document tracking

Steps 1 and 2 enable the document to be tracked. Step 3 enables your app users to reach the document tracking site in order to track and revoke your protected documents.

<dl> 1. Add document tracking metadata  
2. Register the document with the RMS service  
3. Add **Track Usage** button to your app  
</dl>

The implementation details for these steps follow.

## 1. Add document tracking metadata

Document tracking is a feature of the Rights Management system. By adding specific metadata during the document protection process, a document can be registered with the tracking service portal which then provides several options for tracking.

Use these APIs to add/update a content license with document tracking metadata.

-   [**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md)
-   [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md)

    We expect that you will set all of the metadata properties. Here they are, listed by type.

    For more information, see [**License metadata property types**](license-metadata-property-types.md).

    -   **IPC\_MD\_CONTENT\_PATH**

        Use to identify the tracked document. In cases where a full path is not possible, just provide the file name.

    -   **IPC\_MD\_CONTENT\_NAME**

        Use to identify the tracked document name.

    -   **IPC\_MD\_NOTIFICATION\_TYPE**

        Use to specify when notification will be sent. For more information, see [**Notification type**](notification-type.md).

    -   **IPC\_MD\_NOTIFICATION\_PREFERENCE**

        Use to specify the type of notification. For more information, see [**Notification preference**](notification-preference.md).

    -   **IPC\_MD\_DATE\_MODIFIED**

        We suggest that you set this date each time the user clicks **Save**.

    -   **IPC\_MD\_DATE\_CREATED**

        Use to set the origination date of the file.

-   [**IpcSerializeLicenseWithMetadata**](ipcserializelicensemetadata.md)

Use the appropriate one of these APIs to add the metadata to your file or stream.

-   [**IpcfEncryptFileWithMetadata**](ipcfencryptfilewithmetadata.md)
-   [**IpcfEncryptFileStreamWithMetadata**](ipcfencryptfilestreamwithmetadata.md)

Lastly, use this API to register your tracked document with the tracking system.

-   [**IpcRegisterLicense**](ipcregisterlicense.md)

## 2. Register the document with the RMS service

Here's a code snippet showing an example of setting document tracking metadata and the call to register with the tracking system.


```C++
HRESULT hr = S_OK;
    LPCWSTR wszOutputFile = NULL;
    wstring wszWorkingFile;
    IPC_LICENSE_METADATA md = {0};
   
    md.cbSize = sizeof(IPC_LICENSE_METADATA);
    md.dwNotificationType = IPCD_CT_NOTIFICATION_TYPE_ENABLED;
    md.dwNotificationPreference = IPCD_CT_NOTIFICATION_PREF_DIGEST;
    //file origination date, current time for this example
    md.ftDateCreated = GetCurrentTime(); 
    md.ftDateModified = GetCurrentTime();

    LOGSTATUS_EX(L"Encrypt file with official template...");

    hr =IpcfEncryptFileWithMetadata( wszWorkingFile.c_str(),
                                     m_wszTestTemplateID.c_str(),
                                     IPCF_EF_TEMPLATE_ID,
                                     0,
                                     NULL,
                                     NULL,
                                     &amp;md,
                                     &amp;wszOutputFile);

    /* This will contain the serialized license */
    PIPC_BUFFER pSerializedLicense; 
    
    /* the context to use for the call */
    PCIPC_PROMPT_CTX pContext; 
 
    wstring wstrContentName(“MyDocument.txt”);
    bool sendLicenseRegistrationNotificationEmail = FALSE;

    hr = IpcRegisterLicense( pSerializedLicense, 
                              0, 
                              pContext, 
                              wstrContentName.c_str(), 
                              sendLicenseRegistrationNotificationEmail);
```



## 3. Add a **Track Usage** button to your app

Adding a **Track Usage** UI item to your app is as simple as using one of the following URL formats:

-   Using Content ID

    -   Get the content ID by using [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) or [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) if the license is serialized and use the license property **IPC\_LI\_CONTENT\_ID**. For more information, see [**License property types**](license-property-types.md).
    -   With the **ContentId** and **Issuer** metadata, use the following format: `https://track.azurerms.com/#/{ContentId}/{Issuer}`

        Example - `https://track.azurerms.com/#/summary/05405df5-8ad6-4905-9f15-fc2ecbd8d0f7/janedoe@microsoft.com`

-   If you don’t have access to that metadata (i.e. you are examining the unprotected version of the document), you can use the **Content\_Name** in the following format: `https://track.azurerms.com/#/?q={ContentName}`

    Example - `https://track.azurerms.com/#/?q=Secret!.txt`

The client simply needs to open a browser with the appropriate URL. The RMS Document Tracking portal will handle authentication and any required redirection.

## Related topics

<dl> <dt>

[**License metadata property types**](license-metadata-property-types.md)
</dt> <dt>

[**Notification preference**](notification-preference.md)
</dt> <dt>

[**Notification type**](notification-type.md)
</dt> <dt>

[**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md)
</dt> <dt>

[**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md)
</dt> <dt>

[**IpcSerializeLicenseWithMetadata**](ipcserializelicensemetadata.md)
</dt> <dt>

[**IpcfEncryptFileWithMetadata**](ipcfencryptfilewithmetadata.md)
</dt> <dt>

[**IpcfEncryptFileStreamWithMetadata**](ipcfencryptfilestreamwithmetadata.md)
</dt> <dt>

[**IpcRegisterLicense**](ipcregisterlicense.md)
</dt> </dl>

 

 




