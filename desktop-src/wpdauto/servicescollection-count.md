---
title: servicesCollection.Count property
description: The Count property gets the number of Service objects in the collection.
ms.assetid: '13b08aec-3853-4615-b03c-ee29cee0df8d'
keywords: ["Count property WPD Automation", "Count property WPD Automation , servicesCollection object", "servicesCollection object WPD Automation , Count property"]
topic_type:
- apiref
api_name:
- servicesCollection.Count
api_type:
- COM
---

# servicesCollection.Count property

The **Count** property gets the number of **Service** objects in the collection.

This property is read-only.

## Syntax


```JScript
Count = servicesCollection.Count
```



## Property value

The read-only number of **Service** objects in the collection.

## Examples

The following JScript example uses **servicesCollection.Count** to enumerate a collection of services and access them by index.


```JScript
// Retrieve a collection of services from the device.
var services = deviceObject.Services;

// Enumerate the services in the collection and access them by index.
for (i=0; i < services.Count; i++)
{
    var aService = services[i]; 
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 





