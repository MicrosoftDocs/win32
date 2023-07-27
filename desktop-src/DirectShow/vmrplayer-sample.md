---
description: VMRPlayer Sample
ms.assetid: 7fc893a6-afa5-4ada-9295-29122b43b21e
title: VMRPlayer Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VMRPlayer Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

This sample uses the Video Mixing Renderer 9 (VMR-9) filter to alpha blend one or two running videos and a static image.

## Usage

To open the first video, choose **Open Primary Stream** from the **File** menu. To open a second video, choose **Open Secondary Stream** from the **File** menu (you must open the primary stream first). To play the video, click the **Play** button.

You can set the position, size, and alpha values of the videos by selecting **Primary Stream** or **Secondard Stream** from the **VMR Properties** menu.

To add a static bitmap over the video, choose **Static App Image** from the **VMR Properties** menu and click the **Display App Image** box. You can use the same dialog to control the position, size, and alpha value of the bitmap.

To capture the blended video image, choose **Capture Bitmap Image** from the **VMR Properties** menu.

You can also specify the primary image stream from the command line:

**VMRPlayer** **/P** *filename*

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



