---
title: FEATURE\_DATA\_RANDOM\_READABLE structure
description: The FEATURE\_DATA\_RANDOM\_READABLE structure contains data for the random readable feature.
ms.assetid: c235a3aa-f8fe-4034-a645-ef85b2574fa0
keywords:
- FEATURE_DATA_RANDOM_READABLE structure Storage Devices
- PFEATURE_DATA_RANDOM_READABLE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_RANDOM_READABLE
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

# FEATURE\_DATA\_RANDOM\_READABLE structure

The FEATURE\_DATA\_RANDOM\_READABLE structure contains data for the random readable feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_RANDOM_READABLE {
  FEATURE_HEADER Header;
  UCHAR          LogicalBlockSize[4];
  UCHAR          Blocking[2];
  UCHAR          ErrorRecoveryPagePresent  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved2;
} FEATURE_DATA_RANDOM_READABLE, *PFEATURE_DATA_RANDOM_READABLE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**LogicalBlockSize**
</dt> <dd>

Indicates the number of bytes per logical block. The bytes of this value are arranged in big-endian order. **LogicalBlockSize**\[0\] contains the most significant byte, and **LogicalBlockSize**\[3\] contains the least significant byte.

</dd> <dt>

**Blocking**
</dt> <dd>

Indicates the number of logical blocks per device-readable unit. The bytes of this value are arranged in big-endian order. **Blocking**\[0\] contains the most significant byte, and **Blocking**\[1\] contains the least significant byte.

</dd> <dt>

**ErrorRecoveryPagePresent**
</dt> <dd>

Indicates, when set to zero, that the read/write error recovery mode page might not be present. When set to 1, it indicates that the error recovery page is present.

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

This structure holds data for the feature named "Random Readable" by the *MMC-3* specification. Devices that support this feature allow the initiator to read blocks of data on the disk at random locations. These devices do not require that the initiator address disk locations in any particular order.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_RANDOM_READABLE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






