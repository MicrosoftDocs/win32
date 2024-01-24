---
description: Generates implementations for proxy functions for port type operations.
ms.assetid: 9505ee5f-fdb9-41b8-9537-0c5d29f90168
title: proxyFunctionImplementations element
ms.topic: reference
ms.date: 05/31/2018
---

# proxyFunctionImplementations element

Generates implementations for proxy functions for port type operations.

## Usage

``` syntax
<proxyFunctionImplementations>
  child elements
</proxyFunctionImplementations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                     | Description                                                                                                             |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**async**](async.md)<br/>           | Specifies whether asynchronous operations are included in the generated proxy functions.<br/> <br/>         |
| [**events**](events.md)<br/>         | Specifies whether related events are included in the generated functions.<br/> <br/>                        |
| [**faultInfo**](faultinfo.md)<br/>   | Specifies whether parameters used to pass fault information are included in generated functions.<br/> <br/> |
| [**operation**](operation.md)<br/>   | Specifies an operation for which code is to be generated.<br/> <br/>                                        |
| [**portType**](porttype.md)<br/>     | Specifies the port type for which code is to be generated.<br/> <br/>                                       |
| [**proxyClass**](proxyclass.md)<br/> | Specifies the name of the client-side proxy class.<br/> <br/>                                               |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  proxyClass?, 
  events?, 
  async?, 
  faultInfo?
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
| Can be empty                        | Yes           |



 

 




