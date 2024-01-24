---
description: Generates a function that creates a typed host.
ms.assetid: 2b4a4016-cc5d-4912-8e08-ce3a11ab0a06
title: hostBuilderImplementation element
ms.topic: reference
ms.date: 05/31/2018
---

# hostBuilderImplementation element

Generates a function that creates a typed host.

## Usage

``` syntax
<hostBuilderImplementation>
  child elements
</hostBuilderImplementation>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                      |
|---------------------------------------------------|------------------------------------------------------------------|
| [**hostedService**](hostedservice.md)<br/> | The service to be included for the host. <br/> <br/> |



### Child element sequence

``` syntax
hostedService+
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



 

 




