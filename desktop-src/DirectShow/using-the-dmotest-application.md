---
description: Using the DMOTest Application
ms.assetid: 28448e1b-44de-4016-9ab6-0a9e2d916592
title: Using the DMOTest Application
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the DMOTest Application

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> The DMOTest application is no longer available in the SDK.

 

The DMOTest utility can help verify that a DMO meets the DMO specifications. If you develop a DMO, you should include the DMO test application as part of your testing.

DMOTest is installed in the Bin\\DXUtils directory, under the SDK root directory. To use DMOTest, you must first generate some test data for the DMO. The SDK includes a DirectShow filter for this purpose. Details about the filter and the DMOTest application can be found in the DMOTest application Help. In the application, choose **Contents** from the **Help** menu. The Help includes step-by-step instructions for generating test data and running tests.

## Related topics

<dl> <dt>

[Writing a DMO](writing-a-dmo.md)
</dt> </dl>

 

 



