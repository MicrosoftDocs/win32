---
title: IOCTL\_STORAGE\_READ\_CAPACITY control code
description: The IOCTL\_STORAGE\_READ\_CAPACITY request returns the read capacity information for the target storage device.
ms.assetid: FC4CFD33-5632-400A-90E5-583C6D6DFFD9
keywords:
- IOCTL_STORAGE_READ_CAPACITY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_READ_CAPACITY
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

# IOCTL\_STORAGE\_READ\_CAPACITY control code

The **IOCTL\_STORAGE\_READ\_CAPACITY** request returns the read capacity information for the target storage device.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* contains a [**STORAGE\_READ\_CAPACITY**](storage-read-capacity.md) structure.

## Output Buffer Length

*Parameters.DeviceIoControl.OutputBufferLength* in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least **sizeof**(STORAGE\_READ\_CAPACITY).

## Status block

The **Status** field can be set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_BUFFER\_TOO\_SMALL, STATUS\_BUFFER\_OVERFLOW, or some other error status.

## Remarks

A **IOCTL\_STORAGE\_READ\_CAPACITY** request returns the disk capacity information retrieved during disk initialization. The capacity information is obtained by the system with the SCSI READ CAPACITY command.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_READ\_CAPACITY**](storage-read-capacity.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_READ_CAPACITY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






