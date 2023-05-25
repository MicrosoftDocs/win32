---
title: Player.enabled
description: The enabled property specifies or retrieves a value indicating whether the Windows Media Player control is enabled.
ms.assetid: 65fea4d2-3330-4cce-bdaf-fae00304271a
keywords:
- Player.enabled Windows Media Player
topic_type:
- apiref
api_name:
- Player.enabled
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.enabled

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **enabled** property specifies or retrieves a value indicating whether the Windows Media Player control is enabled.

## Syntax

*player* .**enabled**

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                                           |
|-------|-------------------------------------------------------|
| true  | Default. The Windows Media Player control is enabled. |
| false | The Windows Media Player control is disabled.         |



 

## Remarks

If **enabled** equals false then during full-screen playback Windows Media Player hides the user controls.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





