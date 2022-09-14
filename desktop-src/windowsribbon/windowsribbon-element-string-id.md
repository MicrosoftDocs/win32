---
title: String.Id property
description: Represents the unique ID of a string resource.
ms.assetid: 393da279-bdf6-4796-a546-1931cbe49113
keywords:
- String.Id property Windows Ribbon
topic_type:
- apiref
api_name:
- String.Id
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# String.Id property

Represents the unique ID of a string resource.

## Usage

``` syntax
<String.Id/>
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

The value for **String.Id** must be unique.

The ID is associated with a string definition in the Ribbon header file, for example, `#define strSave 59999`.

This element contains a value from the union of types *xs:positiveInteger* and *xs:string*. The value is constrained to a integer value between 2 and 59999, inclusive, or 0x2 and 0xea5f in hexadecimal, inclusive.

The maximum length is 10 characters with optional leading zeros.

## Examples

The following example demonstrates the markup for a [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) element with a **String.Id** declaration.


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



 

 





