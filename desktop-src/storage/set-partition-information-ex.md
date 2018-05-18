---
title: SET\_PARTITION\_INFORMATION\_EX structure
description: SET\_PARTITION\_INFORMATION\_EX is used with the IOCTL IOCTL\_DISK\_SET\_PARTITION\_INFO\_EX to set information for a specific partition.
ms.assetid: 'a30c10d4-5e85-4a59-b262-054a6fdc2fb8'
keywords: ["SET_PARTITION_INFORMATION_EX structure Storage Devices", "PSET_PARTITION_INFORMATION_EX structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SET_PARTITION_INFORMATION_EX
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# SET\_PARTITION\_INFORMATION\_EX structure

**SET\_PARTITION\_INFORMATION\_EX** is used with the IOCTL [**IOCTL\_DISK\_SET\_PARTITION\_INFO\_EX**](ioctl-disk-set-partition-info-ex.md) to set information for a specific partition.

## Syntax


```C++
typedef struct _SET_PARTITION_INFORMATION_EX {
  PARTITION_STYLE PartitionStyle;
  union {
    SET_PARTITION_INFORMATION_MBR Mbr;
    SET_PARTITION_INFORMATION_GPT Gpt;
  };
} SET_PARTITION_INFORMATION_EX, *PSET_PARTITION_INFORMATION_EX;
```



## Members

<dl> <dt>

**PartitionStyle**
</dt> <dd>

Takes a [**PARTITION\_STYLE**](partition-style.md) enumerated value that specifies the type of partition table that contains the partition.

</dd> <dt>

**Mbr**
</dt> <dd>

Contains the information for a Master Boot Record partition that is not held in common with a GUID Partition Table partition. This member is valid when **PartitionStyle** member is set to PARTITION\_STYLE\_MBR. For a definition of this structure, see [**SET\_PARTITION\_INFORMATION\_MBR**](https://msdn.microsoft.com/library/windows/hardware/ff566198).

</dd> <dt>

**Gpt**
</dt> <dd>

Contains the information for a GUID Partition Table partition that is not held in common with a Master Boot Record partition. This member is valid when **PartitionStyle** member is set to PARTITION\_STYLE\_GPT. For a definition of this structure, see [**SET\_PARTITION\_INFORMATION\_GPT**](https://msdn.microsoft.com/library/windows/hardware/ff566196).

</dd> </dl>

## Remarks

In the case of GPT partitions, any value that can be retrieved from the partition can also be set. In the MBR case, only the partition signature can be set.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**SET\_PARTITION\_INFORMATION\_MBR**](https://msdn.microsoft.com/library/windows/hardware/ff566198)
</dt> <dt>

[**SET\_PARTITION\_INFORMATION\_GPT**](https://msdn.microsoft.com/library/windows/hardware/ff566196)
</dt> <dt>

[**IOCTL\_DISK\_SET\_PARTITION\_INFO\_EX**](ioctl-disk-set-partition-info-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SET_PARTITION_INFORMATION_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






