---
description: Generates C constants for XML schema tables for message types.
ms.assetid: 0b322acb-3326-42a2-a852-07251585b314
title: messageTypeDefinitions element
ms.topic: reference
ms.date: 05/31/2018
---

# messageTypeDefinitions element

Generates C constants for XML schema tables for message types.

## Usage

``` syntax
<messageTypeDefinitions>
  child elements
</messageTypeDefinitions>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                       |
|-------------------------------------------|-----------------------------------------------------------------------------------|
| [**operation**](operation.md)<br/> | Specifies an operation for which code is to be generated.<br/> <br/>  |
| [**portType**](porttype.md)<br/>   | Specifies the port type for which code is to be generated.<br/> <br/> |



### Child element sequence

``` syntax
(
  portType?, 
  operation*
)
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

This element is generally used in C source files to provide the schema tables declared by [**messageTypeDeclarations**](messagetypedeclarations.md).

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




