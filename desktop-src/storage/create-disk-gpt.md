---
title: CREATE\_DISK\_GPT structure
description: The CREATE\_DISK\_GPT structure is used with the IOCTL IOCTL\_DISK\_CREATE\_DISK to initialize a disk with an empty GPT partition table.
ms.assetid: 24ae7329-064f-43bf-8c1d-8aad9fdf2254
keywords:
- CREATE_DISK_GPT structure Storage Devices
- PCREATE_DISK_GPT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CREATE_DISK_GPT
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CREATE\_DISK\_GPT structure

The CREATE\_DISK\_GPT structure is used with the IOCTL [**IOCTL\_DISK\_CREATE\_DISK**](ioctl-disk-create-disk.md) to initialize a disk with an empty GPT partition table.

## Syntax


```C++
typedef struct _CREATE_DISK_GPT {
  GUID  DiskId;
  ULONG MaxPartitionCount;
} CREATE_DISK_GPT, *PCREATE_DISK_GPT;
```



## Members

<dl> <dt>

**DiskId**
</dt> <dd>

Specifies the GUID that uniquely identifies the disk.

</dd> <dt>

**MaxPartitionCount**
</dt> <dd>

Specifies the maximum number of partitions allowed on the disk.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**CREATE\_DISK**](create-disk.md)
</dt> <dt>

[**IOCTL\_DISK\_CREATE\_DISK**](ioctl-disk-create-disk.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CREATE_DISK_GPT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






