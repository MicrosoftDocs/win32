---
description: The CImagePalette class manages palettes for video renderers. It can be used to create a logical palette from a video format. This class is intended to be used with the CBaseWindow and CDrawImage classes, so it is somewhat specialized.
ms.assetid: dcbe5049-0e8c-4221-825a-0fd8e6efd2a5
title: CImagePalette class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CImagePalette class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CImagePalette` class manages palettes for video renderers. It can be used to create a logical palette from a video format. This class is intended to be used with the [**CBaseWindow**](cbasewindow.md) and [**CDrawImage**](cdrawimage.md) classes, so it is somewhat specialized.



| Protected Member Variables                                       | Description                                                                                    |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**m\_hPalette**](cimagepalette-m-hpalette.md)                  | Handle to the logical palette that this object manages.                                        |
| [**m\_pBaseWindow**](cimagepalette-m-pbasewindow.md)            | Pointer to the **CBaseWindow** object that manages the window.                                 |
| [**m\_pDrawImage**](cimagepalette-m-pdrawimage.md)              | Pointer to the **CDrawImage** object that draws the video image.                               |
| [**m\_pFilter**](cimagepalette-m-pfilter.md)                    | Pointer to the owning filter.                                                                  |
| Public Methods                                                   | Description                                                                                    |
| [**CImagePalette**](cimagepalette-cimagepalette.md)             | Constructor method.                                                                            |
| [**CopyPalette**](cimagepalette-copypalette.md)                 | Copies the palette from any **VIDEOINFO** structure to any palettized **VIDEOINFO** structure. |
| [**MakeIdentityPalette**](cimagepalette-makeidentitypalette.md) | Attempts to make a palette that maps directly to the palette selected in the display device.   |
| [**MakePalette**](cimagepalette-makepalette.md)                 | Creates a logical palette from the color table in a video format.                              |
| [**PreparePalette**](cimagepalette-preparepalette.md)           | Sets up a palette, based on a media type from the owning filter.                               |
| [**RemovePalette**](cimagepalette-removepalette.md)             | Deletes the existing logical palette.                                                          |



 

 

 



