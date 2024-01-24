---
description: Generates C structure definitions for message types.
ms.assetid: 68459b22-0f35-444a-969e-29695e735774
title: messageStructureDefinitions element
ms.topic: reference
ms.date: 05/31/2018
---

# messageStructureDefinitions element

Generates C structure definitions for message types.

## Usage

``` syntax
<messageStructureDefinitions>
  child elements
</messageStructureDefinitions>
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

Message structures are referenced by generated proxy and stub code. This element is used to generate include files.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




