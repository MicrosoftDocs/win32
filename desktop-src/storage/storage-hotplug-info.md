---
title: STORAGE\_HOTPLUG\_INFO structure
description: The STORAGE\_HOTPLUG\_INFO structure provides hotplug information for a device.
ms.assetid: dcfd5a42-cb76-4386-9f8f-98e0a217c49a
keywords:
- STORAGE_HOTPLUG_INFO structure Storage Devices
- PSTORAGE_HOTPLUG_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_HOTPLUG_INFO
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

# STORAGE\_HOTPLUG\_INFO structure

The STORAGE\_HOTPLUG\_INFO structure provides hotplug information for a device.

## Syntax


```C++
typedef struct _STORAGE_HOTPLUG_INFO {
  ULONG   Size;
  BOOLEAN MediaRemovable;
  BOOLEAN MediaHotplug;
  BOOLEAN DeviceHotplug;
  BOOLEAN WriteCacheEnableOverride;
} STORAGE_HOTPLUG_INFO, *PSTORAGE_HOTPLUG_INFO;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Indicates the size, in bytes, of this structure.

</dd> <dt>

**MediaRemovable**
</dt> <dd>

Specifies whether the media is removable. If set to a nonzero value, the device media is removable. If set to zero, the device media is not removable.

</dd> <dt>

**MediaHotplug**
</dt> <dd>

Specifies whether the media is lockable. If set to a nonzero value, the device media is not lockable. If set to zero, the device media is lockable.

</dd> <dt>

**DeviceHotplug**
</dt> <dd>

Specifies whether the device is a hotplug device. If set to a nonzero value, the device is a hotplug device. If set to zero, the device is not a hotplug device.

</dd> <dt>

**WriteCacheEnableOverride**
</dt> <dd>

Do not use; set the value to **NULL**.

</dd> </dl>

## Remarks

The value of the **Size** member also identifies the version of this structure. New members will be added to this structure in the future. If the value of the **Size** member is **sizeof**(STORAGE\_HOTPLUG\_INFO), the current version of the structure is the same as the version you compiled with. If the value is not **sizeof**(STORAGE\_HOTPLUG\_INFO), the current version contains additional members.

Microsoft Windows XP includes support for hotplug devices. A hotplug device refers to a device whose **RemovalPolicy** value displayed in the Device Manager is **ExpectSurpriseRemoval**. To query whether a particular device is a hotplug device, use the [**IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO**](ioctl-storage-get-hotplug-info.md) request. To set the hotplug properties of a device, use the [**IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO**](ioctl-storage-set-hotplug-info.md) request.

In the case of the IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO request, the **DeviceHotplug** member of the STORAGE\_HOTPLUG\_INFO structure determines what action is taken. If the value of that member is nonzero, the value for the device's removal policy in the registry is set to **ExpectSurpriseRemoval** and all levels of caching are disabled. If the value of **DeviceHotplug** is zero, the removal policy is set to **ExpectOrderlyRemoval**, and caching may be selectively enabled.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_HOTPLUG\_INFO**](ioctl-storage-get-hotplug-info.md)
</dt> <dt>

[**IOCTL\_STORAGE\_SET\_HOTPLUG\_INFO**](ioctl-storage-set-hotplug-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_HOTPLUG_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






