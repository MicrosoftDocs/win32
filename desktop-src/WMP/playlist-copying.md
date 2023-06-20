---
title: PLAYLIST.copying
description: The copying attribute retrieves a value indicating whether the PLAYLIST element is in the act of copying.
ms.assetid: 60f21f4a-51a1-43cd-9bfa-6bff19214a32
keywords:
- PLAYLIST.copying Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.copying
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.copying

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **copying** attribute retrieves a value indicating whether the **PLAYLIST** element is in the act of copying.

``` syntax
        elementID.copying
```

## Possible Values

This attribute is a read-only **Boolean**.



| Value | Description                              |
|-------|------------------------------------------|
| true  | The **PLAYLIST** element is copying.     |
| false | The **PLAYLIST** element is not copying. |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.abortCopy**](playlist-abortcopy.md)
</dt> <dt>

[**PLAYLIST.copy**](playlist-copy.md)
</dt> </dl>

 

 





