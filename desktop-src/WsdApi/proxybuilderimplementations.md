---
description: Generates functions to create typed proxies.
ms.assetid: 75a686ba-8112-4093-8a1b-13419018aa3a
title: proxyBuilderImplementations element
ms.topic: reference
ms.date: 05/31/2018
---

# proxyBuilderImplementations element

Generates functions to create typed proxies.

## Usage

``` syntax
<proxyBuilderImplementations>
  child elements
</proxyBuilderImplementations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                     | Description                                                                                                                                                     |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**codeName**](codename.md)<br/>     | The name to be used for the port type in the generated code. By default, the code name is generated from the port type's qualified name.<br/> <br/> |
| [**portType**](porttype.md)<br/>     | Port type for which code is to be generated.<br/> <br/>                                                                                             |
| [**proxyClass**](proxyclass.md)<br/> | Class name to generate from the proxy builder function.<br/> <br/>                                                                                  |



### Child element sequence

``` syntax
(
  proxyClass, 
  portType+, 
  codeName
)
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



 

 




