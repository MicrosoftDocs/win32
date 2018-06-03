---
title: Service.onObjectUpdated event
description: The onObjectUpdated event occurs after an object has been updated on this Service object.
ms.assetid: 25b8dfe2-f6d9-4e06-a4eb-0b579a09e0f7
keywords:
- onObjectUpdated event WPD Automation
- onObjectUpdated event WPD Automation , Service object
- Service object WPD Automation , onObjectUpdated event
topic_type:
- apiref
api_name:
- Service.onObjectUpdated
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.onObjectUpdated event

The **onObjectUpdated** event occurs after an object has been updated on this **Service** object.

## Syntax


```JScript
Service.onObjectUpdated(
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
Service.onObjectUpdated = HandlerFunction;
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

 

 





