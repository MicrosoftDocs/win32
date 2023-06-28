---
title: Playlist.isIdentical method
description: The isIdentical method retrieves a value indicating whether the supplied Playlist object is identical to the current one.
ms.assetid: 8b18a44a-a394-46bf-91d0-d6ffd503881b
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , Playlist class
- Playlist class Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- Playlist.isIdentical
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlist.isIdentical method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isIdentical** method retrieves a value indicating whether the supplied **Playlist** object is identical to the current one.

## Syntax


```JScript
bRetVal = Playlist.isIdentical(
  playlist
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

**Playlist** object to compare to the current one.

</dd> </dl>

## Return value

This method returns a **Boolean**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 





