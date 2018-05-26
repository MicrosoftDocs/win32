---
title: FEATURE\_DATA\_DVD\_PLUS\_R structure
description: The FEATURE\_DATA\_DVD\_PLUS\_R structure contains information about the DVD+R feature.
ms.assetid: e1501ea9-a55b-4fbc-990b-2172c7369bb1
keywords:
- FEATURE_DATA_DVD_PLUS_R structure Storage Devices
- PFEATURE_DATA_DVD_PLUS_R structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_DVD_PLUS_R
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

# FEATURE\_DATA\_DVD\_PLUS\_R structure

The FEATURE\_DATA\_DVD\_PLUS\_R structure contains information about the DVD+R feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_DVD_PLUS_R {
  FEATURE_HEADER Header;
  UCHAR          Write  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved2[3];
} FEATURE_DATA_DVD_PLUS_R, *PFEATURE_DATA_DVD_PLUS_R;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Write**
</dt> <dd>

Indicates, when set to 1, that the device has an ability that was not specified in the DVD-ROM profile, to write to DVD+R discs according to *DVD+R 4.7 Gbytes Basic Format Specifications.* When set to 0, the device has no extra ability beyond what is specified in the profile.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "DVD+R" by the *MMC-3* specification. Devices that support this feature can specify whether they are able to perform writes to DVD+R discs, even though this ability was not indicated in the device's DVD-ROM profile.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_DVD_PLUS_R%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






