---
title: IOCTL\_TAPE\_WRITE\_MARKS control code
description: Writes one of setmarks, filemarks, short filemarks, or long filemarks to tape.
ms.assetid: cc4dabe3-4e14-4495-89b4-37f1a31ea62d
keywords:
- IOCTL_TAPE_WRITE_MARKS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_TAPE_WRITE_MARKS
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

# IOCTL\_TAPE\_WRITE\_MARKS control code

Writes one of setmarks, filemarks, short filemarks, or long filemarks to tape.

## Input Buffer

The [**TAPE\_WRITE\_MARKS**](tape-write-marks.md) structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** indicates the type and number of marks to write.

If the **Immediate** member is **TRUE**, the operation should be asynchronous.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(TAPE\_WRITE\_MARKS).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to the number of bytes written. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_IO\_DEVICE\_ERROR, STATUS\_DEVICE\_DATA\_ERROR, STATUS\_NO\_SUCH\_DEVICE, STATUS\_IO\_TIMEOUT, STATUS\_DEVICE\_NOT\_READY, STATUS\_MEDIA\_WRITE\_PROTECTED, STATUS\_NO\_MEDIA\_IN\_DEVICE, or STATUS\_VERIFY\_REQUIRED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_WRITE\_MARKS**](tape-write-marks.md)
</dt> <dt>

[**TapeMiniWriteMarks**](https://msdn.microsoft.com/library/windows/hardware/ff567958)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_TAPE_WRITE_MARKS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






