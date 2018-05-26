---
title: About the servicesCollection and storagesCollection Objects
description: The Device object makes available the Services and Storages properties that provide access to a servicesCollection that contains all of the services on a device, and a storagesCollection that contains all of the storages on a device.
ms.assetid: 8bd864a5-068a-47f7-9483-cf64406c5f02
keywords:
- WPD Automation,Device object
- WPD Automation,servicesCollection object
- WPD Automation,storagesCollection object
- WPD Automation,Services properties
- WPD Automation,Storages properties
- WPD Automation,GetServicesByType method
- Device object
- servicesCollection object
- storagesCollection object
- Storages properties
- Services properties
- GetServicesByType
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the servicesCollection and storagesCollection Objects

The [**Device**](device-object.md) object makes available the [**Services**](device-services.md) and [**Storages**](device-storages.md) properties that provide access to a [**servicesCollection**](servicescollection-object.md) that contains all of the services on a device, and a [**storagesCollection**](storagescollection-object.md) that contains all of the storages on a device.

These collection objects are used to enumerate the services and storages on the device so that individual [**Service**](service-object.md) or [**Storage**](storage-object.md) objects can be retrieved. Both of these collection objects provide a [**Count**](storagescollection-count.md) property that returns the number of objects in the collection. The [**Count**](storagescollection-count.md) property also provides a way to index into the collection to retrieve a specific object.

The **servicesCollection** object contains all of the services on a device. The **servicesCollection** object can be accessed through the [**Services**](device-services.md) property of the **Device** object. Specific services in the collection can be retrieved by using a zero-based numeric index, or by using a service Persistent Unique ID (PUID). A *PUID* is a GUID represented in string form that uniquely identifies a service object on a device.

A **servicesCollection** object that is filtered by service type can be retrieved by using the [**GetServicesByType**](device-getservicesbytype.md) method. The services in a **servicesCollection** obtained from this method can be accessed only by zero-based numeric index.

A **storagesCollection** object contains all of the storages on a device. A **storagesCollection** object can be accessed through the [**Storages**](device-storages.md) property. Specific storages in a **storagesCollection** can be retrieved by using a zero-based numeric index or a PUID.

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**storagesCollection Object**](servicescollection-object.md)
</dt> </dl>

 

 




