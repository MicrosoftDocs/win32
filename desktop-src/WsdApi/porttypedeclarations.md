---
description: Generates C constant declarations for port types.
ms.assetid: 05a06206-3cc4-428d-b9f2-b7945e63922c
title: portTypeDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# portTypeDeclarations element

Generates C constant declarations for port types.

## Usage

``` syntax
<portTypeDeclarations>
  child elements
</portTypeDeclarations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                                                                               |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**codeName**](codename.md)<br/>   | Specifies the name to be used for the port type in the generated code. By default, the code name is generated from the port type's qualified name.<br/> <br/> |
| [**operation**](operation.md)<br/> | Specifies an operation for which code is to be generated.<br/> <br/>                                                                                          |
| [**portType**](porttype.md)<br/>   | Specifies the port type for which code is to be generated.<br/> <br/>                                                                                         |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  codeName?
)
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

Port type declarations are referenced by the application and much of the generated code. This element is used to generate include files.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




