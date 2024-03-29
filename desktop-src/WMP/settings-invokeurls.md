---
title: Settings.invokeURLs
description: The invokeURLs property specifies or retrieves a value indicating whether URL events should launch a Web browser.
ms.assetid: 3a28d949-96b7-4c21-97c5-2442c2f7baa5
keywords:
- Settings.invokeURLs Windows Media Player
topic_type:
- apiref
api_name:
- Settings.invokeURLs
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.invokeURLs

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **invokeURLs** property specifies or retrieves a value indicating whether URL events should launch a Web browser.

## Syntax

player.settings.invokeURLs

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                                  |
|-------|----------------------------------------------|
| true  | Default. URL events should launch a browser. |
| false | URL events should not launch a browser.      |



 

## Remarks

Media files can contain URLs. When a URL is sent to the Windows Media Player control, it is passed first to the **ScriptCommand** event handler regardless of the value in **invokeURLs**. After **ScriptCommand** exits, Windows Media Player checks **invokeURLs** to determine whether to launch the default Internet browser with the URL. You can selectively display URLs by checking them in **ScriptCommand** and setting **invokeURLs** as desired.

**Windows Media Player 10 Mobile**: This property only accepts or returns false.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player.ScriptCommand Event**](player-player-scriptcommand.md)
</dt> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





