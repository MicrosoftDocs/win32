---
title: STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER structure
description: The STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER structure defines a device unique identifier (DUID).
ms.assetid: 02de3382-031a-4d42-b349-786248da9c5c
keywords:
- STORAGE_DEVICE_UNIQUE_IDENTIFIER structure Storage Devices
- PSTORAGE_DEVICE_UNIQUE_IDENTIFIER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_UNIQUE_IDENTIFIER
api_location:
- storduid.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER structure

The STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER structure defines a device unique identifier (DUID).

## Syntax


```C++
typedef struct _STORAGE_DEVICE_UNIQUE_IDENTIFIER {
  ULONG Version;
  ULONG Size;
  ULONG StorageDeviceIdOffset;
  ULONG StorageDeviceOffset;
  ULONG DriveLayoutSignatureOffset;
} STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of the DUID.

</dd> <dt>

**Size**
</dt> <dd>

The size, in bytes, of the identifier header and the identifiers (IDs) that follow the header.

</dd> <dt>

**StorageDeviceIdOffset**
</dt> <dd>

The offset, in bytes, from the beginning of the header to the device ID descriptor ([**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md)). The device ID descriptor contains the IDs that are extracted from page 0x83 of the device's vital product data (VPD).

</dd> <dt>

**StorageDeviceOffset**
</dt> <dd>

The offset, in bytes, from the beginning of the header to the device descriptor ([**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)). The device descriptor contains IDs that are extracted from non-VPD inquiry data.

</dd> <dt>

**DriveLayoutSignatureOffset**
</dt> <dd>

The offset, in bytes, to the drive layout signature ([**STORAGE\_DEVICE\_LAYOUT\_SIGNATURE**](storage-device-layout-signature.md)).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storduid.h (include Storduid.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> <dt>

[**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_UNIQUE_IDENTIFIER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






