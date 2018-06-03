---
title: Service.onServiceEventName event
description: The name and occurrence of this event are defined by the service.
ms.assetid: 59f94a3f-7eac-4231-b3dc-d85e29e254c5
keywords:
- onServiceEventName event WPD Automation
- onServiceEventName event WPD Automation , Service object
- Service object WPD Automation , onServiceEventName event
topic_type:
- apiref
api_name:
- Service.onServiceEventName
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.onServiceEventName event

The name and occurrence of this event are defined by the service. For example, if a service defines an event with the name *SomethingHappened*, WPD Automation will expose an event handler called **service***.onSomethingHappened*. You can assign a JScript function to the event handler to be notified whenever this event is raised. The event parameters will also be passed into the script-defined function, and should match the parameters defined by the service for that event.

## Syntax


```JScript
Service.onServiceEventName(
  EventParameters
)
```



## Parameters

<dl> <dt>

*EventParameters* 
</dt> <dd>

Defined by the service.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Any events that are defined by a service can be accessed through the **Service** object that represents that service.

## Examples

The following code shows the handler-function syntax for the *onServiceEventName* event. In this example, the name of the service-defined event is *SomethingHappened*.


```JScript
function HandlerFunction(EventParameters)
{

   // Code to handle the event.

}

// Set the event handler.
Service.onSomethingHappened = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 





