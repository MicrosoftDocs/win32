---
title: Ribbon.HelpButton property
description: Represents a container for the Help Button.
ms.assetid: a64239b2-2440-4bcf-8fd7-079003de6d8c
keywords:
- Ribbon.HelpButton property Windows Ribbon
topic_type:
- apiref
api_name:
- Ribbon.HelpButton
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ribbon.HelpButton property

Represents a container for the [Help Button](windowsribbon-controls-helpbutton.md).

## Usage

``` syntax
<Ribbon.HelpButton>
  child elements
</Ribbon.HelpButton>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                           | Description                                   |
|-------------------------------------------------------------------|-----------------------------------------------|
| [**HelpButton**](windowsribbon-element-helpbutton.md)<br/> | May occur at most once<br/> <br/> |



## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Ribbon**](windowsribbon-element-ribbon.md).

## Examples

The following example demonstrates the basic markup that is required to implement a Ribbon Help button.

This section of code shows the **Ribbon.HelpButton** Command declaration.


```XML
<Command Name="cmdHelp"
         Symbol="IDR_CMD_HELP">      
</Command>
```



This section of code shows the **Ribbon.HelpButton** control declaration.


```XML
<Ribbon.HelpButton>
  <HelpButton CommandName="cmdHelp"/>
</Ribbon.HelpButton>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





