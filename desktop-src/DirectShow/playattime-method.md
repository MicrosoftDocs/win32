---
description: The PlayAtTime method starts playback in the current title at the specified time.
ms.assetid: 83e27c27-e402-43bc-8245-3a23dd49130b
title: PlayAtTime Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayAtTime Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayAtTime` method starts playback in the current title at the specified time.

``` syntax
MSWebDVD.PlayAtTime(sTime)
```

## Parameters

<dl> <dt>

<span id="sTime"></span><span id="stime"></span><span id="STIME"></span>*sTime*
</dt> <dd>

Specifies the time at which to start playing as a string. The string must be in the format "hh:mm:ss:ff" (specifying hours, minutes, seconds, frames).

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[**PlayAtTimeInTitle**](playattimeintitle-method.md)
</dt> </dl>

 

 



