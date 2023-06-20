---
description: Ticker Sample
ms.assetid: 1a3de957-70ea-4b9d-94a0-9b0a74f15d78
title: Ticker Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ticker Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

This sample uses the Video Mixing Renderer to blend video and text. It uses the [**IVMRMixerBitmap9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixerbitmap9) interface to blend text onto the bottom portion of the video window.

The application creates a bitmap with a default text string and scrolls it across the bottom of the screen. To change the text, choose **Set text string...** from the **Ticker** menu. To set the font, choose **Set font...** from the **Ticker** menu. If you select **Use static image** from the **Ticker** menu, the application switches from a dynamic text string to a static bitmap image.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



