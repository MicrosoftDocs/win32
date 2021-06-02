---
description: Generates declarations for stub functions for port type operations.
ms.assetid: d43baeff-c941-4ce9-a6ae-8aa61ef44048
title: stubDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# stubDeclarations element

Generates declarations for stub functions for port type operations.

## Usage

``` syntax
<stubDeclarations>
  child elements
</stubDeclarations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                      |
|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**events**](events.md)<br/>       | Specifies whether related events are included in the generated functions.<br/> <br/> |
| [**operation**](operation.md)<br/> | Specifies an operation for which code is to be generated.<br/> <br/>                 |
| [**portType**](porttype.md)<br/>   | Specifies the port type for which code is to be generated.<br/> <br/>                |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  events?
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



 

 




