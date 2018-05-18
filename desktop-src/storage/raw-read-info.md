---
title: RAW\_READ\_INFO structure
description: The RAW\_READ\_INFO structure is used in conjunction with the IOCTL\_CDROM\_RAW\_READ request to read data from a CD-ROM in raw mode.
ms.assetid: '8786545d-39b2-4331-9d62-3b345eb58d1f'
keywords: ["RAW_READ_INFO structure Storage Devices", "PRAW_READ_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- RAW_READ_INFO
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# RAW\_READ\_INFO structure

The RAW\_READ\_INFO structure is used in conjunction with the [**IOCTL\_CDROM\_RAW\_READ**](ioctl-cdrom-raw-read.md) request to read data from a CD-ROM in raw mode.

## Syntax


```C++
typedef struct __RAW_READ_INFO {
  LARGE_INTEGER   DiskOffset;
  ULONG           SectorCount;
  TRACK_MODE_TYPE TrackMode;
} RAW_READ_INFO, *PRAW_READ_INFO;
```



## Members

<dl> <dt>

**DiskOffset**
</dt> <dd>

Contains an offset into the CD-ROM disc where data will be read. You can calculate this offset by multiplying the starting sector number for the request times 2048.

</dd> <dt>

**SectorCount**
</dt> <dd>

Contains the number of sectors to read.

</dd> <dt>

**TrackMode**
</dt> <dd>

Contains an enumerator of type [**TRACK\_MODE\_TYPE**](track-mode-type.md) that indicates the type of the track mode.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_RAW\_READ**](ioctl-cdrom-raw-read.md)
</dt> <dt>

[**TRACK\_MODE\_TYPE**](track-mode-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RAW_READ_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






