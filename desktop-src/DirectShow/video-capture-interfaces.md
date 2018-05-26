---
Description: Video Capture Interfaces
ms.assetid: a7ec6607-d6fe-4cf4-b3f2-8636c4d15982
title: Video Capture Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Capture Interfaces

These interfaces support video capture, using Microsoft® Windows® Driver Model (WDM) devices or legacy Microsoft® Video for Windows® (VFW) devices.



| Interface                                                        | Description                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IAMAnalogVideoDecoder**](/windows/win32/Strmif/nn-strmif-iamanalogvideodecoder?branch=master)           | Control video digitization on a WDM video capture card.                                                      |
| [**IAMBufferNegotiation**](/windows/win32/Strmif/nn-strmif-iambuffernegotiation?branch=master)             | Control how a pin allocates buffers.                                                                         |
| [**IAMCopyCaptureFileProgress**](/windows/win32/Strmif/nn-strmif-iamcopycapturefileprogress?branch=master) | Callback interface to receive the progress of a file copy operation.                                         |
| [**IAMCrossbar**](/windows/win32/Strmif/nn-strmif-iamcrossbar?branch=master)                               | Create a hardware connection between a WDM audio or video source and a WDM capture device.                   |
| [**IAMDroppedFrames**](/windows/win32/Strmif/nn-strmif-iamdroppedframes?branch=master)                     | Query a capture filter about capture performance.                                                            |
| [**IAMStreamControl**](/windows/win32/Strmif/nn-strmif-iamstreamcontrol?branch=master)                     | Control the start and stop times of individual streams.                                                      |
| [**IAMStreamConfig**](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master)                       | Query and set the capture filter's output format.                                                            |
| [**IAMVfwCaptureDialogs**](/windows/win32/Strmif/nn-strmif-iamvfwcapturedialogs?branch=master)             | Display the dialog boxes provided by VFW capture drivers.                                                    |
| [**IAMVideoControl**](/windows/win32/Strmif/nn-strmif-iamvideocontrol?branch=master)                       | Control the picture from a capture device.                                                                   |
| [**IAMVideoProcAmp**](/windows/win32/Strmif/nn-strmif-iamvideoprocamp?branch=master)                       | Adjust the qualities of a video signal, such as brightness, contrast, hue, saturation, gamma, and sharpness. |
| [**ICaptureGraphBuilder2**](/windows/win32/Strmif/nn-strmif-icapturegraphbuilder2?branch=master)           | Build filter graphs for video capture.                                                                       |
| [**IFileSinkFilter2**](/windows/win32/Strmif/nn-strmif-ifilesinkfilter2?branch=master)                     | Specify the name and attributes of an output file.                                                           |



 

## Related topics

<dl> <dt>

[External Device Control Interfaces](external-device-control-interfaces.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



