---
title: About the WPDObject
description: The WPDObject represents a generic object on a device.
ms.assetid: 5a152279-8d95-4ca3-bf08-8ce6ff2178f9
keywords:
- WPD Automation,WPDObject
- WPD Automation,Service object
- WPD Automation,Storage object
- WPD Automation,childrenCollection
- WPDObject,WPD Automation
- WPDObject,about
- Service object,WPD Automation
- Storage object,WPD Automation
- Service object,WPDObject
- Storage object,WPDObject
- childrenCollection,WPD Automation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the WPDObject

The [**WPDObject**](wpdobject.md) represents a generic object on a device.

The [**Service**](service-object.md) object and the [**Storage**](storage-object.md) object both inherit their functionality from **WPDObject**. This common functionality includes the ability to create, add and remove child objects from an internal collection of children; completion events that occur when children are added or removed; and support for any WPD Automation-defined properties. WPD Automation defines a minimum set of properties for a **WPDObject**, which can be accessed by their names. For a list of these properties, see [**WpdProperty**](wpdobject-wpdproperty.md).

In WPD Automation, a **WPDObject** always exists as one of two specialized types: a **Service** object or a **Storage** object. The **WPDObject** provides the [**Service**](wpdobject-service.md) and [**Storage**](wpdobject-storage.md) properties so that objects of these types that are contained in the [**childrenCollection**](childrencollection-object.md) of objects can determine which parent objects they belong to.

For a reference of the properties, methods, and events of the **WPDObject**, see [**WPDObject**](servicescollection-object.md). For examples of how to use the methods, properties, and events of the **WPDObject**, see the reference pages for the [**Service Object**](service-object.md) and the [**Storage Object**](storage-object.md).

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](servicescollection-object.md)
</dt> </dl>

 

 




