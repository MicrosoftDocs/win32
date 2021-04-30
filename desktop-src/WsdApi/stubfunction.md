---
description: Specifies whether stub function references should be included in the operation structures in the port type definitions for one-way and two-way operations.
ms.assetid: '2547f71d-8a30-4df8-ba38-6707c415708e'
title: stubFunction element
ms.topic: article
ms.date: 05/31/2018
---

# stubFunction element

Specifies whether stub function references should be included in the operation structures in the port type definitions for one-way and two-way operations.

## Usage

``` syntax
<stubFunction/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                       | Description                                                  |
|---------------------------------------------------------------|--------------------------------------------------------------|
| [**portTypeDefinitions**](porttypedefinitions.md)<br/> | Generates C constants for port types.<br/> <br/> |



## Remarks

Stub function references are used in hosting scenarios for one-way and two-way operations.

Valid values for this element are 1 (TRUE/stub function references included) and 0 (FALSE/no stub function references included).

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




