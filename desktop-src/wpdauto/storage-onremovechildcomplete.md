---
title: Storage.onRemoveChildComplete event
description: The onRemoveChildComplete event occurs, and a callback handler is invoked, when a Storage.RemoveChild operation has completed.
ms.assetid: '84227932-2ed6-4daa-8e35-76c051ef16c1'
keywords: ["onRemoveChildComplete event WPD Automation", "onRemoveChildComplete event WPD Automation , Storage object", "Storage object WPD Automation , onRemoveChildComplete event"]
topic_type:
- apiref
api_name:
- Storage.onRemoveChildComplete
api_type:
- COM
---

# Storage.onRemoveChildComplete event

The **onRemoveChildComplete** event occurs, and a callback handler is invoked, when a [**Storage.RemoveChild**](storage-removechild.md) operation has completed.

## Syntax


```JScript
Storage.onRemoveChildComplete(
  hrStatus,
  childPUID
)
```



## Parameters

<dl> <dt>

*hrStatus* 
</dt> <dd>

Contains the overall status of the delete operation (success or failure).

</dd> <dt>

*childPUID* 
</dt> <dd>

The Persistent Unique ID (PUID) of the child **WPDObject** that was removed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for this event before calling the [**Storage.RemoveChild**](storage-removechild.md) method.

## Examples

The following code shows the handler-function syntax for the **onRemoveChildComplete** event.


```JScript
function HandlerFunction(hrStatus, childPUID)
{

   // Code to handle a completed asynchronous RemoveChild operation.             

}

// Set the event handler.
Storage.onRemoveChildComplete = HandlerFunction;
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

 

 





