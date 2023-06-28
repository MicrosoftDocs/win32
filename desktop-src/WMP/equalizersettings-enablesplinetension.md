---
title: EQUALIZERSETTINGS.enableSplineTension
description: The enableSplineTension attribute specifies or retrieves a value indicating whether spline tension is enabled.
ms.assetid: ca52feac-3161-4fd0-976c-abbfb2a238f2
keywords:
- EQUALIZERSETTINGS.enableSplineTension Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.enableSplineTension
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.enableSplineTension

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **enableSplineTension** attribute specifies or retrieves a value indicating whether spline tension is enabled.

``` syntax
        elementID.enableSplineTension
```

## Possible Values

This attribute is a read/write **Boolean** with a default value of true.

## Remarks

Enabling spline tension allows the user to adjust the equalizer bandwidths more smoothly, so that there are no large jumps between the frequency levels.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.splineTension**](equalizersettings-splinetension.md)
</dt> </dl>

 

 





