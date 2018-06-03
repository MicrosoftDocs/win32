---
title: STORAGE\_PHYSICAL\_DEVICE\_DATA structure
description: Specifies the physical device data of a storage device.
ms.assetid: 9D8E67D1-EB7C-4EED-8BDD-43D5E012B99C
keywords:
- STORAGE_PHYSICAL_DEVICE_DATA structure Storage Devices
- PSTORAGE_PHYSICAL_DEVICE_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PHYSICAL_DEVICE_DATA
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_PHYSICAL\_DEVICE\_DATA structure

Specifies the physical device data of a storage device.

## Syntax


```C++
typedef struct _STORAGE_PHYSICAL_DEVICE_DATA {
  ULONG                           DeviceId;
  ULONG                           Role;
  STORAGE_COMPONENT_HEALTH_STATUS HealthStatus;
  STORAGE_PROTOCOL_TYPE           CommandProtocol;
  STORAGE_SPEC_VERSION            SpecVersion;
  STORAGE_DEVICE_FORM_FACTOR      FormFactor;
  UCHAR                           Vendor[8];
  UCHAR                           Model[40];
  UCHAR                           FirmwareRevision[16];
  ULONGLONG                       Capacity;
  UCHAR                           PhysicalLocation[32];
  ULONG                           Reserved[2];
} STORAGE_PHYSICAL_DEVICE_DATA, *PSTORAGE_PHYSICAL_DEVICE_DATA;
```



## Members

<dl> <dt>

**DeviceId**
</dt> <dd>

The hardware ID of the storage device.

</dd> <dt>

**Role**
</dt> <dd>

The role of the storage device. A bitmask can be use to specify multiple roles, including **STORAGE\_COMPONENT\_ROLE\_CACHE** (0x00000001), **STORAGE\_COMPONENT\_ROLE\_TIERING** (0x00000002), and **STORAGE\_COMPONENT\_ROLE\_DATA** (0x00000004).

</dd> <dt>

**HealthStatus**
</dt> <dd>

Indicates the health status of a storage device, of type [**STORAGE\_COMPONENT\_HEALTH\_STATUS**](storage-component-health-status.md).

</dd> <dt>

**CommandProtocol**
</dt> <dd>

Specifies the storage command protocols that are used between software and hardware, of type [**STORAGE\_PROTOCOL\_TYPE**](storage-protocol-type.md).

</dd> <dt>

**SpecVersion**
</dt> <dd>

Indicates the specification of the storage device, of type [**STORAGE\_SPEC\_VERSION**](storage-spec-version.md).

</dd> <dt>

**FormFactor**
</dt> <dd>

Indicates the form factor of a storage device, of type [**STORAGE\_DEVICE\_FORM\_FACTOR**](storage-device-form-factor.md).

</dd> <dt>

**Vendor\[8\]**
</dt> <dd>

The vendor name of the storage device.

</dd> <dt>

**Model\[40\]**
</dt> <dd>

The model name of the storage device.

</dd> <dt>

**FirmwareRevision\[16\]**
</dt> <dd>

The revision number of the storage device.

</dd> <dt>

**Capacity**
</dt> <dd>

The capacity of the storage device in units of kilobytes (1024 bytes).

</dd> <dt>

**PhysicalLocation\[32\]**
</dt> <dd>

This member is reserved for future use.

</dd> <dt>

**Reserved\[2\]**
</dt> <dd>

Specifies if the storage device is reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PHYSICAL_DEVICE_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





