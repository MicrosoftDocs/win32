---
title: Device.Services property
description: The Services property provides read-only access to a collection of all the services on the device.
ms.assetid: cee13298-19f0-466b-8948-9b69c7128072
keywords:
- Services property WPD Automation
- Services property WPD Automation , Device object
- Device object WPD Automation , Services property
topic_type:
- apiref
api_name:
- Device.Services
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device.Services property

The **Services** property provides read-only access to a collection of all the services on the device.

This property is read-only.

## Syntax


```JScript
Services = Device.Services
```



## Property value

Read-only **servicesCollection** object.

## Remarks

The **servicesCollection** returned by the **Services** property can be accessed in three ways: by using a zero-based index, by using a Service Persistent Unique ID (PUID), and by using an Object Identifier (ObjectId).

The following code shows a **servicesCollection** accessed by using a zero-based numeric index.


```JScript
var service = deviceObject.Services[0];
```



If the numeric index value is greater than or equal to the value returned by [**servicesCollection.Count**](servicescollection-count.md), a JScript exception will be thrown.

In the following code, a Service PUID is used to access the **servicesCollection**.


```JScript
var service = deviceObject.Services[servicePUID];
```



The Service PUID for a specific service can be obtained by using the WPD Automation name **ObjectPersistentUniqueID** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID**; as in the following example:


```JScript
var servicePUID = service.ObjectPersistentUniqueID;
```



For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).

Using a Service PUID to access a service collection is valid only for a collection obtained from the **Services** property. This is because a collection obtained from the [**Device.GetServicesByType**](device-getservicesbytype.md) method is already filtered by service type.

The ObjectId of a specific service can be obtained by using the WPD Automation name **ObjectId** that corresponds to the WPD PROPERTYKEY **WPD\_OBJECT\_ID** as in the following example:


```JScript
var serviceObjectId = service.ObjectId;
```



For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).

## Examples

The following JScript example uses the **Services** property to access the collection of all services on a **Device** object and then shows retrieving a service from the collection by using a numeric index, a Service PUID, and by using an ObjectId.


```JScript
// The service object serviceByIndex is obtained using
// the index value 0.
var serviceByIndex = deviceObject.Services[0];

// The Service PUID of serviceByIndex is read using the
// ObjectPersistentUniqueID property.  
var servicePUID = serviceByIndex.ObjectPersistentUniqueID;

// The service object serviceByPUID, which is identical to
// the serviceByIndex object, is obtained by using the
// Service PUID of serviceByIndex. 
var serviceByPUID = deviceObject.Services[servicePUID];

// The ObjectId of serviceByIndex is read using the ObjectID
// property.
var serviceObjectId = serviceByIndex.ObjectId;

// The service object serviceByObjectId, which is identical to
// the serviceByIndex object, is obtained by using the ObjectId
// of serviceByIndex.
var serviceByObjectId = deviceObject.Services[serviceObjectId];
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> </dl>

 

 





