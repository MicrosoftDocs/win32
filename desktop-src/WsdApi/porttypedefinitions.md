---
description: Generates C constants for port types.
ms.assetid: 6ad0d163-df51-48b6-aad7-a4b018688872
title: portTypeDefinitions element
ms.topic: reference
ms.date: 05/31/2018
---

# portTypeDefinitions element

Generates C constants for port types.

## Usage

``` syntax
<portTypeDefinitions>
  child elements
</portTypeDefinitions>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                   | Description                                                                                                                                                                       |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**codeName**](codename.md)<br/>                   | Specifies the name to be used for the port type in the generated code. By default, the code name is generated from the port type's qualified name.<br/> <br/>         |
| [**eventStubFunction**](eventstubfunction.md)<br/> | Specifies whether stub function references should be included in the operation structures in the port type definitions for notification operations.<br/> <br/>        |
| [**operation**](operation.md)<br/>                 | Specifies an operation for which code is to be generated.<br/> <br/>                                                                                                  |
| [**portType**](porttype.md)<br/>                   | Specifies the port type for which code is to be generated.<br/> <br/>                                                                                                 |
| [**stubFunction**](stubfunction.md)<br/>           | Specifies whether stub function references should be included in the operation structures in the port type definitions for one-way and two-way operations.<br/> <br/> |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  stubFunction?, 
  eventStubFunction?, 
  codeName?
)
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

This element is generally used in C source files to provide the port type constants declared by [**portTypeDeclarations**](porttypedeclarations.md).

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




