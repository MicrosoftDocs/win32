---
title: Storage.onObjectUpdated event
description: The onObjectUpdated event occurs after an object has been updated on this Storage object.
ms.assetid: cecbce01-a9f2-4af3-aaa4-d43cb7c5513a
keywords:
- onObjectUpdated event WPD Automation
- onObjectUpdated event WPD Automation , Storage object
- Storage object WPD Automation , onObjectUpdated event
topic_type:
- apiref
api_name:
- Storage.onObjectUpdated
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Storage.onObjectUpdated event

The **onObjectUpdated** event occurs after an object has been updated on this **Storage** object.

## Syntax


```JScript
Storage.onObjectUpdated(
  wpdObject
)
```



## Parameters

<dl> <dt>

*wpdObject* 
</dt> <dd>

The **WPDObject** that was updated.

</dd> </dl>

## Return value

This event does not return a value.

## Examples

The following code shows the handler-function syntax for the **onObjectUpdated** event.


```JScript
function HandlerFunction(wpdObject)
{

   // Code to handle the updated object.

}

// Set the event handler.
Storage.onObjectUpdated = HandlerFunction;
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

 

 





