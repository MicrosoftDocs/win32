---
title: CDROM\_SET\_SPEED structure
description: The CDROM\_SET\_SPEED structure is used with the IOCTL\_CDROM\_SET\_SPEED request to set the spindle speed of a CD-ROM drive during data transfers in which no data loss is permitted.
ms.assetid: '42cffab4-d8a7-4dff-9f53-19aa2769a85c'
keywords: ["CDROM_SET_SPEED structure Storage Devices", "PCDROM_SET_SPEED structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_SET_SPEED
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_SET\_SPEED structure

The CDROM\_SET\_SPEED structure is used with the [**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md) request to set the spindle speed of a CD-ROM drive during data transfers in which no data loss is permitted.

## Syntax


```C++
typedef struct _CDROM_SET_SPEED {
  CDROM_SPEED_REQUEST RequestType;
  USHORT              ReadSpeed;
  USHORT              WriteSpeed;
  WRITE_ROTATION      RotationControl;
} CDROM_SET_SPEED, *PCDROM_SET_SPEED;
```



## Members

<dl> <dt>

**RequestType**
</dt> <dd>

A [**CDROM\_SPEED\_REQUEST**](cdrom-speed-request.md)-typed value that indicates the type of set speed operation for [**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md) to perform.

</dd> <dt>

**ReadSpeed**
</dt> <dd>

The read speed, in kilobytes per second.

</dd> <dt>

**WriteSpeed**
</dt> <dd>

The write speed, in kilobytes per second.

</dd> <dt>

**RotationControl**
</dt> <dd>

A [**WRITE\_ROTATION**](write-rotation.md)-typed value that indicates whether the drive uses constant angular velocity (CAV) or constant linear velocity (CLV) rotation when it writes to a CD.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_SET\_STREAMING**](cdrom-set-streaming.md)
</dt> <dt>

[**CDROM\_SPEED\_REQUEST**](cdrom-speed-request.md)
</dt> <dt>

[**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md)
</dt> <dt>

[**WRITE\_ROTATION**](write-rotation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_SET_SPEED%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






