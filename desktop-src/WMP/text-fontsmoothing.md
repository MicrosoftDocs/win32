---
title: TEXT.fontSmoothing
description: The fontSmoothing attribute specifies or retrieves a value indicating whether font smoothing is enabled.
ms.assetid: bd6f0468-285e-44b3-a5e8-361744c5ce4a
keywords:
- TEXT.fontSmoothing Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.fontSmoothing
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.fontSmoothing

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **fontSmoothing** attribute specifies or retrieves a value indicating whether font smoothing is enabled.

``` syntax
        elementID.fontSmoothing
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                          |
|-------|--------------------------------------|
| true  | Font smoothing is enabled.           |
| false | Default. Font smoothing is disabled. |



 

## Remarks

Font smoothing uses the anti-aliasing feature of the operating system. If font smoothing is enabled and the operating system supports anti-aliasing, Windows Media Player attempts to smooth the text. Not all fonts support anti-aliasing. Windows Media Player 10 uses the Windows XP ClearType anti-aliasing method.

-   **Warning** Font smoothing over a transparent color may cause the transparent color to blend into the characters. It is not recommended that you use **fontSmoothing** if the text will display over a transparency.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> </dl>

 

 





