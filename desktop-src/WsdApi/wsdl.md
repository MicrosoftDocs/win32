---
description: Specifies a WSDL file to process for contract information.
ms.assetid: d8f630cd-0541-431b-86a8-792846a85ea0
title: wsdl element
ms.topic: reference
ms.date: 05/31/2018
---

# wsdl element

Specifies a WSDL file to process for contract information.

## Usage

``` syntax
<wsdl>
  child elements
</wsdl>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**excludeImport**](excludeimport.md)<br/> | Prevents the generation of import statements for specified targets named in a \<wsdl:import> element in a WSDL file. <br/> <br/> |
| [**importHint**](importhint.md)<br/>       | Specifies the download location for a \<wsdl:import> directive that does not explicitly specify a location.<br/> <br/>           |
| [**path**](path.md)<br/>                   | File and path of the WSDL input file.<br/> <br/>                                                                                      |



### Child element sequence

``` syntax
(
  importHint*, 
  excludeImport*, 
  path
)
```

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

Any [**importHint**](importhint.md) or [**excludeImport**](excludeimport.md) elements appearing after the [**path**](path.md) element in an XML configuration file will be ignored.

## Element information



|                                     |               |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




