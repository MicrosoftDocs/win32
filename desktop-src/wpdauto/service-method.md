---
title: Service.Method method
description: The Method method invokes a service-defined method.
ms.assetid: 35e48b4c-07ce-4a98-a1c0-804498f359df
keywords:
- Method method WPD Automation
- Method method WPD Automation , Service object
- Service object WPD Automation , Method method
topic_type:
- apiref
api_name:
- Service.Method
api_location:
- safeint_internal.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service.Method method

The ***Method*** method invokes a service-defined method.

## Syntax


```JScript
retVal = Service.Method(
  Param1, ...
)
```



## Parameters

<dl> <dt>

*Param1, ...* 
</dt> <dd>

The parameters of the service-defined method.

</dd> </dl>

## Return value

The return value of the service-defined method.

## Examples

The following JScript example demonstrates how to invoke a service-defined method.


```JScript
var service = deviceObject.Services[servicePUID];

var results = service.someServiceDefinedMethod(param1, param2);
var myresult = results.someResultParameter;
```



## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Safeint\_internal.h</dt> </dl> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 





