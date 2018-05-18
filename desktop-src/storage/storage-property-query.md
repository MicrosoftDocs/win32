---
title: STORAGE\_PROPERTY\_QUERY structure
description: This structure is used in conjunction with IOCTL\_STORAGE\_QUERY\_PROPERTY to retrieve the properties of a storage device or adapter.
ms.assetid: '5f8e4fbd-706c-4694-bcba-927474a66e86'
keywords: ["STORAGE_PROPERTY_QUERY structure Storage Devices", "PSTORAGE_PROPERTY_QUERY structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_PROPERTY_QUERY
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_PROPERTY\_QUERY structure

This structure is used in conjunction with [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve the properties of a storage device or adapter.

## Syntax


```C++
typedef struct _STORAGE_PROPERTY_QUERY {
  STORAGE_PROPERTY_ID PropertyId;
  STORAGE_QUERY_TYPE  QueryType;
  UCHAR               AdditionalParameters[1];
} STORAGE_PROPERTY_QUERY, *PSTORAGE_PROPERTY_QUERY;
```



## Members

<dl> <dt>

**PropertyId**
</dt> <dd>

Indicates whether the caller is requesting a device descriptor, an adapter descriptor, a write cache property, a device unique ID (DUID), or the device identifiers provided in the device's SCSI vital product data (VPD) page. For a list of the property IDs that can be assigned to this member, see [**STORAGE\_PROPERTY\_ID**](storage-property-id.md).

</dd> <dt>

**QueryType**
</dt> <dd>

Contains flags indicating the type of query to be performed. For a list of the various query types that can be assigned to this member, see [**STORAGE\_QUERY\_TYPE**](storage-query-type.md).

</dd> <dt>

**AdditionalParameters**
</dt> <dd>

Contains an array of bytes with additional input parameters that are needed for the **PropertyId** query. Not all **PropertyId** values require additional input parameters.

</dd> </dl>

## Remarks

The results of the query can be one of several structures depending on the value of the **PropertyId** member. These values are enumerated by the [**STORAGE\_PROPERTY\_ID**](storage-property-id.md) enumeration.

If the **QueryType** member is set to **PropertyExistsQuery**, then no structure is returned. For more info, see [**STORAGE\_QUERY\_TYPE**](storage-query-type.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md)
</dt> <dt>

[**STORAGE\_QUERY\_TYPE**](storage-query-type.md)
</dt> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> <dt>

[**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_ID**](storage-property-id.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROPERTY_QUERY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






