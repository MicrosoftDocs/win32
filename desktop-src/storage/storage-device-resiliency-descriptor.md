---
title: STORAGE\_DEVICE\_RESILIENCY\_DESCRIPTOR structure
description: Reserved for system use.
ms.assetid: 71351CB7-1295-4797-802C-23A6B1C2C53F
keywords:
- STORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure Storage Devices
- PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_RESILIENCY_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_DEVICE\_RESILIENCY\_DESCRIPTOR structure

Reserved for system use.

## Syntax


```C++
typedef struct _STORAGE_DEVICE_RESILIENCY_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG NameOffset;
  ULONG NumberOfLogicalCopies;
  ULONG NumberOfPhysicalCopies;
  ULONG PhysicalDiskRedundancy;
  ULONG NumberOfColumns;
  ULONG Interleave;
} STORAGE_DEVICE_RESILIENCY_DESCRIPTOR, *PSTORAGE_DEVICE_RESILIENCY_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure. Set to `sizeof(STORAGE_DEVICE_RESILIENCY_DESCRIPTOR)`.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

</dd> <dt>

**NameOffset**
</dt> <dd>

Byte offset to the null-terminated ASCII string containing the resiliency properties Name. For devices with no Name property, this will be zero.

</dd> <dt>

**NumberOfLogicalCopies**
</dt> <dd>

Number of logical copies of data that are available.

</dd> <dt>

**NumberOfPhysicalCopies**
</dt> <dd>

Number of complete copies of data that are stored.

</dd> <dt>

**PhysicalDiskRedundancy**
</dt> <dd>

Number of disks that can fail without leading to data loss.

</dd> <dt>

**NumberOfColumns**
</dt> <dd>

Number of columns in the storage device.

</dd> <dt>

**Interleave**
</dt> <dd>

Size of a stripe unit of the storage device, in bytes. This is also referred to as the stripe width or interleave of the storage device.

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_RESILIENCY_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






