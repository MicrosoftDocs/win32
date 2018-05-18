---
Description: WavSink Sample
ms.assetid: '9e1af25f-d55c-45db-8c76-abf814e16700'
title: WavSink Sample
---

# WavSink Sample

Shows how to implement a custom media sink in Microsoft Media Foundation. The sample implements an archive sink that writes uncompressed PCM audio to a .wav file.

## APIs Demonstrated

This sample demonstrates the following Media Foundation interfaces:

-   [**IMFClockStateSink**](imfclockstatesink.md)
-   [**IMFFinalizableMediaSink**](imffinalizablemediasink.md)
-   [**IMFMediaSink**](imfmediasink.md)
-   [**IMFMediaTypeHandler**](imfmediatypehandler.md)
-   [**IMFStreamSink**](imfstreamsink.md)

## Usage

The WavSink sample contains two Visual Studio projects:

-   WavSink.vcproj builds a static library that contains the media sink implementation.
-   WriteWavFile.vcproj builds a console application that uses the media sink to produce a .wav file. This application links to the library created by the WavSink project.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/wavsink).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> </dl>

 

 



