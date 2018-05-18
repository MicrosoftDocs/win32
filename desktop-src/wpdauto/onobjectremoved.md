---
title: Service.onObjectRemoved event
description: The onObjectRemoved event occurs after an object has been removed from this Service object.
ms.assetid: '1d82d1a8-3137-42a5-aa0d-37fe9659ec5b'
keywords: ["onObjectRemoved event WPD Automation", "onObjectRemoved event WPD Automation , Service object", "Service object WPD Automation , onObjectRemoved event"]
topic_type:
- apiref
api_name:
- Service.onObjectRemoved
api_type:
- COM
---

# Service.onObjectRemoved event

The **onObjectRemoved** event occurs after an object has been removed from this **Service** object.

## Syntax


```JScript
Service.onObjectRemoved(
  removedObjectPUID,
  parentWpdObject
)
```



## Parameters

<dl> <dt>

*removedObjectPUID* 
</dt> <dd>

The Persistent Unique ID (PUID) of the object that was removed.

</dd> <dt>

*parentWpdObject* 
</dt> <dd>

The parent **WPDObject** of the object that was removed.

</dd> </dl>

## Return value

This event does not return a value.

## Examples

The following code shows the handler-function syntax for the **onObjectRemoved** event.


```JScript
function HandlerFunction(removedObjectPUID, parentWpdObject)
{

   // Code to handle the removed object.

}

// Set the event handler.
Service.onObjectRemoved = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





