---
description: DMO Demo Sample
ms.assetid: b19f0ca0-65ca-4a3b-97e3-dbd1aafe77d9
title: DMO Demo Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Demo Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

This sample application demonstrates how to use [DirectX Media Objects](directx-media-objects.md) (DMO) in an application. It streams audio data from a WAV file through an audio effect DMO to a DirectSound buffer.

## Usage

Click the **Sound File** button to load a sound file. Use the drop-down combo box to select an audio effect DMO. Click the **Play** button to hear the sound file played with the audio effect.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\DMO\\DMODemo.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> <dt>

[DirectX Media Objects](directx-media-objects.md)
</dt> </dl>

 

 



