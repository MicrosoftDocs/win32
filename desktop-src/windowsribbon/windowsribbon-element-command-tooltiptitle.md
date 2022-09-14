---
title: Command.TooltipTitle property
description: Represents a tooltip title.
ms.assetid: b06a7a6a-fbdd-464b-b804-e62912d6e176
keywords:
- Command.TooltipTitle property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.TooltipTitle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.TooltipTitle property

Represents a tooltip title.

## Usage

``` syntax
<Command.TooltipTitle>
  child elements
</Command.TooltipTitle>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                   | Description                                   |
|-----------------------------------------------------------|-----------------------------------------------|
| [**String**](windowsribbon-element-string.md)<br/> | May occur at most once<br/> <br/> |



## Parent elements



| Element                                                     |
|-------------------------------------------------------------|
| [**Command**](windowsribbon-element-command.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Command**](windowsribbon-element-command.md).

**Command.TooltipTitle** can contain a value of type *xs:string* constrained to any sequence of characters, including white space and line-break characters.

> [!Note]  
> Use the Universal Character Set (UCS) XML character reference `&#xA;` to specify a line break.

 

The maximum length is unbounded.

If no value is supplied for **Command.TooltipTitle**, the [**String**](windowsribbon-element-string.md) child element is required.

> [!Note]  
> If **Command.TooltipTitle** contains both a value and a [**String**](windowsribbon-element-string.md) child element, **String** takes precedence.

 

**Command.TooltipTitle** only supports left alignment.

## Examples

The following example demonstrates the markup for a [**Command**](windowsribbon-element-command.md) element with a **Command.TooltipTitle** declaration.


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



## See also

<dl> <dt>

[UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)
</dt> </dl>

 

 





