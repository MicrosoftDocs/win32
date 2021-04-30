---
description: Video Capture Interfaces
ms.assetid: a7ec6607-d6fe-4cf4-b3f2-8636c4d15982
title: Video Capture Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Video Capture Interfaces

These interfaces support video capture, using Microsoft® Windows® Driver Model (WDM) devices or legacy Microsoft® Video for Windows® (VFW) devices.



| Interface                                                        | Description                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IAMAnalogVideoDecoder**](/windows/desktop/api/Strmif/nn-strmif-iamanalogvideodecoder)           | Control video digitization on a WDM video capture card.                                                      |
| [**IAMBufferNegotiation**](/windows/desktop/api/Strmif/nn-strmif-iambuffernegotiation)             | Control how a pin allocates buffers.                                                                         |
| [**IAMCopyCaptureFileProgress**](/windows/desktop/api/Strmif/nn-strmif-iamcopycapturefileprogress) | Callback interface to receive the progress of a file copy operation.                                         |
| [**IAMCrossbar**](/windows/desktop/api/Strmif/nn-strmif-iamcrossbar)                               | Create a hardware connection between a WDM audio or video source and a WDM capture device.                   |
| [**IAMDroppedFrames**](/windows/desktop/api/Strmif/nn-strmif-iamdroppedframes)                     | Query a capture filter about capture performance.                                                            |
| [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol)                     | Control the start and stop times of individual streams.                                                      |
| [**IAMStreamConfig**](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig)                       | Query and set the capture filter's output format.                                                            |
| [**IAMVfwCaptureDialogs**](/windows/desktop/api/Strmif/nn-strmif-iamvfwcapturedialogs)             | Display the dialog boxes provided by VFW capture drivers.                                                    |
| [**IAMVideoControl**](/windows/desktop/api/Strmif/nn-strmif-iamvideocontrol)                       | Control the picture from a capture device.                                                                   |
| [**IAMVideoProcAmp**](/windows/desktop/api/Strmif/nn-strmif-iamvideoprocamp)                       | Adjust the qualities of a video signal, such as brightness, contrast, hue, saturation, gamma, and sharpness. |
| [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2)           | Build filter graphs for video capture.                                                                       |
| [**IFileSinkFilter2**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter2)                     | Specify the name and attributes of an output file.                                                           |



 

## Related topics

<dl> <dt>

[External Device Control Interfaces](external-device-control-interfaces.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



