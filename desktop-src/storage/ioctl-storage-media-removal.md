---
title: IOCTL\_STORAGE\_MEDIA\_REMOVAL control code
description: Locks the device to prevent removal of the media.
ms.assetid: 'ea8d7924-7ecc-47df-9616-8e2ed60c3de8'
keywords: ["IOCTL_STORAGE_MEDIA_REMOVAL control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_MEDIA_REMOVAL
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# IOCTL\_STORAGE\_MEDIA\_REMOVAL control code

Locks the device to prevent removal of the media. If the driver can prevent the media from being removed while the drive is in use, it disables or enables the mechanism that ejects media on a device - the caller has opened for read or write access.

Unlike [**IOCTL\_STORAGE\_EJECTION\_CONTROL**](ioctl-storage-ejection-control.md), for which the driver tracks requests by caller, the driver ignores IOCTL\_STORAGE\_MEDIA\_REMOVAL unlock requests only if its lock count is already zero, thereby allowing any caller to unlock the drive.

A driver for such a removable-media device that can support this IOCTL must do the following:

1.  Keep a lock count in the device object extension.

2.  Keep the lock count per physical device.

3.  When called with this IOCTL, if the flag to prevent removing the media is set, increment the count; if the flag is clear, decrement the count.

4.  Prevent removal of the media unless all lock counts are zero.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a Boolean value, with **TRUE** indicating that the driver should lock the media in the drive.

## Input Buffer Length

The length of a Boolean.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_NO\_MEDIA\_IN\_DEVICE, or STATUS\_DEVICE\_NOT\_CONNECTED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_EJECTION\_CONTROL**](ioctl-storage-ejection-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_MEDIA_REMOVAL%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






