---
description: Generates a C constant definition for the hosting metadata specified in the hostMetadata element.
ms.assetid: c15f77a2-060b-4bc3-8759-d921ea57e5b5
title: relationshipMetadataDefinition element
ms.topic: reference
ms.date: 05/31/2018
---

# relationshipMetadataDefinition element

Generates a C constant definition for the hosting metadata specified in the [**hostMetadata**](hostmetadata.md) element. This definition is used in a source file.

## Usage

``` syntax
<relationshipMetadataDefinition/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

This element is generally used in C source files to provide the service host metadata declared by **relationshipMetadataDeclaration**.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




