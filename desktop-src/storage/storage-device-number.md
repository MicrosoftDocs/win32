---
title: STORAGE\_DEVICE\_NUMBER structure
description: The STORAGE\_DEVICE\_NUMBER structure is used in conjunction with the IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER request to retrieve the FILE\_DEVICE\_XXX device type, the device number, and, for a device that can be partitioned, the partition number assigned to a device by the driver when the device is started.
ms.assetid: 3efed879-bde4-44ea-9af5-fc35a2ac27fc
keywords:
- STORAGE_DEVICE_NUMBER structure Storage Devices
- PSTORAGE_DEVICE_NUMBER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_NUMBER
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

# STORAGE\_DEVICE\_NUMBER structure

The STORAGE\_DEVICE\_NUMBER structure is used in conjunction with the [**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](ioctl-storage-get-device-number.md) request to retrieve the FILE\_DEVICE\_*XXX* device type, the device number, and, for a device that can be partitioned, the partition number assigned to a device by the driver when the device is started.

## Syntax


```C++
typedef struct _STORAGE_DEVICE_NUMBER {
  DEVICE_TYPE DeviceType;
  ULONG       DeviceNumber;
  ULONG       PartitionNumber;
} STORAGE_DEVICE_NUMBER, *PSTORAGE_DEVICE_NUMBER;
```



## Members

<dl> <dt>

**DeviceType**
</dt> <dd>

Specifies one of the system-defined FILE\_DEVICE\_*XXX* constants indicating the type of device (such as FILE\_DEVICE\_DISK, FILE\_DEVICE\_KEYBOARD, and so forth) or a vendor-defined value for a new type of device. For more information, see [Specifying Device Types](https://msdn.microsoft.com/library/windows/hardware/ff563821).

</dd> <dt>

**DeviceNumber**
</dt> <dd>

Indicates the number of this device. This value is set to 0xFFFFFFFF (-1) for the disks that represent the physical paths of an MPIO disk.

</dd> <dt>

**PartitionNumber**
</dt> <dd>

Indicates the partition number of the device is returned in this member, if the device can be partitioned. Otherwise, -1 is returned.

</dd> </dl>

## Remarks

The [**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](ioctl-storage-get-device-number.md) request is usually issued by a fault-tolerant disk driver.

The values in the STORAGE\_DEVICE\_NUMBER structure are guaranteed to remain unchanged until the system is rebooted. They are not guaranteed to be persistent across boots.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER**](ioctl-storage-get-device-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_NUMBER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






