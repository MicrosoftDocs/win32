---
title: Command.Comment property
description: Represents a comment, or annotation, for a Command.
ms.assetid: 4ac5c7d4-9627-4703-bd3c-594d9497ba24
keywords:
- Command.Comment property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.Comment
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.Comment property

Represents a comment, or annotation, for a Command.

## Usage

``` syntax
<Command.Comment/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                     |
|-------------------------------------------------------------|
| [**Command**](windowsribbon-element-command.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Command**](windowsribbon-element-command.md).

The comment is associated with a Command definition in the Ribbon header file, for example, `#define cmdSave 25003 /* Save */`.

This element contains a value of type *xs:string*.

The maximum length is 250 characters.

## Examples

The following example demonstrates the markup for a [**Command**](windowsribbon-element-command.md) element with a **Command.Comment** declaration.


```XML
<Command>
  <Command.Name>cmdSave</Command.Name>
  <Command.Symbol>ID_FILE_SAVE</Command.Symbol>
  <Command.Comment>Save</Command.Comment>
  <Command.Id>25003</Command.Id>
  <Command.LabelTitle>
    <String>
      <String.Content>Label for Save</String.Content>
      <String.Id>59999</String.Id>
      <String.Symbol>strSave</String.Symbol>
    </String>
  </Command.LabelTitle>
  <Command.TooltipTitle>Tooltip title with &amp;&amp; for Save Command</Command.TooltipTitle>
  <Command.TooltipDescription>Tooltip description for Save Command.</Command.TooltipDescription>
  <Command.Keytip>s1</Command.Keytip>
</Command>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





