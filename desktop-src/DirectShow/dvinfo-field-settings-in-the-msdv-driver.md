---
description: DVINFO Field Settings in the MSDV Driver
ms.assetid: f0723da5-4f53-4f83-a657-ae42815a784e
title: DVINFO Field Settings in the MSDV Driver
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVINFO Field Settings in the MSDV Driver

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how the MSDV driver fills in the [**DVINFO**](/windows/desktop/api/strmif/ns-strmif-dvinfo) structure.

The `DVINFO` structure defines the format block for pin connections between MSDV and other filters. By default, the DV Splitter filter is used when capturing from a DV device, and the DV Mux filter is used when transmitting to the device. However, applications may provide their own custom filters, so it is useful to understand how MSDV populates the `DVINFO` format block.

The `DVINFO` structure contains the following information:

-   Two audio auxiliary (AAUX) source packs, for the first and second audio blocks.
-   Two AAUX source control packs, for the first and second audio blocks.
-   A video auxiliary (VAUX) source pack.
-   A VAUX source control pack.

Every frame in a DV stream contains AAUX and VAUX packs. However, the `DVINFO` format block is static, and is only used to establish the pin connection. When the MSDV driver connects, it does not examine any of the AAUX or VAUX packs in the stream. Instead, it uses a set of default values, based on the following characteristics of the DV device:

-   Whether the device supports a consumer format (DVCR) or professional format (DVCPRO)
-   The signal type
-   Whether the format is NTSC or PAL. (If the device does not report this information, MSDV defaults to the NTSC settings)

Once streaming begins, it is the responsibility of the user-mode filters, such as the DV Splitter, to examine the actual contents of each DV frame. Because the information can change from frame to frame, the filter may need to perform a dynamic format change. For example, if the audio rate changes, the filter might need to renegotiate the audio type.

If you capture a type-1 DV file, the `DVINFO` structure is written into the file as the stream format ('strf') chunk. This data is taken directly from the format block provided by MSDV. As noted, the actual content of the stream might be different. It is the application's responsibility to examine the AAUX and VAUX packs in each frame.

In the following topics, you can find tables listing all of the fields used by MSDV.

-   [AAUX Source (AS) Pack](aaux-source--as--pack.md)
-   [AAUX Source Control (ASC) Pack](aaux-source-control--asc--pack.md)
-   [VAUX Source (VS) Pack](vaux-source--vs--pack.md)
-   [VAUX Source Control (VSC) Pack](vaux-source-control--vsc--pack.md)

When reading these tables, please consult the following specifications:

-   IEC 61834
-   SMPTE 314M
-   SMPTE 370

In each table, the first column gives the field code, followed by the number of bits (in parentheses). The remaining columns give the field values. Many of the AAUX and VAUX fields are not relevant for the pin connection, in which case MSDV sets a dummy value. The numeric value of the entire pack is listed at the bottom of each table.

The notes after each table give more information about selected fields. For complete descriptions, refer to the specifications. Also, some fields do not have the same meaning in SMPTE 314M/SMPTE 370 as they do in IEC 61834.

> [!Note]  
> Currently, DirectShow does not support DVCPRO formats. The values listed for the DVCPRO formats are defined for future use.

 

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[DV Data in the AVI File Format](dv-data-in-the-avi-file-format.md)
</dt> <dt>

[MSDV Driver](msdv-driver.md)
</dt> </dl>

 

 



