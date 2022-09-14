---
description: Generates IDL declarations for subscribe/unsubscribe proxy functions for port type notification operations.
ms.assetid: 240ef2b3-ed72-45bb-b653-441c4e5540b5
title: subscriptionIdlFunctionDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# subscriptionIdlFunctionDeclarations element

Generates IDL declarations for subscribe/unsubscribe proxy functions for port type notification operations.

## Usage

``` syntax
<subscriptionIdlFunctionDeclarations
  extensible = "boolean">
  child elements
</subscriptionIdlFunctionDeclarations>
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



 

 




