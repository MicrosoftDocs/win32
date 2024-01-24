---
title: Network.maxBandwidth
description: The maxBandwidth property specifies or retrieves the maximum allowed bandwidth.
ms.assetid: 303acf51-8d3a-4e58-8aa8-c0b6db1e4fbb
keywords:
- Network.maxBandwidth Windows Media Player
topic_type:
- apiref
api_name:
- Network.maxBandwidth
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.maxBandwidth

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **maxBandwidth** property specifies or retrieves the maximum allowed bandwidth.

## Syntax

*player*.*network*.**maxBandwidth**

## Possible Values

This property is a read/write **Number** (**long**).

## Remarks

This property has no default value. Its value can be specified while Windows Media Player is playing, but the change will not take effect until the current media item is released by opening another one or by calling *Player*.**close**. Windows Media Player attempts to achieve the highest bandwidth possible. Only in the case of the value being set will any bandwidth reduction occur.

This setting is useful for reducing the amount of bandwidth used, particularly in the case of a multiple bit rate (MBR) stream. An MBR stream contains multiple streams with different bit rates. In some cases, it may be desirable to use a stream with a lower bit rate than the client requires. In this case, setting the **maxBandwidth** property will select a lower bit-rate stream.

For example, an MBR stream could include streams encoded at 20 kilobits per second (Kbps), 37 Kbps, and 200 Kbps. Setting the **maxBandwidth** property to 50,000 (50 Kbps) will select the 37 Kbps stream instead of the 200 Kbps stream.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> <dt>

[**Player.close**](player-close.md)
</dt> </dl>

 

 





