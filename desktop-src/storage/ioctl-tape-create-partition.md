---
title: IOCTL\_TAPE\_CREATE\_PARTITION control code
description: Creates the specified number of fixed, select, or initiator partition(s) of the given size on the media.
ms.assetid: da220281-a08d-4aeb-abb4-471aacb2461a
keywords:
- IOCTL_TAPE_CREATE_PARTITION control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_TAPE_CREATE_PARTITION
api_location:
- Ntddtape.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_TAPE\_CREATE\_PARTITION control code

Creates the specified number of fixed, select, or initiator partition(s) of the given size on the media.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a structure of type [**TAPE\_CREATE\_PARTITION**](tape-create-partition.md) that specifies the partition(s) to be created.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(TAPE\_CREATE\_PARTITION).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_IO\_DEVICE\_ERROR, STATUS\_MEDIA\_WRITE\_PROTECTED, STATUS\_DEVICE\_DATA\_ERROR, STATUS\_NO\_SUCH\_DEVICE, STATUS\_IO\_TIMEOUT, STATUS\_DEVICE\_NOT\_READY, STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_NO\_MEDIA\_IN\_DEVICE, or STATUS\_VERIFY\_REQUIRED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_CREATE\_PARTITION**](tape-create-partition.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_TAPE_CREATE_PARTITION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






