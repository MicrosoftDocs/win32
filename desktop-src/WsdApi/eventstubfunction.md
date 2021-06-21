---
description: Specifies whether stub function references should be included in the operation structures in the port type definitions for notification operations.
ms.assetid: 8a2fd7b2-e37b-465a-ba83-a68877a2e0c3
title: eventStubFunction element
ms.topic: reference
ms.date: 05/31/2018
---

# eventStubFunction element

Specifies whether stub function references should be included in the operation structures in the port type definitions for notification operations.

## Usage

``` syntax
<eventStubFunction/>
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

Stub function references are in client scenarios for notification operations (events).

Valid values for this element are 1 (TRUE/stub function references included) and 0 (FALSE/no stub function references included).

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




