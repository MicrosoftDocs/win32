---
title: Service.onAddChildComplete event
description: The onAddChildComplete event occurs, and a callback handler is invoked, when a Service.AddChild operation has completed.
ms.assetid: 8c87c5c5-df7e-483b-adec-a38156698f90
keywords:
- onAddChildComplete event WPD Automation
- onAddChildComplete event WPD Automation , Service object
- Service object WPD Automation , onAddChildComplete event
topic_type:
- apiref
api_name:
- Service.onAddChildComplete
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.onAddChildComplete event

The **onAddChildComplete** event occurs, and a callback handler is invoked, when a [**Service.AddChild**](service-addchild.md) operation has completed.

## Syntax


```JScript
Service.onAddChildComplete(
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

To enable asynchronous behavior, set the handler for this event before calling the [**Service.AddChild**](service-addchild.md) method.

## Examples

The following code shows the handler-function syntax for the **onAddChildComplete** event.


```JScript
function HandlerFunction(hrStatus, childObject)
{

   // Code to handle a completed asynchronous AddChild operation.             

}

// Set the event handler.
Service.onAddChildComplete = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





