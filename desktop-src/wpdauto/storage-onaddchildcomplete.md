---
title: Storage.onAddChildComplete event
description: The onAddChildComplete event occurs, and a callback handler is invoked, when a Storage.AddChild operation has completed.
ms.assetid: 5b76c6ee-16a9-4927-bccf-affc35f3af31
keywords:
- onAddChildComplete event WPD Automation
- onAddChildComplete event WPD Automation , Storage object
- Storage object WPD Automation , onAddChildComplete event
topic_type:
- apiref
api_name:
- Storage.onAddChildComplete
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storage.onAddChildComplete event

The **onAddChildComplete** event occurs, and a callback handler is invoked, when a [**Storage.AddChild**](storage-addchild.md) operation has completed.

## Syntax


```JScript
Storage.onAddChildComplete(
  hrStatus,
  childObject
)
```



## Parameters

<dl> <dt>

*hrStatus* 
</dt> <dd>

Contains the overall status of the add operation (success or failure).

</dd> <dt>

*childObject* 
</dt> <dd>

A reference to the newly added child **WPDObject**.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for this event before calling the [**Storage.AddChild**](storage-addchild.md) method.

## Examples

The following code shows the handler-function syntax for the **onAddChildComplete** event.


```JScript
function HandlerFunction(hrStatus, childObject)
{

   // Code to handle a completed asynchronous AddChild operation.             

}

// Set the event handler.
Storage.onAddChildComplete = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





