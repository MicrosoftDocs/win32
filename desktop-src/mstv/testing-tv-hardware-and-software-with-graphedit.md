---
title: Testing TV Hardware and Software with GraphEdit
description: Testing TV Hardware and Software with GraphEdit
ms.assetid: '10d3e5af-1ff6-4e3b-81a8-0a1adaac5b1d'
---

# Testing TV Hardware and Software with GraphEdit

This topic applies to Windows XP or later.

Whenever you write a DirectShow-based application, it is generally useful to start by creating a prototype filter graph in GraphEdit. Even though GraphEdit does not use the Video Control, creating the prototype is a quick way to verify that your TV device and HDTV-compatible MPEG-2 decoder are installed and working properly.

Before you can build a digital TV graph, you must register the Dynamic Link Library (proppage.dll) provided by the Platform SDK. (At the command line, type "regsvr32 \[path\]proppage.dll".) This DLL contains the property page needed to tune the Network Provider filter. This property page is provided only for testing purposes. Working applications should provide their own user interface.

When building a graph using GraphEdit, it is important to remember that Broadcast Driver Architecture (BDA) allows for flexibility in the "topology" of the device. For application developers, this means that the names and number of filters used to represent the tuning device may vary depending on the manufacturer or the specific card. For example, some cards may expose a demodulator as a separate filter, while others may not. In general, most cards will probably expose two or three filters for a digital filter graph: a tuner, a demodulator, and a capture filter. Likewise, the MPEG-2 decoder may or may not expose a separate filter for audio decoding. The following image illustrates this process.

![mstv filter graph](images/mstv-graph.gif)

When creating this filter graph in GraphEdit, the basic rule is to manually add and connect all the filters up through the MPEG-2 Demultiplexer, and then right-click on the output pins of the Demultiplexer to render each of the streams. "Render" in this context means that GraphEdit will automatically add and connect the remaining filters needed to render the stream. It is still necessary to click on the **Run** button to start the graph playing.

But before starting the graph, you must first tune to a channel. Right click on the Network Provider filter, select **Properties** and click on the **Tune Request** tab. Tune to a physical channel that you know is valid. The "-1" values for minor channel and major channel simply mean to use the defaults. Once the channel is selected, the graph is ready to be put into the Run state. It must be stopped before changing the channel.

**Filters in a Digital Filter Graph**

[BDA Network Provider](bda-network-provider-filter.md): A BDA Network Provider filter is always the first filter in the graph. This particular graph has the ATSC Network Provider. Microsoft also provides Network Providers for DVB. Third parties may also provide their own Network Provider that is customized for their own broadcasts. The Network Provider configures the downstream filters for a particular tuning space, which includes information on content multiplexing, modulation, and transmission standards. This filter implements the [**ITuner**](ituner.md) interface, which applications use to tune the device to the specified channel or frequency.

**Digital TV Tuner**: This kernel-mode KsProxy-based filter represents the tuner on the hardware device. It may or may not have any application-callable interfaces, depending on the implementation of the third-party driver. This filter might also encapsulate a demodulator device.

**Digital TV Capture Filter**: This kernel-mode KsProxy-based filter represents the demodulator/digitizer on the hardware device. Its single output pin delivers the MPEG-2 transport stream to the MPEG-2 Demultiplexer.

[MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715): In a digital TV graph, the MPEG-2 demultiplexer accepts the MPEG-2 transport stream from the capture filter and demultiplexes the stream. It typically has four output pins. Its first output pin delivers raw program service information (PSI) packets to the Transport Information Filter. The second pin delivers the video stream to the MPEG-2 decoder. The third pin delivers the audio to the audio decoder, and the fourth pin delivers IP data.

[BDA MPEG-2 Transport Information Filter](bda-mpeg-2-transport-information-filter.md): So that a receiver can properly acquire all the elementary streams related to a specific program and so that a receiver can tell what programs are contained in the stream, the transport stream will also contain many sets of tables that act as a catalog of information contained in the transport stream. Under direction of the [BDA Network Provider](bda-network-provider-filter.md), the [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) delivers these tables to the Transport Information Filter, which then parses these tables and provides the information to the Network Provider so that it can control the other receiver filters and nodes in the graph. The BDA Transport Information Filter also provides interfaces to enable the Guide Store loader to extract the relevant EPG and locator information and load it into an application-provided database for later retrieval by the application.

**HDTV-capable MPEG-2 Decoder**: A Digital TV filter graph requires a decoder that is capable of decoding High Definition Television (HDTV) video streams. Some decoder implementations may operate on both audio and video streams in the same filter, while others may have separate filters for audio and video.

**Video Renderer**: Two video renderers are present on Microsoft XP, the older [Video Renderer](https://msdn.microsoft.com/library/windows/desktop/dd407349) and the new Video Mixing Renderer (VMR). Both have the same name in GraphEdit but the old renderer is never used by the Video Control, so the "Video Renderer" in a TV graph is always the Video Mixing Renderer. The VMR renders the video stream onto the system's video memory. It can also display an application-specified alpha-blended bitmap over the video rectangle, or mix the TV video stream with other video streams for special effects.

[BDA MPE Filter](bda-mpe-filter.md): This filter extracts IP packets from the Multi-Protocol Encapsulation (MPE) stream and delivers them to IP Sink.

[BDA IP Sink](bda-ip-sink-filter.md): This filter accepts IP packets and delivers them to the host system via Winsock, where interested applications can listen for and receive IP data streams.

 

 




