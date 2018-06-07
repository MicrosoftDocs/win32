---
title: FEATURE\_DATA\_PROFILE\_LIST structure
description: The FEATURE\_DATA\_PROFILE\_LIST structure contains the data for a profile list descriptor.
ms.assetid: 77b8c789-0f3d-43b5-95ff-15d93b67cbe3
keywords:
- FEATURE_DATA_PROFILE_LIST structure Storage Devices
- PFEATURE_DATA_PROFILE_LIST structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_PROFILE_LIST
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

# FEATURE\_DATA\_PROFILE\_LIST structure

The FEATURE\_DATA\_PROFILE\_LIST structure contains the data for a profile list descriptor.

## Syntax


```C++
typedef struct _FEATURE_DATA_PROFILE_LIST {
  FEATURE_HEADER               Header;
  FEATURE_DATA_PROFILE_LIST_EX Profiles[];
} FEATURE_DATA_PROFILE_LIST, *PFEATURE_DATA_PROFILE_LIST;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a header that indicates how many profiles are reported in the profile list descriptor. The [**FEATURE\_HEADER**](feature-header.md) structure is used to describe both feature and profile list descriptors. When FEATURE\_HEADER is used with a profile list descriptor the **FeatureCode** member of FEATURE\_HEADER must be set to zero, the **Current** member must be set to 1, the **Version** member must be set to zero, and the **Persistent** member must be set to 1. The **Persistent** member is set to 1, because all devices that are compliant with the *SCSI Multimedia - 4 (MMC-4)* standard must support reporting of the profile list. The **AdditionalLength** member must be set to ((number of profile descriptors) \* 4). See the *MMC-3* specification For more information about the values assigned to these members.

</dd> <dt>

**Profiles**
</dt> <dd>

Contains a variable length array of [**FEATURE\_DATA\_PROFILE\_LIST\_EX**](feature-data-profile-list-ex.md) structures that describe all the profiles supported by the device.

</dd> </dl>

## Remarks

This structure holds data for the feature named "Profile List" by the *MMC-3* specification. This feature provides a list of all profiles supported by the device.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_PROFILE\_TYPE**](feature-profile-type.md)
</dt> <dt>

[**FEATURE\_DATA\_PROFILE\_LIST\_EX**](feature-data-profile-list-ex.md)
</dt> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_PROFILE_LIST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






