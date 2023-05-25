---
description: The CurrentVolume property retrieves the volume number for the current root directory.
ms.assetid: f8d06a30-d6d5-43b9-b838-741d781f8d01
title: CurrentVolume Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentVolume Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentVolume` property retrieves the volume number for the current root directory.

``` syntax
[ iCurVolume = ] MSWebDVD.CurrentVolume
```

## Return Value

Returns an integer value representing the current DVD volume. If a disc is part of a multi-volume set, then the integer value should be greater than zero.

## Remarks

This property is read-only with no default value.

## See also

<dl> <dt>

[**VolumesAvailable**](volumesavailable-property.md)
</dt> </dl>

 

 



