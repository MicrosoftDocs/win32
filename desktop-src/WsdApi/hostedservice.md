---
description: Defines a service to be hosted in a host builder function.
ms.assetid: 87ff447a-ced0-4079-b46d-239f0db37250
title: hostedService element
ms.topic: reference
ms.date: 05/31/2018
---

# hostedService element

Defines a service to be hosted in a host builder function.

## Usage

``` syntax
<hostedService>
  child elements
</hostedService>
```

## Attributes

There are no attributes.

## Child elements



| Element                                     | Description                                                                                                                                                               |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**codeName**](codename.md)<br/>     | Specifies the name to be used for the port type in the generated code. By default, the code name is generated from the port type's qualified name.<br/> <br/> |
| [**portType**](porttype.md)<br/>     | Port type for which code is to be generated.<br/> <br/>                                                                                                       |
| [**proxyClass**](proxyclass.md)<br/> | Class name to generate from builder function.<br/> <br/>                                                                                                      |
| [**ServiceID**](serviceid.md)<br/>   | A URI that represents the service identifier.<br/> <br/>                                                                                                      |



### Child element sequence

``` syntax
codeName(
  ServiceID, 
  proxyClass, 
  portType+
)
```

## Parent elements



| Element                         | Description                                                                  |
|---------------------------------|------------------------------------------------------------------------------|
| [**file**](file.md)<br/> | The output file specification for the code generator.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




