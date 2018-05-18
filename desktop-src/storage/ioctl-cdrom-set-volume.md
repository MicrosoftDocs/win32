---
title: IOCTL\_CDROM\_SET\_VOLUME control code
description: Resets the volume for its device's audio ports. Obsolete, beginning with Windows Vista.
ms.assetid: '9331ad0b-42e0-4f20-9410-fb135f4791b0'
keywords: ["IOCTL_CDROM_SET_VOLUME control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CDROM_SET_VOLUME
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# IOCTL\_CDROM\_SET\_VOLUME control code

Resets the volume for its device's audio ports. Obsolete, beginning with Windows Vista.

## Input Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* contains the [**VOLUME\_CONTROL**](volume-control.md) value or values to be set.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* in the I/O stack location indicates the size, in bytes, of the buffer, which must be greater than or equal to **sizeof**(VOLUME\_CONTROL).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL, STATUS\_DEVICE\_NOT\_READY, STATUS\_IO\_TIMEOUT, STATUS\_IO\_DEVICE\_ERROR, STATUS\_VERIFY\_REQUIRED, or STATUS\_INVALID\_DEVICE\_REQUEST.

## Remarks

Beginning with Windows Vista, CDROM class drivers do not use this IOCTL. Prior to Windows Vista, this IOCTL was used for audio playback on older CD-ROM drives that supported direct audio output in hardware.

Client applications should use the *Media Control Interface (MCI) API* rather than issuing this IOCTL.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Obsolete, beginning with Windows Vista.<br/>                                                         |
| Header<br/>  | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**VOLUME\_CONTROL**](volume-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_SET_VOLUME%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






