---
title: DISK\_GROW\_PARTITION structure
description: The DISK\_GROW\_PARTITION structure is used in conjunction with the IOCTL\_DISK\_GROW\_PARTITION request to enlarge a partition.
ms.assetid: 'cab9877c-3b7b-4644-83eb-0aa1e9fc77b9'
keywords: ["DISK_GROW_PARTITION structure Storage Devices", "PDISK_GROW_PARTITION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_GROW_PARTITION
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DISK\_GROW\_PARTITION structure

The DISK\_GROW\_PARTITION structure is used in conjunction with the [**IOCTL\_DISK\_GROW\_PARTITION**](ioctl-disk-grow-partition.md) request to enlarge a partition.

## Syntax


```C++
typedef struct _DISK_GROW_PARTITION {
  ULONG         PartitionNumber;
  LARGE_INTEGER BytesToGrow;
} DISK_GROW_PARTITION, *PDISK_GROW_PARTITION;
```



## Members

<dl> <dt>

**PartitionNumber**
</dt> <dd>

Specifies a number identifying the partition to be enlarged.

</dd> <dt>

**BytesToGrow**
</dt> <dd>

Indicates the number of bytes that the partition should be extended by. Note that this value is not the new size of the partition.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_GROW\_PARTITION**](ioctl-disk-grow-partition.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_GROW_PARTITION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






