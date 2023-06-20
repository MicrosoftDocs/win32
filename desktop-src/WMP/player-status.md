---
title: Player.status
description: The status property retrieves a value indicating the status of Windows Media Player.
ms.assetid: 781c44d0-15cf-4be2-9e83-76706ce1cb85
keywords:
- Player.status Windows Media Player
topic_type:
- apiref
api_name:
- Player.status
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.status

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **status** property retrieves a value indicating the status of Windows Media Player.

## Syntax

*player* .**status**

## Possible Values

This property is a read-only String.

## Remarks

The values contained in this property are subject to change at any time, and should be used for display purposes only.

The **StatusChange** event is fired whenever this property changes value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later.<br/>                                      |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.StatusChange Event**](player-player-statuschange.md)
</dt> </dl>

 

 





