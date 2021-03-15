---
title: Color Element
description: Note This section describes functionality designed for use by online stores. | Color Element
ms.assetid: 36fafe16-b708-4dc1-9325-d4f39265069a
keywords:
- Color Element Windows Media Player
topic_type:
- apiref
api_name:
- Color Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Color Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The Color element specifies the background color for online store navigation buttons, button text, and the Features taskbar.

``` syntax
<Color
    MediaPlayer = "#FFFFFF"
    MediaPlayerText = "#FFFFFF"
/>
```

## Attributes

<dl> <dt>

<span id="MediaPlayer__required_"></span><span id="mediaplayer__required_"></span><span id="MEDIAPLAYER__REQUIRED_"></span>**MediaPlayer** (required)
</dt> <dd>

Hexadecimal RGB color value. Specifies the background color for buttons and the taskbar.

</dd> <dt>

<span id="MediaPlayerText__required_"></span><span id="mediaplayertext__required_"></span><span id="MEDIAPLAYERTEXT__REQUIRED_"></span>**MediaPlayerText** (required)
</dt> <dd>

Hexadecimal RGB color value. Specifies the color for the button text.

</dd> </dl>

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

The default value for **MediaPlayer** is \#7C9AD6. The default value for **MediaPlayerText** is \#FFFFFF.

Be sure to use colors that make it easy for the user to read the button text. For example, you should avoid using white button text on light colored buttons.

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 10 or later.<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





