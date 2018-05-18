---
title: IOCTL\_CDROM\_GET\_CONTROL control code
description: This IOCTL request is obsolete. Do not use.Determines the current audio playback mode.
ms.assetid: '3d474eb7-6622-48fd-bf40-c17d03933828'
keywords: ["IOCTL_CDROM_GET_CONTROL control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CDROM_GET_CONTROL
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# IOCTL\_CDROM\_GET\_CONTROL control code

This IOCTL request is obsolete. Do not use.

Determines the current audio playback mode.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**CDROM\_AUDIO\_CONTROL**](cdrom-audio-control.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(CDROM\_AUDIO\_CONTROL).

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL, STATUS\_DEVICE\_NOT\_READY, STATUS\_IO\_DEVICE\_ERROR, STATUS\_IO\_TIMEOUT, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_VERIFY\_REQUIRED, or STATUS\_INVALID\_DEVICE\_REQUEST.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_AUDIO\_CONTROL**](cdrom-audio-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_GET_CONTROL%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






