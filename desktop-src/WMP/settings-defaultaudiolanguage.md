---
title: Settings.defaultAudioLanguage
description: The defaultAudioLanguage property retrieves the LCID of the default audio language specified in Windows Media Player.
ms.assetid: 5f3c8d9e-2741-435d-a566-98b12d04bd75
keywords:
- Settings.defaultAudioLanguage Windows Media Player
topic_type:
- apiref
api_name:
- Settings.defaultAudioLanguage
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.defaultAudioLanguage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **defaultAudioLanguage** property retrieves the LCID of the default audio language specified in Windows Media Player.

## Syntax

player.settings.defaultAudioLanguage

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls.currentAudioLanguage**](controls-currentaudiolanguage.md)
</dt> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





