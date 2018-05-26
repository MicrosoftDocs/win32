---
title: About the Storage Object
description: The Storage object is bound at runtime to represent a given legacy storage on a device. It provides access to all of the properties and content exposed by that storage.
ms.assetid: 85ab290a-16f5-49cd-9ee4-ee640604f855
keywords:
- WPD Automation,WPDObject
- WPD Automation,Storage object
- WPD Automation,CreateNewObject
- WPD Automation,storagesCollection
- WPDObject,WPD Automation
- WPDObject,Service object
- Storage object,about
- Storage object,WPD Automation
- Storage object,WPDObject
- Storage object,CreateNewObject
- Storage object,storagesCollection
- CreateNewObject
- storagesCollection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the Storage Object

The [**Storage**](storage-object.md) object is bound at runtime to represent a given legacy storage on a device. It provides access to all of the properties and content exposed by that storage.

WPD Automation defines a minimum set of properties for each **Storage** object. The properties can be accessed by their names; see the [**WpdProperty**](storage-wpdproperty.md) reference page for a list. The full set of properties for a **Storage** object depends on the storage it represents and how that storage is defined for a particular device.

The **Storage** object inherits the common object functionality included in the properties, methods, and events of the [**WPDObject**](wpdobject.md). This means that a **Storage** object can create new **Storage** objects by using the [**CreateNewObject**](storage-createnewobject.md) method, add objects to its collection of child objects (accessed through its [**Children**](storage-children.md) property) by using the [**WPDObject.AddChild**](wpdobject-addchild.md) method, and can remove child objects from its collection by using the [**WPDObject.RemoveChild**](service-removechild.md) method.

A **Storage** object is retrieved by using a zero-based numeric index into [**Device.Storages**](device-storages.md), which is a [**storagesCollection**](storagescollection-object.md) object that contains all of the storages on the device. A **Storage** object can also be retrieved by a Persistent Unique ID (PUID), or by an Object identifier (ObjectID). For more information on retrieving the PUID or ObjectID for an object, see [Enumerating Services and Storages](enumerating-services-and-storages.md).

The following code shows all three methods for retrieving a **Storage** object.


```JScript
// Retrieve a storage object by index.
var storageObject = deviceObject.Storages[0];

// Get the PUID of a storage object by index,
// and then retrieve a storage object by PUID.
var storagePUID = deviceObject.Storages[0].ObjectPersistentUniqueId;
var storageObject = deviceObject.Storages[storagePUID];

// Get the ObjectID of a storage object by index,
// and then retrieve a storage object by ObjectID.
var storageObjectID = deviceObject.Storages[0].ObjectId;
var storageObject = deviceObject.Storages[storageObjectID];
```



## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[Enumerating Services and Storages](enumerating-services-and-storages.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**storagesCollection Object**](storagescollection-object.md)
</dt> <dt>

[**WPDObject**](servicescollection-object.md)
</dt> </dl>

 

 




