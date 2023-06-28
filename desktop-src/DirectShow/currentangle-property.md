---
description: The CurrentAngle property sets or retrieves the current angle in an angle block.
ms.assetid: 9b18ea65-4c17-4b52-b893-b668598aec0f
title: CurrentAngle Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentAngle Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentAngle` property sets or retrieves the current angle in an angle block.

``` syntax
[ iCurAngle = ] MSWebDVD.CurrentAngle
```

## Return Value

Returns an integer value representing the angle. Must be a value from 1 through 9.

## Remarks

This property is read/write with no default value.

## See also

<dl> <dt>

[**AnglesAvailable**](anglesavailable-property.md)
</dt> </dl>

 

 



