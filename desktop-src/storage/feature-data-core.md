---
title: FEATURE\_DATA\_CORE structure
description: The FEATURE\_DATA\_CORE structure holds data for the Core feature descriptor.
ms.assetid: 'cd8e989a-1030-4f37-bb39-38974764ccb2'
keywords: ["FEATURE_DATA_CORE structure Storage Devices", "PFEATURE_DATA_CORE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FEATURE_DATA_CORE
api_location:
- ntddmmc.h
api_type:
- HeaderDef
---

# FEATURE\_DATA\_CORE structure

The FEATURE\_DATA\_CORE structure holds data for the Core feature descriptor.

## Syntax


```C++
typedef struct _FEATURE_DATA_CORE {
  FEATURE_HEADER Header;
  UCHAR          PhysicalInterface[4];
  UCHAR          DeviceBusyEvent  :1;
  UCHAR          INQUIRY2  :1;
  UCHAR          Reserved1  :6;
  UCHAR          Reserved2[3];
} FEATURE_DATA_CORE, *PFEATURE_DATA_CORE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**PhysicalInterface**
</dt> <dd>

Must be set to the current communication path between initiator and device, as defined in the *SCSI Multimedia - 4 (MMC-4)* specification. The bytes of this array are arranged in big-endian order. **PhysicalInterface**\[0\] contains the most significant byte, and **PhysicalInterface**\[3\] contains the least significant byte.

</dd> <dt>

**DeviceBusyEvent**
</dt> <dd></dd> <dt>

**INQUIRY2**
</dt> <dd></dd> <dt>

**Reserved1**
</dt> <dd></dd> <dt>

**Reserved2**
</dt> <dd></dd> </dl>

## Remarks

Indicates the feature named "Core" by the *MMC-3* specification. This feature encompasses the basic functionality which is mandatory for all devices that support the *MMC-3* standard. See the *MMC-3* specification for a description of the capabilities included in the Core feature.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_CORE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






