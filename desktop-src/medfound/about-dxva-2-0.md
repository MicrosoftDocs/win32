---
description: Overview of DXVA 2 and its relation to DXVA 1.
ms.assetid: 190ed399-a8a8-4087-8d18-b1a715690e4c
title: About DXVA 2.0
ms.topic: article
ms.date: 05/31/2018
---

# About DXVA 2.0

DirectX Video Acceleration (DXVA) is an API and a corresponding DDI for using hardware acceleration to speed up video processing. Software codecs and software video processors can use DXVA to offload certain CPU-intensive operations to the GPU. For example, a software decoder can offload the inverse discrete cosine transform (iDCT) to the GPU.

In DXVA, some decoding operations are implemented by the graphics hardware driver. This set of functionality is termed the *accelerator*. Other decoding operations are implemented by user-mode application software, called the *host decoder* or *software decoder*. (The terms *host decoder* and *software decoder* are equivalent.) Processing performed by the accelerator is called *off-host processing*. Typically the accelerator uses the GPU to speed up some operations. Whenever the accelerator performs a decoding operation, the host decoder must convey to the accelerator buffers containing the information needed to perform the operation

The DXVA 2 API requires Windows Vista or later. The DXVA 1 API is still supported in Windows Vista for backward compatibility. An emulation layer is provided that converts between either version of the API and the opposite version of the DDI:

-   If the graphics driver conforms to the Windows Display Driver Model (WDDM), DXVA 1 API calls are converted to DXVA 2 DDI calls.
-   If the graphics drivers uses the older Windows XP Display Driver Model (XPDM), DXVA 2 API calls are converted to DXVA 1 DDI calls.

The following table shows the operating system requirements and the supported video renderers for each version of the DXVA API.



| API Version | Requirements          | Video Renderer Support                        |
|-------------|-----------------------|-----------------------------------------------|
| DXVA 1      | Windows 2000 or later | Overlay Mixer, VMR-7, VMR-9 (DirectShow only) |
| DXVA 2      | Windows Vista         | EVR (DirectShow and Media Foundation)         |



 

In DXVA 1, the software decoder must access the API through the video renderer. There is no way to use the DXVA 1 API without calling into the video renderer. This limitation has been removed with DXVA 2. Using DXVA 2, the host decoder (or any application) can access the API directly, through the [**IDirectXVideoDecoderService**](/windows/win32/api/dxva2api/nn-dxva2api-idirectxvideodecoderservice) interface.

The DXVA 1 documentation describes the decoding structures used for the following video standards:

-   ITU-T Rec. H.261
-   ITU-T Rec. H.263
-   MPEG-1 video
-   MPEG-2 Main Profile video

The following specifications define DXVA extensions for other video standards:

-   [DXVA Specification for H.264/AVC Decoding](https://www.microsoft.com/downloads/details.aspx?FamilyID=3d1c290b-310b-4ea2-bf76-714063a6d7a6&displaylang=en)
-   [DXVA Specification for H.264/MPEG-4 AVC Multiview Video Coding (MVC), Including the Stereo High Profile](https://www.microsoft.com/download/details.aspx?id=25200)
-   [DXVA Specification for MPEG-1 VLD and Combined MPEG-1/MPEG-2 VLD Video Decoding](https://www.microsoft.com/download/details.aspx?id=9374).
-   [DXVA Specification for Off-Host VLD Mode for MPEG-4 Part 2 Video Decoding](https://www.microsoft.com/download/details.aspx?id=21100)
-   [DXVA Specification for Windows Media Video® v8, v9 and vA Decoding (Including SMPTE 421M "VC-1")](https://www.microsoft.com/downloads/details.aspx?FamilyID=8792dfdb-8459-4cb7-adb4-fef30b609b31&displaylang=en)
-   [DirectX Video Acceleration (DXVA) Specification for H.264/MPEG-4 Scalable Video Coding (SVC) Off-Host VLD Mode Decoding](https://www.microsoft.com/downloads/details.aspx?FamilyID=a38538b6-f52c-470b-94be-0cf7c28d46cc&displaylang=en)
-   [DirectX Video Acceleration Specification for VP8 and VP9 Video Coding](https://www.microsoft.com/download/details.aspx?id=49188)

DXVA 1 and DXVA 2 use the same data structures for decoding. However, the procedure for configuring the decoding session has changed. DXVA 1 uses a "probe and lock" mechanism, wherein the host decoder can test various configurations before setting the desired configuration on the accelerator. In DXVA 2, the accelerator returns a list of supported configurations and the host decoder selects one from the list. Details are given in the following sections:

-   [Supporting DXVA 2.0 in DirectShow](supporting-dxva-2-0-in-directshow.md)
-   [Supporting DXVA 2.0 in Media Foundation](supporting-dxva-2-0-in-media-foundation.md)

## Related topics

<dl> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> <dt>

[DXVA 1.0 specification](/windows-hardware/drivers/display/directx-video-acceleration)
</dt> </dl>

 

 
