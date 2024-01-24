---
title: External.appColorButtonHighlight
description: Note This topic describes functionality designed for use by online stores. | External.appColorButtonHighlight
ms.assetid: 448480bf-e5e1-4f7a-ab50-a0395af6007f
keywords:
- External.appColorButtonHighlight Windows Media Player
topic_type:
- apiref
api_name:
- External.appColorButtonHighlight
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.appColorButtonHighlight

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **appColorButtonHighlight** property retrieves the current button highlight color for the Windows Media Player user interface.

``` syntax
window.external.appColorButtonHighlight
      
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

 

 





