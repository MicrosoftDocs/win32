---
description: Specifies whether parameters used to pass fault information are included in generated functions.
ms.assetid: aba78d50-f884-416a-b022-bb03416aad11
title: faultInfo element
ms.topic: reference
ms.date: 05/31/2018
---

# faultInfo element

Specifies whether parameters used to pass fault information are included in generated functions.

## Usage

``` syntax
<faultInfo/>
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
| [**stubDefinitions**](stubdefinitions.md)<br/>                           | Generates implementations for stub functions for port type operations.<br/> <br/>              |



## Remarks

Possible values are 1 (fault parameters included) and 0 (fault parameters excluded). By default, fault parameters are excluded.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




