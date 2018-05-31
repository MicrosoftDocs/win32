---
title: Microsoft TV Technologies Internals
description: Microsoft TV Technologies Internals
ms.assetid: 8e97052b-6140-4c6c-99e1-f250268141d1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft TV Technologies Internals

This section provides background information on the underlying DirectShow filters and drivers that comprise the Microsoft TV Technologies system architecture. This material is relevant for developers of third-party components such as Guide Store Loaders, MPEG-2 decoders, and BDA device drivers. Applications running on Windows® XP do not communicate directly with the filter graph. Applications running on Windows 98SE, Windows Me, or Windows 2000 cannot use the Video Control, so these applications must build the filter graph and store tune requests.

The following illustration shows all of the Microsoft TV Technologies system components used for the reception of digital TV broadcasts.

![microsoft tv technologies system architecture](images/mstv-architecture.gif)

-   The [BDA Network Provider](bda-network-provider-filter.md) is a user-mode filter that works with the tuner, the MPEG-2 Demultiplexer, and the Transport Information Filter (TIF) to perform tuning and to route of elementary streams based on the tune request.

    Microsoft provides Network Provider filters for ATSC, DVB-C, DVB-T, and DVB-S standards.

-   **BDA Device Filters:** The driver specification associated with Microsoft TV Technologies is called Broadcast Driver Architecture (BDA). It is used by independent hardware vendors (IHVs) who wish to create digital TV tuning devices that work with Windows. IHVs also use BDA to support new network types or custom hardware functionality. BDA-compatible drivers are automatically represented as DirectShow filters through the KsProxy wrapper filter. The exact names of these filters, and the number of different filters that are used to represent the device, may vary depending on the driver. The details of BDA are not important for application developers; BDA is documented in the DirectX 9.0 DDK and the Microsoft Platform DDK for Windows XP.
-   The [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) filter accepts the MPEG-2 transport stream from the capture filter and demultiplexes the stream based on packet IDs (PIDs) provided by the Network Provider. The Network Provider configures the output pins on the demux.
-   The [BDA MPEG-2 Transport Information Filter](bda-mpeg-2-transport-information-filter.md) (TIF) receives the PSI packets, parses the tables, and provides information to the Network Provider. The [**MPEG-2 Sections and Tables**](mpeg-2-sections-and-tables-filter.md) filter also receives PSI packets. Third-parties can develop software components called guide store loaders that receive table data from the TIF and the MPEG-2 Sections and Tables filter, and use this data to create tune requests. For more information, see [The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md).
-   **MPEG-2 Decoders:** A digital TV filter graph requires an MPEG-2 decoder capable of decoding High Definition Television (HDTV) video streams. Some decoders may decode audio and video in the same filter, while others may have separate filters for audio and video. To achieve the performance necessary to support HDTV, the decoder should support Microsoft DirectX Video Acceleration (DXVA), which is a specification for hardware acceleration of digital video decoding processing. DXVA is documented in the DirectX 9.0 DDK and the Microsoft Platform DDK for Windows XP. The user-mode interface for DXVA, [**IAMVideoAccelerator**](https://msdn.microsoft.com/library/windows/desktop/dd375992), is used by software decoders and is documented in this SDK.
    > [!Note]  
    > The preceding illustration shows a software decoder. Hardware decoders are also supported. When a hardware decoder is used, the [Video Port Manager](https://msdn.microsoft.com/library/windows/desktop/dd407346) filter connects to one of the decoder's output pins and manages the video port connection to the graphics card.

     

-   **Video and Audio Renderers:** The Video Mixing Renderer (VMR) is a video rendering filter that replaces both the Overlay Mixer filter and Video Renderer filter. For more information, see [Using the Video Mixing Renderer](https://msdn.microsoft.com/library/windows/desktop/dd407294). The audio renderer plays the decoded audio stream through the system's speakers.
-   **Data Services Filters:** These filters accept IP data from the MPEG-2 Demultiplexer and pass it either to the renderer (in the case of Line 21 or closed captioning data) or else to Winsock. The data services filters that are present in the graph depend on the type of data being processed. The illustration above shows the filters that are used to pass IP data to Winsock: the [BDA MPE](bda-mpe-filter.md) filter and the [BDA IP Sink](bda-ip-sink-filter.md) filter.

## Related topics

<dl> <dt>

[Overview of Microsoft TV Technologies](overview-of-microsoft-tv-technologies.md)
</dt> </dl>

 

 




