---
description: Shows how to use Microsoft Media Foundation to decode audio from a media file.
ms.assetid: 29822e6b-8598-4133-b181-7fb0854553b7
title: Audio Clip Sample
ms.topic: article
ms.date: 05/31/2018
---

# Audio Clip Sample

Shows how to use Microsoft Media Foundation to decode audio from a media file.

The Audio Clip sample application reads audio data from a media file and writes the uncompressed audio to a WAVE file.

## APIs Demonstrated

This sample demonstrates the following Media Foundation interfaces:

-   [**IMFSourceReader**](/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereader)

## Usage

This sample is a command-line application. It uses the following command-line arguments:

``` syntax
audioclip.exe inputfile outputfile.wav
```

-   inputfile: The name of a file that contains an audio stream.
-   outputfile.wav: The name of the WAVE file to write.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/AudioClip).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[Tutorial: Decoding Audio](tutorial--decoding-audio.md)
</dt> </dl>

 

 



