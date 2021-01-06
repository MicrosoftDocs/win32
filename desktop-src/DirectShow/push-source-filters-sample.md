---
description: Push Source Filters Sample
ms.assetid: fc52f7bc-e9c7-4cd4-91e8-5c8f3450ca95
title: Push Source Filters Sample
ms.topic: article
ms.date: 05/31/2018
---

# Push Source Filters Sample

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

 

 



