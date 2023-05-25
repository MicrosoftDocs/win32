---
description: The IsSubpictureStreamEnabled method retrieves a value indicating whether the specified subpicture stream is enabled in the current title.
ms.assetid: c6436f77-ca94-464f-9336-f485f5d5d199
title: IsSubpictureStreamEnabled Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IsSubpictureStreamEnabled Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `IsSubpictureStreamEnabled` method retrieves a value indicating whether the specified subpicture stream is enabled in the current title.

``` syntax
[ bEnabled = ] MSWebDVD.IsSubpictureStreamEnabled(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the subpicture stream as an Integer.



| Value   | Description              |
|---------|--------------------------|
| 0 to 31 | subpicture stream        |
| 63      | muted low-bitrate stream |



 

</dd> </dl>

## Return Value

Returns a Boolean value indicating whether the specified audio stream is available in the current title. True means it is available.

## Remarks

Although a disc can contain up to 32 subpicture streams, each stream is not necessarily available for each title. Always verify that a stream is available for a title before setting the [**CurrentSubpictureStream**](currentsubpicturestream-property.md) property.

 

 



