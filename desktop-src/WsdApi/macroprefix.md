---
description: Defines the prefix to be used in the generated code for names of macros in the namespace.
ms.assetid: ead82070-5546-4036-bff2-8da2714d4264
title: macroPrefix element
ms.topic: reference
ms.date: 05/31/2018
---

# macroPrefix element

Defines the prefix to be used in the generated code for names of macros in the namespace.

## Usage

``` syntax
<macroPrefix/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                   | Description                                                        |
|-------------------------------------------|--------------------------------------------------------------------|
| [**nameSpace**](namespace.md)<br/> | A namespace to be used for code generation.<br/> <br/> |



## Remarks

This element overrides the default URI prefix used for generated macros. For example, if the macro prefix is "AV\_" and the name is "Tuner", the macro generated for the qualified name will be "AV\_Tuner".

By default, the code generated creates a preferred macro prefix from the URI.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




