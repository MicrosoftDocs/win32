---
description: Defines the name to be used to identify the namespace in generated code.
ms.assetid: 4e476be2-fa73-4b3e-b0cc-799c8d16b5de
title: codeName element
ms.topic: reference
ms.date: 05/31/2018
---

# codeName element

Defines the name to be used to identify the namespace in generated code.

## Usage

``` syntax
<codeName/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                         | Description                                                              |
|-----------------------------------------------------------------|--------------------------------------------------------------------------|
| [**nameSpace**](namespace.md)<br/>                       | A namespace to be used for code generation.<br/> <br/>       |
| [**portTypeDeclarations**](porttypedeclarations.md)<br/> | Generates C constant declarations for port types.<br/> <br/> |
| [**portTypeDefinitions**](porttypedefinitions.md)<br/>   | Generates C constants for port types.<br/> <br/>             |



## Remarks

This element overrides the default code name used for generated code. By default, the code generated creates a code name from the URI or qualified name.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




