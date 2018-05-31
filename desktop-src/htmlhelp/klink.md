---
title: KLink
description: Creates Keyword links (KLinks) that jump to target HTML files that contain the specified keyword(s). The list of target topics appears on a pop-up menu or in a dialog box.
ms.assetid: 60EBA705-DFD8-4af2-B2AB-4F07824F0E00
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# KLink

Creates Keyword links (KLinks) that jump to target HTML files that contain the specified keyword(s). The list of target topics appears [on a pop-up menu or in a dialog box](window-types.md).

This command can be used only with a compiled help (.chm) file.

## Syntax

``` syntax
<PARAM  name="Command"       value="KLink [,menu|,dialog]">
<PARAM  name="Item1"         value="<i>.chm file path</i>">
<PARAM  name="Item2"         value="<i>keyword text</i>">
[<PARAM name="Button"        value="[Text: <i>Button text</i>|Bitmap: <i>Bitmap file path</i>|Icon:<i>Icon file path</i>]">]
[<PARAM name="Default Topic" value="<i>File name or HTTP URL</i>">]
[<PARAM name="Font"          value="<i>Facename[, point size[, charset[, color[, PLAIN BOLD ITALIC UNDERLINE]]]]</i>">]
[<PARAM name="Flags"         value=",,1">]
[<PARAM name="Flags"         value="1">]
[<PARAM name="Frame"         value="<i>Frame Name</i>">]
[<PARAM name="Text"          value="Text: <i>Link text</i>">]
```

## Properties

<dl> <dt>

<span id="Button"></span><span id="button"></span><span id="BUTTON"></span>[Button](button-parameter.md)
</dt> <dd>

Specifies the button style. Optional.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>[Command](command-parameter.md)
</dt> <dd>

Calls the KLink command and specifies whether to display target topics [on a pop-up menu or in a dialog box](window-types.md).

If you do not specify a display option, a dialog box appears by default.

To specify the **Topics Found** dialog box, type **dialog**.

To specify a pop-up menu, type **menu**.

</dd> <dt>

<span id="Default_Topic"></span><span id="default_topic"></span><span id="DEFAULT_TOPIC"></span>[Default Topic](default-topic-parameter.md)
</dt> <dd>

Specifies the topic to navigate to if the look up fails. Optional.

</dd> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>[Flags](flags-parameter.md)
</dt> <dd>

Specifies how the command will behave if only one target is found or the target is unavailable.

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

Specifies the compiled help (.chm) file that contains the target topics.

</dd> <dt>

<span id="Item2"></span><span id="item2"></span><span id="ITEM2"></span>[Item2](item-parameter.md)
</dt> <dd>

Specifies a keyword. This text must match a keyword that has previously been inserted into one or more topics using the **Compiler Information** command.

Subsequent keywords are specified as Item3, Item4, etc.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example

Note that KLink targets will appear on a pop-up menu in this example because menu is specified in the **Command** parameter.


```
<OBJECT
   id=MyControl
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="KLink, menu">
   <PARAM name="Button" value="Text:Animal Diets">
   <PARAM name="Item1" value="animals.chm">
   <PARAM name="Item2" value="omnivore">
   <PARAM name="Item3" value="carnivore">
</OBJECT>
```



## Remarks

-   The **Button** parameter is omitted when this command is invoked by a script.
-   To add keywords to a target HTML file, use the **Compiler Information** command, which is available on the **Edit** menu of HTML Help Workshop.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




