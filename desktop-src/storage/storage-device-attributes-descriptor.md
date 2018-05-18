---
title: STORAGE\_DEVICE\_ATTRIBUTES\_DESCRIPTOR structure
description: The STORAGE\_DEVICE\_ATTRIBUTES\_DESCRIPTOR structure is used to retrieve the attributes information for a device.
ms.assetid: 'DA8434EF-6163-4D07-A81D-D1AC2D55BFB4'
keywords: ["STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure Storage Devices", "PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_DEVICE\_ATTRIBUTES\_DESCRIPTOR structure

The STORAGE\_DEVICE\_ATTRIBUTES\_DESCRIPTOR structure is used to retrieve the attributes information for a device.

## Syntax


```C++
typedef struct _STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  ULONG64 Attributes;
} STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, *PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the version of the data reported.

</dd> <dt>

**Size**
</dt> <dd>

Indicates the quantity of data reported, in bytes. This is the `sizeof(STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR)`.

</dd> <dt>**Attributes**</dt> <dd> 

| Value                                                                                                                                                                                                                                                                                                             | Meaning                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <span id="STORAGE_ATTRIBUTE_BYTE_ADDRESSABLE_IO"></span><span id="storage_attribute_byte_addressable_io"></span><dl> <dt>**STORAGE\_ATTRIBUTE\_BYTE\_ADDRESSABLE\_IO**</dt> <dt>0x01</dt> </dl>                | Attribute that indicates a storage device supports byte addressable IO.<br/>                         |
| <span id="STORAGE_ATTRIBUTE_BLOCK_IO"></span><span id="storage_attribute_block_io"></span><dl> <dt>**STORAGE\_ATTRIBUTE\_BLOCK\_IO**</dt> <dt>0x02</dt> </dl>                                                  | Attribute that indicates a storage device supports block IO.<br/>                                    |
| <span id="STORAGE_ATTRIBUTE_DYNAMIC_PERSISTENCE"></span><span id="storage_attribute_dynamic_persistence"></span><dl> <dt>**STORAGE\_ATTRIBUTE\_DYNAMIC\_PERSISTENCE**</dt> <dt>0x04</dt> </dl>                 | Attribute that indicates that persistence of data on storage device may change.<br/>                 |
| <span id="STORAGE_ATTRIBUTE_VOLATILE"></span><span id="storage_attribute_volatile"></span><dl> <dt>**STORAGE\_ATTRIBUTE\_VOLATILE**</dt> <dt>0x08</dt> </dl>                                                   | Attribute that indicates a storage device is volatile and does not support persistence of data.<br/> |
| <span id="STORAGE_ATTRIBUTE_ASYNC_EVENT_NOTIFICATION"></span><span id="storage_attribute_async_event_notification"></span><dl> <dt>**STORAGE\_ATTRIBUTE\_ASYNC\_EVENT\_NOTIFICATION**</dt> <dt>0x10</dt> </dl> | Reserved<br/>                                                                                        |
| <span id="STORAGE_ATTRIBUTE_PERF_SIZE_INDEPENDENT"></span><span id="storage_attribute_perf_size_independent"></span><dl> <dt>**STORAGE\_ATTRIBUTE\_PERF\_SIZE\_INDEPENDENT**</dt> <dt>0x20</dt> </dl>          | Attribute that indicates a storage device has IO performance independent of IO sizes.<br/>           |



 

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10<br/>                                                                                      |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





