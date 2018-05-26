---
Description: Retrieving Properties for Multiple Objects by Object Format
ms.assetid: c3f5edfd-8a6a-4bbd-9787-a4268c38f18f
title: Retrieving Properties for Multiple Objects by Object Format
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Properties for Multiple Objects by Object Format

In addition to a bulk retrieval of properties for a collection of object identifiers, an application can also perform a bulk retrieval of properties for all objects of a particular type. As in the previous example, bulk retrieval for a given type requires that the device driver support bulk retrievals.

Your application can perform a bulk retrieval using the interfaces described in the following table.



| Interface                                                                                      | Description                                                        |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [**IPortableDeviceContent Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master)                             | Provides access to the content-specific methods.                   |
| [**IPortableDeviceKeyCollection Interface**](iportabledevicekeycollection.md)                 | Used to identify the properties to be retrieved.                   |
| [**IPortableDeviceProperties Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master)                       | Used to determine whether a given driver supports bulk operations. |
| [**IPortableDevicePropertiesBulk Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulk?branch=master)               | Supports the bulk retrieval operation.                             |
| [**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md) | Used to store the object identifiers for the bulk operation.       |



 

The ReadContentPropertiesBulkFilteringFormat function in the sample application's ContentProperties.cpp module demonstrates a bulk retrieval operation for objects of a particular type or format.

The code found in the ReadContentPropertiesBulkFilteringFormat function is almost identical to the code found in the ReadContentPropertiesBulk function. (See the [Retrieving Properties for Multiple Objects](retrieving-properties-for-multiple-objects.md) topic for a complete description of this function.)

The one primary difference occurs when the operation is queued. When filtering by type or format, the [**IPortableDevicePropertiesBulk::QueueGetValuesByObjectFormat**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicepropertiesbulk-queuegetvaluesbyobjectformat?branch=master) method is called instead of the [**IPortableDevicePropertiesBulk::QueueGetValuesByObjectList**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicepropertiesbulk-queuegetvaluesbyobjectlist?branch=master) method.


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

[**IPortableDevice Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevice?branch=master)
</dt> <dt>

[**IPortableDeviceContent Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master)
</dt> <dt>

[**IPortableDeviceKeyCollection Interface**](iportabledevicekeycollection.md)
</dt> <dt>

[**IPortableDeviceProperties Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master)
</dt> <dt>

[**IPortableDevicePropertiesBulk Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulk?branch=master)
</dt> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



