---
description: Shows how to use Microsoft DirectX Video Acceleration High Definition (DXVA-HD).
ms.assetid: dfd5cf5c-7d6e-4894-8d9b-41ef0293b3d3
title: DXVA-HD Sample
ms.topic: article
ms.date: 05/31/2018
---

# DXVA-HD Sample

Shows how to use Microsoft DirectX Video Acceleration High Definition (DXVA-HD).

This sample is essentially a port of the [DXVA2\_VideoProc Sample](dxva2-videoproc-sample.md). It has the same basic functions, and most of the keyboard commands are the same.

The sample programmatically generates video with a primary stream and a substream. The primary stream displays SMPTE color bars. The substream is alpha-blended onto the primary stream using luma keying. The user can change the video processing parameters, including the planar alpha value, source and destination rectangles, color adjustments, and color space. The following image shows that video that is generated.

![screen shot of the dxva-hd sample](images/dxva-hd-sample.png)

## APIs Demonstrated

This sample demonstrates the following DXVA-HD interfaces:

-   [**IDXVAHD\_Device**](/windows/desktop/api/dxvahd/nn-dxvahd-idxvahd_device)
-   [**IDXVAHD\_VideoProcessor**](/windows/desktop/api/dxvahd/nn-dxvahd-idxvahd_videoprocessor)

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/DXVA_HD).

## Related topics

<dl> <dt>

[DXVA-HD](dxva-hd.md)
</dt> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> </dl>

 

 



