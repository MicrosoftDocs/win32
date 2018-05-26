---
title: DEVICE\_POWER\_DESCRIPTOR structure
description: Used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY control code to describes the power capabilities of a storage device.
ms.assetid: A5925EE4-768C-421A-9813-015513751A91
keywords:
- DEVICE_POWER_DESCRIPTOR structure Storage Devices
- PDEVICE_POWER_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_POWER_DESCRIPTOR
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

# DEVICE\_POWER\_DESCRIPTOR structure

Used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) control code to describes the power capabilities of a storage device.

## Syntax


```C++
typedef struct _DEVICE_POWER_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  BOOLEAN DeviceAttentionSupported;
  BOOLEAN AsynchronousNotificationSupported;
  BOOLEAN IdlePowerManagementEnabled;
  BOOLEAN D3ColdEnabled;
  BOOLEAN D3ColdSupported;
  BOOLEAN NoVerifyDuringIdlePower;
  UCHAR   Reserved[2];
  ULONG   IdleTimeoutInMS;
} DEVICE_POWER_DESCRIPTOR, *PDEVICE_POWER_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

</dd> <dt>

**DeviceAttentionSupported**
</dt> <dd>

**True** if device attention is supported. Otherwise, **False**.

</dd> <dt>

**AsynchronousNotificationSupported**
</dt> <dd>

**True** if the device supports asynchronous notifications, delivered via **IOCTL\_STORAGE\_EVENT\_NOTIFICATION**. Otherwise, **False**

</dd> <dt>

**IdlePowerManagementEnabled**
</dt> <dd>

**True** if the device has been registered for runtime idle power management. Otherwise, **False**

</dd> <dt>

**D3ColdEnabled**
</dt> <dd>

**True** if the device will be powered off when put into the D3 power state. Otherwise, **False**

</dd> <dt>

**D3ColdSupported**
</dt> <dd>

**True** if the platform supports **D3ColdEnabled** for this device. Otherwise, **False**.

</dd> <dt>

**NoVerifyDuringIdlePower**
</dt> <dd>

**True** if the device requires no verification during idle power transitions. Otherwise, **False**

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**IdleTimeoutInMS**
</dt> <dd>

The idle timeout value in milliseconds. This member is ignored unless **IdlePowerManagementEnabled** is true.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_POWER_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






