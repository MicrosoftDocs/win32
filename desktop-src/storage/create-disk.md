---
title: CREATE\_DISK structure
description: The CREATE\_DISK structure is used with the IOCTL\_DISK\_CREATE\_DISK IOCTL to initialize a disk with an empty partition table. The partition table styles are master boot record (MBR) or GUID partition table (GPT).
ms.assetid: 20989831-5ff0-4457-9dae-ceaf34830a2e
keywords:
- CREATE_DISK structure Storage Devices
- PCREATE_DISK structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CREATE_DISK
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

# CREATE\_DISK structure

The CREATE\_DISK structure is used with the [**IOCTL\_DISK\_CREATE\_DISK**](ioctl-disk-create-disk.md) IOCTL to initialize a disk with an empty partition table. The partition table styles are master boot record (MBR) or GUID partition table (GPT).

## Syntax


```C++
typedef struct _CREATE_DISK {
  PARTITION_STYLE PartitionStyle;
  union {
    CREATE_DISK_MBR Mbr;
    CREATE_DISK_GPT Gpt;
  };
} CREATE_DISK, *PCREATE_DISK;
```



## Members

<dl> <dt>

**PartitionStyle**
</dt> <dd>

Takes a [**PARTITION\_STYLE**](partition-style.md) enumerated value that specifies the type of partition table to use when formatting the disk.

</dd> <dt>

**Mbr**
</dt> <dd>

Contains the signature used to initialize an MBR-style disk partition for the first time. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_MBR. For more information, see [**CREATE\_DISK\_MBR**](create-disk-mbr.md).

</dd> <dt>

**Gpt**
</dt> <dd>

Contains data used to initialize a GPT-style disk partition for the first time. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_GPT. For more information, see [**CREATE\_DISK\_GPT**](create-disk-gpt.md).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_CREATE\_DISK**](ioctl-disk-create-disk.md)
</dt> <dt>

[**CREATE\_DISK\_MBR**](create-disk-mbr.md)
</dt> <dt>

[**CREATE\_DISK\_GPT**](create-disk-gpt.md)
</dt> <dt>

[**PARTITION\_STYLE**](partition-style.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CREATE_DISK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






