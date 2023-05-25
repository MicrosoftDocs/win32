---
title: Player.Buffering event
description: The Buffering event occurs when the Windows Media Player control begins or ends buffering or downloading. | Player.Buffering event
ms.assetid: a0a09bf7-19bc-4838-a403-924e8d83b48d
keywords:
- Buffering event Windows Media Player
- Buffering event Windows Media Player , Player class
- Player class Windows Media Player , Buffering event
topic_type:
- apiref
api_name:
- Player.Buffering
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.Buffering event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Buffering** event occurs when the Windows Media Player control begins or ends buffering or downloading.

## Syntax


```JScript
Player.Buffering(
  Start
)
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

**Boolean** containing one of the following values.



| Value | Description            |
|-------|------------------------|
| true  | Buffering has started. |
| false | Buffering has ended.   |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Use this event to determine when buffering or downloading starts or stops. You can use the same event block for both cases and test *Network*.**bufferingProgress** and *Network*.**downloadProgress** to determine whether Windows Media Player is currently buffering or downloading content.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file by using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network.bufferingProgress**](network-bufferingprogress.md)
</dt> <dt>

[**Network.downloadProgress**](network-downloadprogress.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





