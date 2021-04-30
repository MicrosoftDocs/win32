---
description: Includes the contents of a macro or file in the generated output.
ms.assetid: 450ccfa6-b189-4557-bcb9-4aa29ac2356e
title: include element
ms.topic: reference
ms.date: 05/31/2018
---

# include element

Includes the contents of a macro or file in the generated output.

## Usage

``` syntax
<include
  macro = "character_string"
  file = "character_string"/>
```

## Attributes



| Attribute            | Type                         | Required      | Description                                              |
|----------------------|------------------------------|---------------|----------------------------------------------------------|
| **file**<br/>  | character\_string<br/> | No<br/> | The path to the file to include.<br/> <br/>  |
| **macro**<br/> | character\_string<br/> | No<br/> | The name of the macro to include.<br/> <br/> |



## Child elements

There are no child elements.

## Parent elements



| Element                         | Description                                                                                              |
|---------------------------------|----------------------------------------------------------------------------------------------------------|
| [**file**](file.md)<br/> | Directs the code generator to generate a file and specifies the output file name.<br/> <br/> |



## Remarks

Either the **macro** attribute or the **file** attribute must be specified. Do not specify both attributes.

WsdCodeGen defines a macro named **DoNotModify**. When this macro is included, the generated code contains a high-visibility comment block that instructs developers not to modify the generated code.

## Examples

The following XML shows how to include the **DoNotModify** macro. This XML can be added to an XML configuration file for WsdCodeGen.

``` syntax
<include macro="DoNotModify">
```

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




