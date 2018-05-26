---
Description: Digital Signal Processors
ms.assetid: cd3952ca-3958-4944-8fde-f0163a47bff9
title: Digital Signal Processors
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Digital Signal Processors

This section describes the digital signal processor (DSP) objects provided by Windows.

Microsoft uses the term *digital signal processor* to designate a set of COM objects that perform transformations on uncompressed audio and video data. The DSPs described in this SDK transform audio and video in a variety of uncompressed formats.

The DSPs can be used by themselves, or in combination with audio and video codecs. With the exception of the Voice Capture DSP, each DSP listed here implements two separate but similar interfaces.



| Interface                              | Description                                 |
|----------------------------------------|---------------------------------------------|
| [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master)   | Compatible with Microsoft Media Foundation. |
| [**IMediaObject**](dshow.imediaobject) | Compatible with DirectShow.                 |



 

You can configure the DSPs by using the [**IPropertyStore**](properties.IPropertyStore) interface to set properties. Some of the DSPs have additional interfaces that set properties. To use these interfaces, call the [**QueryInterface**](com.iunknown_queryinterface) method of any other interface of the DSP. The reference topic for each DSP lists the supported properties, interfaces, and other features.

This section contains the following topics.



| DSP                                                      | Description                                          |
|----------------------------------------------------------|------------------------------------------------------|
| [Audio Resampler DSP](audioresampler.md)                | Converts the sampling rate of an audio stream.       |
| [Color Control Transform DSP](colorcontroltransform.md) | Adjusts the color characteristics of a video stream. |
| [Color Converter DSP](colorconverter.md)                | Converts a video stream between color formats.       |
| [Frame Rate Converter DSP](framerateconverter.md)       | Changes the frame rate of a video stream.            |
| [Video Resizer DSP](videoresizer.md)                    | Resizes a video stream.                              |
| [Voice Capture DSP](voicecapturedmo.md)                 | Encapsulates several DSPs related to voice capture.  |



 

## Related topics

<dl> <dt>

[Media Foundation Programming Reference](media-foundation-programming-reference.md)
</dt> </dl>

 

 



