---
description: The PlayAtTimeInTitle method starts playback at the specified time within the specified title.
ms.assetid: 82726885-8393-409b-b8a1-29a8e9e9ac65
title: PlayAtTimeInTitle Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayAtTimeInTitle Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayAtTimeInTitle` method starts playback at the specified time within the specified title.

``` syntax
MSWebDVD.PlayAtTimeInTitle(sTime, iTitle)
```

## Parameters

<dl> <dt>

<span id="sTime"></span><span id="stime"></span><span id="STIME"></span>*sTime*
</dt> <dd>

Specifies the time at which to start playback as a string. The string must be in the format "hh:mm:ss:ff" (specifying hours, minutes, seconds, frames).

</dd> <dt>

<span id="iTitle"></span><span id="ititle"></span><span id="ITITLE"></span>*iTitle*
</dt> <dd>

Specifies the index of the title as an Integer.

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[**CurrentTitle**](currenttitle-property.md)
</dt> <dt>

[**PlayAtTime**](playattime-method.md)
</dt> <dt>

[**TitlesAvailable**](titlesavailable-property.md)
</dt> </dl>

 

 



