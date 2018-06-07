---
title: FEATURE\_DATA\_DVD\_RW\_RESTRICTED\_OVERWRITE structure
description: The FEATURE\_DATA\_DVD\_RW\_RESTRICTED\_OVERWRITE structure contains information for the Restricted Overwrite feature.
ms.assetid: 1669872a-4306-4773-bd7e-6f481c5e689d
keywords:
- FEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE structure Storage Devices
- PFEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE
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

# FEATURE\_DATA\_DVD\_RW\_RESTRICTED\_OVERWRITE structure

The FEATURE\_DATA\_DVD\_RW\_RESTRICTED\_OVERWRITE structure contains information for the Restricted Overwrite feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE {
  FEATURE_HEADER Header;
  UCHAR          Blank  :1;
  UCHAR          Intermediate  :1;
  UCHAR          DefectStatusDataRead  :1;
  UCHAR          DefectStatusDataGenerate  :1;
  UCHAR          Reserved0  :4;
  UCHAR          Reserved1[3];
} FEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE, *PFEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Blank**
</dt> <dd>

Indicates, when set to 1, that the device supports the BLANK command defined by the *SCSI Multimedia - 4 (MMC-4)* specification, with Blanking Types of zero and one. When set to zero, this bit indicates that the device does not support this command.

</dd> <dt>

**Intermediate**
</dt> <dd>

Indicates, when set to 1, that the device supports writing on an intermediate state-bordered area and quick formatting (Format Type of 15 - Quick Format, as defined by the *MMC-3* specification). When set to zero, this bit indicates that the device does not support writing on an intermediate state-bordered area nor does it support quick formatting.

</dd> <dt>

**DefectStatusDataRead**
</dt> <dd>

Corresponds to the Defect Status Bitmap Read (DSBR) bit as defined by the *MMC-3* specification. When set to 1, this bit indicates that the device allows initiators to read the Defect Status Bitmap of a medium. When set to zero, this bit indicates that the device does not support the reading of Defect Status Bitmap.

</dd> <dt>

**DefectStatusDataGenerate**
</dt> <dd>

Corresponds to the Defect Status Bitmap Generate (DSBG) bit as defined by the *MMC-3* specification. When set to 1, this bit indicates that the device can generate a Defect Status Bitmap during formatting. When set to zero, this bit indicates that the device cannot generate a Defect Status Bitmap during formatting.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "DVD-RW Restricted Overwrite" by the *MMC-3* specification. In the [**FEATURE\_NUMBER**](feature-number.md) enumeration, this feature is named **FeatureRigidRestrictedOverwrite**.

Devices that support this feature can only write on block boundaries. These devices cannot perform read or write operations that transfer less than a block of data. See the *MMC-3* specification for more information.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_DVD_RW_RESTRICTED_OVERWRITE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






