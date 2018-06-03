---
title: Storage.onGetChildrenByFormatComplete event
description: The onGetChildrenByFormatComplete event occurs, and a callback handler is invoked, when a Storage.GetChildrenByFormat method operation has completed.
ms.assetid: 8cf8d353-6de2-4107-9b9d-c62e7da2a2fe
keywords:
- onGetChildrenByFormatComplete event WPD Automation
- onGetChildrenByFormatComplete event WPD Automation , Storage object
- Storage object WPD Automation , onGetChildrenByFormatComplete event
topic_type:
- apiref
api_name:
- Storage.onGetChildrenByFormatComplete
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storage.onGetChildrenByFormatComplete event

The **onGetChildrenByFormatComplete** event occurs, and a callback handler is invoked, when a [**Storage.GetChildrenByFormat**](storage-getchildrenbyformat.md) method operation has completed.

## Syntax


```JScript
Storage.onGetChildrenByFormatComplete(
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

Contains the child objects returned by the **Storage.GetChildrenByFormat** method. If no children match the requested formats in the **Storage.GetChildrenByFormat** method operation, this collection will be empty.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for this event before calling the [**Storage.GetChildrenByFormat**](storage-getchildrenbyformat.md) method.

## Examples

The following code shows the handler-function syntax for the **onGetChildrenByFormatComplete** event.


```JScript
function HandlerFunction(hrStatus, childrenCollection)
{

   // Code to handle a completed asynchronous
   // GetChildrenByFormat operation.           

}

// Set the event handler.
Storage.onGetChildrenByFormatComplete = HandlerFunction;
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

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





