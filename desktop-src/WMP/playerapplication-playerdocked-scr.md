---
title: PLAYERAPPLICATION.playerDocked Attribute
description: The playerDocked attribute retrieves a value indicating whether Windows Media Player is in a docked state.
ms.assetid: 8b95da72-037b-4179-a564-fc9bc63368ac
keywords:
- PLAYERAPPLICATION.playerDocked Windows Media Player
topic_type:
- apiref
api_name:
- PLAYERAPPLICATION.playerDocked
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYERAPPLICATION.playerDocked

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **playerDocked** attribute retrieves a value indicating whether Windows Media Player is in a docked state.

``` syntax
        elementID.playerDocked
```

## Possible Values

This attribute is a read-only **Boolean**.



| Value | Description                       |
|-------|-----------------------------------|
| True  | Windows Media Player is docked.   |
| False | Windows Media Player is undocked. |



 

## Remarks

This attribute is used only when remoting the Windows Media Player control.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYERAPPLICATION Element**](playerapplication-element.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 





