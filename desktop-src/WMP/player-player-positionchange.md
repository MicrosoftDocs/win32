---
title: Player.PositionChange event
description: The PositionChange event occurs when the current position of the media item has been changed.
ms.assetid: 0561c58c-da5d-438e-adf8-2472405c6b9e
keywords:
- PositionChange event Windows Media Player
- PositionChange event Windows Media Player , Player class
- Player class Windows Media Player , PositionChange event
topic_type:
- apiref
api_name:
- Player.PositionChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.PositionChange event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PositionChange** event occurs when the current position of the media item has been changed.

## Syntax


```JScript
Player.PositionChange(
  oldPosition,
  newPosition
)
```



## Parameters

<dl> <dt>

*oldPosition* 
</dt> <dd>

Number (**double**) specifying the old position.

</dd> <dt>

*newPosition* 
</dt> <dd>

**Number** (**double**) specifying the new position.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event is not raised routinely during playback. It only occurs when something actively changes the current position of the playing media item, such as the user moving the seek handle or code specifying a value for *Controls*.**currentPosition**.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





