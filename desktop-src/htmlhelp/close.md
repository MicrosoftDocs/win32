---
title: Close
description: Closes the window in which the current topic appears.
ms.assetid: 435057B3-6184-447c-915E-7EF9DBAB71DB
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Close

Closes the window in which the current topic appears.

You can use the Close command to close a secondary window that does not include a Close button.

The Close command could also be used with a help wizard. For example, a user could answer the question "Did this solve your problem?" by clicking **No**, which would link to the next topic, or clicking **Yes**, which would close the window.

This command can be used only with a compiled help (.chm) file.

## Syntax

``` syntax
<PARAM  name="Command" value="Close">
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

Calls the Close command.

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
   <PARAM name="Command" value="Close">
   <PARAM name="Button" value="Text:Close this window!">
</OBJECT>
```



## Remarks

-   The **Button** parameter is omitted when this command is invoked by a script.

## Related topics

<dl> <dt>

[About commands](about-commands.md)
</dt> </dl>

 

 




