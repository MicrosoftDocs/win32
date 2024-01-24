---
description: Specifies whether related events are included in the generated functions.
ms.assetid: 23ca463c-b305-496b-a1e3-58dbb793f17e
title: events element
ms.topic: reference
ms.date: 05/31/2018
---

# events element

Specifies whether related events are included in the generated functions.

## Usage

``` syntax
<events/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                                         | Description                                                                                                |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**functionDeclarations**](functiondeclarations.md)<br/>                 | Generates implementation declarations for proxy functions for port type operations.<br/> <br/> |
| [**idlFunctionDeclarations**](idlfunctiondeclarations.md)<br/>           | Generates IDL declarations for proxy functions for port type operations.<br/> <br/>            |
| [**proxyFunctionImplementations**](proxyfunctionimplementations.md)<br/> | Generates implementations for proxy functions for port type operations.<br/> <br/>             |
| [**stubDeclarations**](stubdeclarations.md)<br/>                         | Generates declarations for stub functions for port type operations.<br/> <br/>                 |
| [**stubDefinitions**](stubdefinitions.md)<br/>                           | Generates implementations for stub functions for port type operations.<br/> <br/>              |



## Remarks

Possible values are 1 (events included) and 0 (default, events excluded).

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




