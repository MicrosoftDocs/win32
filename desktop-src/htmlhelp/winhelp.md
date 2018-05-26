---
title: WinHelp
description: Displays a WinHelp topic in the WinHelp primary window, a WinHelp secondary window, or in a WinHelp pop-up window.
ms.assetid: C637D6BA-4A2A-4d37-BCF8-4ABFA50F1568
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WinHelp

Displays a WinHelp topic in the WinHelp primary window, a WinHelp secondary window, or in a WinHelp pop-up window. The specific window attributes, such as size and position, background color, and button bar items, are based on the definitions in the \[WINDOWS\] section of the specified WinHelp project (.hpj) file.

This command can be used only with a compiled help (.chm) file.

## Syntax

``` syntax
<PARAM  name="Command" value="WinHelp [,Popup]>
<PARAM  name="Item2"   value="<i>topic ID</i>|<i>map number</i>">
<PARAM  name="Item1"   value="<i>WinHelp (.hlp) file path</i> [><i>window name</i>]">
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

Calls the WinHelp command and specifies a [WinHelp window type](winhelp-window-types.md).

-   To display a pop-up WinHelp window, type **Popup**.
-   To display a secondary WinHelp window, do not specify a window type and specify a window name in the **Item1** parameter.
-   To display the WinHelp main window, do not specify a window type or a window name (in the **Item1** parameter).

</dd> <dt>

<span id="Font"></span><span id="font"></span><span id="FONT"></span>[Font](font-parameter.md)
</dt> <dd>

Specifies the font attributes. Optional.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the file path of the WinHelp (.hlp) file in which the WinHelp topic is stored, and the window name of the target window.

The window name must be preceded by the "&gt;" character.

Do not specify a window name if you typed **Popup** in the **Command** parameter or if you want the topic to appear in the WinHelp main window.

</dd> <dt>

<span id="Item2"></span><span id="item2"></span><span id="ITEM2"></span>[Item2](item-parameter.md)
</dt> <dd>

Specifies the topic ID or map number of the WinHelp topic to display.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example


```
<OBJECT
   id=winhelp
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="WinHelp">
   <PARAM name="Button" value="Text: Candomble Overview">
   <PARAM name="Item1" value="c:\winhelp\candomble_wh.hlp>MyWindow">
   <PARAM name="Item2" value="myth_candomble_overview">
</OBJECT>
```



## Remarks

-   The **Button** parameter is omitted when this command is invoked by a script.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




