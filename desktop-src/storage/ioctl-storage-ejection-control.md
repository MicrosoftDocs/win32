---
title: IOCTL\_STORAGE\_EJECTION\_CONTROL control code
description: Locks the device to prevent removal of the media.
ms.assetid: 0b9726a1-0658-4eda-8f27-abf647cdc046
keywords:
- IOCTL_STORAGE_EJECTION_CONTROL control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_EJECTION_CONTROL
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_EJECTION\_CONTROL control code

Locks the device to prevent removal of the media. If the driver can prevent the media from being removed while the drive is in use, the driver disables or enables the mechanism that ejects media, thereby locking the drive. A caller must open the device with FILE\_READ\_ATTRIBUTES to send this request.

Unlike [**IOCTL\_STORAGE\_MEDIA\_REMOVAL**](ioctl-storage-media-removal.md), the driver tracks **IOCTL\_STORAGE\_EJECTION\_CONTROL** requests by caller and ignores unlock requests for which it has not received a lock request from the same caller, thereby preventing other callers from unlocking the drive.

A driver for a removable-media device - can support this IOCTL must do the following:

1.  Keep a lock count, tagged by caller, in the device object extension.

2.  Keep the lock count per physical device.

3.  When called with this IOCTL, if the flag to prevent removing the media is set, increment the count; if the flag is clear and the driver has previously received a lock request from the same caller, decrement the count.

4.  Prevent removal of the media unless all lock counts are zero.

Under normal circumstances, the caller who locked the device using IOCTL\_STORAGE\_EJECTION\_CONTROL, unlocks the device by sending IOCTL\_STORAGE\_EJECTION\_CONTROL again with **Irp-&gt;AssociatedIrp.SystemBuffer** set to a boolean value of **FALSE**. However, sometimes the caller fails to unlock the device properly.

To ensure that media removal locks are released properly, the class driver keeps track of callers who lock the media with IOCTL\_STORAGE\_EJECTION\_CONTROL. If the caller terminates without unlocking the device, the class driver unlocks the device.

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

[**IOCTL\_STORAGE\_EJECT\_MEDIA**](ioctl-storage-eject-media.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_EJECTION_CONTROL%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






