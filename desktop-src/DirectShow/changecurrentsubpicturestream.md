---
description: The ChangeCurrentSubpictureStream event is sent when the disc enables or disables changing the subpicture stream.
ms.assetid: f55e63b6-b3ad-4cf3-a7c4-6636b5375b12
title: ChangeCurrentSubpictureStream (Segment.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ChangeCurrentSubpictureStream

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ChangeCurrentSubpictureStream` event is sent when the disc enables or disables changing the subpicture stream.

``` syntax
ChangeCurrentSubpictureStream(bEnabled)
```

## Parameters

<dl> <dt>

<span id="bEnabled"></span><span id="benabled"></span><span id="BENABLED"></span>*bEnabled*
</dt> <dd>

Specifies whether the operation is enabled or disabled as a Boolean.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



 

 




