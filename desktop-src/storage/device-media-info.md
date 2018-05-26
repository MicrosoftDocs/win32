---
title: DEVICE\_MEDIA\_INFO structure
description: A storage class driver returns an array of DEVICE\_MEDIA\_INFO structures, embedded in a GET\_MEDIA\_TYPES structure, in response to an IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX device-control request.
ms.assetid: 87906511-7bcb-4f4d-9383-44b0501536e3
keywords:
- DEVICE_MEDIA_INFO structure Storage Devices
- PDEVICE_MEDIA_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_MEDIA_INFO
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DEVICE\_MEDIA\_INFO structure

A storage class driver returns an array of **DEVICE\_MEDIA\_INFO** structures, embedded in a [**GET\_MEDIA\_TYPES**](get-media-types.md) structure, in response to an [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md) device-control request.

## Syntax


```C++
typedef struct _DEVICE_MEDIA_INFO {
  union {
    struct {
      LARGE_INTEGER      Cylinders;
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              TracksPerCylinder;
      ULONG              SectorsPerTrack;
      ULONG              BytesPerSector;
      ULONG              NumberMediaSides;
      ULONG              MediaCharacteristics;
    } DiskInfo;
    struct {
      LARGE_INTEGER      Cylinders;
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              TracksPerCylinder;
      ULONG              SectorsPerTrack;
      ULONG              BytesPerSector;
      ULONG              NumberMediaSides;
      ULONG              MediaCharacteristics;
    } RemovableDiskInfo;
    struct {
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              MediaCharacteristics;
      ULONG              CurrentBlockSize;
      STORAGE_BUS_TYPE   BusType;
      union {
        struct {
          UCHAR MediumType;
          UCHAR DensityCode;
        } ScsiInformation;
      } BusSpecificData;
    } TapeInfo;
  } DeviceSpecific;
} DEVICE_MEDIA_INFO, *PDEVICE_MEDIA_INFO;
```



## Members

<dl> <dt>

**DeviceSpecific**
</dt> <dd> <dl> <dt>

**DiskInfo**
</dt> <dd>

Describes a nonremovable (fixed) disk.

<dl> <dt>

**Cylinders**
</dt> <dd>

Specifies the number of cylinders on this disk.

</dd> <dt>

**MediaType**
</dt> <dd>

Specifies a [**MEDIA\_TYPE**](media-type.md) of **FixedMedia**.

</dd> <dt>

**TracksPerCylinder**
</dt> <dd>

Specifies the number of tracks per cylinder.

</dd> <dt>

**SectorsPerTrack**
</dt> <dd>

Specifies the number of sectors per track.

</dd> <dt>

**BytesPerSector**
</dt> <dd>

Specifies the number of bytes per sector.

</dd> <dt>

**NumberMediaSides**
</dt> <dd>

Specifies the number of sides of the disk that can contain data: either 1 for one-sided media or 2 for two-sided media.

</dd> <dt>

**MediaCharacteristics**
</dt> <dd>

Specifies characteristics of the disk indicated by one or more of the following flags.

<dl><span id="MEDIA_CURRENTLY_MOUNTED_"></span><span id="media_currently_mounted_"></span><dt>

**MEDIA\_CURRENTLY\_MOUNTED** 
</dt><span id="MEDIA_ERASEABLE_"></span><span id="media_eraseable_"></span><dt>

**MEDIA\_ERASEABLE** 
</dt><span id="MEDIA_READ_ONLY_"></span><span id="media_read_only_"></span><dt>

**MEDIA\_READ\_ONLY** 
</dt><span id="MEDIA_READ_WRITE_"></span><span id="media_read_write_"></span><dt>

**MEDIA\_READ\_WRITE** 
</dt><span id="MEDIA_WRITE_ONCE_"></span><span id="media_write_once_"></span><dt>

**MEDIA\_WRITE\_ONCE** 
</dt><span id="MEDIA_WRITE_PROTECTED_"></span><span id="media_write_protected_"></span><dt>

**MEDIA\_WRITE\_PROTECTED** 
</dt> </dl> </dd> </dl> </dd> <dt>

**RemovableDiskInfo**
</dt> <dd>

Describes a removable (nonfixed) disk.

<dl> <dt>

**Cylinders**
</dt> <dd>

Specifies the number of cylinders on this disk.

</dd> <dt>

**MediaType**
</dt> <dd>

Specifies a [**MEDIA\_TYPE**](media-type.md) or [**STORAGE\_MEDIA\_TYPE**](storage-media-type.md) value that indicates the type of removable disk.

</dd> <dt>

**TracksPerCylinder**
</dt> <dd>

Specifies the number of tracks per cylinder.

</dd> <dt>

**SectorsPerTrack**
</dt> <dd>

Specifies the number of sectors per track.

</dd> <dt>

**BytesPerSector**
</dt> <dd>

Specifies the number of bytes per sector.

</dd> <dt>

**NumberMediaSides**
</dt> <dd>

Specifies the number of sides of the disk that can contain data: 1 for one-sided media or 2 for two-sided media.

</dd> <dt>

**MediaCharacteristics**
</dt> <dd>

Specifies characteristics of the disk, indicated by MEDIA\_*XXX* flags ORed together. For a list of these flags, see the **DeviceSpecific.DiskInfo.MediaCharacteristics** member of the **DeviceSpecific.DiskInfo** structure.

</dd> </dl> </dd> <dt>

**TapeInfo**
</dt> <dd>

Describes a tape.

<dl> <dt>

**MediaType**
</dt> <dd>

Specifies a [**STORAGE\_MEDIA\_TYPE**](storage-media-type.md) value that indicates the type of tape described in this structure.

</dd> <dt>

**MediaCharacteristics**
</dt> <dd>

Specifies characteristics of the tape, indicated by MEDIA\_*XXX* flags ORed together. For a list of these flags, see the **DeviceSpecific.DiskInfo.MediaCharacteristics** member of the **DeviceSpecific.DiskInfo** structure.

</dd> <dt>

**CurrentBlockSize**
</dt> <dd>

Specifies the current block size, in bytes.

</dd> <dt>

**BusType**
</dt> <dd>

Specifies a value of type [**STORAGE\_BUS\_TYPE**](storage-bus-type.md) that indicates the bus type.

</dd> <dt>

**BusSpecificData**
</dt> <dd> <dl> <dt>

**ScsiInformation**
</dt> <dd>

Specifies bus-specific information from mode page data that describes the medium supported by the tape drive. Values for other bus types will be supplied in a later release.

<dl> <dt>

**MediumType**
</dt> <dd>

Specifies the SCSI-specific medium type.

</dd> <dt>

**DensityCode**
</dt> <dd>

Specifies the SCSI-specific current operating density for read/write operations.

</dd> </dl> </dd> </dl> </dd> </dl> </dd> </dl> </dd> </dl>

## Remarks

This structure is used by a storage driver to indicate the types of media supported by a device and which type is currently mounted, if any. A driver must provide this information if it might control drives in a media library or changer or if its device might be accessed by the Removable Storage Manager (RSM).

The driver fills in an array of **DEVICE\_MEDIA\_INFO** structures, one for each medium type supported by the device, embedded in a [**GET\_MEDIA\_TYPES**](get-media-types.md) structure.

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TapeMiniGetMediaTypes**](https://msdn.microsoft.com/library/windows/hardware/ff567939)
</dt> <dt>

[**STORAGE\_MEDIA\_TYPE**](storage-media-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_MEDIA_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






