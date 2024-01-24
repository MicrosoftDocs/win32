---
title: EQUALIZERSETTINGS.bypass
description: The bypass attribute specifies or retrieves a value indicating whether the equalizer filter is bypassed in the filter graph.
ms.assetid: b189a6f1-e0d0-4cfa-9a99-73d3ccd705e0
keywords:
- EQUALIZERSETTINGS.bypass Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.bypass
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.bypass

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **bypass** attribute specifies or retrieves a value indicating whether the equalizer filter is bypassed in the filter graph.

``` syntax
        elementID.bypass
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                |
|-------|--------------------------------------------|
| true  | Default. The equalizer filter is bypassed. |
| false | The equalizer filter is used.              |



 

## Remarks

If this attribute is not specified, the previous value will be retained.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> </dl>

 

 





