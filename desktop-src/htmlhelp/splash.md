---
title: Splash
description: Displays an image for a specified number of seconds when the file that contains the HTML Help ActiveX control is opened.
ms.assetid: 'B6B67828-B844-46d1-92C6-19755C158670'
---

# Splash

Displays an image for a specified number of seconds when the file that contains the HTML Help ActiveX control is opened. For example, using the **Splash** command, you could display a product logo or welcome message when a compiled help (.chm) file or Web page is first opened.

This command can be used with either a compiled help file or uncompiled HTML files.

## Syntax

``` syntax
<PARAM  name="Command" value="Splash">
<PARAM  name="Item1"   value="<i>image file path</i>">
<PARAM  name="Item2"   value="<i>millisecond value</i>">
[<PARAM name="Item3"   value="<i>alternate image file path</i>">]
```

## Properties

<dl> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>[Command](command-parameter.md)
</dt> <dd>

Calls the **Splash** command.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the image file path. Supported image file formats are .gif, .jpeg, or .bmp.

</dd> <dt>

<span id="Item2"></span><span id="item2"></span><span id="ITEM2"></span>[Item2](item-parameter.md)
</dt> <dd>

Specifies the length of time to display the image in milliseconds (1000 milliseconds = 1 second).

</dd> <dt>

<span id="Item3"></span><span id="item3"></span><span id="ITEM3"></span>[Item3](item-parameter.md)
</dt> <dd>

Specifies an alternate image file to display if the user's display configuration supports more than 256 colors. Optional.

</dd> </dl>

## Example


```
<OBJECT
   id=splash
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
>
   <PARAM name="Command" value="Splash">
   <PARAM name="Item1" value="test.gif">
   <PARAM name="Item2" value="5000">
</OBJECT>
```



## Sample Splash command

Click [here](splash-command-example.md) to see a Splash screen.

## Remarks

-   You should insert the HTML Help ActiveX control between the **&lt;BODY&gt;** start and end tags of the file. Use of the control within the **&lt;FRAMESET&gt;** start and end tags is currently not supported. If you want to use the **Splash** command with a frameset, insert the control within the default HTML file that is specified in the frameset document.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




