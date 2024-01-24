---
description: Specifies whether asynchronous operations are included in the generated proxy functions.
ms.assetid: 7b57d5c6-589b-4e03-bfcf-1faa671ebd77
title: async element
ms.topic: reference
ms.date: 05/31/2018
---

# async element

Specifies whether asynchronous operations are included in the generated proxy functions.

## Usage

``` syntax
<async/>
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



## Remarks

Possible values are 1 (asynchronous operations included) and 0 (default, asynchronous operations excluded).

A proxy can have both asynchronous and synchronous versions of the same operations.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




