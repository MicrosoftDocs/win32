---
Description: Alphabetical List of DirectShow Interfaces
ms.assetid: 9c7f56f4-92af-40c6-8124-f2715ac3f6d7
title: Alphabetical List of DirectShow Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Alphabetical List of DirectShow Interfaces

The following is an alphabetical list of DirectShow interfaces.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Interface</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IAMAnalogVideoDecoder</strong>](/windows/win32/Strmif/nn-strmif-iamanalogvideodecoder?branch=master)</td>
<td>Sets and retrieves information about the analog-to-digital conversion process in a video capture filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMAudioInputMixer</strong>](/windows/win32/Strmif/nn-strmif-iamaudioinputmixer?branch=master)</td>
<td>Controls audio capture properties.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMAudioRendererStats</strong>](/windows/win32/Strmif/nn-strmif-iamaudiorendererstats?branch=master)</td>
<td>Retrieves statistical performance information from an audio renderer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMBufferNegotiation</strong>](/windows/win32/Strmif/nn-strmif-iambuffernegotiation?branch=master)</td>
<td>Requests the number of buffers for a filter to create and size of each buffer.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMCameraControl</strong>](/windows/win32/Strmif/nn-strmif-iamcameracontrol?branch=master)</td>
<td>Controls camera settings such as zoom, pan, aperture adjustment, or shutter speed.</td>
</tr>
<tr class="even">
<td>[<strong>IAMCertifiedOutputProtection</strong>](/windows/win32/Strmif/nn-strmif-iamcertifiedoutputprotection?branch=master)</td>
<td>Sends Certified Output Protection Protocol (COPP) messages to the graphics driver.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMChannelInfo</strong>](/windows/win32/Qnetwork/nn-qnetwork-iamchannelinfo?branch=master)</td>
<td>Gets and sets channel information for Windows Media Station (.nsc) files.</td>
</tr>
<tr class="even">
<td>[<strong>IAMClockAdjust</strong>](/windows/win32/Strmif/nn-strmif-iamclockadjust?branch=master)</td>
<td>Adjusts the reference clock.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMClockSlave</strong>](/windows/win32/Strmif/nn-strmif-iamclockslave?branch=master)</td>
<td>Controls the tolerance of an audio renderer when it is matching rates with another clock.</td>
</tr>
<tr class="even">
<td>[<strong>IAMCopyCaptureFileProgress</strong>](/windows/win32/Strmif/nn-strmif-iamcopycapturefileprogress?branch=master)</td>
<td>Callback interface for the [<strong>ICaptureGraphBuilder2::CopyCaptureFile</strong>](/windows/win32/Strmif/nf-strmif-icapturegraphbuilder2-copycapturefile?branch=master) method.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMCrossbar</strong>](/windows/win32/Strmif/nn-strmif-iamcrossbar?branch=master)</td>
<td>Routes signals from an analog or digital source to a video capture filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMDecoderCaps</strong>](/windows/win32/Strmif/nn-strmif-iamdecodercaps?branch=master)</td>
<td>Returns capabilities information from an MPEG decoder filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMDeviceRemoval</strong>](/windows/win32/Strmif/nn-strmif-iamdeviceremoval?branch=master)</td>
<td>Provides a way for the Filter Graph Manager to register for device removal events for a capture device.</td>
</tr>
<tr class="even">
<td>[<strong>IAMDirectSound</strong>](/windows/win32/Amaudio/nn-amaudio-iamdirectsound?branch=master)</td>
<td>Specifies which window has focus for controlling DirectSound audio playback.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMDroppedFrames</strong>](/windows/win32/Strmif/nn-strmif-iamdroppedframes?branch=master)</td>
<td>Retrieves performance information from a video capture filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMExtDevice</strong>](/windows/win32/Strmif/nn-strmif-iamextdevice?branch=master)</td>
<td>Controls an external device, such as a DV camera or video tape recoder (VTR).</td>
</tr>
<tr class="odd">
<td>[<strong>IAMExtTransport</strong>](/windows/win32/Strmif/nn-strmif-iamexttransport?branch=master)</td>
<td>Controls the transport on a VTR or camcorder.</td>
</tr>
<tr class="even">
<td>[<strong>IAMExtendedSeeking</strong>](/windows/win32/Qnetwork/nn-qnetwork-iamextendedseeking?branch=master)</td>
<td>Seeks to a marker in a Windows Media stream or changes the playback rate for a Windows Media file.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMFilterGraphCallback</strong>](/windows/win32/Strmif/nn-strmif-iamfiltergraphcallback?branch=master)</td>
<td>Callback interface for graph building.</td>
</tr>
<tr class="even">
<td>[<strong>IAMFilterMiscFlags</strong>](/windows/win32/Strmif/nn-strmif-iamfiltermiscflags?branch=master)</td>
<td>Queries whether a filter is a source filter or a renderer.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMGraphBuilderCallback</strong>](/windows/win32/Strmif/nn-strmif-iamgraphbuildercallback?branch=master)</td>
<td>Callback interface for graph building.</td>
</tr>
<tr class="even">
<td>[<strong>IAMGraphStreams</strong>](/windows/win32/Strmif/nn-strmif-iamgraphstreams?branch=master)</td>
<td>Controls a filter graph that renders a live source.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMLatency</strong>](/windows/win32/Strmif/nn-strmif-iamlatency?branch=master)</td>
<td>Reports the amount of latency that a filter introduces into the graph.</td>
</tr>
<tr class="even">
<td>[<strong>IAMLine21Decoder</strong>](/windows/win32/il21dec/nn-il21dec-iamline21decoder?branch=master)</td>
<td>Sets and retrieves information about closed captions.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMMediaContent</strong>](/windows/win32/Qnetwork/nn-qnetwork-iammediacontent?branch=master)</td>
<td>Retrieves metadata from a stream.</td>
</tr>
<tr class="even">
<td>[<strong>IAMNetShowConfig</strong>](/windows/win32/Qnetwork/nn-qnetwork-iamnetshowconfig?branch=master)</td>
<td>Configures the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMNetShowExProps</strong>](/windows/win32/Qnetwork/nn-qnetwork-iamnetshowexprops?branch=master)</td>
<td>Configures the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMNetShowPreroll</strong>](/windows/win32/Qnetwork/nn-qnetwork-iamnetshowpreroll?branch=master)</td>
<td>Sets and retrieves the preroll settings for the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMNetworkStatus</strong>](/windows/win32/Qnetwork/nn-qnetwork-iamnetworkstatus?branch=master)</td>
<td>Reports the quality of the network connection for the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMOpenProgress</strong>](/windows/win32/Strmif/nn-strmif-iamopenprogress?branch=master)</td>
<td>Reports the progress of a file-open operation.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMOverlayFX</strong>](/windows/win32/Strmif/nn-strmif-iamoverlayfx?branch=master)</td>
<td>Controls how the video overlay appears on the user's screen.</td>
</tr>
<tr class="even">
<td>[<strong>IAMParse</strong>](/windows/win32/Amparse/nn-amparse-iamparse?branch=master)</td>
<td>Sets and retrieves the parse time for an MPEG-2 stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMPushSource</strong>](/windows/win32/Strmif/nn-strmif-iampushsource?branch=master)</td>
<td>Synchronizes a filter graph that renders a live source.</td>
</tr>
<tr class="even">
<td>[<strong>IAMResourceControl</strong>](/windows/win32/Strmif/nn-strmif-iamresourcecontrol?branch=master)</td>
<td>Opens and holds an audio device resource.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMStats</strong>](/windows/win32/Control/nn-control-iamstats?branch=master)</td>
<td>Retrieves performance data from the Filter Graph Manager.</td>
</tr>
<tr class="even">
<td>[<strong>IAMStreamConfig</strong>](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master)</td>
<td>Sets the output format on certain capture and compression filters.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMStreamControl</strong>](/windows/win32/Strmif/nn-strmif-iamstreamcontrol?branch=master)</td>
<td>Controls individual streams on a filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMStreamSelect</strong>](/windows/win32/Strmif/nn-strmif-iamstreamselect?branch=master)</td>
<td>selects from the available streams on a parser filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMTimecodeReader</strong>](/windows/win32/Strmif/nn-strmif-iamtimecodereader?branch=master)</td>
<td>Reads SMPTE or MIDI timecode from an external device.</td>
</tr>
<tr class="even">
<td>[<strong>IAMTuner</strong>](/windows/win32/Strmif/nn-strmif-iamtuner?branch=master)</td>
<td>Controls a TV tuner.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMTVAudio</strong>](/windows/win32/Strmif/nn-strmif-iamtvaudio?branch=master)</td>
<td>Controls audio from a television source.</td>
</tr>
<tr class="even">
<td>[<strong>IAMTVTuner</strong>](/windows/win32/Strmif/nn-strmif-iamtvtuner?branch=master)</td>
<td>Controls a TV tuner.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVfwCaptureDialogs</strong>](/windows/win32/Strmif/nn-strmif-iamvfwcapturedialogs?branch=master)</td>
<td>Displays a dialog box provided by a Video for Windows (VFW) capture driver.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVfwCompressDialogs</strong>](/windows/win32/Strmif/nn-strmif-iamvfwcompressdialogs?branch=master)</td>
<td>Displays a dialog box provided by a Video for Windows (VFW) codec.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoAccelerator</strong>](/windows/win32/videoacc/nn-videoacc-iamvideoaccelerator?branch=master)</td>
<td>Enables a video decoder filter to access DirectX Video Acceleration (DXVA) 1.0 functionality.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVideoAcceleratorNotify</strong>](/windows/win32/videoacc/nn-videoacc-iamvideoacceleratornotify?branch=master)</td>
<td>Callback interface for DXVA 1.0.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoCompression</strong>](/windows/win32/Strmif/nn-strmif-iamvideocompression?branch=master)</td>
<td>Sets and retrieves video compression properties.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVideoControl</strong>](/windows/win32/Strmif/nn-strmif-iamvideocontrol?branch=master)</td>
<td>Controls certain video capture operations such as enumerating available frame rates and image orientation.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoDecimationProperties</strong>](/windows/win32/Strmif/nn-strmif-iamvideodecimationproperties?branch=master)</td>
<td>Controls how the Overlay Mixer performs video decimation.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVideoProcAmp</strong>](/windows/win32/Strmif/nn-strmif-iamvideoprocamp?branch=master)</td>
<td>Adjusts the qualities of an incoming video signal.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMWMBufferPass</strong>](/windows/win32/Dshowasf/nn-dshowasf-iamwmbufferpass?branch=master)</td>
<td>Gets or sets properties on individual samples in an ASF stream.</td>
</tr>
<tr class="even">
<td>[<strong>IAMWMBufferPassCallback</strong>](/windows/win32/Dshowasf/nn-dshowasf-iamwmbufferpasscallback?branch=master)</td>
<td>Callback interface used with the [<strong>IAMWMBufferPass</strong>](/windows/win32/Dshowasf/nn-dshowasf-iamwmbufferpass?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMWstDecoder</strong>](/windows/win32/Iwstdec/nn-iwstdec-iamwstdecoder?branch=master)</td>
<td>Sets and retrieves information about World Standard Teletext (WST)</td>
</tr>
<tr class="even">
<td>[<strong>IAsyncReader</strong>](/windows/win32/Strmif/nn-strmif-iasyncreader?branch=master)</td>
<td>Performs an asynchronous data request on a filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)</td>
<td>Exposed by filters. This is the primary interface for all DirectShow filters.</td>
</tr>
<tr class="even">
<td>[<strong>IBasicAudio</strong>](/windows/win32/Control/nn-control-ibasicaudio?branch=master)</td>
<td>Controls the volume and balance of the audio stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IBasicVideo</strong>](/windows/win32/Control/nn-control-ibasicvideo?branch=master)</td>
<td>Sets video properties such as the destination and source rectangles.</td>
</tr>
<tr class="even">
<td>[<strong>IBasicVideo2</strong>](/windows/win32/Control/nn-control-ibasicvideo2?branch=master)</td>
<td>Extends the [<strong>IBasicVideo</strong>](/windows/win32/Control/nn-control-ibasicvideo?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>ICameraControl</strong>](/windows/win32/Vidcap/nn-vidcap-icameracontrol?branch=master)</td>
<td>Controls the camera settings on a capture device.</td>
</tr>
<tr class="even">
<td>[<strong>ICaptureGraphBuilder2</strong>](/windows/win32/Strmif/nn-strmif-icapturegraphbuilder2?branch=master)</td>
<td>Builds capture graphs and other custom filter graphs.</td>
</tr>
<tr class="odd">
<td>[<strong>ICodecAPI</strong>](/windows/win32/Strmif/nn-strmif-icodecapi?branch=master)</td>
<td>Configures an encoder or decoder.</td>
</tr>
<tr class="even">
<td>[<strong>IConfigAsfWriter</strong>](/windows/win32/Dshowasf/nn-dshowasf-iconfigasfwriter?branch=master)</td>
<td>Configures the [WM ASF Writer](wm-asf-writer-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IConfigAsfWriter2</strong>](/windows/win32/Dshowasf/nn-dshowasf-iconfigasfwriter2?branch=master)</td>
<td>Extends the [<strong>IConfigAsfWriter</strong>](/windows/win32/Dshowasf/nn-dshowasf-iconfigasfwriter?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IConfigAviMux</strong>](/windows/win32/Strmif/nn-strmif-iconfigavimux?branch=master)</td>
<td>Configures the [AVI Mux](avi-mux-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IConfigInterleaving</strong>](/windows/win32/Strmif/nn-strmif-iconfiginterleaving?branch=master)</td>
<td>Controls how the AVI Mux interleaves audio and video samples.</td>
</tr>
<tr class="even">
<td>[<strong>ICreateDevEnum</strong>](/windows/win32/Strmif/nn-strmif-icreatedevenum?branch=master)</td>
<td>Creates an enumerator for a category of filters.</td>
</tr>
<tr class="odd">
<td>[<strong>IDDrawExclModeVideo</strong>](/windows/win32/Strmif/nn-strmif-iddrawexclmodevideo?branch=master)</td>
<td>Enables video playback in DirectDraw exclusive full-screen mode.</td>
</tr>
<tr class="even">
<td>[<strong>IDDrawExclModeVideoCallback</strong>](/windows/win32/Strmif/nn-strmif-iddrawexclmodevideocallback?branch=master)</td>
<td>Callback interface for the [<strong>IDDrawExclModeVideoCallback</strong>](/windows/win32/Strmif/nn-strmif-iddrawexclmodevideocallback?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IDecimateVideoImage</strong>](/windows/win32/Strmif/nn-strmif-idecimatevideoimage?branch=master)</td>
<td>Specifies decimation on a decoder filter.</td>
</tr>
<tr class="even">
<td>[<strong>IDeferredCommand</strong>](/windows/win32/Control/nn-control-ideferredcommand?branch=master)</td>
<td>Cancels or modifies graph-control commands that were queued using the [<strong>IQueueCommand</strong>](/windows/win32/Control/nn-control-iqueuecommand?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawVideo</strong>](/windows/win32/Amvideo/nn-amvideo-idirectdrawvideo?branch=master)</td>
<td>Queries the [Video Renderer](video-renderer-filter.md) filter about DirectDraw surfaces and hardware capabilities.</td>
</tr>
<tr class="even">
<td>[<strong>IDirectDrawMediaSample</strong>](/windows/win32/Amstream/nn-amstream-idirectdrawmediasample?branch=master)</td>
<td>Provides access to DirectDraw surfaces allocated by the [Overlay Mixer](overlay-mixer-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawMediaSampleAllocator</strong>](/windows/win32/Amstream/nn-amstream-idirectdrawmediasampleallocator?branch=master)</td>
<td>Allocates samples that contain DirectDraw surfaces.</td>
</tr>
<tr class="even">
<td>[<strong>IDistributorNotify</strong>](/windows/win32/Strmif/nn-strmif-idistributornotify?branch=master)</td>
<td>Enables a plug-in distributor to be notified when the filter graph changes.</td>
</tr>
<tr class="odd">
<td>[<strong>IDMOWrapperFilter</strong>](/windows/win32/Dmodshow/nn-dmodshow-idmowrapperfilter?branch=master)</td>
<td>Enables an application to use a DirectX Media Object (DMO) inside a filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IDShowPlugin</strong>](/windows/win32/Qnetwork/nn-qnetwork-idshowplugin?branch=master)</td>
<td>Enables the Windows Media Source filter to communicate with the Windows Media Player 6.4 Plug-in for Netscape Navigator.</td>
</tr>
<tr class="odd">
<td>[<strong>IDvdCmd</strong>](/windows/win32/Strmif/nn-strmif-idvdcmd?branch=master)</td>
<td>Waits for DVD commands to start or end.</td>
</tr>
<tr class="even">
<td>[<strong>IDvdControl2</strong>](/windows/win32/Strmif/nn-strmif-idvdcontrol2?branch=master)</td>
<td>Navigates and plays DVD-Video titles.</td>
</tr>
<tr class="odd">
<td>[<strong>IDvdGraphBuilder</strong>](/windows/win32/Strmif/nn-strmif-idvdgraphbuilder?branch=master)</td>
<td>Builds a filter graph for DVD-Video playback.</td>
</tr>
<tr class="even">
<td>[<strong>IDvdInfo2</strong>](/windows/win32/Strmif/nn-strmif-idvdinfo2?branch=master)</td>
<td>Reports attributes of a DVD disc or the current state of the DVD Navigator filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IDvdState</strong>](/windows/win32/Strmif/nn-strmif-idvdstate?branch=master)</td>
<td>Saves the current DVD playback location and state.</td>
</tr>
<tr class="even">
<td>[<strong>IDVEnc</strong>](/windows/win32/Strmif/nn-strmif-idvenc?branch=master)</td>
<td>Sets and retrieves properties on the [DV Video Encoder](dv-video-encoder-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IDVRGB219</strong>](/windows/win32/Strmif/nn-strmif-idvrgb219?branch=master)</td>
<td>Controls the dynamic range in the DV Video Encoder and [DV Video Decoder](dv-video-decoder-filter.md) filters.</td>
</tr>
<tr class="even">
<td>[<strong>IDVSplitter</strong>](/windows/win32/Strmif/nn-strmif-idvsplitter?branch=master)</td>
<td>Downgrades the frame rate on a digital video (DV) stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IEnumFilters</strong>](/windows/win32/Strmif/nn-strmif-ienumfilters?branch=master)</td>
<td>Enumerates the filters in a filter graph</td>
</tr>
<tr class="even">
<td>[<strong>IEnumMediaTypes</strong>](/windows/win32/Strmif/nn-strmif-ienummediatypes?branch=master)</td>
<td>Enumerates a pin's preferred media types</td>
</tr>
<tr class="odd">
<td>[<strong>IEnumPIDMap</strong>](/windows/win32/Bdaiface/nn-bdaiface-ienumpidmap?branch=master)</td>
<td>Enumerates the mappings of Packet IDs (PID) to output pins on the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) filter.</td>
</tr>
<tr class="even">
<td>[<strong>IEnumPins</strong>](/windows/win32/Strmif/nn-strmif-ienumpins?branch=master)</td>
<td>Enumerates pins on a filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IEnumStreamIdMap</strong>](/windows/win32/Strmif/nn-strmif-ienumstreamidmap?branch=master)</td>
<td>Enumerates the mappings of stream IDs to output pins on the MPEG-2 Demultiplexer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IFileSinkFilter</strong>](/windows/win32/Strmif/nn-strmif-ifilesinkfilter?branch=master)</td>
<td>Exposed by filters that write data to a file.</td>
</tr>
<tr class="odd">
<td>[<strong>IFileSinkFilter2</strong>](/windows/win32/Strmif/nn-strmif-ifilesinkfilter2?branch=master)</td>
<td>Extends the [<strong>IFileSinkFilter</strong>](/windows/win32/Strmif/nn-strmif-ifilesinkfilter?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IFileSourceFilter</strong>](/windows/win32/Strmif/nn-strmif-ifilesourcefilter?branch=master)</td>
<td>Exposed by source filters.</td>
</tr>
<tr class="odd">
<td>[<strong>IFilterChain</strong>](/windows/win32/Strmif/nn-strmif-ifilterchain?branch=master)</td>
<td>Starting, stops, or removes chains of filters in a filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IFilterGraph</strong>](/windows/win32/Strmif/nn-strmif-ifiltergraph?branch=master)</td>
<td>Builds a filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IFilterGraph2</strong>](/windows/win32/Strmif/nn-strmif-ifiltergraph2?branch=master)</td>
<td>Extends the [<strong>IGraphBuilder</strong>](/windows/win32/Strmif/nn-strmif-igraphbuilder?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IFilterGraph3</strong>](/windows/win32/Strmif/nn-strmif-ifiltergraph3?branch=master)</td>
<td>Extends the [<strong>IFilterGraph2</strong>](/windows/win32/Strmif/nn-strmif-ifiltergraph2?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IFilterMapper2</strong>](/windows/win32/Strmif/nn-strmif-ifiltermapper2?branch=master)</td>
<td>Registers and unregisters filters, and locates filters in the registry.</td>
</tr>
<tr class="even">
<td>[<strong>IFilterMapper3</strong>](/windows/win32/Strmif/nn-strmif-ifiltermapper3?branch=master)</td>
<td>Extends the [<strong>IFilterMapper2</strong>](/windows/win32/Strmif/nn-strmif-ifiltermapper2?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IFullScreenVideoEx</strong>](/windows/win32/Amvideo/nn-amvideo-ifullscreenvideoex?branch=master)</td>
<td>Exposed by the [Full Screen Renderer](full-screen-renderer-filter.md) filter.</td>
</tr>
<tr class="even">
<td>[<strong>IGetCapabilitiesKey</strong>](/windows/win32/Strmif/nn-strmif-igetcapabilitieskey?branch=master)</td>
<td>Retrieves the capabilities of a software or hardware encoder from the registry.</td>
</tr>
<tr class="odd">
<td>[<strong>IGraphBuilder</strong>](/windows/win32/Strmif/nn-strmif-igraphbuilder?branch=master)</td>
<td>Extends the [<strong>IFilterGraph</strong>](/windows/win32/Strmif/nn-strmif-ifiltergraph?branch=master) interface. This is the primary interface of the Filter Graph Manager.</td>
</tr>
<tr class="even">
<td>[<strong>IGraphConfig</strong>](/windows/win32/Strmif/nn-strmif-igraphconfig?branch=master)</td>
<td>Reconfigures the filter graph while the graph is running.</td>
</tr>
<tr class="odd">
<td>[<strong>IGraphConfigCallback</strong>](/windows/win32/Strmif/nn-strmif-igraphconfigcallback?branch=master)</td>
<td>Callback interface for the [<strong>IGraphConfig</strong>](/windows/win32/Strmif/nn-strmif-igraphconfig?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IGraphVersion</strong>](/windows/win32/Strmif/nn-strmif-igraphversion?branch=master)</td>
<td>Retrieves the current version number of the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IIPDVDec</strong>](/windows/win32/Strmif/nn-strmif-iipdvdec?branch=master)</td>
<td>Configures the [DV Video Decoder](dv-video-decoder-filter.md) filter.</td>
</tr>
<tr class="even">
<td>[<strong>IKsNodeControl</strong>](/windows/win32/Vidcap/nn-vidcap-iksnodecontrol?branch=master)</td>
<td>Exposed by USB Video Class (UVC) extension units.</td>
</tr>
<tr class="odd">
<td>[<strong>IKsPin</strong>](ikspin.md)</td>
<td>Retrieves the mediums supported by a kernel-mode pin.</td>
</tr>
<tr class="even">
<td>[<strong>IKsPropertySet</strong>](ikspropertyset.md)</td>
<td>Sets properties on a kernel-mode filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IKsTopologyInfo</strong>](/windows/win32/Vidcap/nn-vidcap-ikstopologyinfo?branch=master)</td>
<td>Enumerates the nodes in a stream class driver.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaControl</strong>](/windows/win32/Control/nn-control-imediacontrol?branch=master)</td>
<td>Controls the flow of data through the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaEvent</strong>](/windows/win32/Control/nn-control-imediaevent?branch=master)</td>
<td>Retrieves event notifications from the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaEventEx</strong>](/windows/win32/Control/nn-control-imediaeventex?branch=master)</td>
<td>Extends the [<strong>IMediaEvent</strong>](/windows/win32/Control/nn-control-imediaevent?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaEventSink</strong>](/windows/win32/Strmif/nn-strmif-imediaeventsink?branch=master)</td>
<td>Notifies the Filter Graph Manager of events that occur within the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaFilter</strong>](/windows/win32/Strmif/nn-strmif-imediafilter?branch=master)</td>
<td>Controls the streaming state of a filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master)</td>
<td>Controls seeking in the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaPropertyBag</strong>](/windows/win32/Strmif/nn-strmif-imediapropertybag?branch=master)</td>
<td>Sets and retrieves INFO and DISP chunks in Audio-Video Interleaved (AVI) files.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaSample</strong>](/windows/win32/Strmif/nn-strmif-imediasample?branch=master)</td>
<td>Sets and retrieves properties on media samples.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaSample2</strong>](/windows/win32/Strmif/nn-strmif-imediasample2?branch=master)</td>
<td>Extends the [<strong>IMediaSample</strong>](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaSample2Config</strong>](/windows/win32/Strmif/nn-strmif-imediasample2config?branch=master)</td>
<td>Returns a pointer to a Direct3D surface representing a VRAM capture buffer.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master)</td>
<td>Controls seeking in the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IMemAllocator</strong>](/windows/win32/Strmif/nn-strmif-imemallocator?branch=master)</td>
<td>Allocates media samples.</td>
</tr>
<tr class="even">
<td>[<strong>IMemAllocatorCallbackTemp</strong>](/windows/win32/Strmif/nn-strmif-imemallocatorcallbacktemp?branch=master)</td>
<td>Enables a filter to receive a callback notification from an allocator.
<blockquote>
[!Note]<br />
Deprecated.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMemAllocatorNotifyCallbackTemp</strong>](/windows/win32/Strmif/nn-strmif-imemallocatornotifycallbacktemp?branch=master)</td>
<td>Callback interface for the [<strong>IMemAllocatorCallbackTemp</strong>](/windows/win32/Strmif/nn-strmif-imemallocatorcallbacktemp?branch=master) interface.
<blockquote>
[!Note]<br />
Deprecated.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master)</td>
<td>Delivers media data to an input pin.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerOCX</strong>](/windows/win32/Mixerocx/nn-mixerocx-imixerocx?branch=master)</td>
<td>Exposed by the Overlay Mixer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerOCXNotify</strong>](/windows/win32/Mixerocx/nn-mixerocx-imixerocxnotify?branch=master)</td>
<td>Callback interface for the [<strong>IMixerOCX</strong>](/windows/win32/Mixerocx/nn-mixerocx-imixerocx?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerPinConfig</strong>](/windows/win32/Mpconfig/nn-mpconfig-imixerpinconfig?branch=master)</td>
<td>Manipulates video streams on the Overlay Mixer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerPinConfig2</strong>](/windows/win32/Mpconfig/nn-mpconfig-imixerpinconfig2?branch=master)</td>
<td>Extends the [<strong>IMixerPinConfig</strong>](/windows/win32/Mpconfig/nn-mpconfig-imixerpinconfig?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMpeg2Demultiplexer</strong>](/windows/win32/Strmif/nn-strmif-impeg2demultiplexer?branch=master)</td>
<td>Configures the MPEG-2 Demultiplexer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IMPEG2PIDMap</strong>](/windows/win32/Bdaiface/nn-bdaiface-impeg2pidmap?branch=master)</td>
<td>Associates an output pin on the MPEG-2 Demultiplexer filter with one or more packet IDs (PIDs).</td>
</tr>
<tr class="odd">
<td>[<strong>IMPEG2StreamIdMap</strong>](/windows/win32/Strmif/nn-strmif-impeg2streamidmap?branch=master)</td>
<td>Associates an output pin on the MPEG-2 Demultiplexer filter with one or more stream IDs.</td>
</tr>
<tr class="even">
<td>[<strong>IMpegAudioDecoder</strong>](/windows/win32/mpegtype/nn-mpegtype-impegaudiodecoder?branch=master)</td>
<td>Configures the MPEG-1 Audio Decoder.</td>
</tr>
<tr class="odd">
<td>[<strong>IOverlay</strong>](/windows/win32/Strmif/nn-strmif-ioverlay?branch=master)</td>
<td>Enables a filter to write directly to video memory.</td>
</tr>
<tr class="even">
<td>[<strong>IOverlayNotify</strong>](/windows/win32/Strmif/nn-strmif-ioverlaynotify?branch=master)</td>
<td>Callback interface for the [<strong>IOverlay</strong>](/windows/win32/Strmif/nn-strmif-ioverlay?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IOverlayNotify2</strong>](/windows/win32/Strmif/nn-strmif-ioverlaynotify2?branch=master)</td>
<td>Callback interface for the [<strong>IOverlay</strong>](/windows/win32/Strmif/nn-strmif-ioverlay?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IPersistMediaPropertyBag</strong>](/windows/win32/Strmif/nn-strmif-ipersistmediapropertybag?branch=master)</td>
<td>Sets and retrieves INFO and DISP chunks in Audio-Video Interleaved (AVI) streams.</td>
</tr>
<tr class="odd">
<td>[<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master)</td>
<td>Exposed by all filter pins.</td>
</tr>
<tr class="even">
<td>[<strong>IPinConnection</strong>](/windows/win32/Strmif/nn-strmif-ipinconnection?branch=master)</td>
<td>Reconnects an input pin while the filter is still running.</td>
</tr>
<tr class="odd">
<td>[<strong>IPinFlowControl</strong>](/windows/win32/Strmif/nn-strmif-ipinflowcontrol?branch=master)</td>
<td>Blocks data flow from an active output pin.</td>
</tr>
<tr class="even">
<td>[<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)</td>
<td>Provides support for quality control in the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IQualProp</strong>](/windows/win32/Amvideo/nn-amvideo-iqualprop?branch=master)</td>
<td>Retrieves performance information from video renderers.</td>
</tr>
<tr class="even">
<td>[<strong>IQueueCommand</strong>](/windows/win32/Control/nn-control-iqueuecommand?branch=master)</td>
<td>Queues a command on the filter graph for processing at a designated time.</td>
</tr>
<tr class="odd">
<td>[<strong>IReferenceClock</strong>](/windows/win32/Strmif/nn-strmif-ireferenceclock?branch=master)</td>
<td>Provides the reference time for the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IReferenceClockTimerControl</strong>](/windows/win32/Strmif/nn-strmif-ireferenceclocktimercontrol?branch=master)</td>
<td>Changes the timer period used by a reference clock.</td>
</tr>
<tr class="odd">
<td>[<strong>IRegisterServiceProvider</strong>](/windows/win32/Strmif/nn-strmif-iregisterserviceprovider?branch=master)</td>
<td>Registers an object as a service with the Filter Graph Manager.</td>
</tr>
<tr class="even">
<td>[<strong>IResourceConsumer</strong>](/windows/win32/Strmif/nn-strmif-iresourceconsumer?branch=master)</td>
<td>Callback interface for the [<strong>IResourceManager</strong>](/windows/win32/Strmif/nn-strmif-iresourcemanager?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IResourceManager</strong>](/windows/win32/Strmif/nn-strmif-iresourcemanager?branch=master)</td>
<td>Resolves contentions for system resources.</td>
</tr>
<tr class="even">
<td>[<strong>ISeekingPassThru</strong>](/windows/win32/Strmif/nn-strmif-iseekingpassthru?branch=master)</td>
<td>Implements seeking for one-input filters.</td>
</tr>
<tr class="odd">
<td>[<strong>ISelector</strong>](/windows/win32/Vidcap/nn-vidcap-iselector?branch=master)</td>
<td>Selects source nodes in a stream class driver.</td>
</tr>
<tr class="even">
<td>[<strong>IStreamBuilder</strong>](/windows/win32/Strmif/nn-strmif-istreambuilder?branch=master)</td>
<td>Enables an output pin to build the downstream section of the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoFrameStep</strong>](/windows/win32/Strmif/nn-strmif-ivideoframestep?branch=master)</td>
<td>Steps through a video stream.</td>
</tr>
<tr class="even">
<td>[<strong>IVideoProcAmp</strong>](/windows/win32/Vidcap/nn-vidcap-ivideoprocamp?branch=master)</td>
<td>Controls the image adjustment (ProcAmp) settings on a capture device.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoWindow</strong>](/windows/win32/Control/nn-control-ivideowindow?branch=master)</td>
<td>Sets properties on the video window.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRAspectRatioControl</strong>](/windows/win32/Strmif/nn-strmif-ivmraspectratiocontrol?branch=master)</td>
<td>controls whether the [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7) preserves the aspect ratio of the source video.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRAspectRatioControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmraspectratiocontrol9?branch=master)</td>
<td>Controls whether the [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9) preserves the aspect ratio of the source video</td>
</tr>
<tr class="even">
<td>[<strong>IVMRDeinterlaceControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrdeinterlacecontrol?branch=master)</td>
<td>Supports hardware-accelerated deinterlacing using the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRDeinterlaceControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9?branch=master)</td>
<td>Supports hardware-accelerated deinterlacing using the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRFilterConfig</strong>](/windows/win32/Strmif/nn-strmif-ivmrfilterconfig?branch=master)</td>
<td>Configures the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRFilterConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrfilterconfig9?branch=master)</td>
<td>Configures the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImageCompositor</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagecompositor?branch=master)</td>
<td>Exposed by VMR-7 compositors.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRImageCompositor9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrimagecompositor9?branch=master)</td>
<td>Exposed by VMR-9 compositors.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImagePresenter</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagepresenter?branch=master)</td>
<td>Exposed by VMR-7 allocator-presenters.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRImagePresenter9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenter9?branch=master)</td>
<td>Exposed by VMR-9 allocator-presenters.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImagePresenterConfig</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagepresenterconfig?branch=master)</td>
<td>Sets the renderering preferences on the image presenter used by the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRImagePresenterConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenterconfig9?branch=master)</td>
<td>Sets the renderering preferences on the image presenter used by the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImagePresenterExclModeConfig</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagepresenterexclmodeconfig?branch=master)</td>
<td>Setting and retrieves the renderering preferences on the Exclusive Mode Allocator-Presenter for the VMR-7</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRMixerBitmap</strong>](/windows/win32/Strmif/nn-strmif-ivmrmixerbitmap?branch=master)</td>
<td>Blends a static image onto the video stream, when using the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRMixerBitmap9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmixerbitmap9?branch=master)</td>
<td>Blends a static image onto the video stream, when using the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRMixerControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrmixercontrol?branch=master)</td>
<td>Manipulates the incoming video streams on the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRMixerControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmixercontrol9?branch=master)</td>
<td>Manipulates the incoming video streams on the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRMonitorConfig</strong>](/windows/win32/Strmif/nn-strmif-ivmrmonitorconfig?branch=master)</td>
<td>Controls monitor usage by the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRMonitorConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmonitorconfig9?branch=master)</td>
<td>Controls monitor usage by the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurface</strong>](/windows/win32/Strmif/nn-strmif-ivmrsurface?branch=master)</td>
<td>Exposed by media samples from the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRSurface9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurface9?branch=master)</td>
<td>Exposed by media samples from the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurfaceAllocator</strong>](/windows/win32/Strmif/nn-strmif-ivmrsurfaceallocator?branch=master)</td>
<td>Allocates the DirectDraw surfaces used by the VMR-7 allocator-presenter.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRSurfaceAllocator9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocator9?branch=master)</td>
<td>Allocates the Direct3D surfaces used by the VMR-9 allocator-presenter.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurfaceAllocatorEx9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatorex9?branch=master)</td>
<td>Extends the [<strong>IVMRSurfaceAllocator9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocator9?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRSurfaceAllocatorNotify</strong>](/windows/win32/Strmif/nn-strmif-ivmrsurfaceallocatornotify?branch=master)</td>
<td>Enables the allocator-presenter to notify the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurfaceAllocatorNotify9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9?branch=master)</td>
<td>Enables the allocator-presenter to notify the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRVideoStreamControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrvideostreamcontrol?branch=master)</td>
<td>Controls input pins on the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRVideoStreamControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrvideostreamcontrol9?branch=master)</td>
<td>Controls input pins on the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRWindowlessControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrwindowlesscontrol?branch=master)</td>
<td>Controls how the VMR-7 renders a video stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRWindowlessControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrwindowlesscontrol9?branch=master)</td>
<td>Controls how the VMR-9 renders a video stream.</td>
</tr>
<tr class="even">
<td>[<strong>IVPBaseConfig</strong>](/windows/win32/Vpconfig/nn-vpconfig-ivpbaseconfig?branch=master)</td>
<td>Base interface for the [<strong>IVPConfig</strong>](/windows/win32/Vpconfig/nn-vpconfig-ivpconfig?branch=master) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IVPBaseNotify</strong>](/windows/win32/Vpnotify/nn-vpnotify-ivpbasenotify?branch=master)</td>
<td>Base interface for the [<strong>IVPNotify</strong>](/windows/win32/Vpnotify/nn-vpnotify-ivpnotify?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IVPConfig</strong>](/windows/win32/Vpconfig/nn-vpconfig-ivpconfig?branch=master)</td>
<td>Enables a video port to communicate with the Overlay Mixer filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IVPManager</strong>](/windows/win32/Strmif/nn-strmif-ivpmanager?branch=master)</td>
<td>Exposed by the Video Port Manager filter.</td>
</tr>
<tr class="even">
<td>[<strong>IVPNotify</strong>](/windows/win32/Vpnotify/nn-vpnotify-ivpnotify?branch=master)</td>
<td>Enables the Overlay Mixer to control the properties of a hardware device that uses a video port.</td>
</tr>
<tr class="odd">
<td>[<strong>IVPNotify2</strong>](/windows/win32/Vpnotify/nn-vpnotify-ivpnotify2?branch=master)</td>
<td>Extends the [<strong>IVPNotify</strong>](/windows/win32/Vpnotify/nn-vpnotify-ivpnotify?branch=master) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IXMLGraphBuilder</strong>](/windows/win32/amxmlgraphbuilder/nn-amxmlgraphbuilder-ixmlgraphbuilder?branch=master)</td>
<td>Persists a DirectShow filter graph using an XML file format.
<blockquote>
[!Note]<br />
Deprecated.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




