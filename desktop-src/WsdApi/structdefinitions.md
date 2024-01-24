---
description: Generates C structure definitions for known types.
ms.assetid: 38ba2e8a-d5b1-47b2-b410-ae161f5039bf
title: structDefinitions element
ms.topic: reference
ms.date: 05/31/2018
---

# structDefinitions element

Generates C structure definitions for known types.

## Usage

``` syntax
<structDefinitions/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

Structures for known types are referenced by much of the generated code and by application code. This element is used to generate include files. This element should occur after a [**structDeclarations**](structdeclarations.md) element so that references between structures are handled properly.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




