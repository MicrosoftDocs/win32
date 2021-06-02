---
description: Configuring the Demux Output Pins
ms.assetid: c53f3fe6-5588-4faf-ba5c-6a6cf7e16f3a
title: Configuring the Demux Output Pins
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Demux Output Pins

When the MPEG-2 demux receives a packet of data, it must determine which output pin should parse and deliver the data. In program stream mode, the demux maps stream IDs to output pins. In transport stream mode, it maps PIDs to output pins. For example, in transport stream mode, if PID 0x31 is mapped to pin 0, then every TS packet with that PID number is routed to output pin 0. If the demux receives a packet whose stream ID or PID is not mapped to any output pin, it simply discards the packet.

In pull mode, the demux automatically creates output pins for the audio and video streams in the file, and maps the stream IDs to the pins.

In push mode, the output pins must be configured by the application or by another filter. For digital television sources using the Broadcast Driver Architecture (BDA), the network provider filter works with the TIF filter to configure the demux. The application does not have to do anything. In other scenarios, the application must configure the output pins.

The demux starts with no output pins. To create an output pin, call the [**IMpeg2Demultiplexer::CreateOutputPin**](/windows/desktop/api/Strmif/nf-strmif-impeg2demultiplexer-createoutputpin) method on the filter. This method takes a media type and a pin name, and returns an **IPin** pointer. The media type is used when the pin connects to another filter, typically a decoder—an example is given the section [Using the Demux with Elementary Streams](using-the-demux-with-elementary-streams.md). The pin name can be anything you like, except that duplicate pin names are not allowed.

Next, assign one or more stream IDs or PIDs to the new output pin. For program streams, query the pin for **IMPEG2StreamIdMap** and call [**IMPEG2StreamIdMap::MapStreamId**](/windows/desktop/api/Strmif/nf-strmif-impeg2streamidmap-mapstreamid). For transport streams, query the pin for **IMPEG2PIDMap** and call [**IMPEG2PIDMap::MapPID**](/previous-versions/windows/desktop/api/Bdaiface/nf-bdaiface-impeg2pidmap-mappid).

There are several ways that the demux can parse TS packets. For each output pin, the parsing method is determined by the *MediaSampleContent* parameter to the **MapPID** method.



| Value                     | Description                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MEDIA\_ELEMENTARY\_STREAM | The filter delivers PES payloads. In this mode, the filter depacketizes the PES packets, so the downstream filter receives the ES byte stream, without the PES packet headers. (Audio and video streams only.)                                                                                                                                                     |
| MEDIA\_MPEG2\_PSI         | The filter delivers complete PSI sections, such as PAT tables, PMT tables, CAT tables, and so forth.                                                                                                                                                                                                                                                               |
| MEDIA\_TRANSPORT\_PAYLOAD | The filter extracts the payloads from the TS packets and delivers them without further parsing. For elementary streams, this means the demux will deliver entire PES packets, including the PES packet headers.                                                                                                                                                    |
| MEDIA\_TRANSPORT\_PACKET  | The filter delivers entire TS packets. The demux routes the TS packets according to their PIDs, but does not otherwise examine or process the packets. Packets with errors are not filtered out. The demux does not re-multiplex the packets, and the resulting output stream is not a compliant MPEG-2 transport stream. This mode is called *pass through* mode. |



 

For program streams, the demux always delivers PES payloads.

## Related topics

<dl> <dt>

[Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md)
</dt> </dl>

 

 



