---
title: Command.Id property
description: Represents a unique ID for a Command.
ms.assetid: 937ca9d6-6910-4133-9cfa-d7e3f895f876
keywords:
- Command.Id property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.Id
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.Id property

Represents a unique ID for a Command.

## Usage

``` syntax
<Command.Id/>
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

The ID is associated with a Command definition in the Ribbon header file, for example, `#define cmdSave 25003 /* Save */`.

This element contains a value from the union of types *xs:positiveInteger* and *xs:string* constrained to an integer value between 2 and 59999, inclusive, or 0x2 and 0xea5f in hexadecimal, inclusive.

The maximum length is 10 characters, including optional leading zeros.

## Examples

The following example demonstrates the markup for a [**Command**](windowsribbon-element-command.md) element with a **Command.Id** declaration.


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



 

 





