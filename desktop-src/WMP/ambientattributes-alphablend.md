---
title: AmbientAttributes.alphaBlend
description: The alphaBlend attribute specifies or retrieves a value for alpha blending any VIEW, SUBVIEW, or UI widget.
ms.assetid: a6c47d32-a497-4bfa-8fa3-ef94e267d94b
keywords:
- AmbientAttributes.alphaBlend Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.alphaBlend
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.alphaBlend

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **alphaBlend** attribute specifies or retrieves a value for alpha blending any **VIEW**, **SUBVIEW**, or UI widget.

``` syntax
        elementID.alphaBlend
```

## Possible Values

This attribute is a read/write **Number** (**long**) with a value ranging from 0 (no opacity) to 255 (full opacity) and a default value of 255.

## Remarks

This attribute allows an element to appear semitransparent, depending on the amount of opacity set. The less opacity, the more transparent the element will appear. Each element in the skin can have a separate opacity value except for button elements in a **BUTTONGROUP** control. When **alphaBlend** is set in **VIEW**, the opacity of the entire skin will be set. Alpha blend will not work for windowed controls, including **PLAYLIST**, **EFFECTS**, **LISTBOX**, **POPUP**, **EDITBOX**, and **VIDEO** (if **windowless** is set to false). When **alphaBlend** is set on **VIEW**, the whole skin becomes transparent. The **transparencyColor** attributes used by several elements are not supported with **alphaBlend**.

When you use **alphaBlend** with a **TEXT** element that does not have the **backgroundColor** specified, a background color of black will be used. If the foreground color is also black (which is the default value for *TEXT*.**foregroundColor**), your text may become unreadable. To prevent this, always specify the **backgroundColor** attribute, or set **foregroundColor** to a color other than black.

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

[**AmbientAttributes.alphaBlendTo**](ambientattributes-alphablendto.md)
</dt> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.backgroundColor**](text-backgroundcolor.md)
</dt> <dt>

[**TEXT.foregroundColor**](text-foregroundcolor.md)
</dt> </dl>

 

 





