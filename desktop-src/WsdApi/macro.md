---
description: Defines text or CDATA to be reused by the include element.
ms.assetid: bf5cc1e2-b08e-45b6-8e07-5c69865b695b
title: macro element
ms.topic: reference
ms.date: 05/31/2018
---

# macro element

Defines text or CDATA to be reused by the [**include**](include.md) element.

## Usage

``` syntax
<macro
  name = "character_string"/>
```

## Attributes



| Attribute           | Type                         | Required       | Description                                   |
|---------------------|------------------------------|----------------|-----------------------------------------------|
| **name**<br/> | character\_string<br/> | Yes<br/> | The name of the macro.<br/> <br/> |



## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                                                         |
|---------------------------------------------|-------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of a WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

WsdCodeGen defines a macro named **DoNotModify**. When this macro is included, the generated code contains a high-visibility comment block that instructs developers not to modify the generated code.

The following XML shows how to include the **DoNotModify** macro. This XML can be added to an XML configuration file for WsdCodeGen.

``` syntax
<include macro="DoNotModify">
```

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




