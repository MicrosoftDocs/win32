---
title: CDROM\_AUDIO\_CONTROL structure
description: The CDROM\_AUDIO\_CONTROL structure is used in conjunction with the IOCTL\_CDROM\_GET\_CONTROL request to report the audio playback mode.
ms.assetid: f99ad24d-e1cf-4381-93b9-c10e4b19b401
keywords:
- CDROM_AUDIO_CONTROL structure Storage Devices
- PCDROM_AUDIO_CONTROL structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_AUDIO_CONTROL
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDROM\_AUDIO\_CONTROL structure

The CDROM\_AUDIO\_CONTROL structure is used in conjunction with the IOCTL\_CDROM\_GET\_CONTROL request to report the audio playback mode.

## Syntax


```C++
typedef struct _CDROM_AUDIO_CONTROL {
  UCHAR  LbaFormat;
  USHORT LogicalBlocksPerSecond;
} CDROM_AUDIO_CONTROL, *PCDROM_AUDIO_CONTROL;
```



## Members

<dl> <dt>

**LbaFormat**
</dt> <dd>

Contains the logical block address (LBA) format.

</dd> <dt>

**LogicalBlocksPerSecond**
</dt> <dd>

Contains the number of logical blocks per second.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_CONTROL**](ioctl-cdrom-get-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_AUDIO_CONTROL%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






