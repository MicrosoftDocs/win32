---
description: PlayCap Sample
ms.assetid: 3faba514-23b7-4107-aca6-5b113a0ca164
title: PlayCap Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlayCap Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

Simple capture application.

This application creates a preview window for the first video capture device that it locates on the user's system (if any). It demonstrates a simple example of using the [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) and [**ICreateDevEnum**](/windows/desktop/api/Strmif/nn-strmif-icreatedevenum) interfaces to build a capture graph.

For a sample capture application that supports more features, see [AmCap Sample](amcap-sample.md).

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Capture\\PlayCap.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



