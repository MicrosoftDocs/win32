---
title: Service.onRemoveChildComplete event
description: The onRemoveChildComplete event occurs, and a callback handler is invoked, when a Service.RemoveChild operation has completed.
ms.assetid: dbfe722f-5b38-417b-8b7e-fdcb9fe53d61
keywords:
- onRemoveChildComplete event WPD Automation
- onRemoveChildComplete event WPD Automation , Service object
- Service object WPD Automation , onRemoveChildComplete event
topic_type:
- apiref
api_name:
- Service.onRemoveChildComplete
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.onRemoveChildComplete event

The **onRemoveChildComplete** event occurs, and a callback handler is invoked, when a [**Service.RemoveChild**](service-removechild.md) operation has completed.

## Syntax


```JScript
Service.onRemoveChildComplete(
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

To enable asynchronous behavior, set the handler for this event before calling the [**Service.RemoveChild**](service-removechild.md) method.

## Examples

The following code shows the handler-function syntax for the **onRemoveChildComplete** event.


```JScript
function HandlerFunction(hrStatus, childPUID)
{

   // Code to handle a completed asynchronous RemoveChild operation.             

}

// Set the event handler.
Service.onRemoveChildComplete = HandlerFunction;
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

 

 





