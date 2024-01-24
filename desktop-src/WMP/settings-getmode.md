---
title: Settings.getMode method
description: The getMode method determines whether the loop mode or shuffle mode is active.
ms.assetid: '41c3725f-ae8f-4b45-856a-b7245c9ad2b3'
keywords:
- getMode method Windows Media Player
- getMode method Windows Media Player , Settings class
- Settings class Windows Media Player , getMode method
topic_type:
- apiref
api_name:
- Settings.getMode
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.getMode method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getMode** method determines whether the loop mode or shuffle mode is active.

## Syntax


```JScript
bRetVal = Settings.getMode(
  modeName
)
```



## Parameters

<dl> <dt>

*modeName* \[in\]
</dt> <dd>

**String** specifying the name of the mode in question, containing one of the following values.



| String     | Description                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------|
| autoRewind | Tracks are restarted at the beginning after playing to the end.                                                          |
| loop       | The sequence of tracks repeats itself.                                                                                   |
| showFrame  | The nearest key frame is displayed at the current position when not playing. This mode is not relevant for audio tracks. |
| shuffle    | Tracks are played in random order.                                                                                       |



 

</dd> </dl>

## Return value

This method returns a **Boolean** value indicating whether the specified mode is active.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | For loop and shuffle modes, Windows Media Player version 7.0 or later. For autoRewind and showFrame modes, Windows Media Player 9 Series or later.<br/> |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl>                                                                            |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Settings.setMode**](settings-setmode.md)
</dt> </dl>

 

 





