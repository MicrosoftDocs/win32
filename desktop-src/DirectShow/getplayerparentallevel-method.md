---
description: The GetPlayerParentalLevel retrieves the parental management level set in the MSWebDVD object.
ms.assetid: 451e0891-4e5d-4a01-94b8-290f5a804ff1
title: GetPlayerParentalLevel Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetPlayerParentalLevel Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetPlayerParentalLevel` retrieves the parental management level set in the **MSWebDVD** object.

``` syntax
[ iLevel = ] MSWebDVD.GetPlayerParentalLevel()
```

## Return Value

Returns an integer value specifying the current parental level in the DVD Navigator, or -1 if parental management is disabled.

## Remarks

A player application is responsible for enforcing parental controls. The player parental level is a value set by an application than can be used to indicate the highest parental level the current user can view. When the DVD Navigator encounters a new parental level, use this method to determine whether the new level is greater than the level that was set by the application through [**SelectParentalLevel**](selectparentallevel-method.md).

## See also

<dl> <dt>

[**GetTitleParentalLevels**](gettitleparentallevels-method.md)
</dt> <dt>

[**GetPlayerParentalCountry**](getplayerparentalcountry-method.md)
</dt> <dt>

[**SelectParentalCountry**](selectparentalcountry-method.md)
</dt> <dt>

[**SelectParentalLevel**](selectparentallevel-method.md)
</dt> </dl>

 

 



