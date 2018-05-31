---
title: TCard
description: Sends a Windows WM\_TCARD message to the calling program to invoke a training card topic or to perform some other action.
ms.assetid: B9A09DBA-7200-4b12-810F-EE171D0C7236
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TCard

Sends a Windows **WM\_TCARD** message to the calling program to invoke a training card topic or to perform some other action.

Training cards are help topics that interact with the calling program by sending the appropriate message parameters via **WM\_TCARD** in response to a user action, such as clicking a button within the help window. The calling program then handles the message and responds by performing a specific action. The action can be anything from calling an HTML Help API function to opening an application dialog box.

Typical uses of training cards include guiding users through the steps of a certain task or a troubleshooting process.

This command can be used only with a compiled help (.chm) file.

## Syntax

``` syntax
<PARAM  name="Command" value="TCard">
<PARAM  name="Item1"   value="<i>wPARAM</i>, <i>lPARAM</i>">
[<PARAM name="Button"  value="[Text: <i>Button text</i>|Bitmap: <i>Bitmap file path</i>|Icon:<i>Icon file path</i>]">]
[<PARAM name="Text"    value="Text: <i>Link text</i>">]
[<PARAM name="Font"    value="<i>Facename[, point size[, charset[, color[, PLAIN BOLD ITALIC UNDERLINE]]]]</i>">]
```

## Properties

<dl> <dt>

<span id="Button"></span><span id="button"></span><span id="BUTTON"></span>[Button](button-parameter.md)
</dt> <dd>

Specifies the button style. Optional.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>[Command](command-parameter.md)
</dt> <dd>

Calls the TCard command.

</dd> <dt>

<span id="Font"></span><span id="font"></span><span id="FONT"></span>[Font](font-parameter.md)
</dt> <dd>

Specifies the font attributes. Optional.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the *wPARAM* and the *lPARAM* parameter values to pass to the **WM\_TCARD** message.

*wPARAM* usually identifies a user action; this value must be numeric

*lPARAM* may contain additional data, depending on the value of *wPARAM*; this value may be numeric or string.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>[Text](text-parameter.md)
</dt> <dd>

Specifies the link text. Optional.

</dd> </dl>

## Example


```
<OBJECT
   id=training
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100
   height=100
>
   <PARAM name="Command" value="TCard">
   <PARAM name="Button" value="Text: This is a training card">
   <PARAM name="Item1" value="5555, MyText">
</OBJECT>
```



## Remarks

-   The TCard command accepts both numeric and string arguments.
-   To call the TCard command multiple times using a scripting language, use the [TCard method](tcard-method.md).
-   To implement training card topics, code must be added to the calling program to handle **WM\_TCARD** messages.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




