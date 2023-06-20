---
description: The TotalTitleTime property retrieves the total playback time for the current title.
ms.assetid: b05bb76b-d4ba-42e6-92ea-8e48f4c8f409
title: TotalTitleTime Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TotalTitleTime Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `TotalTitleTime` property retrieves the total playback time for the current title.

``` syntax
[ sTotalTime = ] MSWebDVD.TotalTitleTime
```

## Return Value

Returns the total playing time of the current title as a String in the format "hh:mm:ss:ff".

## Remarks

This property is read-only with no default value. The returned string will be 11 characters long in the format "hh:mm:ss:ff" (hours, minutes, seconds, frames).

## See also

<dl> <dt>

[**PlayAtTime**](playattime-method.md)
</dt> <dt>

[**PlayAtTimeInTitle**](playattimeintitle-method.md)
</dt> </dl>

 

 



