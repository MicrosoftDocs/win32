---
title: STORAGE\_MEDIUM\_PRODUCT\_TYPE\_DESCRIPTOR structure
description: Used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to describe the product type of a storage device.
ms.assetid: AC0C09DF-EFD4-457B-8ABC-C60890D3AF6A
keywords:
- STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR structure Storage Devices
- PSTORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR
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

# STORAGE\_MEDIUM\_PRODUCT\_TYPE\_DESCRIPTOR structure

Used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to describe the product type of a storage device.

## Syntax


```C++
typedef struct _STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG MediumProductType;
} STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR, *PSTORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of this structure, in bytes, as defined by `Sizeof(STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR)`. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

</dd> <dt>

**MediumProductType**
</dt> <dd>

Specifies the product type of the storage device.



| **MediumProductType** value | Description                   |
|-----------------------------|-------------------------------|
| `00h`                       | Not indicated                 |
| `01h`                       | CFast                         |
| `02h`                       | CompactFlash                  |
| `03h`                       | Memory Stick                  |
| `04h`                       | MultiMediaCard                |
| `05h`                       | Secure Digital Card (SD Card) |
| `06h`                       | QXD                           |
| `07h`                       | Universal Flash Storage       |
| `08h` to `EFh`              | Reserved                      |
| `F0h` to `FFh`              | Vendor-specific               |



 

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                     |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






