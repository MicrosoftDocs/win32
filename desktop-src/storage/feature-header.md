---
title: FEATURE\_HEADER structure
description: The FEATURE\_HEADER structure is used in conjunction with the IOCTL\_CDROM\_GET\_CONFIGURATION request to report header information for both feature and profile descriptors.
ms.assetid: 61831fbb-48ad-4831-8b69-7b1a5cafa629
keywords:
- FEATURE_HEADER structure Storage Devices
- PFEATURE_HEADER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_HEADER
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

# FEATURE\_HEADER structure

The FEATURE\_HEADER structure is used in conjunction with the [**IOCTL\_CDROM\_GET\_CONFIGURATION**](ioctl-cdrom-get-configuration.md) request to report header information for both feature and profile descriptors.

## Syntax


```C++
typedef struct _FEATURE_HEADER {
  UCHAR FeatureCode[2];
  UCHAR Current  :1;
  UCHAR Persistent  :1;
  UCHAR Version  :4;
  UCHAR Reserved0  :2;
  UCHAR AdditionalLength;
} FEATURE_HEADER, *PFEATURE_HEADER;
```



## Members

<dl> <dt>

**FeatureCode**
</dt> <dd>

Contains a value between zero and 0xffff that indicates a feature. The [**FEATURE\_NUMBER**](feature-number.md) enumeration provides a list of currently supported feature numbers. **FeatureCode**\[0\] contains the most significant byte of the feature number. **FeatureCode**\[1\] contains the least significant byte.

</dd> <dt>

**Current**
</dt> <dd>

Indicates, when set to 1, that this feature is currently active and the data reported for the feature is valid. When set to zero, this bit indicates that the feature is not currently active and that the data reported for the feature might not be valid.

</dd> <dt>

**Persistent**
</dt> <dd>

Indicates, when set to 1, that the feature is always active. When set to zero, this bit indicates that the feature is not always active.

</dd> <dt>

**Version**
</dt> <dd>

Must be set to zero unless otherwise specified within the description for a particular feature.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved.

</dd> <dt>

**AdditionalLength**
</dt> <dd>

Indicates the number of bytes of feature information that follow this header. This member must be an integral multiple of 4. The total size of the data related to this feature will be **AdditionalLength** + **sizeof**(FEATURE\_HEADER).

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_CONFIGURATION**](ioctl-cdrom-get-configuration.md)
</dt> <dt>

[**GET\_CONFIGURATION\_HEADER**](get-configuration-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






