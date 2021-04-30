---
description: Defines the number of the code layer to be generated.
ms.assetid: ad67a6fb-4bb6-4550-a9e9-f5219f3868c6
title: layerNumber element
ms.topic: reference
ms.date: 05/31/2018
---

# layerNumber element

Defines the number of the code layer to be generated.

## Usage

``` syntax
<layerNumber/>
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

Layer numbers are used in runtime tables to distinguish one layer of code for another. WSDAPI itself uses generated code that has a layer number of 0.

Typically, this value will be 1, indicating that the generated code is layered on top of WSDAPI and no other layer. In some cases, higher numbers may be used. For example, if one company produces code for a device class (numbered layer 1), a particular hardware vendor may want to add an additional layer numbered layer 2.

Legal values, except in the case of WSDAPI itself are greater than 0 and less than 16.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




