---
title: Service.WpdProperty property
description: The WpdProperty property gets or sets a predefined WPD property for this Service object.
ms.assetid: 4a9d37e3-ea68-4c24-b550-711898a9ae99
keywords:
- WpdProperty property WPD Automation
- WpdProperty property WPD Automation , Service object
- Service object WPD Automation , WpdProperty property
topic_type:
- apiref
api_name:
- Service.WpdProperty
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.WpdProperty property

The **WpdProperty** property gets or sets a predefined WPD property for this **Service** object.

This property is read/write.

## Syntax


```JScript
WpdProperty = Service.WpdProperty
Service.WpdProperty = WpdProperty
```



## Property value

This property has the same value as the predefined WPD property that is being read from or written to.

## Remarks

The following table contains the minimum required set of predefined WPD properties for a **Service Object**. The properties are accessed by the WPD Automation name that corresponds to the WPD PROPERTYKEY. For example, the WPD-defined property WPD\_OBJECT\_NAME would be accessed like this: `service.ObjectName`.

For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).



| WPD PROPERTYKEY                     | WPD Automation Name      |
|-------------------------------------|--------------------------|
| WPD\_OBJECT\_ID                     | ObjectId                 |
| WPD\_OBJECT\_NAME                   | ObjectName               |
| WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID | ObjectPersistentUniqueId |
| WPD\_OBJECT\_FORMAT                 | ObjectFormat             |
| WPD\_FUNCTIONAL\_OBJECT\_CATEGORY   | FunctionalObjectCategory |
| WPD\_SERVICE\_VERSION               | ServiceVersion           |



 

## Examples

The following JScript example demonstrates how to get and set the predefined *WPDProperty* "ServiceVersion".


```JScript
var service = deviceObject.Services[ServicePUID];

// Get a value from the predefined WPD property "ServiceVersion".
// Notice that the property is called by using the Property Name, 
// not the WPD PROPERTYKEY. 
var serviceVersion = service.ServiceVersion;

// Set the WPD property to a new value.
service.ServiceVersion = "New Service Version";
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

 

 





