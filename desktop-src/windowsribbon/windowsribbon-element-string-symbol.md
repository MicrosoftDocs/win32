---
title: String.Symbol property
description: Represents the name of a string resource.
ms.assetid: 7c1d0197-2c9b-4f42-afba-73fd1c366deb
keywords:
- String.Symbol property Windows Ribbon
topic_type:
- apiref
api_name:
- String.Symbol
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# String.Symbol property

Represents the name of a string resource.

## Usage

``` syntax
<String.Symbol/>
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

The symbol is associated with a string definition in the Ribbon header file, for example, `#define strSave 59999`.

This element contains a value of type *xs:string*. The value is constrained to a string composed of a letter or underscore followed by any sequence of letters, digits, or underscores.

The maximum length is 100 characters.

## Examples

The following example demonstrates the markup for a [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) element with a **String.Symbol** declaration.


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



 

 





