---
description: Specifies the download location for a wsdl:import directive that does not explicitly specify a location.
ms.assetid: 81d0a30b-8f15-4518-b833-de57e0dae978
title: importHint element
ms.topic: reference
ms.date: 05/31/2018
---

# importHint element

Specifies the download location for a \<wsdl:import> directive that does not explicitly specify a location.

## Usage

``` syntax
<importHint>
  child elements
</importHint>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                                       |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**location**](location.md)<br/>   | The location of the file to import. The location may be a relative path, an absolute path, or an HTTP URL.<br/> <br/> |
| [**nameSpace**](namespace.md)<br/> | The namespace to import. This should match the namespace specified in the \<wsdl:import> element.<br/> <br/>     |



### Child element sequence

``` syntax
(
  nameSpace, 
  location
)
```

## Parent elements



| Element                         | Description                                                                       |
|---------------------------------|-----------------------------------------------------------------------------------|
| [**wsdl**](wsdl.md)<br/> | Specifies a WSDL file to process for contract information.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




