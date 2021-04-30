---
description: DirectX Video Acceleration 2.0
ms.assetid: acb73b20-89fa-4a48-be4a-846715a239b0
title: DirectX Video Acceleration 2.0
ms.topic: article
ms.date: 05/31/2018
---

# DirectX Video Acceleration 2.0

DirectX Video Acceleration (DXVA) is an API and a corresponding DDI for using hardware-acceleration to speed up video codec processing. Software codecs and software video processors can use DXVA to offload certain CPU-intensive operations to the GPU. For example, a software decoder can offload the inverse discrete cosine transform (iDCT) to the GPU.

This section contains the following topics.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About DXVA 2.0](about-dxva-2-0.md)<br/>                                                   | Overview of DXVA 2 and its relation to DXVA 1.<br/>                                                                                                                                                        |
| [Direct3D Device Manager](direct3d-device-manager.md)<br/>                                 | The Microsoft Direct3D device manager enables two or more objects to share the same Microsoft Direct3D 9 device.<br/>                                                                                      |
| [Supporting DXVA 2.0 in DirectShow](supporting-dxva-2-0-in-directshow.md)<br/>             | This topic describes how to support DirectX Video Acceleration (DXVA) 2.0 in a DirectShow decoder filter.<br/>                                                                                             |
| [Supporting DXVA 2.0 in Media Foundation](supporting-dxva-2-0-in-media-foundation.md)<br/> | This topic describes how to support DirectX Video Acceleration (DXVA) 2.0 in a Media Foundation transform (MFT) using Direct3D 9<br/>                                                                      |
| [DXVA Video Processing](dxva-video-processing.md)<br/>                                     | DXVA video processing encapsulates the functions of the graphics hardware that are devoted to processing uncompressed video images. Video processing services include deinterlacing and video mixing.<br/> |
| [DXVA-HD](dxva-hd.md)<br/>                                                                 | Microsoft DirectX Video Acceleration High Definition (DXVA-HD) is an API for hardware-accelerated video processing. <br/>                                                                                  |



 

## Related topics

<dl> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> <dt>

[DXVA 1 Specification](/windows-hardware/drivers/display/directx-video-acceleration)
</dt> </dl>

 

 
