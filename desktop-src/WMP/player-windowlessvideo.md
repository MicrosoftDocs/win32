---
title: Player.windowlessVideo
description: The windowlessVideo property specifies or retrieves a value indicating whether the Windows Media Player control renders video in windowless mode.
ms.assetid: 314a75a3-d096-4cd4-a747-e31367e0e265
keywords:
- Player.windowlessVideo Windows Media Player
topic_type:
- apiref
api_name:
- Player.windowlessVideo
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.windowlessVideo

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **windowlessVideo** property specifies or retrieves a value indicating whether the Windows Media Player control renders video in windowless mode.

## Syntax

*player*.**windowlessVideo**

## Possible Values

This property is a **Boolean** that is specified at design time and is read-only thereafter.



| Value | Description                                      |
|-------|--------------------------------------------------|
| true  | The video is rendered in windowless mode.        |
| false | Default. The video is rendered in windowed mode. |



 

## Remarks

By default, an embedded Windows Media Player control renders video in its own window within the client area. When **windowlessVideo** is set to true, the Player control renders video directly in the client area, so you can apply special effects or layer the video with text.

In Windows Vista, rendering video in windowless mode can degrade performance.

The **windowlessVideo** property is not supported for Netscape Navigator. Setting a value for this property in Navigator may yield unexpected results.

**Windows Media Player 10 Mobile:** This property is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



 

 





