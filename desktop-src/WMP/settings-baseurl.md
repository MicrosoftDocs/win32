---
title: Settings.baseURL
description: The baseURL property specifies or retrieves the base URL used for relative path resolution with URL script commands that are embedded in media items.
ms.assetid: bb2db144-6d1e-4ed6-baed-dc5dbff44aa0
keywords:
- Settings.baseURL Windows Media Player
topic_type:
- apiref
api_name:
- Settings.baseURL
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Settings.baseURL

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **baseURL** property specifies or retrieves the base URL used for relative path resolution with URL script commands that are embedded in media items.

## Syntax

player.settings.baseURL

## Possible Values

This property is a read/write **String**.

## Remarks

This property specifies the base HTTP URL that is passed as the command parameter by the **ScriptCommand** event. The base URL is concatenated with the relative URL as follows:

1.  A trailing forward slash (/) is added to the value of the **baseURL** property.
2.  A leading period, backward slash, or forward slash (., \\, and /) are deleted from the relative URL.
3.  The relative URL is added to the end of the base URL.
4.  All slashes in the resulting fully qualified URL are pointed in the same direction (converted to forward or backward slashes) based on the direction of the first slash character encountered in the new URL.

**Note**

The player control does not support the use of two periods (..) in the relative URL to indicate the parent of the current location.

**Windows Media Player 10 Mobile**: This property is read-only, and always returns an empty string.

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

 

 





