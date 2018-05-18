---
title: PARTITION\_INFORMATION\_MBR structure
description: PARTITION\_INFORMATION\_MBR contains information for a Master Boot Record partition that is not held in common with a GUID Partition Table partition.
ms.assetid: '846f3a1c-ee0a-42d2-bdf1-7bf09406c955'
keywords: ["PARTITION_INFORMATION_MBR structure Storage Devices", "PPARTITION_INFORMATION_MBR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- PARTITION_INFORMATION_MBR
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# PARTITION\_INFORMATION\_MBR structure

PARTITION\_INFORMATION\_MBR contains information for a Master Boot Record partition that is not held in common with a GUID Partition Table partition.

## Syntax


```C++
typedef struct _PARTITION_INFORMATION_MBR {
  UCHAR   PartitionType;
  BOOLEAN BootIndicator;
  BOOLEAN RecognizedPartition;
  ULONG   HiddenSectors;
} PARTITION_INFORMATION_MBR, *PPARTITION_INFORMATION_MBR;
```



## Members

<dl> <dt>

**PartitionType**
</dt> <dd>

Specifies the partition type. See [**PARTITION\_INFORMATION**](partition-information.md) for a list of system-defined partition types.

</dd> <dt>

**BootIndicator**
</dt> <dd>

Indicates, when **TRUE**, that the partition is bootable. When **FALSE**, the partition is not bootable.

</dd> <dt>

**RecognizedPartition**
</dt> <dd>

Indicates, when **TRUE**, that this is a partition with a recognized partition type. When **FALSE** this is a not a partition with a recognized partition.

</dd> <dt>

**HiddenSectors**
</dt> <dd>

Contains the number of hidden sectors in the partition.

</dd> </dl>

## Requirements



|                   |                                                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntddk.h or Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**PARTITION\_INFORMATION\_EX**](partition-information-ex.md)
</dt> <dt>

[**PARTITION\_INFORMATION\_GPT**](partition-information-gpt.md)
</dt> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PARTITION_INFORMATION_MBR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






