---
title: IOCTL\_TAPE\_PREPARE control code
description: Loads or unloads the tape, resets tape tension, locks or unlocks the ejection mechanism, or formats the tape.
ms.assetid: '0e016f3a-4f3a-4256-bb7b-10a5f955b930'
keywords: ["IOCTL_TAPE_PREPARE control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_TAPE_PREPARE
api_location:
- Ntddtape.h
api_type:
- HeaderDef
---

# IOCTL\_TAPE\_PREPARE control code

Loads or unloads the tape, resets tape tension, locks or unlocks the ejection mechanism, or formats the tape.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**TAPE\_PREPARE**](tape-prepare.md) structure that indicates the type of operation.

If the **Immediate** member is **TRUE**, the operation should be asynchronous.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(TAPE\_PREPARE).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_NO\_SUCH\_DEVICE, STATUS\_IO\_TIMEOUT, STATUS\_IO\_DEVICE\_ERROR, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_DEVICE\_NOT\_CONNECTED, STATUS\_MEDIA\_WRITE\_PROTECTED, STATUS\_NO\_MEDIA\_IN\_DEVICE, or STATUS\_VERIFY\_REQUIRED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TapeMiniPrepare**](https://msdn.microsoft.com/library/windows/hardware/ff567950)
</dt> <dt>

[**TAPE\_PREPARE**](tape-prepare.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_TAPE_PREPARE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






