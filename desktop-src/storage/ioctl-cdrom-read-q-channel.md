---
title: IOCTL\_CDROM\_READ\_Q\_CHANNEL control code
description: Returns the current position, media catalog, or ISRC track data. Obsolete, beginning with Windows Vista.
ms.assetid: bbcf1535-6454-45b5-bcbd-752b8bfd6517
keywords:
- IOCTL_CDROM_READ_Q_CHANNEL control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_READ_Q_CHANNEL
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_CDROM\_READ\_Q\_CHANNEL control code

Returns the current position, media catalog, or ISRC track data. Obsolete, beginning with Windows Vista.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**CDROM\_SUB\_Q\_DATA\_FORMAT**](cdrom-sub-q-data-format.md) structure with the **Format** member set to one of the following:

<dl> IOCTL\_CDROM\_CURRENT\_POSITION  
IOCTL\_CDROM\_MEDIA\_CATALOG  
IOCTL\_CDROM\_TRACK\_ISRC  
</dl>

If **Format** is set to IOCTL\_CDROM\_TRACK\_ISRC, **Track** must be set to the track for which ISRC data is requested.

## Input Buffer Length

Length of a **Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(SUB\_Q\_CHANNEL\_DATA).

.

## Output Buffer

The driver returns the [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md) information in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

Length of a [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md).

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL, STATUS\_IO\_DEVICE\_ERROR, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_NO\_MEDIA\_IN\_DEVICE, STATUS\_DEVICE\_NOT\_READY, STATUS\_IO\_TIME\_OUT, or STATUS\_VERIFY\_REQUIRED.

## Remarks

Beginning with Windows Vista, CDROM class drivers do not use this IOCTL. Prior to Windows Vista, this IOCTL was used for audio playback on older CD-ROM drives that supported direct audio output in hardware.

Client applications should use the *Media Control Interface (MCI) API* rather than issuing this IOCTL.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Obsolete, beginning with Windows Vista.<br/>                                                         |
| Header<br/>  | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_READ_Q_CHANNEL%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






