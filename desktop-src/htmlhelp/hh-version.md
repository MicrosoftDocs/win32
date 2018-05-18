---
title: HH Version
description: Displays the version number of the HTML Help ActiveX control (Hhctrl.ocx) in a dialog box.
ms.assetid: '6F6CD51D-EDAA-4235-9998-4C258329B544'
---

# HH Version

Displays the version number of the HTML Help ActiveX control (Hhctrl.ocx) in a dialog box.

This command helps users to determine whether they are using the most current version of HTML Help.

This command can be used with either a compiled help (.chm) file or uncompiled HTML files.

## Syntax

``` syntax
<PARAM  name="Command" value="HH Version">
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

Calls the HH Version command.

</dd> <dt>

<span id="Font"></span><span id="font"></span><span id="FONT"></span>[Font](font-parameter.md)
</dt> <dd>

Specifies the font attributes. Optional.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example


```
<OBJECT
   id=MyControl
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="HH Version">
   <PARAM name="Button" value="Text:Click for version number">
</OBJECT>
```



 

 




