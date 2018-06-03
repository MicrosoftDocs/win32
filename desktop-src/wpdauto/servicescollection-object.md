---
title: servicesCollection object
description: The servicesCollection object represents a collection of Service objects.
ms.assetid: d5acc839-f675-4e31-88f5-d07bb36c668c
keywords:
- servicesCollection object WPD Automation
- servicesCollection object WPD Automation , described
topic_type:
- apiref
api_name:
- servicesCollection
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# servicesCollection object

The **servicesCollection** object represents a collection of **Service** objects.

## Members

The **servicesCollection** object has these types of members:

-   [Properties](#properties)

### Properties

The **servicesCollection** object has these properties.



| Property                                             | Access type          | Description                                                          |
|:-----------------------------------------------------|:---------------------|:---------------------------------------------------------------------|
| [**Count**](servicescollection-count.md)<br/> | Read-only<br/> | Gets the number of **Service** objects in the collection.<br/> |



 

## Remarks

A **servicesCollection** object that contains all of the services on a device can be accessed through the [**Device.Services**](device-services.md) property. Specific services in the **Device.Services** collection can be retrieved by using either a zero-based numeric index or a Service Persistent Unique ID (PUID).

A **servicesCollection** object that is filtered by service type can be retrieved using the [**Device.GetServicesByType**](device-getservicesbytype.md) method. The services in a **servicesCollection** obtained from this method can only be accessed by a zero-based numeric index.

## Examples

The following JScript example shows how to create a **servicesCollection** and enumerate the services in the collection, accessing them by index.


```JScript
// Retrieve a collection of services from the device.
var services = deviceObject.GetServicesByType("ServiceTypeGUID");

// Enumerate the services in the collection and access them by index.
for (i=0; i < services.Count; i++)
{
    var aService = services[i]; 
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the servicesCollection and storagesCollection Objects](about-the-servicescollection-and-storagescollection-objects.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> </dl>

 

 





