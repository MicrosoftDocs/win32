---
title: TextPopup Method
description: Use the TextPopup method to open a pop-up window.
ms.assetid: 039C0F02-37D4-4e60-B45E-BBACC900A410
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TextPopup Method

Use the TextPopup method to open a pop-up window.

The instance of the HTML Help ActiveX control that you reference using the TextPopup method does not need to specify a [command](about-commands.md).

This method can be used with either a compiled help (.chm) file or uncompiled HTML files.

## Applies to

This method is independent of any of the HTML Help ActiveX control commands.

## Syntax

``` syntax
TextPopup(BSTR <i>pszText</i>, BSTR <i>pszFont</i>, int <i>horzMargins</i>, int <i>vertMargins</i>, COLORREF <i>clrForeground</i>, COLORREF <i>clrBackground</i>)
```

## Parameters

<dl> <dt>

<span id="pszText_"></span><span id="psztext_"></span><span id="PSZTEXT_"></span>*pszText* 
</dt> <dd>

A string variable that specifies the text to display in the pop-up window.

</dd> <dt>

<span id="pszFont_"></span><span id="pszfont_"></span><span id="PSZFONT_"></span>*pszFont* 
</dt> <dd>

A string variable that specifies the following font attributes:

-   Font family
-   Point size
-   Character set
-   Color
-   Format options

The format is as follows:


```
<i>Facename</i>[, <i>point size</i>[, <i>charset</i>[, PLAIN BOLD ITALIC UNDERLINE]]]
```



The default font settings are: "Helvetica,12,,PLAIN"

</dd> <dt>

<span id="horzMargins_"></span><span id="horzmargins_"></span><span id="HORZMARGINS_"></span>*horzMargins* 
</dt> <dd>

An integer that determines, in pixels, the side margins relative to the center of the pop-up window.

</dd> <dt>

<span id="vertMargins_"></span><span id="vertmargins_"></span><span id="VERTMARGINS_"></span>*vertMargins* 
</dt> <dd>

An integer that determines, in pixels, the top and bottom margins relative to the center of the pop-up window.

</dd> <dt>

<span id="clrForeground_"></span><span id="clrforeground_"></span><span id="CLRFOREGROUND_"></span>*clrForeground* 
</dt> <dd>

Specifies the color of the text in RRGGBB format. To specify the default text color (black), type **-1**.

</dd> <dt>

<span id="clrBackground_"></span><span id="clrbackground_"></span><span id="CLRBACKGROUND_"></span>*clrBackground* 
</dt> <dd>

Specifies the background color of the pop-up window in RRGGBB format. To specify the default background color (pale yellow), type **-1**.

</dd> </dl>

## Example

The code for the control:


```
<OBJECT
   id=sample 
   type="application/x-oleobject" 
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
>
<PARAM name="Command" value="HH Version">
</OBJECT>
```



The JavaScript code to specify the text and font variables:


```
<script> 
FontFace="Verdana,8,,bold" 
TopicText="This is an HTML Help pop-up window. This window can display text only." 
TopicText2="This is another HTML Help pop-up window." 
</script> 
```



The JavaScript code to invoke the control:


```
<a href="JavaScript:test.TextPopup (TopicText, FontFace, 10,10,10,10)"> TextPopup Example</a> 
```



## Remarks

-   Colors do not display properly.
-   You can store text variables in a separate text file with a .js extension.

## Related topics

<dl> <dt>

[About the HTML Help ActiveX Control Methods](about-methods.md)
</dt> </dl>

 

 




