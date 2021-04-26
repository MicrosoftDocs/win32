---
description: Generates implementation declarations for subscribe/unsubscribe proxy functions for port type notification operations.
ms.assetid: 0e5b2232-c9bf-4741-921d-bb3bce4ee293
title: subscriptionFunctionDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# subscriptionFunctionDeclarations element

Generates implementation declarations for subscribe/unsubscribe proxy functions for port type notification operations.

## Usage

``` syntax
<subscriptionFunctionDeclarations
  extensible = "boolean">
  child elements
</subscriptionFunctionDeclarations>
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



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
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



 

 




