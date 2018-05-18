---
title: Shortcut
description: Creates a shortcut to a specified action by passing Windows-based messages and parameters.
ms.assetid: 'CD76BCC4-7F0E-4eaa-AF9C-9EB310109DA5'
---

# Shortcut

Creates a shortcut to a specified action by passing Windows-based messages and parameters. For example, if a topic discusses a procedure that involves a specific dialog box, you can provide a link that a user can click in the topic to open the dialog box in the program.

This command can be used only with a compiled help (.chm) file.

## Syntax

``` syntax
<PARAM  name="Command" value="ShortCut">
<PARAM  name="Item1"   value=",<i>program name</i>,<i>parameters</i>">
<PARAM  name="Item2"   value="<i>message ID</i>,<i>wPARAM</i>,<i>lPARAM</i>">
[<PARAM name="Button"  value="[Text: <i>Button text</i>|Bitmap: <i>Bitmap file path</i>|Icon:<i>Icon file path</i>]">]
[<PARAM name="Font"    value="<i>Facename[, point size[, charset[, color[, PLAIN BOLD ITALIC UNDERLINE]]]]</i>">]
[<PARAM name="Text"    value="Text: <i>Link text</i>">]
```

## Properties

<dl> <dt>

<span id="Button"></span><span id="button"></span><span id="BUTTON"></span>[Button](button-parameter.md)
</dt> <dd>

Specifies the button style. Optional.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>[Command](command-parameter.md)
</dt> <dd>

Calls the Shortcut command.

</dd> <dt>

<span id="Font"></span><span id="font"></span><span id="FONT"></span>[Font](font-parameter.md)
</dt> <dd>

Specifies the font attributes. Optional.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the file path to the executable file (.exe) for the program, and any parameters to be sent to the program. These values are delimited by a comma.

HTML Help does not support %WINDIR% or other system variables in the file path.

</dd> <dt>

<span id="Item2"></span><span id="item2"></span><span id="ITEM2"></span>[Item2](item-parameter.md)
</dt> <dd>

Specifies the message ID of a standard Windows message, a *wPARAM* value, and a *lPARAM* value. These values are delimited by a comma.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example


```
<OBJECT
   id=shortcut
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="ShortCut">
   <PARAM name="Button" value="Bitmap:shortcut">
   <PARAM name="Item1" value="notepad,notepad.exe,">
   <PARAM name="Item2" value="273,1,1">
</OBJECT>
```



## Remarks

The **Button** parameter is omitted when this command is invoked by a script.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




