---
title: FEATURE\_DATA\_DISC\_CONTROL\_BLOCKS\_EX structure
description: The FEATURE\_DATA\_DISC\_CONTROL\_BLOCKS\_EX structure holds the data reported for a Disc Control Block.
ms.assetid: 08344cf3-7724-4c11-8855-ba061a0284f8
keywords:
- FEATURE_DATA_DISC_CONTROL_BLOCKS_EX structure Storage Devices
- PFEATURE_DATA_DISC_CONTROL_BLOCKS_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_DISC_CONTROL_BLOCKS_EX
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

# FEATURE\_DATA\_DISC\_CONTROL\_BLOCKS\_EX structure

The FEATURE\_DATA\_DISC\_CONTROL\_BLOCKS\_EX structure holds the data reported for a Disc Control Block.

## Syntax


```C++
typedef struct _FEATURE_DATA_DISC_CONTROL_BLOCKS_EX {
  UCHAR ContentDescriptor[4];
} FEATURE_DATA_DISC_CONTROL_BLOCKS_EX, *PFEATURE_DATA_DISC_CONTROL_BLOCKS_EX;
```



## Members

<dl> <dt>

**ContentDescriptor**
</dt> <dd>

Contains the first of one or more control blocks. The bytes in this array are arranged in big-endian order. **ContentDescriptor**\[0\] contains the most significant byte, and **ContentDescriptor**\[3\] contains the least significant byte.

</dd> </dl>

## Remarks

This structure holds data for the feature named "Disc Control Blocks" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature can read or write Disc Control Blocks.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_DATA\_DISC\_CONTROL\_BLOCKS**](feature-data-disc-control-blocks.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_DISC_CONTROL_BLOCKS_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






