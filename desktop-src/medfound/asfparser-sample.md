---
description: ASFParser Sample
ms.assetid: 6be1e12f-7d4a-4564-88ae-14fd71fd2cf9
title: ASFParser Sample
ms.topic: article
ms.date: 05/31/2018
---

# ASFParser Sample

Shows how to parse data from an Advanced Systems Format (ASF) file by using the low-level ASF components in Media Foundation. The sample demonstrates the following tasks:

-   Enumerating the audio and video streams in an ASF file.
-   Selecting an audio or a video stream for parsing.
-   Seeking to a packet at a desired playback time.
-   Generating compressed samples for the selected stream.
-   Decoding audio and video samples.

## APIs Demonstrated

This sample demonstrates the following Microsoft Media Foundation interfaces:

-   [**IMFASFContentInfo**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfcontentinfo)
-   [**IMFASFIndexer**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfindexer)
-   [**IMFASFSplitter**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfsplitter)

## Usage

1.  To open an ASF file, click the **Open Media File...** button.
2.  Select an ASF file and click **Open**. Information about the file is shown on the **Information** pane.
3.  Under **Parser Configuration**, select a stream to parse.
4.  To generate samples in reverse, select **Reverse**.
5.  To specify the start point, drag the slider to the desired location.
6.  To begin parsing, click the **Generate Samples** button. Information about the samples is shown on the **Information** pane.
7.  To test the samples for the audio stream, click the **Test Audio** button.
8.  To test the samples for the video stream, click the **Show Bitmap** button.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/asfparser).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> <dt>

[Tutorial: Reading an ASF File](tutorial--reading-an-asf-file.md)
</dt> <dt>

[WMContainer ASF Components](wmcontainer-asf-components.md)
</dt> </dl>

 

 



