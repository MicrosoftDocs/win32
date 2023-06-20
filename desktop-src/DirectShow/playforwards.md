---
description: The PlayForwards event is sent when the PlayForwards command has been enabled or disabled.
ms.assetid: '3f6ad4c8-d610-4053-bbe8-fe4fa3f45b63'
title: PlayForwards
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayForwards

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayForwards` event is sent when the `PlayForwards` command has been enabled or disabled.

``` syntax
PlayForwards(bEnabled)
```

## Parameters

<dl> <dt>

<span id="bEnabled"></span><span id="benabled"></span><span id="BENABLED"></span>*bEnabled*
</dt> <dd>

Specifies whether the operation is enabled or disabled as a Boolean.

</dd> </dl>

 

 



