---
title: Player.isRemote
description: The isRemote property retrieves a value indicating whether the Windows Media Player control is running in remote mode.
ms.assetid: bfeab968-affb-4d5d-b88b-5caf50d34cee
keywords:
- Player.isRemote Windows Media Player
topic_type:
- apiref
api_name:
- Player.isRemote
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.isRemote

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isRemote** property retrieves a value indicating whether the Windows Media Player control is running in remote mode.

## Syntax

*player* .**isRemote**

## Possible Values

This property is a read-only **Boolean**.



| Value | Description                                   |
|-------|-----------------------------------------------|
| true  | The Player control is running in remote mode. |
| false | The Player control is running in local mode.  |



 

## Remarks

**Windows Media Player 10 Mobile:** This property always returns false.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 





