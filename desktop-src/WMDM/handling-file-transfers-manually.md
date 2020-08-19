---
title: Handling File Transfers Manually
description: Handling File Transfers Manually
ms.assetid: ff94191b-a0f2-4118-996c-d040f214fb9b
keywords:
- Windows Media Device Manager,manual file transfers
- Device Manager,manual file transfers
- programming guide,manual file transfers
- desktop applications,manual file transfers
- creating Windows Media Device Manager applications,manual file transfers
- manual file transfers
ms.topic: article
ms.date: 05/31/2018
---

# Handling File Transfers Manually

Your application can implement the [**IWMDMOperation**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmoperation) interface to manage part of the reading or writing process. On a read from device, the implementation enables the application to receive blocks of raw data from a device file. On a write to device, it enables the application to send blocks of raw data to a file on the device.

In both read and write operations, the [**IWMDMOperation::TransferObjectData**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-transferobjectdata) method passes the data between the computer and the device. To know the direction of the data transfer, your application must set a flag when Windows Media Device Manager calls [**BeginRead**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-beginread) or [**BeginWrite**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-beginwrite). When the [**End**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-end) method is called, the application should reset this flag.

> [!Note]  
> If the service provider and device properly implement [**IMDSPObject2**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspobject2), it will first call the application's [IWMDMOperation3::TransferObjectDataOnClearChannel](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation3-transferobjectdataonclearchannel) method, if implemented. This method is a more efficient way of transferring data. **TransferObjectDataOnClearChannel** is handled the same way as **TransferObjectData**, except that the data is never encrypted and has no MAC values to verify.

 

The following sections describe both the reading and the writing process, when your application implements **IWMDMOperation**.

**Reading from a device**

When reading a file from a device, Windows Media Device Manager calls the following **IWMDMOperation** methods in order:

-   [**BeginRead**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-beginread) Called to notify the application that a read from device is beginning.
-   [**TransferObjectData**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-transferobjectdata) Called one or more times. The processing of data is described in the following steps:
    1.  **TransferObjectData** receives a buffer, *pData*, of size *pdwSize* bytes, filled with data, and a MAC to verify the incoming data.
    2.  The application verifies the incoming parameters with the incoming data MAC.
    3.  The application decrypts and reads as much of the data in *pData* as it can, and modifies the returned value of *pdwSize* to indicate how many bytes were actually read.
    4.  The application decrypts the data, using [**CSecureChannelClient::DecryptParam**](/previous-versions/bb231586(v=vs.85)), and stores it or uses it, as needed.
    5.  **TransferObjectData** returns S\_OK.
    6.  Windows Media Device Manager continues to call **TransferObjectData** until the application has read all the data from the file, or the application returns WMDM\_E\_USER\_CANCELLED to cancel the operation (in which case the read is canceled, and Windows Media Device Manager calls **End**).
-   [**End**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-end) Called to notify the application that a read from device is ending.

**Writing to a device**

When writing a file to the device, Windows Media Device Manager calls the following **IWMDMOperation** methods in order:

-   [**GetObjectName**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-getobjectname) Called to allow the application to specify a name for the new storage. This method is only called if the application did not specify a name in the **Insert** method.
-   [**GetObjectAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-getobjectattributes) Called to allow the application to specify attributes for the new storage on the device.
-   [**BeginWrite**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-beginwrite) Called to notify that that a write to device is beginning.
-   [**GetObjectTotalSize**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-getobjecttotalsize) Called to retrieve the total size of the object being written to the device, to enable optimization of the transfer, and also to give Windows Media Device Manager an opportunity to cancel the transfer if the file is too large for the device.
-   [**TransferObjectData**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-transferobjectdata) Called one or more times. The processing of data is described in the following steps:
    1.  **TransferObjectData** receives a pointer to a buffer of size *pdwSize* bytes.
    2.  The application gets a block of data to send to the device, usually by reading data from a file, and fills the received buffer with up to *pdwSize* bytes. It should modify *pdwSize* (if necessary) to reflect how many bytes were added to the buffer.
    3.  The application creates a MAC of all the method parameters.
    4.  The application encrypts the data in the buffer, using [**CSecureChannelClient::EncryptParam**](/previous-versions/bb231587(v=vs.85)).
    5.  **TransferObjectData** returns S\_OK to indicate that there is more data, or S\_FALSE to indicate that there is no more data. If the application returns WMDM\_E\_USER\_CANCELLED, the write operation is canceled and Windows Media Device Manager will call **End**.
    6.  Windows Media Device Manager continues to call **TransferObjectData** as long as the application returns S\_OK.
-   [**End**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmoperation-end) Called to notify that a write to device is ending.

For a code example, see [Encryption and Decryption](encryption-and-decryption.md).

## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> </dl>

 

 