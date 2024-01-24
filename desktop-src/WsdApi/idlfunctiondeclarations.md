---
description: Generates IDL declarations for proxy functions for port type operations.
ms.assetid: e56fdd68-b72d-4167-9e4c-b5bbf103880b
title: idlFunctionDeclarations element
ms.topic: reference
ms.date: 05/31/2018
---

# idlFunctionDeclarations element

Generates IDL declarations for proxy functions for port type operations.

## Usage

``` syntax
<idlFunctionDeclarations>
  child elements
</idlFunctionDeclarations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                             |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**async**](async.md)<br/>         | Specifies whether asynchronous operations are included in the generated proxy functions.<br/> <br/>         |
| [**eventArg**](eventarg.md)<br/>   | Specifies whether related event arguments are included in the generated functions.<br/> <br/>               |
| [**events**](events.md)<br/>       | Specifies whether related events are included in the generated functions.<br/> <br/>                        |
| [**faultInfo**](faultinfo.md)<br/> | Specifies whether parameters used to pass fault information are included in generated functions.<br/> <br/> |
| [**operation**](operation.md)<br/> | Specifies an operation for which code is to be generated.<br/> <br/>                                        |
| [**portType**](porttype.md)<br/>   | Specifies the port type for which code is to be generated.<br/> <br/>                                       |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  eventArg?, 
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

This element generates declarations of member functions corresponding to operations called out by the contract. These declarations are in a form appropriate for consumption by the MIDL compiler and are generally used in .idl files.

Example:

``` syntax
<idlFunctionDeclarations events = "true"/>
```

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




