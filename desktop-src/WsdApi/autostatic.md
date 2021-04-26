---
description: Indicates whether or not WsdCodeGen should try to automatically flag certain generated fields as static.
ms.assetid: 0c858567-e17a-46a0-b3ff-a0dc8089b0cd
title: autoStatic element
ms.topic: reference
ms.date: 05/31/2018
---

# autoStatic element

Indicates whether or not WsdCodeGen should try to automatically flag certain generated fields as static. This behavior is enabled by default.

## Usage

``` syntax
<autoStatic/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

The **autoStatic** element is not required and may be omitted from the XML configuration file. The element can be used to disable the flagging of generated fields as static or to explicitly force the flagging of certain generated fields as static.

Possible values are 1 (enabled, default) and 0 (disabled). Enabling **autoStatic** may cause compilation issues depending on how the code generator is directed to output data.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




