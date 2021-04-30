---
description: Generates implementation declarations for proxy functions for port type operations.
ms.assetid: 6ba7dbb6-6598-4569-97e1-d703e4b896c7
title: functionDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# functionDeclarations element

Generates implementation declarations for proxy functions for port type operations.

## Usage

``` syntax
<functionDeclarations>
  child elements
</functionDeclarations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                             |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**async**](async.md)<br/>         | Specifies whether asynchronous operations are included in the generated proxy functions.<br/> <br/>         |
| [**events**](events.md)<br/>       | Specifies whether related events are included in the generated functions.<br/> <br/>                        |
| [**faultInfo**](faultinfo.md)<br/> | Specifies whether parameters used to pass fault information are included in generated functions.<br/> <br/> |
| [**operation**](operation.md)<br/> | Specifies an operation for which code is to be generated.<br/> <br/>                                        |
| [**portType**](porttype.md)<br/>   | Specifies the port type for which code is to be generated.<br/> <br/>                                       |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  events?, 
  async?, 
  faultInfo?
)
```

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

This element generates declarations of member functions corresponding to operations called out by the contract. These declarations are in a form appropriate for consumption by a C++ compiler and are generally used in .cpp files.

Example:

``` syntax
<functionDeclarations events = "true"/>
```

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




