---
description: Generates implementations for subscribe/unsubscribe proxy functions for port type notification operations.
ms.assetid: aa26a3f1-df1e-4caa-9ada-6f4a6627b6b8
title: subscriptionProxyFunctionImplementations element
ms.topic: reference
ms.date: 05/31/2018
---

# subscriptionProxyFunctionImplementations element

Generates implementations for subscribe/unsubscribe proxy functions for port type notification operations.

## Usage

``` syntax
<subscriptionProxyFunctionImplementations
  extensible = "boolean">
  child elements
</subscriptionProxyFunctionImplementations>
```

## Attributes



| Attribute                 | Type               | Required      | Description                                                                                                                   |
|---------------------------|--------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| **extensible**<br/> | boolean<br/> | No<br/> | The ability to add extensibility points to functions and interfaces. This value is always set to true.<br/> <br/> |



## Child elements



| Element                                                           | Description                                                                                            |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**notificationInterface**](notificationinterface.md)<br/> | Specifies the name of the notification interface used with event subscriptions.<br/> <br/> |
| [**operation**](operation.md)<br/>                         | Specifies an operation for which code is to be generated.<br/> <br/>                       |
| [**portType**](porttype.md)<br/>                           | Specifies the port type for which code is to be generated.<br/> <br/>                      |
| [**proxyClass**](proxyclass.md)<br/>                       | Specifies the name of the client-side proxy class.<br/> <br/>                              |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  proxyClass?, 
  notificationInterface?
)
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




