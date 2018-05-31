---
title: Related Topics
description: Displays a list of target topics that a user can jump to. The Item parameter stores information about each target. The list of target topics appears on a pop-up menu or in a dialog box.
ms.assetid: F0C4B216-23C8-4eee-885A-6460A0C3F49F
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Related Topics

Displays a list of target topics that a user can jump to. The **Item** parameter stores information about each target. The list of target topics appears [on a pop-up menu or in a dialog box](window-types.md).

This command can be used with either a compiled help (.chm) file or uncompiled HTML files.

## Syntax

``` syntax
<PARAM  name="Command" value="Related Topics [,menu|,dialog]">
<PARAM  name="Item1"   value="<i>Topic1;Main URL for Topic1;Alternate URL for Topic1</i>">
[<PARAM name="Button"  value="[Text: <i>Button text</i>|Bitmap: <i>Bitmap file path</i>|Icon:<i>Icon file path</i>]">]
[<PARAM name="Font"    value="<i>Facename[, point size[, charset[, color[, PLAIN BOLD ITALIC UNDERLINE]]]]</i>">]
[<PARAM name="Frame"   value="<i>Frame Name</i>">]
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

Calls the Related Topics command and specifies whether to display target topics [on a pop-up menu or in a dialog box](window-types.md).

If you do not specify a display option, a dialog box appears by default.

To specify the **Topics Found** dialog box, type **dialog**.

To specify a pop-up menu, type **menu**.

</dd> <dt>

<span id="Font"></span><span id="font"></span><span id="FONT"></span>[Font](font-parameter.md)
</dt> <dd>

Specifies the font attributes. Optional.

</dd> <dt>

<span id="Frame"></span><span id="frame"></span><span id="FRAME"></span>[Frame](frame-parameter.md)
</dt> <dd>

Specifies the frame in which to display the selected topic. Optional.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the following information about the target topic:

-   Topic title as you want it to appear in the Topics Found dialog box or on a pop-up menu.
-   Topic file path.
-   Alternate topic to display if the first topic is unavailable.

Multiple values are delimited by a semicolon.

To specify subsequent topic information, use Item2, Item3, etc.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example


```
<OBJECT
   id=candomble
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="Related Topics, MENU">
   <PARAM name="Button" value="Text:See Also">
   <PARAM name="Item1" value="About Oxala;oxala.html;http://example.microsoft.com/">
   <PARAM name="Item2" value="About Yemanja;Yemanja.html;http://example.microsoft.com/">
   <PARAM name="Item3" value="About Oba;oba.html;http://example.microsoft.com/">
   <PARAM name="Item4" value="About Ogum;ogum.html;http://example.microsoft.com/">
   <PARAM name="Item5" value="Bad Link;bad_link.html;http://example.microsoft.com/">
</OBJECT>
```



## Remarks

-   The **Button** parameter is omitted when this command is invoked by a script.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




