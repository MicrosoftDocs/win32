---
title: FEATURE\_DATA\_PROFILE\_LIST\_EX structure
description: The FEATURE\_DATA\_PROFILE\_LIST\_EX structure contains information corresponding to a profile list element in a profile list descriptor.
ms.assetid: c15f9be2-1f35-41cf-a1de-880e3662f2b4
keywords:
- FEATURE_DATA_PROFILE_LIST_EX structure Storage Devices
- PFEATURE_DATA_PROFILE_LIST_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_PROFILE_LIST_EX
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

# FEATURE\_DATA\_PROFILE\_LIST\_EX structure

The FEATURE\_DATA\_PROFILE\_LIST\_EX structure contains information corresponding to a profile list element in a profile list descriptor.

## Syntax


```C++
typedef struct _FEATURE_DATA_PROFILE_LIST_EX {
  UCHAR ProfileNumber[2];
  UCHAR Current  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2;
} FEATURE_DATA_PROFILE_LIST_EX, *PFEATURE_DATA_PROFILE_LIST_EX;
```



## Members

<dl> <dt>

**ProfileNumber**
</dt> <dd>

Contains the profile number. This number must be one of the values defined by the [**FEATURE\_PROFILE\_TYPE**](feature-profile-type.md) enumeration. **ProfileNumber**\[0\] must contain the most significant byte of the profile number. **ProfileNumber**\[1\] must contain the least significant byte.

</dd> <dt>

**Current**
</dt> <dd>

Indicates, when set to 1, that this feature is currently active and the feature data is valid. When set to zero, this bit indicates that the feature is not currently active and that the feature data might not be valid.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_PROFILE\_TYPE**](feature-profile-type.md)
</dt> <dt>

[**FEATURE\_DATA\_PROFILE\_LIST**](feature-data-profile-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_PROFILE_LIST_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






