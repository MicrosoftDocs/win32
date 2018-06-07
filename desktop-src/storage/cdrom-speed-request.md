---
title: CDROM\_SPEED\_REQUEST enumeration
description: The CDROM\_SPEED\_REQUEST enumeration indicates which command that the CD-ROM class driver will use to set the spindle speed of a CD-ROM drive.
ms.assetid: 147d2c1c-c12d-4c39-bec5-579ece083ee7
keywords:
- CDROM_SPEED_REQUEST enumeration Storage Devices
- PCDROM_SPEED_REQUEST enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_SPEED_REQUEST
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CDROM\_SPEED\_REQUEST enumeration

The CDROM\_SPEED\_REQUEST enumeration indicates which command that the CD-ROM class driver will use to set the spindle speed of a CD-ROM drive.

## Syntax


```C++
typedef enum _CDROM_SPEED_REQUEST { 
  CdromSetSpeed      = 0,
  CdromSetStreaming  = 1
} CDROM_SPEED_REQUEST, *PCDROM_SPEED_REQUEST;
```



## Constants

<dl> <dt>

<span id="CdromSetSpeed"></span><span id="cdromsetspeed"></span><span id="CDROMSETSPEED"></span>**CdromSetSpeed**
</dt> <dd>

The CD-ROM class driver will use the SET CD SPEED command to set the spindle speed.

</dd> <dt>

<span id="CdromSetStreaming"></span><span id="cdromsetstreaming"></span><span id="CDROMSETSTREAMING"></span>**CdromSetStreaming**
</dt> <dd>

The CD-ROM class driver will use the SET STREAMING command to set the spindle speed.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_SET\_SPEED**](cdrom-set-speed.md)
</dt> <dt>

[**CDROM\_SET\_STREAMING**](cdrom-set-streaming.md)
</dt> <dt>

[**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_SPEED_REQUEST%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






