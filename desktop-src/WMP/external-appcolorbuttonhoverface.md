---
title: External.appColorButtonHoverFace
description: Note This topic describes functionality designed for use by online stores. | External.appColorButtonHoverFace
ms.assetid: bf3a0898-b2fb-48bf-84b2-11e9aada4bf3
keywords:
- External.appColorButtonHoverFace Windows Media Player
topic_type:
- apiref
api_name:
- External.appColorButtonHoverFace
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.appColorButtonHoverFace

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **appColorButtonHoverFace** property retrieves the current button hover color for the Windows Media Player user interface. This color is displayed when the user moves the mouse pointer over a button.

``` syntax
window.external.appColorButtonHoverFace
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

Users can change the color of the Windows Media Player user interface. You can use this property to customize the appearance of your hosted webpage to match the Player.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 10 or later.<br/>                                       |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> </dl>

 

 





