---
description: Specifies the type of deallocator to be used by a stub function.
ms.assetid: 58228dfd-1d4b-41e5-b423-a54525021c22
title: deallocator element
ms.topic: reference
ms.date: 05/31/2018
---

# deallocator element

Specifies the type of deallocator to be used by a stub function.

## Usage

``` syntax
<deallocator/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                               | Description                                                                                   |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**stubDefinitions**](stubdefinitions.md)<br/> | Generates implementations for stub functions for port-type operations.<br/> <br/> |



## Remarks

The deallocator type should be enclosed in a pair of <deallocator></deallocator> tags. The following strings are valid deallocator values:

-   none
-   WSDFreeLinkedMemory
-   CoTaskMemFree
-   free
-   delete
-   deleteArray
-   Release

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




