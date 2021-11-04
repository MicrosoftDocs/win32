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
ms.date: 05/31/2018
---

# Player.windowlessVideo

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



 

 





