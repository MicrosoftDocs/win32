---
title: FEATURE\_DATA\_DVD\_RECORDABLE\_WRITE structure
description: The FEATURE\_DATA\_DVD\_RECORDABLE\_WRITE structure holds information for the DVD-R/RW Write feature.
ms.assetid: 13a816f9-c41a-49f1-ac79-98106f4630d4
keywords:
- FEATURE_DATA_DVD_RECORDABLE_WRITE structure Storage Devices
- PFEATURE_DATA_DVD_RECORDABLE_WRITE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_DVD_RECORDABLE_WRITE
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FEATURE\_DATA\_DVD\_RECORDABLE\_WRITE structure

The FEATURE\_DATA\_DVD\_RECORDABLE\_WRITE structure holds information for the DVD-R/RW Write feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_DVD_RECORDABLE_WRITE {
  FEATURE_HEADER Header;
  UCHAR          Reserved1  :1;
  UCHAR          DVD_RW  :1;
  UCHAR          TestWrite  :1;
  UCHAR          RDualLayer  :1;
  UCHAR          Reserved02  :2;
  UCHAR          BufferUnderrunFree  :1;
  UCHAR          Reserved3  :1;
  UCHAR          Reserved4[3];
} FEATURE_DATA_DVD_RECORDABLE_WRITE, *PFEATURE_DATA_DVD_RECORDABLE_WRITE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**DVD\_RW**
</dt> <dd>

Indicates, when set to 1, that the device supports writing and erasing on DVD-RW media. For more information about this feature see the *SCSI Multimedia - 4 (MMC-4)* specification.

</dd> <dt>

**TestWrite**
</dt> <dd>

Indicates, when set to 1, that the device is capable of performing test writes. When set to zero, the device cannot perform test writes.

</dd> <dt>

**RDualLayer**
</dt> <dd></dd> <dt>

**Reserved02**
</dt> <dd></dd> <dt>

**BufferUnderrunFree**
</dt> <dd>

Indicates, when set to 1, that the device can perform under-run-free recording.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "DVD-R Write" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature can write data to a write-once DVD media in "Disc-at-Once" mode.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_DVD_RECORDABLE_WRITE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






