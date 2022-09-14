---
description: Generates C constant declarations for XML schema tables for message types.
ms.assetid: 17556708-9350-444f-84a3-d982270b31d1
title: messageTypeDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# messageTypeDeclarations element

Generates C constant declarations for XML schema tables for message types.

## Usage

``` syntax
<messageTypeDeclarations>
  child elements
</messageTypeDeclarations>
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

Schema tables are referenced by port type definitions. This element is therefore generally used just prior to [**portTypeDefinitions**](porttypedefinitions.md) elements.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




