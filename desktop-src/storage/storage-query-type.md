---
title: STORAGE\_QUERY\_TYPE enumeration
description: The STORAGE\_QUERY\_TYPE enumeration is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the properties of a storage device or adapter.
ms.assetid: '3f346a09-071e-4512-bf77-994d277cef4d'
keywords: ["STORAGE_QUERY_TYPE enumeration Storage Devices", "PSTORAGE_QUERY_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_QUERY_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_QUERY\_TYPE enumeration

The STORAGE\_QUERY\_TYPE enumeration is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the properties of a storage device or adapter.

## Syntax


```C++
typedef enum _STORAGE_QUERY_TYPE { 
  PropertyStandardQuery    = 0,
  PropertyExistsQuery,
  PropertyMaskQuery,
  PropertyQueryMaxDefined
} STORAGE_QUERY_TYPE, *PSTORAGE_QUERY_TYPE;
```



## Constants

<dl> <dt>

<span id="PropertyStandardQuery"></span><span id="propertystandardquery"></span><span id="PROPERTYSTANDARDQUERY"></span>**PropertyStandardQuery**
</dt> <dd>

Instructs the port driver to report a device descriptor, an adapter descriptor or a unique hardware device ID (DUID).

</dd> <dt>

<span id="PropertyExistsQuery"></span><span id="propertyexistsquery"></span><span id="PROPERTYEXISTSQUERY"></span>**PropertyExistsQuery**
</dt> <dd>

Instructs the port driver to report whether the descriptor is supported.

</dd> <dt>

<span id="PropertyMaskQuery"></span><span id="propertymaskquery"></span><span id="PROPERTYMASKQUERY"></span>**PropertyMaskQuery**
</dt> <dd>

Not currently supported. Do not use.

</dd> <dt>

<span id="PropertyQueryMaxDefined"></span><span id="propertyquerymaxdefined"></span><span id="PROPERTYQUERYMAXDEFINED"></span>**PropertyQueryMaxDefined**
</dt> <dd>

Specifies the upper limit of the list of query types. This is used to validate the query type.

</dd> </dl>

## Remarks

Caller specifies the type of query by choosing one of the enumeration values.

Caller defines the exact nature of an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request by specifying the query type together with the property ID. See [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) for an explanation of how these two values are combined to define the query.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_ID**](storage-property-id.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_QUERY_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






