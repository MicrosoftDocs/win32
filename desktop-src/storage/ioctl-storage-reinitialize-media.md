---
title: IOCTL\_STORAGE\_REINITIALIZE\_MEDIA control code
description: A driver can use the IOCTL\_STORAGE\_REINITIALIZE\_MEDIA control code to reinitialize/erase a device.
ms.assetid: 4ECF51C3-D098-49E2-A675-78066A15C221
keywords:
- IOCTL_STORAGE_REINITIALIZE_MEDIA control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_REINITIALIZE_MEDIA
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

# IOCTL\_STORAGE\_REINITIALIZE\_MEDIA control code

A driver can use the **IOCTL\_STORAGE\_REINITIALIZE\_MEDIA** control code to reinitialize/erase a device. The IOCTL offloads the erasure to the storage device; there is no guarantee as to the successful deletion or recoverability of the data of the storage device after the command completes. This IOCTL is limited to data disks on devices in the desktop device family. In Windows Preinstallation Environment (WinPE), this IOCTL is supported for both boot and data disks.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero if the operation completes successfully; otherwise, it is set to a non-zero value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1607<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                        |
| Header<br/>                   | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_REINITIALIZE_MEDIA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





