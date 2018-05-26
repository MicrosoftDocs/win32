---
title: STORAGE\_PHYSICAL\_TOPOLOGY\_DESCRIPTOR structure
description: Describes the physical topology of storage in a system.
ms.assetid: FD5714DF-9D34-4396-86BC-40054C199A0E
keywords:
- STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR structure Storage Devices
- PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_PHYSICAL\_TOPOLOGY\_DESCRIPTOR structure

Describes the physical topology of storage in a system.

## Syntax


```C++
typedef struct _STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR {
  ULONG                      Version;
  ULONG                      Size;
  ULONG                      NodeCount;
  ULONG                      Reserved;
  STORAGE_PHYSICAL_NODE_DATA Node[ANYSIZE_ARRAY];
} STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR, *PSTORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of the physical topology.

</dd> <dt>

**Size**
</dt> <dd>

The total size of data in the system.

</dd> <dt>

**NodeCount**
</dt> <dd>

The total number of storage nodes in the system.

</dd> <dt>

**Reserved**
</dt> <dd>

Indicates if storage in the system is reserved.

</dd> <dt>

**Node\[ANYSIZE\_ARRAY\]**
</dt> <dd>

Describes the storage nodes in the system.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





