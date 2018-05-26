---
title: DEVICE\_SEEK\_PENALTY\_DESCRIPTOR structure
description: The DEVICE\_SEEK\_PENALTY\_DESCRIPTOR structure is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the seek penalty descriptor data for a device.
ms.assetid: c12b66a4-fdb5-40d3-a767-c15477391179
keywords:
- DEVICE_SEEK_PENALTY_DESCRIPTOR structure Storage Devices
- PDEVICE_SEEK_PENALTY_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_SEEK_PENALTY_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DEVICE\_SEEK\_PENALTY\_DESCRIPTOR structure

The DEVICE\_SEEK\_PENALTY\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the seek penalty descriptor data for a device.

## Syntax


```C++
typedef struct _DEVICE_SEEK_PENALTY_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  BOOLEAN IncursSeekPenalty;
} DEVICE_SEEK_PENALTY_DESCRIPTOR, *PDEVICE_SEEK_PENALTY_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of the structure DEVICE\_SEEK\_PENALTY\_DESCRIPTOR. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the descriptor, in bytes.

</dd> <dt>

**IncursSeekPenalty**
</dt> <dd>

Specifies whether the device incurs a seek penalty.

</dd> </dl>

## Remarks

Storage class drivers issue a device-control request with the I/O control code [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve this structure, which contains seek penalty information for data transfer operations. The structure can be retrieved either from the device object for the bus or from an FDO, which forwards the request to the underlying bus.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_SEEK_PENALTY_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






