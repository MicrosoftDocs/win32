---
title: ACCELERATORS resource
description: Defines one or more accelerators for an application. An accelerator is a keystroke defined by the application to give the user a quick way to perform a task.
ms.assetid: 5953ee2d-b7a7-45d2-8445-4cba1207e272
keywords:
- ACCELERATORS resource Menus and Other Resources
topic_type:
- apiref
api_name:
- ACCELERATORS
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ACCELERATORS resource

Defines one or more accelerators for an application. An accelerator is a keystroke defined by the application to give the user a quick way to perform a task.

``` syntax
acctablename ACCELERATORS [optional-statements] {event, idvalue, [type] [options]... }
```

## Parameters

<dl> <dt>

<span id="acctablename"></span><span id="ACCTABLENAME"></span>*acctablename*
</dt> <dd>

Unique name or a 16-bit unsigned integer value that identifies the resource.

</dd> <dt>

<span id="optional-statements"></span><span id="OPTIONAL-STATEMENTS"></span>*optional-statements*
</dt> <dd>

Zero or more of the following statements.



| Statement                                                        | Description                                                                                                                                                                             |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CHARACTERISTICS**](characteristics-statement.md) *dword*     | User-defined information about a resource that can be used by tools that read and write resource files. For more information, see [**CHARACTERISTICS**](characteristics-statement.md). |
| [**LANGUAGE**](language-statement.md) *language*, *sublanguage* | Specifies the language for the resource. For more information, see [**LANGUAGE**](language-statement.md).                                                                              |
| [**VERSION**](version-statement.md) *dword*                     | User-defined version number for the resource that can be used by tools that read and write resource files. For more information, see [**VERSION**](version-statement.md).              |



 

</dd> <dt>

<span id="event"></span><span id="EVENT"></span>*event*
</dt> <dd>

Keystroke to be used as an accelerator. It can be any one of the following character types.



| Type                    | Description                                                                                                                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "*char*"                | A single character enclosed in double quotation marks ("). The character can be preceded by a caret (^), meaning that the character is a control character.                                                                                  |
| *Character*             | An integer value representing a character. The *type* parameter must be **ASCII**.                                                                                                                                                           |
| *virtual-key character* | An integer value representing a virtual key. The virtual key for alphanumeric keys can be specified by placing the uppercase letter or number in double quotation marks (for example, "9" or "C"). The *type* parameter must be **VIRTKEY**. |



 

</dd> <dt>

<span id="idvalue"></span><span id="IDVALUE"></span>*idvalue*
</dt> <dd>

a 16-bit unsigned integer value that identifies the accelerator.

</dd> <dt>

<span id="type"></span><span id="TYPE"></span>*type*
</dt> <dd>

Required only when the *event* parameter is a *character* or a *virtual-key character*. The *type* parameter specifies either **ASCII** or **VIRTKEY**; the integer value of *event* is interpreted accordingly. When **VIRTKEY** is specified and *event* contains a string, *event* must be uppercase.

</dd> <dt>

<span id="options"></span><span id="OPTIONS"></span>*options*
</dt> <dd>

options that define the accelerator. This parameter can be one or more of the following values.



| Option                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NOINVERT**                       | Specifies that no top-level menu item is highlighted when the accelerator is used. This is useful when defining accelerators for actions such as scrolling that do not correspond to a menu item. If **NOINVERT** is omitted, a top-level menu item will be highlighted (if possible) when the accelerator is used. This attribute is obsolete and retained only for backward compatibility with resource files designed for 16-bit Windows. |
| **ALT**                            | Causes the accelerator to be activated only if the ALT key is down. Applies only to virtual keys.                                                                                                                                                                                                                                                                                                                                            |
| **SHIFT**                          | Causes the accelerator to be activated only if the SHIFT key is down. Applies only to virtual keys                                                                                                                                                                                                                                                                                                                                           |
| [**CONTROL**](control-control.md) | Defines the character as a control character (the accelerator is only activated if the CONTROL key is down). This has the same effect as using a caret (^) before the accelerator character in the *event* parameter. Applies only to virtual keys                                                                                                                                                                                           |



 

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Remarks

The [**TranslateAccelerator**](/windows/win32/api/winuser/nf-winuser-translateacceleratora) function is used to translate accelerator messages from the application queue into [**WM\_COMMAND**](./wm-command.md) or [**WM\_SYSCOMMAND**](./wm-syscommand.md) messages.

## Examples

The following example demonstrates the use of accelerator keys.

``` syntax
1 ACCELERATORS
{
  "^C",  IDDCLEAR         ; control C
  "K",   IDDCLEAR         ; shift K
  "k",   IDDELLIPSE, ALT  ; alt k
  98,    IDDRECT, ASCII   ; b
  66,    IDDSTAR, ASCII   ; B (shift b)
  "g",   IDDRECT          ; g
  "G",   IDDSTAR          ; G (shift G)
  VK_F1, IDDCLEAR, VIRTKEY                ; F1
  VK_F1, IDDSTAR, CONTROL, VIRTKEY        ; control F1
  VK_F1, IDDELLIPSE, SHIFT, VIRTKEY       ; shift F1
  VK_F1, IDDRECT, ALT, VIRTKEY            ; alt F1
  VK_F2, IDDCLEAR, ALT, SHIFT, VIRTKEY    ; alt shift F2
  VK_F2, IDDSTAR, CONTROL, SHIFT, VIRTKEY ; ctrl shift F2
  VK_F2, IDDRECT, ALT, CONTROL, VIRTKEY   ; alt control F2
}
```

## See also

<dl> <dt>

[Using Keyboard Accelerators](./using-keyboard-accelerators.md)
</dt> <dt>

[**TranslateAccelerator**](/windows/win32/api/winuser/nf-winuser-translateacceleratora)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**DIALOG**](dialog-resource.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 