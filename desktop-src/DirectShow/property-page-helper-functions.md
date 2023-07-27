---
description: Property Page Helper Functions
ms.assetid: 97450126-0d11-448e-a7bc-7372e84c07ae
title: Property Page Helper Functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Property Page Helper Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Videoctl.h header file in the Microsoft® DirectShow® base classes provides functions to help with property page implementations.



| Function                                                 | Description                                                                            |
|----------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**GetDialogSize**](getdialogsize.md)                   | Retrieves the size of a resource dialog box in screen pixels.                          |
| [**StringFromResource**](stringfromresource.md)         | Loads a string from a resource file with the given resource identifier.                |
| [**WideStringFromResource**](widestringfromresource.md) | Loads a wide-character string from a resource file with the given resource identifier. |



 

 

 



