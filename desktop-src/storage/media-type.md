---
title: \_MEDIA\_TYPE enumeration
description: The MEDIA\_TYPE enumerators are used in conjunction with the IOCTL\_DISK\_FORMAT\_TRACKS request to format the specified set of contiguous tracks on the disk.
ms.assetid: '3fae425a-fff7-4988-9df6-22bf15d51a7f'
keywords: ["_MEDIA_TYPE enumeration Storage Devices", "MEDIA_TYPE enumeration Storage Devices", "PMEDIA_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MEDIA_TYPE
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# \_MEDIA\_TYPE enumeration

The MEDIA\_TYPE enumerators are used in conjunction with the [**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md) request to format the specified set of contiguous tracks on the disk.

## Syntax


```C++
typedef enum _MEDIA_TYPE { 
  Unknown         = 0,
  F5_1Pt2_512     = 1,
  F3_1Pt44_512    = 2,
  F3_2Pt88_512    = 3,
  F3_20Pt8_512    = 4,
  F3_720_512      = 5,
  F5_360_512      = 6,
  F5_320_512      = 7,
  F5_320_1024     = 8,
  F5_180_512      = 9,
  F5_160_512      = 10,
  RemovableMedia  = 11,
  FixedMedia      = 12,
  F3_120M_512     = 13,
  F3_640_512      = 14,
  F5_640_512      = 15,
  F5_720_512      = 16,
  F3_1Pt2_512     = 17,
  F3_1Pt23_1024   = 18,
  F5_1Pt23_1024   = 19,
  F3_128Mb_512    = 20,
  F3_230Mb_512    = 21,
  F8_256_128      = 22,
  F3_200Mb_512    = 23,
  F3_240M_512     = 24,
  F3_32M_512      = 25
} MEDIA_TYPE, *PMEDIA_TYPE;
```



## Constants

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown**
</dt> <dd>

Format is unknown.

</dd> <dt>

<span id="F5_1Pt2_512"></span><span id="f5_1pt2_512"></span><span id="F5_1PT2_512"></span>**F5\_1Pt2\_512**
</dt> <dd>

Indicates 5.25", 1.2 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_1Pt44_512"></span><span id="f3_1pt44_512"></span><span id="F3_1PT44_512"></span>**F3\_1Pt44\_512**
</dt> <dd>

Indicates 3.5", 1.44 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_2Pt88_512"></span><span id="f3_2pt88_512"></span><span id="F3_2PT88_512"></span>**F3\_2Pt88\_512**
</dt> <dd>

Indicates 3.5", 2.88 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_20Pt8_512"></span><span id="f3_20pt8_512"></span><span id="F3_20PT8_512"></span>**F3\_20Pt8\_512**
</dt> <dd>

Indicates 3.5", 20.8 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_720_512"></span><span id="f3_720_512"></span>**F3\_720\_512**
</dt> <dd>

Indicates 3.5", 720 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F5_360_512"></span><span id="f5_360_512"></span>**F5\_360\_512**
</dt> <dd>

Indicates 5.25", 360 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F5_320_512"></span><span id="f5_320_512"></span>**F5\_320\_512**
</dt> <dd>

Indicates 5.25", 320 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F5_320_1024"></span><span id="f5_320_1024"></span>**F5\_320\_1024**
</dt> <dd>

Indicates 5.25", 320 KB, 1024 bytes/sector media.

</dd> <dt>

<span id="F5_180_512"></span><span id="f5_180_512"></span>**F5\_180\_512**
</dt> <dd>

Indicates 5.25", 180 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F5_160_512"></span><span id="f5_160_512"></span>**F5\_160\_512**
</dt> <dd>

Indicates 5.25", 160 KB, 512 bytes/sector media.

</dd> <dt>

<span id="RemovableMedia"></span><span id="removablemedia"></span><span id="REMOVABLEMEDIA"></span>**RemovableMedia**
</dt> <dd>

Indicates removable media other than a floppy disk.

</dd> <dt>

<span id="FixedMedia"></span><span id="fixedmedia"></span><span id="FIXEDMEDIA"></span>**FixedMedia**
</dt> <dd>

Indicates fixed hard disk media.

</dd> <dt>

<span id="F3_120M_512"></span><span id="f3_120m_512"></span>**F3\_120M\_512**
</dt> <dd>

Indicates 3.5", 120 MB media.

</dd> <dt>

<span id="F3_640_512"></span><span id="f3_640_512"></span>**F3\_640\_512**
</dt> <dd>

Indicates 3.5", 640 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F5_640_512"></span><span id="f5_640_512"></span>**F5\_640\_512**
</dt> <dd>

Indicates 5.25", 640 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F5_720_512"></span><span id="f5_720_512"></span>**F5\_720\_512**
</dt> <dd>

Indicates 5.25", 720 KB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_1Pt2_512"></span><span id="f3_1pt2_512"></span><span id="F3_1PT2_512"></span>**F3\_1Pt2\_512**
</dt> <dd>

Indicates 3.5", 1.2 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_1Pt23_1024"></span><span id="f3_1pt23_1024"></span><span id="F3_1PT23_1024"></span>**F3\_1Pt23\_1024**
</dt> <dd>

Indicates 3.5", 1.23 MB, 1024 bytes/sector media.

</dd> <dt>

<span id="F5_1Pt23_1024"></span><span id="f5_1pt23_1024"></span><span id="F5_1PT23_1024"></span>**F5\_1Pt23\_1024**
</dt> <dd>

Indicates 5.25", 1.23 MB, 1024 bytes/sector media.

</dd> <dt>

<span id="F3_128Mb_512"></span><span id="f3_128mb_512"></span><span id="F3_128MB_512"></span>**F3\_128Mb\_512**
</dt> <dd>

Indicates 3.5" magneto-optical (MO), 128 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F3_230Mb_512"></span><span id="f3_230mb_512"></span><span id="F3_230MB_512"></span>**F3\_230Mb\_512**
</dt> <dd>

Indicates 3.5" magneto-optical (MO), 230 MB, 512 bytes/sector media.

</dd> <dt>

<span id="F8_256_128"></span><span id="f8_256_128"></span>**F8\_256\_128**
</dt> <dd>

Indicates 8", 256 KB, 128 bytes/sector media.

</dd> <dt>

<span id="F3_200Mb_512"></span><span id="f3_200mb_512"></span><span id="F3_200MB_512"></span>**F3\_200Mb\_512**
</dt> <dd>

3.5", 200M Floppy (HiFD)

</dd> <dt>

<span id="F3_240M_512"></span><span id="f3_240m_512"></span>**F3\_240M\_512**
</dt> <dd>

3.5", 240Mb Floppy (HiFD)

</dd> <dt>

<span id="F3_32M_512"></span><span id="f3_32m_512"></span>**F3\_32M\_512**
</dt> <dd>

3.5", 32Mb Floppy

</dd> </dl>

## Remarks

The caller of the IOCTL\_DISK\_FORMAT\_TRACK request indicates the disk size and number of bytes per sector, along with other formatting information, by specifying one of these values in the **MediaType** member of the [**FORMAT\_PARAMETERS**](format-parameters.md) structure.

Removable disks include zip drivers, jaz drives, magneto-optical (MO) drives, and LS-120 floppies as well as regular floppies.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md)
</dt> <dt>

[**FORMAT\_PARAMETERS**](format-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_MEDIA_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






