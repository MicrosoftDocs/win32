---
title: Storage.onObjectRemoved event
description: The onObjectRemoved event occurs after an object has been removed from this Storage object.
ms.assetid: 'f6640f2b-2f91-47ea-822a-3ee6d5c2376d'
keywords: ["onObjectRemoved event WPD Automation", "onObjectRemoved event WPD Automation , Storage object", "Storage object WPD Automation , onObjectRemoved event"]
topic_type:
- apiref
api_name:
- Storage.onObjectRemoved
api_type:
- COM
---

# Storage.onObjectRemoved event

The **onObjectRemoved** event occurs after an object has been removed from this **Storage** object.

## Syntax


```JScript
Storage.onObjectRemoved(
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
Storage.onObjectRemoved = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





