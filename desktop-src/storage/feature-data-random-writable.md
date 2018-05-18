---
title: FEATURE\_DATA\_RANDOM\_WRITABLE structure
description: The FEATURE\_DATA\_RANDOM\_WRITABLE structure holds information about the Random Writable feature.
ms.assetid: 'b2637f5e-15b0-44ae-8cd0-98712e735998'
keywords: ["FEATURE_DATA_RANDOM_WRITABLE structure Storage Devices", "PFEATURE_DATA_RANDOM_WRITABLE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FEATURE_DATA_RANDOM_WRITABLE
api_location:
- ntddmmc.h
api_type:
- HeaderDef
---

# FEATURE\_DATA\_RANDOM\_WRITABLE structure

The FEATURE\_DATA\_RANDOM\_WRITABLE structure holds information about the Random Writable feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_RANDOM_WRITABLE {
  FEATURE_HEADER Header;
  UCHAR          LastLBA[4];
  UCHAR          LogicalBlockSize[4];
  UCHAR          Blocking[2];
  UCHAR          ErrorRecoveryPagePresent  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved2;
} FEATURE_DATA_RANDOM_WRITABLE, *PFEATURE_DATA_RANDOM_WRITABLE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**LastLBA**
</dt> <dd>

Contains the logical block address of the last addressable block on the medium. The bytes of this array are arranged in big-endian order. **LastLBA**\[0\] contains the most significant byte, and **LastLBA**\[3\] contains the least significant byte.

</dd> <dt>

**LogicalBlockSize**
</dt> <dd>

Specifies the number of bytes per logical block. The bytes of this array are arranged in big-endian order. **LogicalBlockSize**\[0\] contains the most significant byte, and **LogicalBlockSize**\[3\] contains the least significant byte.

</dd> <dt>

**Blocking**
</dt> <dd>

Indicates the number of logical blocks per device. The bytes of this array are arranged in big-endian order. **Blocking**\[0\] contains the most significant byte, and **Blocking**\[1\] contains the least significant byte.

</dd> <dt>

**ErrorRecoveryPagePresent**
</dt> <dd>

Indicates, when set to zero, that the Read/Write Error Recovery Mode Page might not be present. See the *SCSI Multimedia -3* (*MMC-3*) specification for an explanation of this page.

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

This structure holds data for the feature named "Random Writable" by the *MMC-3* specification. Devices that support this feature can write blocks of data to random locations on the disk. These devices do not require that the initiator address disk locations in any particular order.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_RANDOM_WRITABLE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






