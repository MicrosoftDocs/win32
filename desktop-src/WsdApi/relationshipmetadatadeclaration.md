---
description: Generates a forward declaration for the hosting metadata specified in the hostMetadata element.
ms.assetid: 595adb84-e1a7-4636-b61f-eb0a4b3057b9
title: relationshipMetadataDeclaration element
ms.topic: reference
ms.date: 05/31/2018
---

# relationshipMetadataDeclaration element

Generates a forward declaration for the hosting metadata specified in the [**hostMetadata**](hostmetadata.md) element. This declaration is used in a header file.

## Usage

``` syntax
<relationshipMetadataDeclaration/>
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

Hosting metadata is referenced by the application when it initializes the host. This element is used to generate include files that are included by the application source code.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




