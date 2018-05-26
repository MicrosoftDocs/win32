---
title: Service.onObjectAdded event
description: The onObjectAdded event occurs after an object has been added to this Service object.
ms.assetid: 2c8ca65a-c4e0-434e-9d64-1496399fe813
keywords:
- onObjectAdded event WPD Automation
- onObjectAdded event WPD Automation , Service object
- Service object WPD Automation , onObjectAdded event
topic_type:
- apiref
api_name:
- Service.onObjectAdded
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service.onObjectAdded event

The **onObjectAdded** event occurs after an object has been added to this **Service** object.

## Syntax


```JScript
Service.onObjectAdded(
  wpdObject
)
```



## Parameters

<dl> <dt>

*wpdObject* 
</dt> <dd>

The **WPDObject** that was added.

</dd> </dl>

## Return value

This event does not return a value.

## Examples

The following code shows the handler-function syntax for the **onObjectAdded** event.


```JScript
function HandlerFunction(wpdObject)
{

   // Code to handle a newly added object.               

}

// Set the event handler.
Service.onObjectAdded = HandlerFunction;
```



> [!Note]  
> We recommend that you clear the event handler of a **Service** object variable by setting it to **null**, before reusing that variable to represent a new object. This will keep an event handler object from persisting as a property of the old **Service** object.

 

The following example demonstrates this with the **Service** object variable "currentService". The variable is used to represent one **Service** object, and a handler-function is set for that object. The handler-function is then cleared before currentService is used to represent a new **Service** object.


```JScript
// Set this variable to represent a Service object.
currentService = deviceObject.Services[0];

// Set the event handler for the Service object.
currentService.onObjectAdded = HandlerFunction;

// Do something with the service object.
...

// Clear the event handler when done with the service object.
currentService.onObjectAdded = null;

// Set the variable to represent a new Service object.
currentService = deviceObject.Services[1];
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

 

 





