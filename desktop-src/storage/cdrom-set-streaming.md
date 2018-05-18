---
title: CDROM\_SET\_STREAMING structure
description: The CDROM\_SET\_SPEED structure is used with the IOCTL\_CDROM\_SET\_SPEED request to set the spindle speed of a CD-ROM drive during isochronous transfers that permit some data loss.
ms.assetid: 'e5c2d421-5994-4f1d-9022-718500eef1a9'
keywords: ["CDROM_SET_STREAMING structure Storage Devices", "PCDROM_SET_STREAMING structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_SET_STREAMING
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_SET\_STREAMING structure

The CDROM\_SET\_SPEED structure is used with the [**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md) request to set the spindle speed of a CD-ROM drive during isochronous transfers that permit some data loss.

## Syntax


```C++
typedef struct _CDROM_SET_STREAMING {
  CDROM_SPEED_REQUEST RequestType;
  ULONG               ReadSize;
  ULONG               ReadTime;
  ULONG               WriteSize;
  ULONG               WriteTime;
  ULONG               StartLba;
  ULONG               EndLba;
  WRITE_ROTATION      RotationControl;
  BOOLEAN             RestoreDefaults;
  BOOLEAN             SetExact;
  BOOLEAN             RandomAccess;
  BOOLEAN             Persistent;
} CDROM_SET_STREAMING, *PCDROM_SET_STREAMING;
```



## Members

<dl> <dt>

**RequestType**
</dt> <dd>

A [**CDROM\_SPEED\_REQUEST**](cdrom-speed-request.md)-typed value that indicates which multimedia command to use when setting the spindle speed.

</dd> <dt>

**ReadSize**
</dt> <dd>

The number of kilobytes to read in each unit of time, where a unit of time is specified by **ReadTime**. A value of 0xFFFF in **ReadSize** selects the optimal data transfer speed of the drive.

</dd> <dt>

**ReadTime**
</dt> <dd>

The number of milliseconds in which to read **ReadSize** kilobytes of data.

</dd> <dt>

**WriteSize**
</dt> <dd>

The number of kilobytes to write in each unit of time, where a unit of time is defined by **WriteTime**. A value of 0xFFFF in **WriteSize** selects the optimal data transfer speed of the drive.

</dd> <dt>

**WriteTime**
</dt> <dd>

The number of milliseconds in which to write **WriteSize** kilobytes of data.

</dd> <dt>

**StartLba**
</dt> <dd>

The first logical block address, in bytes, of the IOCTL\_CDROM\_SET\_SPEED request.

</dd> <dt>

**EndLba**
</dt> <dd>

The last logical block address, in bytes, of the IOCTL\_CDROM\_SET\_SPEED request.

</dd> <dt>

**RotationControl**
</dt> <dd>

A [**WRITE\_ROTATION**](write-rotation.md)-typed value that indicates whether the device will write to the media by using CLV (constant linear velocity) rotation or CLA (constant angular velocity) rotation.

</dd> <dt>

**RestoreDefaults**
</dt> <dd>

A BOOLEAN value that, when **TRUE**, instructs the CD-ROM class driver to make the CD-ROM drive run at its default spindle speed. A value of **FALSE** instructs the class driver to calculate the spindle speed from the **ReadSize**, **ReadTime**, **WriteSize**, and **WriteTime** members of this structure.

</dd> <dt>

**SetExact**
</dt> <dd>

A BOOLEAN value that, when **TRUE**, instructs the CD-ROM class driver to set the CD-ROM drive to the exact speed that is specified by the **ReadSize**, **ReadTime**, **WriteSize**, and **WriteTime** members of this structure. If the class driver cannot set the spindle speed to the exact value that is specified by these members, it fails the request. A value of **FALSE** in **SetExact** instructs the class driver to make the spindle speed of the drive match as closely as possible the speed that is specified by **ReadSize**, **ReadTime**, **WriteSize**, and **WriteTime**; the class driver does not fail the request if the drive cannot run at the exact value that these members specify.

</dd> <dt>

**RandomAccess**
</dt> <dd>

A BOOLEAN value that, when **TRUE**, instructs the CD-ROM class driver to configure the CD-ROM drive, so that it will switch back and forth between read and write operations to maximize performance (data throughput), even if switching between read and write operations causes a particular read or write operation to occur more slowly. In other words, a value of **TRUE** in **RandomAccess** permits the drive to lower the speed of some individual read and write operations to ensure better overall performance in data transfers. A value of **FALSE** instructs the CD-ROM class driver to configure the CD-ROM drive to guarantee the speeds of read and write operations, independent of one another. The data transfer rate of each operation is rigid, and the drive will not alter the speed to achieve performance gains.

</dd> <dt>

**Persistent**
</dt> <dd>

A BOOLEAN value that, when **TRUE**, instructs the CD-ROM class driver to configure the CD-ROM drive to restore the default speed when the user changes the media. A value of **FALSE** instructs the CD-ROM class driver to configure the CD-ROM drive to maintain its speed until the computer restarts or the class driver changes the speed with another command.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_SET\_SPEED**](cdrom-set-speed.md)
</dt> <dt>

[**CDROM\_SPEED\_REQUEST**](cdrom-speed-request.md)
</dt> <dt>

[**IOCTL\_CDROM\_SET\_SPEED**](ioctl-cdrom-set-speed.md)
</dt> <dt>

[**WRITE\_ROTATION**](write-rotation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_SET_STREAMING%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






