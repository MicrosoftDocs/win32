---
title: Sending the File to the Device
description: Sending the File to the Device
ms.assetid: 202185b8-f10e-4108-a950-60658c006cec
keywords:
- Windows Media Device Manager,sending files to devices
- Device Manager,sending files to devices
- programming guide,sending files to devices
- desktop applications,sending files to devices
- creating Windows Media Device Manager applications,sending files to devices
- writing files to devices,sending files to devices
ms.topic: article
ms.date: 05/31/2018
---

# Sending the File to the Device

After the file has been transcoded if necessary, and all metadata including the format has been set, your application can send the file to the device. In order to do so, you must first get an **IWMDMStorageControl** interface (or a later version) for a target location on the device. The **Insert** flags specify whether the new storage should be a sibling or child of the target. Once you have gotten the target, you can call [**IWMDMStorageControl::Insert**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-insert), [**IWMDMStorageControl2::Insert2**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol2-insert2), or [**IWMDMStorageControl3::Insert3**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol3-insert3) to transfer the file. The application can handle reading the file data itself by implementing [**IWMDMOperation**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmoperation), or it can allow the **Insert** method to read and transfer the file automatically by not providing a pointer to an application-implemented **IWMDMOperation**.

The following C++ code demonstrates calling **Insert3** to write a file to a device. If the *pOperation* pointer passed to **Insert3** is **NULL**, the file will be sent in one step; if this pointer is a valid interface pointer, Windows Media Device Manager will call your callback method to get data in blocks. For details on how to implement **IWMDMOperation**, see [Handling File Transfers Manually](handling-file-transfers-manually.md).


```C++
// Set the flags for the operation
UINT flags = WMDM_MODE_BLOCK | // Synchronous call. 
    WMDM_STORAGECONTROL_INSERTINTO | // Insert it into the destination folder.
    WMDM_CONTENT_FILE | // We're inserting a file.
    WMDM_FILE_CREATE_OVERWRITE; // Overwrite existing files.
if (pOperation != NULL)
    flags |= WMDM_CONTENT_OPERATIONINTERFACE;

// Send the file and metadata.
hr = pStgCtl3->Insert3(
    flags,
    WMDM_FILE_ATTR_FOLDER, // The current storage is a folder.
    const_cast<WCHAR*>(pwszFileName), // Source file.
    L"My New File.wma",//NULL, // Destination file name.
    pOperation, // NULL to allow the SDK to read the file; 
                // non-NULL to present raw data bytes to the SDK.
    pProgress, // Interface to send simple progress notifications.
    pMetadata, // IWMDMMetaData interface previously created and filled.
    NULL, 
    &pNewStorage); // Out: handle to the new storage, if the method succeeds.
```



## Related topics

<dl> <dt>

[**Writing Files to the Device**](writing-files-to-the-device.md)
</dt> </dl>

 

 




