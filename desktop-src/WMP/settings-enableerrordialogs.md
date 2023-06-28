---
title: Settings.enableErrorDialogs
description: The enableErrorDialogs property specifies or retrieves a value indicating whether error dialog boxes are shown automatically.
ms.assetid: 16b10bea-4b3e-469f-a903-02f19ffcdf31
keywords:
- Settings.enableErrorDialogs Windows Media Player
topic_type:
- apiref
api_name:
- Settings.enableErrorDialogs
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.enableErrorDialogs

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **enableErrorDialogs** property specifies or retrieves a value indicating whether error dialog boxes are shown automatically.

## Syntax

player.settings.enableErrorDialogs

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                                     |
|-------|-------------------------------------------------|
| true  | Default. Error dialogs are shown automatically. |
| false | Error dialogs are not shown automatically.      |



 

## Remarks

This property exhibits specific behavior for remoted instances of the Player control. For more information, see [Remoting the Windows Media Player Control](remoting-the-windows-media-player-control.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





