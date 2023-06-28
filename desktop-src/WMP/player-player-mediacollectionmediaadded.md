---
title: Player.MediaCollectionMediaAdded event
description: The MediaCollectionMediaAdded event occurs when a media item is added to the local library. | Player.MediaCollectionMediaAdded event
ms.assetid: 01696d28-e83b-4fd2-8e88-2871831b61e7
keywords:
- MediaCollectionMediaAdded event Windows Media Player
- MediaCollectionMediaAdded event Windows Media Player , Player class
- Player class Windows Media Player , MediaCollectionMediaAdded event
topic_type:
- apiref
api_name:
- Player.MediaCollectionMediaAdded
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.MediaCollectionMediaAdded event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The MediaCollectionMediaAdded event occurs when a media item is added to the local library.

## Syntax


```JScript
Player.MediaCollectionMediaAdded(
  pdispMedia
)
```



## Parameters

<dl> <dt>

*pdispMedia* 
</dt> <dd>

**Media** object that was added.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event only occurs for the local library.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.mediaCollection**](player-mediacollection.md)
</dt> </dl>

 

 





