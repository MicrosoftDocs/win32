---
title: Service.onMethodComplete event
description: The onMethodComplete event occurs after a service-defined method has completed.
ms.assetid: '76c70090-dcf5-44bf-acdd-f7c0f685b262'
keywords: ["onMethodComplete event WPD Automation", "onMethodComplete event WPD Automation , Service object", "Service object WPD Automation , onMethodComplete event"]
topic_type:
- apiref
api_name:
- Service.onMethodComplete
api_type:
- COM
---

# Service.onMethodComplete event

The **on*Method*Complete** event occurs after a service-defined method has completed.

## Syntax


```JScript
Service.onMethodComplete(
  MethodResult
)
```



## Parameters

<dl> <dt>

*MethodResult* 
</dt> <dd>

Contains the result of the service-defined method.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The name and parameters of this method are defined by the service. For example, if a service defines a method with the name *DoSomething*, WPD Automation will expose a method complete handler called **service**.*onDoSomethingComplete*. You can assign a JScript function to the method complete handler to be notified whenever this method has completed. Setting this handler will result in the method being called asynchronously rather than synchronously.

## Examples

The following code shows the handler-function syntax for the **on*Method*Complete** event. In this example, the name of the service-defined method is *DoSomething*.


```JScript
function HandlerFunction(MethodResult)
{

   // Code to handle a completed asynchronous method operation.             

}

// Set the event handler.
Service.onDoSomethingComplete = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 





