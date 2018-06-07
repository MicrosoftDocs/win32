---
title: STORAGE\_DESCRIPTOR\_HEADER structure
description: The STORAGE\_DESCRIPTOR\_HEADER structure is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the properties of a storage device or adapter.
ms.assetid: 57d019b0-7914-42f6-a888-16042aa97444
keywords:
- STORAGE_DESCRIPTOR_HEADER structure Storage Devices
- PSTORAGE_DESCRIPTOR_HEADER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DESCRIPTOR_HEADER
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

# STORAGE\_DESCRIPTOR\_HEADER structure

The STORAGE\_DESCRIPTOR\_HEADER structure is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the properties of a storage device or adapter.

## Syntax


```C++
typedef struct _STORAGE_DESCRIPTOR_HEADER {
  ULONG Version;
  ULONG Size;
} STORAGE_DESCRIPTOR_HEADER, *PSTORAGE_DESCRIPTOR_HEADER;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the version of the data reported.

</dd> <dt>

**Size**
</dt> <dd>

Indicates the quantity of data reported, in bytes.

</dd> </dl>

## Remarks

The data retrieved by IOCTL\_STORAGE\_QUERY\_PROPERTY is reported in the buffer immediately following this structure.

The IOCTL\_STORAGE\_QUERY\_PROPERTY request reports one of three types of properties: a device descriptor, an adapter descriptor, or a set of device IDs taken from the device's SCSI vital product data pages. Device descriptors are reported in a structure of type [**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md). Adapter descriptors are reported in a structure of type [**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md). Vital product page device IDs are reported in a structure of type [**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DESCRIPTOR_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






