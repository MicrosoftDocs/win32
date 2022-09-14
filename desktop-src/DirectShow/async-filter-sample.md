---
description: Async Filter Sample
ms.assetid: ad1f2386-6d23-4a6d-8542-bbca53df4825
title: Async Filter Sample
ms.topic: article
ms.date: 05/31/2018
---

# Async Filter Sample

## Description

The Async Filter sample is a file reader filter that supports progressive download. This sample filter implements the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) and [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter) interfaces. It supports MPEG files, but not AVI files.

## Usage

This sample includes a small command-line application, Memfile.exe, that demonstrates the filter. The command-line arguments specify a media file and a bit rate, in kilobytes per second. The application reads the file into memory at the specified rate and plays the file. To do so, it creates an instance of the filter, adds the filter to the filter graph, and renders the filter's output pin.

At the command line, type:

**Memfile Filename BitRate**  

The Async sample filter does not support AVI files, because it cannot connect to the [AVI Splitter](avi-splitter-filter.md) filter. The Async filter's output pin proposes MEDIATYPE\_Stream and MEDIASUBTYPE\_NULL for the media type. The input pin on the AVI Splitter filter does not accept MEDIASUBTYPE\_NULL, and does not propose any types of its own. Therefore, the pin connection fails. The Async filter could be enhanced to offer MEDIASUBTYPE\_Avi when appropriate. For example, it could examine the file format, or use the file extension.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: \[*SDK Root*\]\\Samples\\Multimedia\\DirectShow\\Filters\\Async.

## Related topics



[DirectShow Samples](directshow-samples.md)


 

 



