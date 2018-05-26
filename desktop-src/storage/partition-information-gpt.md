---
title: PARTITION\_INFORMATION\_GPT structure
description: PARTITION\_INFORMATION\_GPT contains information for a GUID Partition Table partition that is not held in common with a Master Boot Record partition.
ms.assetid: f2d76b4c-7acd-4701-b978-3d29dc8cde0b
keywords:
- PARTITION_INFORMATION_GPT structure Storage Devices
- PPARTITION_INFORMATION_GPT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PARTITION_INFORMATION_GPT
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PARTITION\_INFORMATION\_GPT structure

PARTITION\_INFORMATION\_GPT contains information for a GUID Partition Table partition that is not held in common with a Master Boot Record partition.

## Syntax


```C++
typedef struct _PARTITION_INFORMATION_GPT {
  GUID    PartitionType;
  GUID    PartitionId;
  ULONG64 Attributes;
  WCHAR   Name[36];
} PARTITION_INFORMATION_GPT, *PPARTITION_INFORMATION_GPT;
```



## Members

<dl> <dt>

**PartitionType**
</dt> <dd>

Specifies a GUID that uniquely identifies the partition type. The GUID data type is described on the [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392) reference page.

</dd> <dt>

**PartitionId**
</dt> <dd>

Specifies a GUID that uniquely identifies the partition. The GUID data type is described on the [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392) reference page.

</dd> <dt>

**Attributes**
</dt> <dd>

Specifies the partition entry attributes used for diagnostics, recovery tools, and other firmware essential to the operation of the device. See Intel's *Extensible Firmware Interface* specification for further information.

</dd> <dt>

**Name**
</dt> <dd>

Specifies the partition name in Unicode.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**PARTITION\_INFORMATION\_EX**](partition-information-ex.md)
</dt> <dt>

[**IoReadPartitionTableEx**](ioreadpartitiontableex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PARTITION_INFORMATION_GPT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






