---
description: Shows how to implement a video effect as a Media Foundation Transform (MFT).
ms.assetid: ad7d20bc-5eab-4390-a48b-5ea8e97ead7d
title: MFT_Grayscale Sample
ms.topic: article
ms.date: 05/31/2018
---

# MFT\_Grayscale Sample

Shows how to implement a video effect as a Media Foundation Transform (MFT). The grayscale MFT converts YUV video to grayscale by setting the chroma values in the video to neutral. The MFT accepts uncompressed video in UYVY, YUY2, or NV12 formats.

## APIs Demonstrated

This sample demonstrates the following Microsoft Media Foundation interfaces:

-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

## Usage

The MFT\_GrayScale sample builds a DLL that is a COM server for the MFT. Before using the MFT, you must register the DLL.

To see the grayscale MFT in use, run the [PlaybackFX Sample](/previous-versions//bb970336(v=vs.85)). You can also use the TopoEdit tool to build a topology that includes the grayscale MFT. For more information about TopoEdit, see [TopoEdit](topoedit.md).

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/mft_grayscale).

## Related topics

<dl> <dt>

[About YUV Video](about-yuv-video.md)
</dt> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> <dt>

[MFT\_AudioDelay Sample](mft-audiodelay-sample.md)
</dt> <dt>

[Writing a Custom MFT](writing-a-custom-mft.md)
</dt> </dl>

 

 
