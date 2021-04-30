---
description: Generates a declaration for a function that creates a typed host.
ms.assetid: 3c08e913-b47e-4ca7-b8bc-7b036e57db01
title: hostBuilderDeclaration element
ms.topic: reference
ms.date: 05/31/2018
---

# hostBuilderDeclaration element

Generates a declaration for a function that creates a typed host.

## Usage

``` syntax
<hostBuilderDeclaration>
  child elements
</hostBuilderDeclaration>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                                                                                                                                  |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**interface**](interface.md)<br/> | The name of service interface to be included for host. The value of this element must match the value of the [**interface**](interface.md) child element of [**hostedService**](hostedservice.md). <br/> <br/> |



### Child element sequence

``` syntax
interface+
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




