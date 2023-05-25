---
description: DVDRect Object
ms.assetid: 8f540ac6-1c1e-43d8-a0dd-bba3b5983b02
title: DVDRect Object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVDRect Object

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

> [!Note]  
> This API is deprecated. For information about DVD playback and navigation in DirectShow, see [DVD Applications](dvd-applications.md).

 

The properties of the `DVDRect` object enable a scripting application to specify and receive rectangle coordinates in [MSWebDVD](mswebdvd-object.md) methods such as [**GetButtonRect**](getbuttonrect-method.md), [**GetClipVideoRect**](getclipvideorect-method.md), [**GetVideoSize**](getvideosize-method.md) and [**SetClipVideoRect**](setclipvideorect-method.md).



| Properties                        | Description                                                            |
|-----------------------------------|------------------------------------------------------------------------|
| [**x**](x-property.md)           | Sets or retrieves the x position of the rectangle's upper-left corner. |
| [**y**](y-property.md)           | Sets or retrieves the y position of the rectangle's upper-left corner. |
| [**Width**](width-property.md)   | Sets or retrieves the width of the rectangle, in pixels.               |
| [**Height**](height-property.md) | Sets or retrieves the height of the rectangle, in pixels.              |



 

## Related topics

<dl> <dt>

[MSWebDVD ActiveX Control](mswebdvd-activex-control.md)
</dt> </dl>

 

 



