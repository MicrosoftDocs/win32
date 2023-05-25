---
title: PlayerApplication.playerDocked
description: The playerDocked property retrieves a value indicating whether Windows Media Player is in a docked state.
ms.assetid: c6f82188-0826-4854-992c-85ad84701fb7
keywords:
- PlayerApplication.playerDocked Windows Media Player
topic_type:
- apiref
api_name:
- PlayerApplication.playerDocked
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayerApplication.playerDocked

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **playerDocked** property retrieves a value indicating whether Windows Media Player is in a docked state.

## Syntax

*playerApplication*.**playerDocked**

## Possible Values

This property is a read-only **Boolean**.

## Remarks

This property is used only when remoting the Windows Media Player control.

**Windows Media Player 10 Mobile:** This property always returns **false**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**PlayerApplication Object**](playerapplication-object.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 





