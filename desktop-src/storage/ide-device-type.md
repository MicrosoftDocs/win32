---
title: IDE\_DEVICE\_TYPE enumeration
description: The IDE\_DEVICE\_TYPE enumeration type indicates the device type.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 6d94189f-d6ab-40ad-85e5-f4efe8c30ed8
keywords:
- IDE_DEVICE_TYPE enumeration Storage Devices
topic_type:
- apiref
api_name:
- IDE_DEVICE_TYPE
api_location:
- irb.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# IDE\_DEVICE\_TYPE enumeration

The IDE\_DEVICE\_TYPE enumeration type indicates the device type.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum  { 
  DeviceUnknown   = 0,
  DeviceIsAta     = 1,
  DeviceIsAtapi   = 2,
  DeviceNotExist  = 3
} IDE_DEVICE_TYPE;
```



## Constants

<dl> <dt>

<span id="DeviceUnknown"></span><span id="deviceunknown"></span><span id="DEVICEUNKNOWN"></span>**DeviceUnknown**
</dt> <dd>

Indicates that the device does not communicate by means of a known protocol.

</dd> <dt>

<span id="DeviceIsAta"></span><span id="deviceisata"></span><span id="DEVICEISATA"></span>**DeviceIsAta**
</dt> <dd>

Indicates an ATA device.

</dd> <dt>

<span id="DeviceIsAtapi"></span><span id="deviceisatapi"></span><span id="DEVICEISATAPI"></span>**DeviceIsAtapi**
</dt> <dd>

Indicates an ATAPI device.

</dd> <dt>

<span id="DeviceNotExist"></span><span id="devicenotexist"></span><span id="DEVICENOTEXIST"></span>**DeviceNotExist**
</dt> <dd>

Indicates that the device does not exist.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_DEVICE_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





