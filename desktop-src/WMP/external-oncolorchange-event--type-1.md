---
title: External.OnColorChange Event (Type 1)
description: Note This topic describes functionality designed for use by online stores. | External.OnColorChange Event (Type 1)
ms.assetid: 45e6ec4a-e680-4d50-8fb7-410f12383eef
keywords:
- External.OnColorChange Event (Type 1) Windows Media Player
topic_type:
- apiref
api_name:
- External.OnColorChange Event (Type 1)
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.OnColorChange Event (Type 1)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnColorChange** event occurs when the color of the Windows Media Player user interface changes.

``` syntax
window.external.OnColorChange = FunctionName
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this event takes no parameters.

## Remarks

Users can change the color of the Windows Media Player user interface. You can use this event to customize the appearance of your hosted webpage to match the Player.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





