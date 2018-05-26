---
title: IOCTL\_TAPE\_SET\_POSITION control code
description: Moves the current position on the tape to the specified partition and offset, according to the given method.
ms.assetid: 93918e09-2742-47ca-94a5-043af2a3a338
keywords:
- IOCTL_TAPE_SET_POSITION control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_TAPE_SET_POSITION
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

# IOCTL\_TAPE\_SET\_POSITION control code

Moves the current position on the tape to the specified partition and offset, according to the given method.

## Input Buffer

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(TAPE\_SET\_POSITION).

The [**TAPE\_SET\_POSITION**](tape-set-position.md) structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** indicates the partition and offset to which the tape is to be moved.

If the **Immediate** member is **TRUE**, the operation should be asynchronous.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(TAPE\_SET\_POSITION).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_IO\_DEVICE\_ERROR, STATUS\_DEVICE\_DATA\_ERROR, STATUS\_NO\_SUCH\_DEVICE, STATUS\_IO\_TIMEOUT, STATUS\_DEVICE\_NOT\_READY, STATUS\_NO\_MEDIA\_IN\_DEVICE, or STATUS\_VERIFY\_REQUIRED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_SET\_POSITION**](tape-set-position.md)
</dt> <dt>

[**TapeMiniSetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff567954)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_TAPE_SET_POSITION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






