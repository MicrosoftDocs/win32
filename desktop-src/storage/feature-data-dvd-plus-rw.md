---
title: FEATURE\_DATA\_DVD\_PLUS\_RW structure
description: The FEATURE\_DATA\_DVD\_PLUS\_RW structure contains information about the DVD+RW feature.
ms.assetid: 55cbef36-dea7-4f7c-ac43-fb819b61a858
keywords:
- FEATURE_DATA_DVD_PLUS_RW structure Storage Devices
- PFEATURE_DATA_DVD_PLUS_RW structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_DVD_PLUS_RW
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FEATURE\_DATA\_DVD\_PLUS\_RW structure

The FEATURE\_DATA\_DVD\_PLUS\_RW structure contains information about the DVD+RW feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_DVD_PLUS_RW {
  FEATURE_HEADER Header;
  UCHAR          Write  :1;
  UCHAR          Reserved1  :7;
  UCHAR          CloseOnly  :1;
  UCHAR          QuickStart  :1;
  UCHAR          Reserved02  :6;
  UCHAR          Reserved03[2];
} FEATURE_DATA_DVD_PLUS_RW, *PFEATURE_DATA_DVD_PLUS_RW;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Write**
</dt> <dd>

Indicates, when set to 1, that the device can do background formatting of DVD+RW discs according to *DVD+RW 4.7 Gbytes Basic Format Specifications*, and can write to discs that have been formatted in this manner.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**CloseOnly**
</dt> <dd>

Indicates, when set to 1, then the device supports only read compatibility stops. When set to 0, the device supports both forms of background format stop. For more information about background format stops, see the *SCSI Multimedia Commands - 4 (MMC-4)* specification published by the American National Standards Institute (ANSI).

</dd> <dt>

**QuickStart**
</dt> <dd></dd> <dt>

**Reserved02**
</dt> <dd></dd> <dt>

**Reserved03**
</dt> <dd></dd> </dl>

## Remarks

This structure holds data for the feature named "DVD+RW" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature can read a recorded DVD+RW disc that is formatted according to the *DVD+RW 4.7 Gbytes Basic Format Specification.*

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_DVD_PLUS_RW%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






