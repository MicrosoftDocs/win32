---
description: Specifies the type deallocator to be used by an operations stub function.
ms.assetid: 52e6235d-90e6-4559-b17c-14ca3be896ff
title: operationDeallocator element
ms.topic: reference
ms.date: 05/31/2018
---

# operationDeallocator element

Specifies the type deallocator to be used by an operation's stub function.

## Usage

``` syntax
<operationDeallocator
  operation = "character_string"
  deallocator = "character_string"/>
```

## Attributes



| Attribute                  | Type                         | Required       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------|------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **deallocator**<br/> | character\_string<br/> | Yes<br/> | The deallocator to use for the operation.<br/> <br/> The following strings are valid values.<br/> <br/> <dl><span id="none"></span><span id="NONE"></span><dt>****none****</dt><span id="WSDFreeLinkedMemory"></span><span id="wsdfreelinkedmemory"></span><span id="WSDFREELINKEDMEMORY"></span><dt>****WSDFreeLinkedMemory****</dt><span id="CoTaskMemFree"></span><span id="cotaskmemfree"></span><span id="COTASKMEMFREE"></span><dt>****CoTaskMemFree****</dt><span id="free"></span><span id="FREE"></span><dt>****free****</dt><span id="delete"></span><span id="DELETE"></span><dt>****delete****</dt><span id="deleteArray"></span><span id="deletearray"></span><span id="DELETEARRAY"></span><dt>****deleteArray****</dt><span id="Release"></span><span id="release"></span><span id="RELEASE"></span><dt>****Release****</dt> </dl> |
| **operation**<br/>   | character\_string<br/> | Yes<br/> | The name of the operation.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |



## Child elements

There are no child elements.

## Parent elements



| Element                                               | Description                                                                                   |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**stubDefinitions**](stubdefinitions.md)<br/> | Generates implementations for stub functions for port type operations.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




