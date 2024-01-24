---
title: AmbientAttributes.alphaBlendTo
description: The alphaBlendTo method adjusts the alphaBlend property over a period of time.
ms.assetid: 5cb259bd-3010-4086-be9d-65022be297b7
keywords:
- AmbientAttributes.alphaBlendTo Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.alphaBlendTo
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# AmbientAttributes.alphaBlendTo

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **alphaBlendTo** method adjusts the **alphaBlend** property over a period of time.

``` syntax
        elementID.alphaBlendTo(newVal, alphaTime)
```

## Parameters

<dl> <dt>

<span id="newVal"></span><span id="newval"></span><span id="NEWVAL"></span>*newVal*
</dt> <dd>

**Number** (long) specifying the new opacity value. Ranges from 0 (no opacity) to 255 (full opacity).

</dd> <dt>

<span id="alphaTime"></span><span id="alphatime"></span><span id="ALPHATIME"></span>*alphaTime*
</dt> <dd>

**Number** (**long**) specifying the time, in milliseconds, that it takes the element to change opacity.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method is useful for making elements gradually appear or disappear.

When you use **alphaBlendTo** with a **TEXT** element that does not have the **backgroundColor** specified, a background color of black will be used. If the foreground color is also black (which is the default value for *TEXT*.**foregroundColor**), your text may become unreadable. To prevent this, always specify the **backgroundColor** attribute, or set **foregroundColor** to a color other than black.

> [!Note]  
> This attribute is not supported in Windows 98.

 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.alphaBlend**](ambientattributes-alphablend.md)
</dt> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.backgroundColor**](text-backgroundcolor.md)
</dt> <dt>

[**TEXT.foregroundColor**](text-foregroundcolor.md)
</dt> </dl>

 

 





