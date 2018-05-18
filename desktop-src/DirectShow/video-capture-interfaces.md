---
Description: Video Capture Interfaces
ms.assetid: 'a7ec6607-d6fe-4cf4-b3f2-8636c4d15982'
title: Video Capture Interfaces
---

# Video Capture Interfaces

These interfaces support video capture, using Microsoft® Windows® Driver Model (WDM) devices or legacy Microsoft® Video for Windows® (VFW) devices.



| Interface                                                        | Description                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IAMAnalogVideoDecoder**](iamanalogvideodecoder.md)           | Control video digitization on a WDM video capture card.                                                      |
| [**IAMBufferNegotiation**](iambuffernegotiation.md)             | Control how a pin allocates buffers.                                                                         |
| [**IAMCopyCaptureFileProgress**](iamcopycapturefileprogress.md) | Callback interface to receive the progress of a file copy operation.                                         |
| [**IAMCrossbar**](iamcrossbar.md)                               | Create a hardware connection between a WDM audio or video source and a WDM capture device.                   |
| [**IAMDroppedFrames**](iamdroppedframes.md)                     | Query a capture filter about capture performance.                                                            |
| [**IAMStreamControl**](iamstreamcontrol.md)                     | Control the start and stop times of individual streams.                                                      |
| [**IAMStreamConfig**](iamstreamconfig.md)                       | Query and set the capture filter's output format.                                                            |
| [**IAMVfwCaptureDialogs**](iamvfwcapturedialogs.md)             | Display the dialog boxes provided by VFW capture drivers.                                                    |
| [**IAMVideoControl**](iamvideocontrol.md)                       | Control the picture from a capture device.                                                                   |
| [**IAMVideoProcAmp**](iamvideoprocamp.md)                       | Adjust the qualities of a video signal, such as brightness, contrast, hue, saturation, gamma, and sharpness. |
| [**ICaptureGraphBuilder2**](icapturegraphbuilder2.md)           | Build filter graphs for video capture.                                                                       |
| [**IFileSinkFilter2**](ifilesinkfilter2.md)                     | Specify the name and attributes of an output file.                                                           |



 

## Related topics

<dl> <dt>

[External Device Control Interfaces](external-device-control-interfaces.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



