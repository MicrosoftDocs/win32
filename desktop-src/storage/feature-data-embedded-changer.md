---
title: FEATURE\_DATA\_EMBEDDED\_CHANGER structure
description: The FEATURE\_DATA\_EMBEDDED\_CHANGER structure holds data for the Embedded Changer feature.
ms.assetid: 1335d1fa-af96-4a31-a1cf-266f7a3325ef
keywords:
- FEATURE_DATA_EMBEDDED_CHANGER structure Storage Devices
- PFEATURE_DATA_EMBEDDED_CHANGER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_EMBEDDED_CHANGER
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

# FEATURE\_DATA\_EMBEDDED\_CHANGER structure

The FEATURE\_DATA\_EMBEDDED\_CHANGER structure holds data for the Embedded Changer feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_EMBEDDED_CHANGER {
  FEATURE_HEADER Header;
  UCHAR          Reserved1  :2;
  UCHAR          SupportsDiscPresent  :1;
  UCHAR          Reserved2  :1;
  UCHAR          SideChangeCapable  :1;
  UCHAR          Reserved3  :3;
  UCHAR          Reserved4[2];
  UCHAR          HighestSlotNumber  :5;
  UCHAR          Reserved  :3;
} FEATURE_DATA_EMBEDDED_CHANGER, *PFEATURE_DATA_EMBEDDED_CHANGER;
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

**SupportsDiscPresent**
</dt> <dd>

Indicates, when set to 1, that the device can report the contents of the slots after a reset or magazine change. When set to zero, this bit indicates that the device can report the contents of the slots after reset or magazine change.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**SideChangeCapable**
</dt> <dd>

Indicates, when set to 1, that the device is capable of selecting both sides of the media. When set to zero, this bit indicates that the device is not capable of selecting both sides of the media.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved.

</dd> <dt>

**HighestSlotNumber**
</dt> <dd>

Indicates the number of slots minus 1.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "Embedded Changer" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature can move media back and forth between a media storage area and the mechanism that actually accesses the media.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_EMBEDDED_CHANGER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






