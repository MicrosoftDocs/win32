---
title: FEATURE\_DATA\_DVD\_CPRM structure
description: The FEATURE\_DATA\_DVD\_CPRM structure holds information about the DVD Content Protection for Recorded Media (CPRM) feature.
ms.assetid: 060c1e9a-14d3-4f9b-b898-d8042f5efd7e
keywords:
- FEATURE_DATA_DVD_CPRM structure Storage Devices
- PFEATURE_DATA_DVD_CPRM structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_DVD_CPRM
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

# FEATURE\_DATA\_DVD\_CPRM structure

The FEATURE\_DATA\_DVD\_CPRM structure holds information about the DVD Content Protection for Recorded Media (CPRM) feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_DVD_CPRM {
  FEATURE_HEADER Header;
  UCHAR          Reserved0[3];
  UCHAR          CPRMVersion;
} FEATURE_DATA_DVD_CPRM, *PFEATURE_DATA_DVD_CPRM;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved.

</dd> <dt>

**CPRMVersion**
</dt> <dd>

Contains the CPRM version number. Must be set to 1.

</dd> </dl>

## Remarks

This structure holds data for the feature named "DVD CPRM" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature can perform DVD Content Protection for Recordable Media (CPRM) authentication and key management.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_DVD_CPRM%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






