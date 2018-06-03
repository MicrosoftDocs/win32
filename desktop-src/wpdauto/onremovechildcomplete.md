---
title: WPDObject.onRemoveChildComplete event
description: The onRemoveChildComplete event occurs, and a callback handler is invoked, when a RemoveChild operation has completed.
ms.assetid: 1e7a6dc5-0c46-4d34-8ecc-0c9f80c399d6
keywords:
- onRemoveChildComplete event WPD Automation
- onRemoveChildComplete event WPD Automation , WPDObject property
- WPDObject property WPD Automation , onRemoveChildComplete event
topic_type:
- apiref
api_name:
- WPDObject.onRemoveChildComplete
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPDObject.onRemoveChildComplete event

The **onRemoveChildComplete** event occurs, and a callback handler is invoked, when a [**RemoveChild**](wpdobject-removechild.md) operation has completed.

## Syntax


```JScript
WPDObject.onRemoveChildComplete(
  hrStatus,
  childPUID
)
```



## Parameters

<dl> <dt>

*hrStatus* 
</dt> <dd>

Contains the overall status of the remove operation (success or failure).

</dd> <dt>

*childPUID* 
</dt> <dd>

The Persistent Unique ID (PUID) of the child **WPDObject** that was removed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for this event before calling the [**RemoveChild**](wpdobject-removechild.md) method.

## Examples

The following code shows the handler-function syntax for the **onRemoveChildComplete** event.


```JScript
function HandlerFunction(hrStatus, childPUID)
{

   // Code to handle a completed asynchronous RemoveChild operation.             

}

// Set the event handler.
WPDObject.onRemoveChildComplete = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





