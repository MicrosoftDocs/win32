---
title: IOCTL\_STORAGE\_CHECK\_VERIFY control code
description: Determines whether the media has changed on a removable-media device that the caller has opened for read or write access.
ms.assetid: 12e98642-2ed5-47d6-9461-9d6c52149749
keywords:
- IOCTL_STORAGE_CHECK_VERIFY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_CHECK_VERIFY
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_CHECK\_VERIFY control code

Determines whether the media has changed on a removable-media device that the caller has opened for read or write access. If read or write access to the device is not necessary, the caller can improve performance by opening the device with FILE\_READ\_ATTRIBUTES and issuing an[**IOCTL\_STORAGE\_CHECK\_VERIFY2**](ioctl-storage-check-verify2.md) request instead.

For more information, see [Supporting Removable Media](https://msdn.microsoft.com/library/windows/hardware/ff563916).

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

Optionally, for disk and CD-ROM devices, **Irp-&gt;AssociatedIrp.SystemBuffer** points to a buffer to receive the media change count. The driver fills this buffer only if **Parameters.DeviceIoControl.OutputBufferLength** was nonzero and the return value is STATUS\_SUCCESS. The media change count is a ULONG indicating how many times the media has changed since the driver started.

Otherwise, this request has no output.

## Output Buffer Length

Optionally, for disk and CD-ROM devices, **Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of a buffer, which must be &gt;= **sizeof**(ULONG). This field is zero if the optional buffer is not specified.

Otherwise, this request has no input.

## Status block

If a disk or CD-ROM driver has no indication that the media has changed, the driver sets the **Status** field to STATUS\_SUCCESS. In addition, if the optional media change buffer was specified, the driver returns the media change count in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** and sets the **Information** field to **sizeof**(ULONG). If the optional media change buffer was not specified, the driver sets **Information** to zero.

If the driver detects that the media has changed and the volume is mounted (VPB\_MOUNTED is set in the VPB), it must:

1.  Set **Information** to zero.

2.  Set **Status** to STATUS\_VERIFY\_REQUIRED.

3.  Set the DO\_VERIFY\_VOLUME flag in the **DeviceObject.**

4.  Call **IoCompleteRequest** with the input IRP.

If the driver detects that the media has changed, but the volume is not mounted, the driver must not set the DO\_VERIFY\_VOLUME bit. Instead, it should do the following:

1.  Set **Status** to STATUS\_IO\_DEVICE\_ERROR.

2.  Set **Information** to zero.

3.  Call **IoCompleteRequest** with the IRP.

If the driver detects an error such as STATUS\_BUFFER\_TOO\_SMALL, STATUS\_INSUFFICIENT\_RESOURCES, or a device error, it sets **Information** to zero and sets the appropriate error value in the **Status** field.

For a tape driver, the **Information** field is set to zero and the **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_VERIFY\_REQUIRED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_CHECK\_VERIFY2**](ioctl-storage-check-verify2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_CHECK_VERIFY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






