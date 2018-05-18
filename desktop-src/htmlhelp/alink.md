---
title: ALink
description: Creates Associative links (ALinks) that jump to target HTML files that contain the specified ALink names. The list of target topics appears on a pop-up menu or in a dialog box.
ms.assetid: '00AAC497-60F6-4a64-8B55-A8A8C8601F12'
---

# ALink

Creates Associative links (ALinks) that jump to target HTML files that contain the specified ALink names. The list of target topics appears [on a pop-up menu or in a dialog box](window-types.md).

This command can be used only with a compiled help (.chm) file.

## Syntax

``` syntax
<PARAM  name="Command"       value="ALink [,menu|,dialog]">;
<PARAM  name="Item1"         value="<i>.chm file path</i>">;
<PARAM  name="Item2"         value="<i>ALink text</i>">;
[<PARAM name="Button"        value="[Text: <i>Button text</i>|Bitmap:<i>Bitmap file path</i>|Icon:<i>Icon file path</i>]">]
[<PARAM name="DefaultTopic" value="<i>File name or HTTP URL</i>">]
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

Calls the ALink command and specifies whether to display target topics [on a pop-up menu or in a dialog box](window-types.md).

If you do not specify a display option, a dialog box appears by default.

To specify the **Topics Found** dialog box, type **dialog**.

To specify a pop-up menu, type **menu**.

</dd> <dt>

<span id="DefaultTopic"></span><span id="defaulttopic"></span><span id="DEFAULTTOPIC"></span>[DefaultTopic](default-topic-parameter.md)
</dt> <dd>

Specifies the topic to navigate to if the look up fails. Optional.

</dd> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>[Flags](flags-parameter.md)
</dt> <dd>

Specifies how to behave if only one target is found or if the target is unavailable.

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

Specifies the compiled help file that contains the target topics.

</dd> <dt>

<span id="Item2"></span><span id="item2"></span><span id="ITEM2"></span>[Item2](item-parameter.md)
</dt> <dd>

Specifies the text for one ALink name. This text must match an ALink name that has previously been inserted into one or more topics using the **Compiler Information** feature.

Subsequent ALink names are specified as Item3, Item4, etc.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example

Note that in this example ALink targets will appear in the Topics Found dialog box because neither dialog nor menu is specified in the **Command** parameter value.


```
<OBJECT
   id=MyControl
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="ALink">
   <PARAM name="Button" value="Text:See Also">
   <PARAM name="Item1" value="c:\Help\MyFile.chm">
   <PARAM name="Item2" value="overview">
   <PARAM name="Item3" value="bibliography">
</OBJECT>
```



## Sample ALink command

HTML Help ActiveX control overview topics

-   [Overview topic template](about-the-overview-topic-template.md)
-   [Decision topic template](about-the-decision-topic-template.md)
-   [Multi-step procedure topic template](about-the-procedure-topic-template.md)
-   [One-step procedure topic template](about-the-one-step-procedure-topic-template.md)
-   [Source-code example topic template](about-the-source-code-example-topic-template.md)

## Remarks

-   The **Button** parameter is omitted when this command is invoked by a script.
-   To add ALink names to an HTML file, use the **Compiler Information** command, which is available on the **Edit** menu of HTML Help Workshop.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




