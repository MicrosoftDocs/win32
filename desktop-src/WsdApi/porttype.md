---
description: Specifies the port type for which code is to be generated.
ms.assetid: 8a7762ae-2e39-46e1-b49f-09cae1af9b0d
title: portType element
ms.topic: reference
ms.date: 05/31/2018
---

# portType element

Specifies the port type for which code is to be generated.

## Usage

``` syntax
<portType/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                                                                 | Description                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**functionDeclarations**](functiondeclarations.md)<br/>                                         | Generates implementation declarations for proxy functions for port type operations.<br/> <br/>                                    |
| [**idlFunctionDeclarations**](idlfunctiondeclarations.md)<br/>                                   | Generates IDL declarations for proxy functions for port type operations.<br/> <br/>                                               |
| [**messageStructureDefinitions**](messagestructuredefinitions.md)<br/>                           | Generates C structure definitions for message types.<br/> <br/>                                                                   |
| [**messageTypeDeclarations**](messagetypedeclarations.md)<br/>                                   | Generates C constant declarations for XML schema tables for message types.<br/> <br/>                                             |
| [**messageTypeDefinitions**](messagetypedefinitions.md)<br/>                                     | Generates C constants for XML schema tables for message types.<br/> <br/>                                                         |
| [**portTypeDeclarations**](porttypedeclarations.md)<br/>                                         | Generates C constant declarations for port types.<br/> <br/>                                                                      |
| [**portTypeDefinitions**](porttypedefinitions.md)<br/>                                           | Generates C constants for port types.<br/> <br/>                                                                                  |
| [**proxyFunctionImplementations**](proxyfunctionimplementations.md)<br/>                         | Generates implementations for proxy functions for port type operations.<br/> <br/>                                                |
| [**stubDeclarations**](stubdeclarations.md)<br/>                                                 | Generates declarations for stub functions for port type operations.<br/> <br/>                                                    |
| [**stubDefinitions**](stubdefinitions.md)<br/>                                                   | Generates implementations for stub functions for port type operations.<br/> <br/>                                                 |
| [**subscriptionFunctionDeclarations**](subscriptionfunctiondeclarations.md)<br/>                 | Generates implementation declarations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/> |
| [**subscriptionIdlFunctionDeclarations**](subscriptionidlfunctiondeclarations.md)<br/>           | Generates IDL declarations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>            |
| [**subscriptionProxyFunctionImplementations**](subscriptionproxyfunctionimplementations.md)<br/> | Generates implementations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>             |



## Remarks

By default, code is generated for all port types in WSDL input files.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




