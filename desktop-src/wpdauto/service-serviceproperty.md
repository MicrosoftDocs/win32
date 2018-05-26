---
title: Service.ServiceProperty property
description: The ServiceProperty property gets or sets a service-defined property of this Service object.
ms.assetid: c26dee9c-9349-4390-bc06-a95ba024783f
keywords:
- ServiceProperty property WPD Automation
- ServiceProperty property WPD Automation , Service object
- Service object WPD Automation , ServiceProperty property
topic_type:
- apiref
api_name:
- Service.ServiceProperty
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service.ServiceProperty property

The ***ServiceProperty*** property gets or sets a service-defined property of this **Service** object.

This property is read/write.

## Syntax


```JScript
ServiceProperty = Service.ServiceProperty
Service.ServiceProperty = ServiceProperty
```



## Property value

This property has the same value as the service-defined property that it is reading from or writing to.

## Examples

The following JScript example demonstrates how to get and set a service-defined property.


```JScript
var service = deviceObject.Services[ServicePUID];

// Retrieve a value from a service-defined property.
var someValue = service.someServiceProperty;

// Set the service-defined property to a new value.
service.someServiceProperty = newValue;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 





