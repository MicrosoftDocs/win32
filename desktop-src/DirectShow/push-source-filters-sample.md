---
description: Push Source Filters Sample
ms.assetid: fc52f7bc-e9c7-4cd4-91e8-5c8f3450ca95
title: Push Source Filters Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Push Source Filters Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

This sample consists of a set of three source filters that provide the following source data as a video stream:

-   CPushSourceBitmap: Single bitmap (loaded from current directory)
-   CPushSourceBitmapSet: Set of bitmaps (loaded from current directory)
-   CPushSourceDesktop: Copy of current desktop image (GDI only)

## Usage

To use a filter, load it into GraphEdit and render its output pin. This will connect a video renderer (and possibly a Color Space Converter filter) and allow you to display the output. If you want to render the output to an AVI file, load the AVI Mux, load a File Writer Filter, provide an output name to the File Writer, and render the PushSource filter's output pin. You can also load and connect video compressors, video effects, and so on.

> [!Note]  
> The desktop capture filter does not support hardware overlays, so it will not capture video rendered to an overlay surface or cursors displayed via hardware overlay. It uses GDI to convert the current desktop image into a bitmap, which is passed to the output pin as a media sample.

 

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\PushSource.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



