---
title: STORAGE\_DEVICE\_ID\_DESCRIPTOR structure
description: The STORAGE\_DEVICE\_ID\_DESCRIPTOR structure is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the device ID descriptor data for a device.
ms.assetid: 'e0e1bd3e-ee8d-40f2-904d-d6dcc4185406'
keywords: ["STORAGE_DEVICE_ID_DESCRIPTOR structure Storage Devices", "PSTORAGE_DEVICE_ID_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_ID_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_DEVICE\_ID\_DESCRIPTOR structure

The **STORAGE\_DEVICE\_ID\_DESCRIPTOR** structure is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the device ID descriptor data for a device.

## Syntax


```C++
typedef struct _STORAGE_DEVICE_ID_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG NumberOfIdentifiers;
  UCHAR Identifiers[1];
} STORAGE_DEVICE_ID_DESCRIPTOR, *PSTORAGE_DEVICE_ID_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Indicates the version of the descriptor.

</dd> <dt>

**Size**
</dt> <dd>

Indicates the size in bytes of the descriptor.

</dd> <dt>

**NumberOfIdentifiers**
</dt> <dd>

Contains the number of identifiers reported by the device in the **Identifiers** array.

</dd> <dt>

**Identifiers**
</dt> <dd>

Contains a variable-length array of identification descriptors.

</dd> </dl>

## Remarks

The device descriptor consists of an array of device IDs taken from the SCSI-3 vital product page data that was retrieved during discovery.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md)
</dt> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> <dt>

[**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_ID_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






