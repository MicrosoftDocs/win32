---
Description: Retrieving Properties for Multiple Objects by Object Format
ms.assetid: 'c3f5edfd-8a6a-4bbd-9787-a4268c38f18f'
title: Retrieving Properties for Multiple Objects by Object Format
---

# Retrieving Properties for Multiple Objects by Object Format

In addition to a bulk retrieval of properties for a collection of object identifiers, an application can also perform a bulk retrieval of properties for all objects of a particular type. As in the previous example, bulk retrieval for a given type requires that the device driver support bulk retrievals.

Your application can perform a bulk retrieval using the interfaces described in the following table.



| Interface                                                                                      | Description                                                        |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [**IPortableDeviceContent Interface**](iportabledevicecontent.md)                             | Provides access to the content-specific methods.                   |
| [**IPortableDeviceKeyCollection Interface**](iportabledevicekeycollection.md)                 | Used to identify the properties to be retrieved.                   |
| [**IPortableDeviceProperties Interface**](iportabledeviceproperties.md)                       | Used to determine whether a given driver supports bulk operations. |
| [**IPortableDevicePropertiesBulk Interface**](iportabledevicepropertiesbulk.md)               | Supports the bulk retrieval operation.                             |
| [**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md) | Used to store the object identifiers for the bulk operation.       |



 

The ReadContentPropertiesBulkFilteringFormat function in the sample application's ContentProperties.cpp module demonstrates a bulk retrieval operation for objects of a particular type or format.

The code found in the ReadContentPropertiesBulkFilteringFormat function is almost identical to the code found in the ReadContentPropertiesBulk function. (See the [Retrieving Properties for Multiple Objects](retrieving-properties-for-multiple-objects.md) topic for a complete description of this function.)

The one primary difference occurs when the operation is queued. When filtering by type or format, the [**IPortableDevicePropertiesBulk::QueueGetValuesByObjectFormat**](iportabledevicepropertiesbulk-queuegetvaluesbyobjectformat.md) method is called instead of the [**IPortableDevicePropertiesBulk::QueueGetValuesByObjectList**](iportabledevicepropertiesbulk-queuegetvaluesbyobjectlist.md) method.


```C++
hr = pPropertiesBulk->QueueGetValuesByObjectFormat(WPD_OBJECT_FORMAT_WMA,
                                                   WPD_DEVICE_OBJECT_ID,
                                                   100,
                                                   pPropertiesToRead,
                                                   pCallback,
                                                   &amp;guidContext);
```



## Related topics

<dl> <dt>

[**IPortableDevice Interface**](iportabledevice.md)
</dt> <dt>

[**IPortableDeviceContent Interface**](iportabledevicecontent.md)
</dt> <dt>

[**IPortableDeviceKeyCollection Interface**](iportabledevicekeycollection.md)
</dt> <dt>

[**IPortableDeviceProperties Interface**](iportabledeviceproperties.md)
</dt> <dt>

[**IPortableDevicePropertiesBulk Interface**](iportabledevicepropertiesbulk.md)
</dt> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



