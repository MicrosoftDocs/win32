---
title: STORAGE\_DEVICE\_IO\_CAPABILITY\_DESCRIPTOR structure
description: The output buffer for the StorageDeviceIoCapabilityProperty as defined in STORAGE\_PROPERTY\_ID.
ms.assetid: '98377F8F-62C8-4E8F-838B-A63DC63E4A0C'
keywords: ["STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR structure Storage Devices", "PSTORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_DEVICE\_IO\_CAPABILITY\_DESCRIPTOR structure

The output buffer for the StorageDeviceIoCapabilityProperty as defined in [**STORAGE\_PROPERTY\_ID**](storage-property-id.md).

## Syntax


```C++
typedef struct _STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG LunMaxIoCount;
  ULONG AdapterMaxIoCount;
} STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR, *PSTORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. The Size serves as the version.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure.

</dd> <dt>

**LunMaxIoCount**
</dt> <dd>

The logical unit number (LUN) max outstanding I/O count.

</dd> <dt>

**AdapterMaxIoCount**
</dt> <dd>

The adapter max outstanding I/O count.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                 |
| Server<br/> | Windows Server 2016<br/>                                                        |
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





