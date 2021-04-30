---
description: Defines the prefix to use in the generated code to assure uniqueness of generated symbols.
ms.assetid: 50cb443a-15ae-4f8f-b5f7-b8708810a6c3
title: layerPrefix element
ms.topic: reference
ms.date: 05/31/2018
---

# layerPrefix element

Defines the prefix to use in the generated code to assure uniqueness of generated symbols.

## Usage

``` syntax
<layerPrefix/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

Each code generator script should define a unique prefix string for the modules created. For example, the Picture Frame scripts use a prefix of "PFDEMO".

WSDAPI uses the prefix "WSD".

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




