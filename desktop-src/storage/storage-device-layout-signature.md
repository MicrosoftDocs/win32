---
title: STORAGE\_DEVICE\_LAYOUT\_SIGNATURE structure
description: The STORAGE\_DEVICE\_LAYOUT\_SIGNATURE structure defines a device layout structure.
ms.assetid: 3c433fe5-1782-4a00-aa7b-1558b0f56080
keywords:
- STORAGE_DEVICE_LAYOUT_SIGNATURE structure Storage Devices
- PSTORAGE_DEVICE_LAYOUT_SIGNATURE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_LAYOUT_SIGNATURE
api_location:
- storduid.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_DEVICE\_LAYOUT\_SIGNATURE structure

The STORAGE\_DEVICE\_LAYOUT\_SIGNATURE structure defines a device layout structure.

## Syntax


```C++
typedef struct _STORAGE_DEVICE_LAYOUT_SIGNATURE {
  ULONG   Version;
  ULONG   Size;
  BOOLEAN Mbr;
  union {
    ULONG MbrSignature;
    GUID  GptDiskId;
  } DeviceSpecific;
} STORAGE_DEVICE_LAYOUT_SIGNATURE, *PSTORAGE_DEVICE_LAYOUT_SIGNATURE;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of the DUID.

</dd> <dt>

**Size**
</dt> <dd>

The size, in bytes, of this STORAGE\_DEVICE\_LAYOUT\_SIGNATURE structure.

</dd> <dt>

**Mbr**
</dt> <dd>

A Boolean value that indicates whether the partition table of the disk is formatted with a master boot record (MBR). If **TRUE**, the partition table of the disk is formatted with a master boot record (MBR). If **FALSE**, the disk has a GUID partition table (GPT).

</dd> <dt>

**DeviceSpecific**
</dt> <dd> <dl> <dt>

**MbrSignature**
</dt> <dd>

The signature value, which uniquely identifies the disk.

</dd> <dt>

**GptDiskId**
</dt> <dd>

The GUID that uniquely identifies the disk.

</dd> </dl> </dd> </dl>

## Remarks

The device layout signature contributes to the definition of a device unique identifier (DUID). For more information about DUIDs, see the description of the [**STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER**](storage-device-unique-identifier.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storduid.h (include Storduid.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER**](storage-device-unique-identifier.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_LAYOUT_SIGNATURE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






