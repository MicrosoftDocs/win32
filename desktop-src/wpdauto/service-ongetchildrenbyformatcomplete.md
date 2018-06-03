---
title: Service.onGetChildrenByFormatComplete event
description: The onGetChildrenByFormatComplete event occurs, and a callback handler is invoked, when a Service.GetChildrenByFormat method operation is completed.
ms.assetid: 8c185284-d3b2-4074-af55-2544f1f81aeb
keywords:
- onGetChildrenByFormatComplete event WPD Automation
- onGetChildrenByFormatComplete event WPD Automation , Service object
- Service object WPD Automation , onGetChildrenByFormatComplete event
topic_type:
- apiref
api_name:
- Service.onGetChildrenByFormatComplete
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.onGetChildrenByFormatComplete event

The **onGetChildrenByFormatComplete** event occurs, and a callback handler is invoked, when a [**Service.GetChildrenByFormat**](service-getchildrenbyformat.md) method operation is completed.

## Syntax


```JScript
Service.onGetChildrenByFormatComplete(
  hrStatus,
  childrenCollection
)
```



## Parameters

<dl> <dt>

*hrStatus* 
</dt> <dd>

Contains the overall status of the enumeration operation (success or failure).

</dd> <dt>

*childrenCollection* 
</dt> <dd>

Contains the child objects returned by the **Service.GetChildrenByFormat** method. If no children match the requested formats in the **Service.GetChildrenByFormat** method operation, this collection will be empty.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for this event before calling the **Service.GetChildrenByFormat** method.

## Examples

The following code shows the handler-function syntax for the **onGetChildrenByFormatComplete** event.


```JScript
function HandlerFunction(hrStatus, childrenCollection)
{

   // Code to handle a completed asynchronous GetChildrenByFormat operation.              

}

// Set the event handler.
Service.onGetChildrenByFormatComplete = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





