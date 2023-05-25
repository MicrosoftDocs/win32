---
description: The CurrentTime property retrieves the current playback time.
ms.assetid: 94f94eb1-49fa-4b8c-95a6-da307b0abd62
title: CurrentTime Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentTime Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentTime` property retrieves the current playback time.

``` syntax
[ sCurTime = ] MSWebDVD.CurrentTime
```

## Return Value

Returns an 11-character **string** representing the current playback time in the format "*hh:mm:ss:ff*" (hours, minutes, seconds, frames).

## Remarks

This property is read-only with no default value.

## See also

<dl> <dt>

[**TotalTitleTime**](totaltitletime-property.md)
</dt> </dl>

 

 



