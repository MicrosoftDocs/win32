---
title: Command.LabelTitle property
description: Represents a label title.
ms.assetid: 97378ec3-7988-4e39-9cf5-c382b246c5c9
keywords:
- Command.LabelTitle property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.LabelTitle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.LabelTitle property

Represents a label title.

## Usage

``` syntax
<Command.LabelTitle>
  child elements
</Command.LabelTitle>
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

**Command.LabelTitle** can contain a value of type *xs:string* constrained to any sequence of characters, including white space and line-break characters.

> [!Note]  
> Use the Universal Character Set (UCS) XML character reference `&#xA;` to specify a line break.

 

The maximum length is unbounded.

If no value is supplied for **Command.LabelTitle**, the [**String**](windowsribbon-element-string.md) child element is required.

> [!Note]  
> If **Command.LabelTitle** contains both a value and a [**String**](windowsribbon-element-string.md) child element, **String** takes precedence.

 

**Command.LabelTitle** only supports left alignment.

If a Command is exposed through a menu item and the value of **Command.LabelTitle** or [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md) contains a letter preceded by an ampersand, as shown in the following example, this letter is treated as both a keytip and a keyboard accelerator for that Command by the Ribbon framework.


```XML
<Command Name="cmdNew"
         Symbol="ID_FILE_NEW"
         Comment="New"
         Id="25001"
         LabelTitle="&amp;New"/>
```



To display an ampersand in a label, escape the special character designation with a double ampersand (`&&`) as shown in the following example.


```XML
<Command Name="cmdOpen"
         Symbol="ID_FILE_OPEN"
         Comment="Open"
         Id="25002"
         LabelTitle="&amp;&amp;Open"/>
```



## Examples

The following example demonstrates the markup for a [**Command**](windowsribbon-element-command.md) element with a **Command.LabelTitle** declaration.


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

[UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)
</dt> </dl>

 

 





