---
title: Player.CurrentMediaItemAvailable event
description: The CurrentMediaItemAvailable event occurs when a graphic metadata item in the current media item becomes available. | Player.CurrentMediaItemAvailable event
ms.assetid: dc692b14-67d3-4867-8f99-ddfcf7d1610c
keywords:
- CurrentMediaItemAvailable event Windows Media Player
- CurrentMediaItemAvailable event Windows Media Player , Player class
- Player class Windows Media Player , CurrentMediaItemAvailable event
topic_type:
- apiref
api_name:
- Player.CurrentMediaItemAvailable
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.CurrentMediaItemAvailable event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CurrentMediaItemAvailable** event occurs when a graphic metadata item in the current media item becomes available.

## Syntax


```JScript
Player.CurrentMediaItemAvailable(
  bstrItemName
)
```



## Parameters

<dl> <dt>

*bstrItemName* 
</dt> <dd>

**String** containing the name of the current media item.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Because playback can begin before a media item is fully downloaded, any metadata graphics contained in the media item (such as album cover art) may not be available when it starts to play. This event alerts you when a metadata graphic item is finished downloading. You can then retrieve the **Media** object by passing the value of *bstrItemName* to the *MediaCollection*.**getByName** method, after which you can access the metadata graphic item by using *Media*.**getItemInfoByType** and specifying **WM/Picture** for the attribute name.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Media.getItemInfoByType**](media-getiteminfobytype.md)
</dt> <dt>

[**MediaCollection.getByName**](mediacollection-getbyname.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





