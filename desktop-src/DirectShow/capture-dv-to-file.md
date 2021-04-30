---
description: Capture DV to File
ms.assetid: f7a8bcbb-a744-43c4-a226-354ae2d94df8
title: Capture DV to File
ms.topic: article
ms.date: 05/31/2018
---

# Capture DV to File

This section describes how to capture digital video (DV) from a DV camera or from a VTR tape.

1.  Create an instance of the [MSDV Driver](msdv-driver.md) filter. For more information, see [Selecting a Capture Device](selecting-a-capture-device.md).
2.  Initialize the Capture Graph Builder, as described in [About the Capture Graph Builder](about-the-capture-graph-builder.md).
3.  Build the capture graph, depending on the target file type:
    -   [Capture a Type-1 DV File](capture-a-type-1-dv-file.md)
    -   [Capture a Type-2 DV File](capture-a-type-2-dv-file.md)
    -   [Capture DV to Uncompressed RGB](capture-dv-to-uncompressed-rgb.md)
4.  Run the graph.

Capturing from a VTR tape works just like capturing live video from the camera, except that you must play the tape, as described in [Controlling a DV Camcorder](controlling-a-dv-camcorder.md). To avoid losing any frames, run the graph first, and then play the tape. When you are done transmitting, stop the tape first and then stop the graph.

> [!Note]  
> The camcorder must be in VTR mode. See [Device Mode](device-mode.md).

 

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[Type-1 vs. Type-2 DV AVI Files](type-1-vs--type-2-dv-avi-files.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



