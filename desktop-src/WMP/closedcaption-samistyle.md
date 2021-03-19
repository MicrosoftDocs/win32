---
title: ClosedCaption.SAMIStyle
description: The SAMIStyle property specifies or retrieves the closed captioning style.
ms.assetid: 5535fb31-f1c0-49c4-b758-df74964b1e67
keywords:
- ClosedCaption.SAMIStyle Windows Media Player
topic_type:
- apiref
api_name:
- ClosedCaption.SAMIStyle
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.SAMIStyle

The **SAMIStyle** property specifies or retrieves the closed captioning style.

``` syntax
player.closedCaption.SAMIStyle
```

## Possible Values

This property is a read/write **String**.

## Remarks

A SAMI file can contain several format style definitions. SAMI styles are defined between the <STYLE> and </STYLE> tags in the SAMI file. A style is defined with a text string preceded by a \# character. For example:


```
#Emphasis1 {Name: Big Bold Italic; font-size: 14pt; text-align: center;
            color: blue; font-family: sans-serif; font-weight: bold;
            font-style: italic;}

```



This specifies a style that produces a particular font.

If no SAMI style is specified, the first style defined in the SAMI file is used by default.

**Windows Media Player 10 Mobile:** This property is read only, and always returns an empty string.

## Examples

The following JScript example creates an HTML SELECT element that uses *closedCaption*.**SAMIStyle** to change the appearance of the closed caption text. The **Player** object was created with ID = "Player".


```JScript
<!-- Create the SELECT element. -->
<SELECT ID = CCMode  NAME = "CCMode"  LANGUAGE = "JScript"

       /* Change the text style when the SELECT element changes. */
        onChange = "Player.closedCaption.SAMIStyle = CCMode.value;
        ">

       /* Fill the SELECT list with options, set the default to Strong. */
        <OPTION VALUE = "Normal">Normal
        <OPTION VALUE = "Small">Small 
        <OPTION VALUE = "Big Bold Italic" SELECTED>Strong
</SELECT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**ClosedCaption Object**](closedcaption-object.md)
</dt> </dl>

 

 





