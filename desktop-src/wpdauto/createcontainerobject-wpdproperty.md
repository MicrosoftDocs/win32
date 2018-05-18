---
title: createContainer.WpdProperty property
description: The WpdProperty sets the value of a predefined WPD property on this Creation Container object.
ms.assetid: '0cf19f3f-882c-4ec8-80f6-1f31bb0ed3fa'
keywords: ["WpdProperty property WPD Automation", "WpdProperty property WPD Automation , createContainer object", "createContainer object WPD Automation , WpdProperty property"]
topic_type:
- apiref
api_name:
- createContainer.WpdProperty
api_type:
- COM
---

# createContainer.WpdProperty property

The **WpdProperty** sets the value of a predefined WPD property on this [**Creation Container**](creation-container-object.md) object.

This property is write-only.

## Syntax


```JScript
createContainer.WpdProperty = WpdProperty
```



## Property value

This property has the same name as the predefined WPD property.

## Remarks

For a list of the minimum required set of predefined WPD properties for a **Service Object**, see [**Service.WpdProperty**](service-wpdproperty.md); and for a **Storage Object**, see [**Storage.WpdProperty**](storage-wpdproperty.md).

## Examples

The following JScript example uses the **WpdProperty** property to set the value of a predefined WPD property on a [**Creation Container**](creation-container-object.md) object.


```JScript
var createContainer = serviceObject.CreateNewObject("Mp3");

createContainer.ObjectName = "My Object Name";
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





