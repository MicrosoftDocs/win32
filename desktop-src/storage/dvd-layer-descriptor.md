---
title: DVD\_LAYER\_DESCRIPTOR structure
description: The DVD\_LAYER\_DESCRIPTOR structure is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request to retrieve a DVD layer descriptor.
ms.assetid: dd981cc1-ab82-49de-8cf1-ba2b7451c7ef
keywords:
- DVD_LAYER_DESCRIPTOR structure Storage Devices
- PDVD_LAYER_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_LAYER_DESCRIPTOR
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DVD\_LAYER\_DESCRIPTOR structure

The DVD\_LAYER\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request to retrieve a DVD layer descriptor.

## Syntax


```C++
typedef struct _DVD_LAYER_DESCRIPTOR {
  UCHAR BookVersion  :4;
  UCHAR BookType  :4;
  UCHAR MinimumRate  :4;
  UCHAR DiskSize  :4;
  UCHAR LayerType  :4;
  UCHAR TrackPath  :1;
  UCHAR NumberOfLayers  :2;
  UCHAR Reserved1  :1;
  UCHAR TrackDensity  :4;
  UCHAR LinearDensity  :4;
  ULONG StartingDataSector;
  ULONG EndDataSector;
  ULONG EndLayerZeroSector;
  UCHAR Reserved5  :7;
  UCHAR BCAFlag  :1;
} DVD_LAYER_DESCRIPTOR, *PDVD_LAYER_DESCRIPTOR;
```



## Members

<dl> <dt>

**BookVersion**
</dt> <dd>

Specifies the version of the specified book that this media complies with.

</dd> <dt>

**BookType**
</dt> <dd>

Specifies the DVD book this media complies with. This member can have one of the following values:



| Value        | Meaning            |
|--------------|--------------------|
| 0<br/> | DVD-ROM<br/> |
| 1<br/> | DVD-RAM<br/> |
| 2<br/> | DVD-R<br/>   |
| 3<br/> | DVD-RW<br/>  |
| 9<br/> | DVD+RW<br/>  |



 

</dd> <dt>

**MinimumRate**
</dt> <dd>

Specifies the read rate to use for the media. This member can have one of the following values:



| Value        | Meaning            |
|--------------|--------------------|
| 0<br/> | DVD-ROM<br/> |
| 1<br/> | DVD-RAM<br/> |
| 2<br/> | DVD-R<br/>   |
| 3<br/> | DVD-RW<br/>  |
| 9<br/> | DVD+RW<br/>  |



 

</dd> <dt>

**DiskSize**
</dt> <dd>

Specifies the physical size of the media. A value of zero indicates 120 mm. A value of 1 indicates a size of 80 mm.

</dd> <dt>

**LayerType**
</dt> <dd>

Indicates the type of layer. This member can have one of the following values:



| Value        | Meaning                     |
|--------------|-----------------------------|
| 1<br/> | Read-only layer<br/>  |
| 2<br/> | Recordable layer<br/> |
| 4<br/> | Rewritable layer<br/> |



 

</dd> <dt>

**TrackPath**
</dt> <dd>

Specifies the direction of the layers when more than one layer is used. If the **TrackPath** member is zero, this media uses a parallel track path (PTP). With PTP, each layer is independent and has its own lead-in and lead-out areas. If **TrackPath** is 1, the media uses opposite track path (OTP). With opposite track path, the two layers are united, and there is only one lead-in and lead-out area. For further details, see the *SCSI Multimedia Commands - 3 (MMC-3)* specification.

</dd> <dt>

**NumberOfLayers**
</dt> <dd>

Specifies the number of layers present on the side of the media being read. A value of zero indicates that the media has one layer. A value of 1 indicates that the media has two layers.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**TrackDensity**
</dt> <dd>

Indicates the track width used for this media in units of micrometers per track. This member can have one of the following values:



| Value        | Meaning                  |
|--------------|--------------------------|
| 0<br/> | 0.74 m/track<br/>  |
| 1<br/> | 0.80 m/track<br/>  |
| 2<br/> | 0.615 m/track<br/> |



 

</dd> <dt>

**LinearDensity**
</dt> <dd>

Indicates the minimum/maximum pit length used for this layer in units of micrometers per bit. This member can have one of the following values:



| Value        | Meaning                         |
|--------------|---------------------------------|
| 0<br/> | 0.267 m/bit<br/>          |
| 1<br/> | 0.293 m/bit<br/>          |
| 2<br/> | 0.409 to 0.435 m/bit<br/> |
| 4<br/> | 0.280 to 0.291 m/bit<br/> |
| 8<br/> | 0.353 m/bit<br/>          |



 

</dd> <dt>

**StartingDataSector**
</dt> <dd>

Specifies the first block that contains user data. This member can have one of the following values:



| Value              | Meaning                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------|
| 0x30000<br/> | An initial block value of 0x30000 indicates that the media type is DVD-ROM or DVD-R/-RW<br/> |
| 0x31000<br/> | An initial block value of 0x30000 indicates that the media type is DVD-RAM or DVD+RW<br/>    |



 

</dd> <dt>

**EndDataSector**
</dt> <dd>

Specifies the last sector of the user data in the last layer of the media.

</dd> <dt>

**EndLayerZeroSector**
</dt> <dd>

Specifies the last sector of the user data in layer zero. If this media does not use the opposite track path method and contains multiple layers, this value is set to zero.

</dd> <dt>

**Reserved5**
</dt> <dd>

Reserved.

</dd> <dt>

**BCAFlag**
</dt> <dd>

Indicates, if set to 1, the presence of data in the burst cutting area (BCA). If set to zero, it indicates that there is no BCA data.

</dd> </dl>

## Remarks

For more information, see the *SCSI Multimedia Commands - 3 (MMC-3)* specification.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_LAYER_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






