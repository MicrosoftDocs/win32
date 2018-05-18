---
title: About the Service Object
description: The Service object represents a device service, and provides access to all of the properties, methods, events, and content exposed by that service.
ms.assetid: '035edd34-75e9-4edd-8785-66021380070c'
keywords: ["WPD Automation,WPDObject", "WPD Automation,Service object", "WPD Automation,CreateNewObject", "WPDObject,WPD Automation", "WPDObject,Service object", "Service object,about", "Service object,WPD Automation", "Service object,WPDObject", "Service object,CreateNewObject", "CreateNewObject"]
---

# About the Service Object

The [**Service**](service-object.md) object represents a device service, and provides access to all of the properties, methods, events, and content exposed by that service.

WPD Automation defines a minimum set of properties (see [**WpdProperty**](service-wpdproperty.md)) for each **Service** object. The full set of properties, methods, and events for a **Service** object depends entirely on the service definition of the service that it represents.

Any service-defined property (or ServiceProperty in WPD Automation) can be accessed by its name, as specified in the service definition. For more information and an example, see [**ServiceProperty**](service-serviceproperty.md).

Service-defined methods and events can also be accessed by their defined names. For an example of how to invoke a service-defined method, see [Invoking a Service-Defined Method](invoking-a-service-defined-method.md). For information about working with service-defined events, see [Handling Service-Defined Events](handling-service-defined-events.md).

The **Service** object inherits the common object functionality included in the properties, methods, and events of the [**WPDObject**](wpdobject.md). This means that a **Service** object can create new **Service** objects by calling the [**CreateNewObject**](service-createnewobject.md) method, add objects to its collection of child objects by calling the [**WPDObject.AddChild**](wpdobject-addchild.md) method, and remove child objects from its collection by calling the [**WPDObject.RemoveChild**](service-removechild.md) method.

A **Service** object can be retrieved from the collection of all services on a [**Device Object**](device-object.md) by a zero-based numeric index, by a Persistent Unique ID (PUID), by an Object identifier (ObjectID), or by Service Type, as shown in the following code.


```JScript
// Retrieve a service object by index.
var serviceObject = deviceObject.Services[Index];

// Get the PUID of a service object by index,
// and then retrieve a service object by PUID.
var servicePUID = deviceObject.Services[0].ObjectPersistentUniqueId;
var serviceObject = deviceObject.Services[servicePUID];

// Get the ObjectID of a service object by index,
// and then retrieve a service object by ObjectID.
var serviceObjectID = deviceObject.Services[0].ObjectId;
var serviceObject = deviceObject.Services[serviceObjectID];

// Retrieve a serviceCollection of service objects by service type, 
// and then retrieve a service object from the collection by index.
var coolServicesCollection = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F60E6A9F8E}");
var serviceObject = coolServicesCollection[Index];
```



## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Services Collection**](servicescollection-object.md)
</dt> <dt>

[**WPDObject**](servicescollection-object.md)
</dt> </dl>

 

 




