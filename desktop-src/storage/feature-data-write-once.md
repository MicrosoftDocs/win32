---
title: FEATURE\_DATA\_WRITE\_ONCE structure
description: The FEATURE\_DATA\_WRITE\_ONCE structure holds information for the Write Once feature.
ms.assetid: d8352a73-6b3e-4890-a4ae-000d453d1143
keywords:
- FEATURE_DATA_WRITE_ONCE structure Storage Devices
- PFEATURE_DATA_WRITE_ONCE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_WRITE_ONCE
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

# FEATURE\_DATA\_WRITE\_ONCE structure

The FEATURE\_DATA\_WRITE\_ONCE structure holds information for the Write Once feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_WRITE_ONCE {
  FEATURE_HEADER Header;
  UCHAR          LogicalBlockSize[4];
  UCHAR          Blocking[2];
  UCHAR          ErrorRecoveryPagePresent  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved2;
} FEATURE_DATA_WRITE_ONCE, *PFEATURE_DATA_WRITE_ONCE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**LogicalBlockSize**
</dt> <dd>

Indicates the number of bytes per logical block. The bytes in this array are arranged in big-endian order. **LogicalBlockSize**\[0\] holds the most significant byte. **LogicalBlockSize**\[3\] holds the least significant byte.

</dd> <dt>

**Blocking**
</dt> <dd>

Indicates the number of logical blocks per device. The bytes in this array are arranged in big-endian order. **Blocking**\[0\] holds the most significant byte. **Blocking**\[1\] holds the least significant byte.

</dd> <dt>

**ErrorRecoveryPagePresent**
</dt> <dd>

Indicates, when set to 1, that the Read/Write Error Recovery Mode Page is present. When set to zero, indicates that it might not be present. See the *SCSI Multimedia 3* (*MMC-3*) specification for a description of this page.

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

This structure holds data for the feature named "Write Once" by the *MMC-3* specification. Devices that support this feature can write to any previously unused logical block.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_WRITE_ONCE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






