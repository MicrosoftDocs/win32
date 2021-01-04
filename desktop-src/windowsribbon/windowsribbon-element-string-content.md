---
title: String.Content property
description: Represents the content of a string resource.
ms.assetid: 86f34cdc-1311-4f52-979f-201d71bbb9e9
keywords:
- String.Content property Windows Ribbon
topic_type:
- apiref
api_name:
- String.Content
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# String.Content property

Represents the content of a string resource.

## Usage

``` syntax
<String.Content/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**String**](windowsribbon-element-string.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**String**](windowsribbon-element-string.md) element.

This element contains a value of type *xs:string*. The value is constrained to a string composed of any sequence of characters, including white space and line-break characters.

The maximum length is unbounded.

## Examples

The following example demonstrates the markup for a [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) element with a **String.Content** declaration.


```XML
<Command.LabelTitle>
  <String>
    <String.Content>Label for Save</String.Content>
    <String.Id>59999</String.Id>
    <String.Symbol>strSave</String.Symbol>
  </String>
</Command.LabelTitle>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





