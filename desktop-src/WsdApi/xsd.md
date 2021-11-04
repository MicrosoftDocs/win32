---
description: Specifies an XSD file to process for contract information.
ms.assetid: 6fe40e77-d23f-4ae9-a4d6-1f567a0fffe7
title: xsd element
ms.topic: reference
ms.date: 05/31/2018
---

# xsd element

Specifies an XSD file to process for contract information.

## Usage

``` syntax
<xsd
  path = "pathname string">
  child elements
</xsd>
```

## Attributes



| Attribute           | Type                       | Required       | Description                                                 |
|---------------------|----------------------------|----------------|-------------------------------------------------------------|
| **path**<br/> | pathname string<br/> | Yes<br/> | File and path of the XSD input file.<br/> <br/> |



## Child elements



| Element                               | Description                                                          |
|---------------------------------------|----------------------------------------------------------------------|
| [**typeUri**](typeuri.md)<br/> | Specifies a type to include from an XSD file.<br/> <br/> |



### Child element sequence

``` syntax
typeUri*
```

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

The filename string should include complete path information as well.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




