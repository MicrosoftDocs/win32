---
title: Command.Keytip property
description: Represents the keytip for a control.
ms.assetid: 214f69ae-dd35-4abf-b294-d898d7802aa6
keywords:
- Command.Keytip property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.Keytip
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.Keytip property

Represents the keytip for a control.

## Usage

``` syntax
<Command.Keytip>
  child elements
</Command.Keytip>
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

May occur at most once for each [**Command**](windowsribbon-element-command.md) element.

**Command.Keytip** can contain a value of type *xs:string* constrained to any sequence of Unicode characters, including white space.

A **Command.Keytip** can begin with a number only when associated with a control within a [Tab](windowsribbon-controls-tab.md) or the [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md).

To display the keytips that are valid for the current state of the ribbon, press and hold the ALT key. The following screen shot shows the initial, or first level, keytips that are displayed in Microsoft Paint for Windows 7. After a first-level keytip has been selected, only second-level keytips are displayed.

![first-level keytips in microsoft paint for windows 7](images/properties/ui-pkey-label-keytips.png)

**Command.Keytip** acts as the keyboard accelerator for a command unless that command is exposed through a menu item. In this case, the framework ignores the **Command.Keytip** value and instead uses a character preceded by an ampersand as specified by [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) or [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md). If no ampersand is specified by **Command.LabelTitle** or UI\_PKEY\_Label, no keytip or keyboard accelerator is exposed.

If no value is supplied for **Command.Keytip**, the [**String**](windowsribbon-element-string.md) child element is required.

> [!Note]  
> If **Command.Keytip** contains both a value and a [**String**](windowsribbon-element-string.md) child element, **String** takes precedence.

 

By default, the following letters are used by the framework to automatically generate keytips:

-   **F** is assigned to the [Application Menu](windowsribbon-controls-applicationmenu.md).
-   **Y** is assigned to any command that does not have a keytip specified by the application.
-   **Z** is assigned to each [Group](windowsribbon-controls-group.md) control and cannot be customized. A Group keytip is displayed only when the [**ScalingPolicy**](windowsribbon-element-scalingpolicy.md) for the control specifies a **Popup** size option. For more information, see [Customizing a Ribbon Through Size Definitions and Scaling Policies](windowsribbon-templates.md).

> [!Note]  
> None of these letters are reserved by the framework. Each can be assigned to one or more commands as required.

 

The framework resolves keytip conflicts in the following ways:

-   If one or more [Tab](windowsribbon-controls-tab.md) controls are associated with the same keytip, a number is appended to each keytip, starting at 1, and increasing sequentially (2, 3,...) for each control in the order of declaration. If any Tab controls are assigned the letter F as a keytip, the [Application Menu](windowsribbon-controls-applicationmenu.md) is assigned F1 with the remaining keytips adjusted as described.
-   When associated with a single control within a [Tab](windowsribbon-controls-tab.md), the keytip F is valid for both the control and the [Application Menu](windowsribbon-controls-applicationmenu.md). The default Application Menu keytip is not changed, but precedence is given to the control on the active tab.
-   If one or more controls within a [Tab](windowsribbon-controls-tab.md) are associated with the same keytip, the framework automatically refactors the keytips of those controls, as described previously.

> [!Note]  
> A slight variation in text color is used to highlight refactored keytips in a standard ribbon implementation. For a nonstandard ribbon implementation where the ribbon color has been customized, this framework behavior is overridden and all keytips are displayed with the same text color. For more information, see [Customizing Ribbon Colors](ribbon-color.md).

 

The maximum length is unbounded.

## Examples

The following example demonstrates the markup for a [**Command**](windowsribbon-element-command.md) element with a **Command.Keytip** declaration.


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

[UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)
</dt> </dl>

 

 





