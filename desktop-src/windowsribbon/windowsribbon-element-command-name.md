---
title: Command.Name property
description: Represents the name of a Command.
ms.assetid: 36fb0b93-143f-4706-8c32-e6c818cce16f
keywords:
- Command.Name property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.Name
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.Name property

Represents the name of a Command.

## Usage

``` syntax
<Command.Name/>
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

**Command.Name** is referenced in markup to associate a Command with a control through the *CommandName* attribute of the control.

This element contains a value of type *xs:string*.

The value is constrained to a string that consists of a letter or underscore followed by any sequence of letters, digits, and underscores.

The maximum length is 100 characters.

## Examples

The following example demonstrates the markup for a [**Command**](windowsribbon-element-command.md) element with a **Command.Name** declaration.


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



 

 





