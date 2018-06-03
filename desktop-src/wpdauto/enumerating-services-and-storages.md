---
title: Enumerating Services and Storages
description: The collections of Services and Storages on a device are accessed through the read-only Device object properties of Device.Services and Device.Storages.
ms.assetid: 06aa8bab-0530-4ddf-9006-98c01f841594
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Services and Storages

The collections of Services and Storages on a device are accessed through the read-only [**Device**](device-object.md) object properties of [**Device.Services**](device-services.md) and [**Device.Storages**](device-storages.md). These collections can be enumerated directly through these properties, or they can be extracted into [**servicesCollection**](servicescollection-object.md) and [**storagesCollection**](storagescollection-object.md) objects and enumerated separately.

## Enumerating Services

There are four ways to enumerate services: by index into a services collection, by Persistent Unique ID (PUID), by Object identifier (ObjectID), and by service type.

### Enumerating a Service by an Index into the Services Collection

Individual services in a services collection can be accessed by using a zero-based numeric index. The following examples show how to retrieve a specific service by using an index.

Retrieve a service directly from the services collection in the **Device** object by using an index.


```JScript
var aService = DeviceObject.Services[0];
```



Retrieve a separate collection of all services on a device, and then access a specific service by indexing into the collection.


```JScript
var services = DeviceObject.Services;

for (i=0; i < services.Count; i++)
{
    var aService = services[i];

    // Do something with aService.
}
```



### Enumerating a Service by PUID

A *PUID* is a string that uniquely identifies a service on the device. The PUID for a specific service can be obtained by using the WPD Automation name **ObjectPersistentUniqueID** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID**; for example:

`var servicePUID = service.ObjectPersistentUniqueID;`

The following examples show how to retrieve a specific service by using its PUID.

Retrieve a service directly from the services collection in the **Device** object by using its PUID.


```JScript
var servicePUID = DeviceObject.Services[0].ObjectPersistentUniqueId;
var service = DeviceObject.Services[servicePUID];
```



Retrieve a separate collection of all services on a device, and then access a specific service by using its PUID.


```JScript
var services = DeviceObject.Services;
var servicePUID = services[0].ObjectPersistentUniqueId;

// Any service can be accessed by using its PUID.
var service = services[servicePUID];
```



### Enumerating a Service by ObjectID

An *ObjectID* is a string that uniquely identifies a service object on the device. The ObjectId of a specific service can be obtained by using the WPD Automation name **ObjectId** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_ID**; for example:

`var serviceObjectId = service.ObjectId;`

The following example shows how to retrieve a specific service by using its ObjectID.

Retrieve a service directly from the services collection in the **Device** object by using its ObjectID.


```JScript
var objectID = DeviceObject.Services[0].ObjectId;
var service = DeviceObject.Services[objectID];
```



Retrieve a separate collection of all services on a device, and then access a specific service by using its ObjectID.


```JScript
var services = DeviceObject.Services;
var serviceID = services[0].ObjectId;

// Any service can be accessed by using its ObjectID.
var service = services[serviceID];
```



### Enumerating a Service by Service Type

The Device object also exposes the [**GetServicesByType**](device-getservicesbytype.md) method to retrieve a collection of services by Service Type. This method is useful if you do not know the PUID or ObjectID of a particular service, or if you want to create separate collections of services based on type. After you retrieve the collection with the [**GetServicesByType**](device-getservicesbytype.md) method, each item in the collection is accessed by index, as shown in the following example.

Retrieve a collection of services for a particular Service Type, and then access each item in the collection by index.


```JScript
var ringtoneServices = DeviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F60E6A9F8E}");

for (i=0; i < ringtoneServices.Count; i++)
{
    var aRingtoneService = ringtoneServices[i];

    // Do something with aRingtoneService.
}
```



## Enumerating Storages

Individual storages in the [**Device.Storages**](device-storages.md) collection or in a separate [**storagesCollection**](storagescollection-object.md) are enumerated by using a zero-based numeric index, by PUID, and by ObjectID.

### Enumerating a Storage by an Index into the Storages Collection

The following examples show how to retrieve a specific storage by using an index.

Retrieve a storage directly from the storages collection in the **Device** object by using an index.


```JScript
var aStorage = DeviceObject.Storages[0];
```



Retrieve a separate collection of all the storages on a device, and then access a specific storage by indexing into the collection.


```JScript
var storages = DeviceObject.Storages;

for (i=0; i < storages.Count; i++)
{
    var aStorage = storages[i];

    // Do something with aStorage.
}
```



### Enumerating a Storage by PUID

A *PUID* is a string that uniquely identifies a storage on the device. The PUID for a specific storage can be obtained by using the WPD Automation name **ObjectPersistentUniqueID** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID**. The following examples show how to retrieve a specific storage by using its PUID.

Retrieve a storage directly from the storages collection in the **Device** object by using its PUID.


```JScript
var storagePUID = DeviceObject.Storages[0].ObjectPersistentUniqueId;
var storage = DeviceObject.Storages[storagePUID];
```



Retrieve a separate collection of all storages on a device, and then access a specific storage by using its PUID.


```JScript
var storages = DeviceObject.Storages;
var storagePUID = storages[0].ObjectPersistentUniqueId;

// Any storage can be accessed by using its PUID.
var storage = storages[storagePUID];
```



### Enumerating a Storage by ObjectID

An *ObjectID* is a string that uniquely identifies a storage object on the device. The ObjectId of a specific storage can be obtained by using the WPD Automation name **ObjectId** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_ID**. The following example shows how to retrieve a specific storage by using its ObjectID.

Retrieve a storage directly from the storages collection in the **Device** object by using its ObjectID.


```JScript
var storageID = DeviceObject.Storages[0].ObjectId;
var storage = DeviceObject.Storages[objectID];
```



Retrieve a separate collection of all storages on a device, and then access a specific storage by using its ObjectID.


```JScript
var storages = DeviceObject.Storages;
var storageID = storages[0].ObjectId;

// Any storage can be accessed by using its ObjectID.
var storage = storages[storageID];
```



## Related topics

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**storagesCollection Object**](storagescollection-object.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




