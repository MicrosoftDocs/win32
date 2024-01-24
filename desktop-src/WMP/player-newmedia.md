---
title: Player.newMedia method
description: The newMedia method creates a new Media object.
ms.assetid: 'fccf1559-bac3-4edf-bd88-da2c72cdec21'
keywords:
- newMedia method Windows Media Player
- newMedia method Windows Media Player , Player class
- Player class Windows Media Player , newMedia method
topic_type:
- apiref
api_name:
- Player.newMedia
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.newMedia method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **newMedia** method creates a new **Media** object.

## Syntax


```JScript
retVal = Player.newMedia(
  URL
)
```



## Parameters

<dl> <dt>

*URL* \[in\]
</dt> <dd>

**String** containing the URL of the digital media file to create the **Media** object with.

</dd> </dl>

## Return value

This method returns a **Media** object.

## Remarks

The *URL* parameter must not be an empty string or null.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





