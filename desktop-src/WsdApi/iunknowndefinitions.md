---
description: Generates implementations for the QueryInterface, AddRef and Release functions.
ms.assetid: 4b6abd0b-7570-4ae0-a727-cdb6cec58daf
title: IUnknownDefinitions element
ms.topic: reference
ms.date: 05/31/2018
---

# IUnknownDefinitions element

Generates implementations for the QueryInterface, AddRef and Release functions.

## Usage

``` syntax
<IUnknownDefinitions
  proxyClass = "character_string"
  refCountVar = "character_string">
  child elements
</IUnknownDefinitions>
```

## Attributes



| Attribute                  | Type                         | Required       | Description                                                |
|----------------------------|------------------------------|----------------|------------------------------------------------------------|
| **proxyClass**<br/>  | character\_string<br/> | Yes<br/> | The name of the implementing class.<br/> <br/> |
| **refCountVar**<br/> | character\_string<br/> | Yes<br/> | The reference count variable name.<br/> <br/>  |



## Child elements



| Element                                   | Description                                                                        |
|-------------------------------------------|------------------------------------------------------------------------------------|
| [**interface**](interface.md)<br/> | The name of the interface to be returned by QueryInterface.<br/> <br/> |



### Child element sequence

``` syntax
interface
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




