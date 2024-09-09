---
description: Overview of MPEG-2 Systems
ms.assetid: 1ebfb194-002f-40ac-9be5-267861b6687b
title: Overview of MPEG-2 Systems
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Overview of MPEG-2 Systems

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section gives a general, non-technical overview of the MPEG-2 Systems layer. MPEG-2 Systems is the standard that defines how audio and video streams are multiplexed in MPEG-2.

**Elementary Streams**

MPEG-2 multiplexing starts with one or more byte streams, called elementary streams (ES), that contain video, audio, or other data. For example, a video ES contains compressed video frames, plus sequence headers, group-of-picture (GOP) headers, and anything else needed by the decoder to decode the stream. The Systems layer does not define the contents of the ES byte stream.

An elementary stream is broken up into packets, forming a *packetized elementary stream* (PES). PES packets have variable length. The contents of the packet are called the *payload*. Each PES packet also includes a header. The multiplexer assigns a 1-byte stream ID to every PES; individual PES packets are identified by the stream ID in the packet header. For audio streams, the stream ID has the form 110*xxxxx*. For video, the stream ID has the form 1110*yyyy*.

The MPEG-2 standard defines two ways to deliver packetized elementary streams: *program streams* and *transport streams*.

**Program Streams**

Program streams are designed for environments that are relatively error-free, such as local file storage. In a program stream, the PES packets are multiplexed and organized into units called *packs*. All of the PES streams in a program stream are synchronized to the same clock.

**Transport Streams**

Transport streams (TS) are designed for unreliable or error-prone environments, such as network broadcasts. Also, they can contain multiple programs that are synchronized to different clocks. A transport stream adds a second layer of packetizing — the PES streams are packaged inside transport stream packets, which have a fixed size of 188 bytes per packet. TS packets can also contain program information streams, which are described in the following section.

Each TS packet has a 4-byte header, plus an optional adaptation field that contains additional header information. The multiplexer assigns a program ID (PID) to each PES stream or program information stream. The PIDs are used to identify the TS packets, similar to the way stream IDs identify PES packets. (If a transport stream contains multiple programs, the *stream* IDs might not be unique, but the PID assignments are unique within the transport stream.)

**Program Specific Information**

Because a transport stream can carry multiple programs, there must be a way to associate the various PES packets with the programs they belong to. This is accomplished using tables that identify the program streams. Collectively, this data is called Program Specific Information (PSI). The PSI data is carried in TS packets, just like the PES data. There are various types of PSI data, including:

-   Program Association Table (PAT). The PAT is always assigned to PID 0x000. Each entry in the PAT is a PID that identifies the PMT packets for that program (see next item).
-   Program Map Table (PMT). Each PMT defines one program. The PMT contains a list of streams; each table entry gives the PID for that stream, plus a code that identifies the stream type. ISO/IEC 13818-1 defines some standard stream types; an abbreviated list is shown in the following table.

    | stream\_type | Description  |
    |--------------|--------------|
    | 0x01         | MPEG-1 video |
    | 0x02         | MPEG-2 video |
    | 0x03         | MPEG-1 audio |
    | 0x04         | MPEG-2 audio |
    | 0x80 - 0xFF  | User private |

    

     

    Other standards that are based on MPEG-2, such as ATSC, may define additional stream types in the "user private" range. For example, ATSC defines 0x81 as Dolby AC-3 audio.

-   Conditional Access Tables (CAT)
-   Network Identification Tables (NIT)

## Related topics

<dl> <dt>

[MPEG-2 Support in DirectShow](mpeg-2-support-in-directshow.md)
</dt> </dl>

 

 



