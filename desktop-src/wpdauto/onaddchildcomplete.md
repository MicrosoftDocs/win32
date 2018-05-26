---
title: WPDObject.onAddChildComplete event
description: The onAddChildComplete event occurs, and a callback handler is invoked, when an AddChild operation has completed.
ms.assetid: 957a7af2-a57a-4597-8282-fc8cb19d26af
keywords:
- onAddChildComplete event WPD Automation
- onAddChildComplete event WPD Automation , WPDObject object
- WPDObject object WPD Automation , onAddChildComplete event
topic_type:
- apiref
api_name:
- WPDObject.onAddChildComplete
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPDObject.onAddChildComplete event

The **onAddChildComplete** event occurs, and a callback handler is invoked, when an [**AddChild**](wpdobject-addchild.md) operation has completed.

## Syntax


```JScript
WPDObject.onAddChildComplete(
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

To enable asynchronous behavior, set the handler for this event before calling the [**AddChild**](wpdobject-addchild.md) method.

## Examples

The following code shows the handler-function syntax for the **onAddChildComplete** event.


```JScript
function HandlerFunction(hrStatus, childObject)
{

   // Code to handle a completed asynchronous AddChild operation.             

}

// Set the event handler.
WPDObject.onAddChildComplete = HandlerFunction;
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

 

 





