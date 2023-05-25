---
title: VIEW.category
description: The category attribute specifies or retrieves the category for which the VIEW is intended.
ms.assetid: ab724647-8898-4bbf-82a3-b5852faed858
keywords:
- VIEW.category Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.category
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.category

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **category** attribute specifies or retrieves the category for which the **VIEW** is intended.

``` syntax
        elementID.category
```

## Possible Values

This attribute is a read/write **String** containing one of the following values.



| Value | Description                           |
|-------|---------------------------------------|
| All   | Default. Theme for all types of media |
| Radio | The UI for Radio Playback             |
| CD    | The UI for CD playback                |
| DVD   | The UI for DVD playback               |
| Music | The UI for MP3, WAV, MIDI, WMA        |
| Video | The UI for Video playback             |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





