---
title: WRITE\_ROTATION enumeration
description: The WRITE\_ROTATION enumeration specifies whether a CD-ROM drive uses constant linear velocity (CLV) rotation or constant angular velocity (CAV) rotation when it writes to a CD.
ms.assetid: e3569e38-cb56-4e33-baba-c479fc4368da
keywords:
- WRITE_ROTATION enumeration Storage Devices
- PWRITE_ROTATION enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- WRITE_ROTATION
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WRITE\_ROTATION enumeration

The WRITE\_ROTATION enumeration specifies whether a CD-ROM drive uses constant linear velocity (CLV) rotation or constant angular velocity (CAV) rotation when it writes to a CD.

## Syntax


```C++
typedef enum _WRITE_ROTATION { 
  CdromDefaultRotation  = 0,
  CdromCAVRotation      = 1
} WRITE_ROTATION, *PWRITE_ROTATION;
```



## Constants

<dl> <dt>

<span id="CdromDefaultRotation"></span><span id="cdromdefaultrotation"></span><span id="CDROMDEFAULTROTATION"></span>**CdromDefaultRotation**
</dt> <dd>

The CD-ROM drive uses the (default) constant linear velocity (CLV) method when it writes to a CD.

</dd> <dt>

<span id="CdromCAVRotation"></span><span id="cdromcavrotation"></span><span id="CDROMCAVROTATION"></span>**CdromCAVRotation**
</dt> <dd>

The CD-ROM drive uses the (default) constant angular velocity (CAV) method when it writes to a CD.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_SPEED\_REQUEST**](cdrom-speed-request.md)
</dt> <dt>

[**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WRITE_ROTATION%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






