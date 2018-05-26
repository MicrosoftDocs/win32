---
title: STORAGE\_PHYSICAL\_NODE\_DATA structure
description: Specifies the physical device data of a storage node.
ms.assetid: F6C1EE86-FB1C-467D-9E03-B238CB132D1A
keywords:
- STORAGE_PHYSICAL_NODE_DATA structure Storage Devices
- PSTORAGE_PHYSICAL_NODE_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PHYSICAL_NODE_DATA
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

# STORAGE\_PHYSICAL\_NODE\_DATA structure

Specifies the physical device data of a storage node.

## Syntax


```C++
typedef struct _STORAGE_PHYSICAL_NODE_DATA {
  ULONG NodeId;
  ULONG AdapterCount;
  ULONG AdapterDataLength;
  ULONG AdapterDataOffset;
  ULONG DeviceCount;
  ULONG DeviceDataLength;
  ULONG DeviceDataOffset;
  ULONG Reserved[3];
} STORAGE_PHYSICAL_NODE_DATA, *PSTORAGE_PHYSICAL_NODE_DATA;
```



## Members

<dl> <dt>

**NodeId**
</dt> <dd>

The hardware ID of the storage node.

</dd> <dt>

**AdapterCount**
</dt> <dd>

A value of 0 or 1 that indicates the adapter count in the storage node.

</dd> <dt>

**AdapterDataLength**
</dt> <dd>

The data length of the storage adapter in the storage node, in units of kilobytes (1024 bytes).

</dd> <dt>

**AdapterDataOffset**
</dt> <dd>

The data offset from the beginning of the data structure. The buffer contains an array of [**STORAGE\_PHYSICAL\_ADAPTER\_DATA**](storage-physical-adapter-data.md).

</dd> <dt>

**DeviceCount**
</dt> <dd>

A value less than or equal to 1.

</dd> <dt>

**DeviceDataLength**
</dt> <dd>

The data length of the storage device in the storage node, in units of kilobytes (1024 bytes).

</dd> <dt>

**DeviceDataOffset**
</dt> <dd>

The data offset from the beginning of the data structure. The buffer contains an array of [**STORAGE\_PHYSICAL\_DEVICE\_DATA**](storage-physical-device-data.md).

</dd> <dt>

**Reserved\[3\]**
</dt> <dd>

Specifies if the storage adapter is reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PHYSICAL_NODE_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





