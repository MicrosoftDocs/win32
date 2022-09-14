---
description: Generates implementations for stub functions for port-type operations.
ms.assetid: 69899302-db54-493b-90de-596750be566f
title: stubDefinitions element
ms.topic: reference
ms.date: 05/31/2018
---

# stubDefinitions element

Generates implementations for stub functions for port-type operations.

## Usage

``` syntax
<stubDefinitions>
  child elements
</stubDefinitions>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                         | Description                                                                                                             |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**deallocator**](deallocator.md)<br/>                   | Specifies the type of deallocator to be used by a stub function.<br/> <br/>                                 |
| [**eventArg**](eventarg.md)<br/>                         | Specifies whether related event arguments are included in the generated functions.<br/> <br/>               |
| [**events**](events.md)<br/>                             | Specifies whether related events are included in the generated functions.<br/> <br/>                        |
| [**faultInfo**](faultinfo.md)<br/>                       | Specifies whether parameters used to pass fault information are included in generated functions.<br/> <br/> |
| [**operation**](operation.md)<br/>                       | Specifies an operation for which code is to be generated.<br/> <br/>                                        |
| [**operationDeallocator**](operationdeallocator.md)<br/> | Specifies the type of deallocator to be used by an operation's stub function.<br/> <br/>                    |
| [**portType**](porttype.md)<br/>                         | Specifies the port type for which code is to be generated.<br/> <br/>                                       |
| [**serverClass**](serverclass.md)<br/>                   | Specifies the name of the host-side server class.<br/> <br/>                                                |



### Child element sequence

``` syntax
(
  portType?, 
  operation*, 
  serverClass, 
  eventArg?, 
  events?, 
  operationDeallocator*, 
  deallocator?, 
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
| Can be empty                        | No            |



 

 




