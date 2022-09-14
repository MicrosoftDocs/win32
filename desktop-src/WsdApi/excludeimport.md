---
description: Prevents the generation of import statements for specified targets named in a wsdl:import element in a WSDL file.
ms.assetid: 9a50ee38-fadf-4112-8430-cb5a07ae04ce
title: excludeImport element
ms.topic: reference
ms.date: 05/31/2018
---

# excludeImport element

Prevents the generation of import statements for specified targets named in a \<wsdl:import> element in a WSDL file. This can be used to keep WsdCodeGen from importing well-known targets, such as the WS-Addressing and WS-Eventing specifications, even though these targets are referenced in the WSDL.

The value of this element must be set to the namespace named in the \<wsdl:import> element to exclude.

## Usage

``` syntax
<excludeImport/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                         | Description                                                                       |
|---------------------------------|-----------------------------------------------------------------------------------|
| [**wsdl**](wsdl.md)<br/> | Specifies a WSDL file to process for contract information.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




