---
title: CDROM\_SEEK\_AUDIO\_MSF structure
description: The CDROM\_SEEK\_AUDIO\_MSF structure contains the minute, second, and frame that the device must seek to upon receipt of a device control IRP with a control code of IOCTL\_CDROM\_SEEK\_AUDIO\_MSF.
ms.assetid: '8fd4e642-5ed4-409e-bcc2-94d309a1e04c'
keywords: ["CDROM_SEEK_AUDIO_MSF structure Storage Devices", "PCDROM_SEEK_AUDIO_MSF structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_SEEK_AUDIO_MSF
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_SEEK\_AUDIO\_MSF structure

The CDROM\_SEEK\_AUDIO\_MSF structure contains the minute, second, and frame that the device must seek to upon receipt of a device control IRP with a control code of [**IOCTL\_CDROM\_SEEK\_AUDIO\_MSF**](ioctl-cdrom-seek-audio-msf.md).

## Syntax


```C++
typedef struct _CDROM_SEEK_AUDIO_MSF {
  UCHAR M;
  UCHAR S;
  UCHAR F;
} CDROM_SEEK_AUDIO_MSF, *PCDROM_SEEK_AUDIO_MSF;
```



## Members

<dl> <dt>

**M**
</dt> <dd>

Contains an integer between 0 and 74 that indicates the minute to seek to.

</dd> <dt>

**S**
</dt> <dd>

Contains an integer between 0 and 59 that indicates the second to seek to.

</dd> <dt>

**F**
</dt> <dd>

Contains an integer between 0 and 74 that indicates the frame to seek to.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_SEEK\_AUDIO\_MSF**](ioctl-cdrom-seek-audio-msf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_SEEK_AUDIO_MSF%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






