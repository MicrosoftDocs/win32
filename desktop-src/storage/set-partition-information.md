---
title: SET\_PARTITION\_INFORMATION structure
description: SET\_PARTITION\_INFORMATION is used with IOCTL\_DISK\_SET\_PARTITION\_INFO to change the partition type of a specified Master Boot Record (MBR) disk partition.
ms.assetid: '882aedda-5ed5-43e0-a370-59a7c7e4c802'
keywords: ["SET_PARTITION_INFORMATION structure Storage Devices", "PSET_PARTITION_INFORMATION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SET_PARTITION_INFORMATION
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# SET\_PARTITION\_INFORMATION structure

SET\_PARTITION\_INFORMATION is used with IOCTL\_DISK\_SET\_PARTITION\_INFO to change the partition type of a specified Master Boot Record (MBR) disk partition.

## Syntax


```C++
typedef struct _SET_PARTITION_INFORMATION {
  UCHAR PartitionType;
} SET_PARTITION_INFORMATION, *PSET_PARTITION_INFORMATION;
```



## Members

<dl> <dt>

**PartitionType**
</dt> <dd>

Indicates the partition type. IOCTL\_DISK\_SET\_PARTITION\_INFO uses this value to set the partition type. See [**PARTITION\_INFORMATION**](partition-information.md) for a list of system-defined GPT partition types.

</dd> </dl>

## Remarks

The single byte unsigned value, *PartitionType*, contained in this structure defines a traditional AT Master Boot Record style of partition and cannot be used to define an Extensible Firmware Interface partition (also known as a GUID Partition Table partition). GPT partitions use a GUID to indicate the partition type.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**SET\_PARTITION\_INFORMATION\_EX**](set-partition-information-ex.md)
</dt> <dt>

[**SET\_PARTITION\_INFORMATION\_MBR**](https://msdn.microsoft.com/library/windows/hardware/ff566198)
</dt> <dt>

[**SET\_PARTITION\_INFORMATION\_GPT**](https://msdn.microsoft.com/library/windows/hardware/ff566196)
</dt> <dt>

[**IOCTL\_DISK\_SET\_PARTITION\_INFO**](ioctl-disk-set-partition-info.md)
</dt> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SET_PARTITION_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






