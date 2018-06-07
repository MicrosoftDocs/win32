---
Description: Alphabetical List of DirectShow Interfaces
ms.assetid: 9c7f56f4-92af-40c6-8124-f2715ac3f6d7
title: Alphabetical List of DirectShow Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>IAMAnalogVideoDecoder</strong>](/windows/desktop/api/Strmif/nn-strmif-iamanalogvideodecoder)</td>
<td>Sets and retrieves information about the analog-to-digital conversion process in a video capture filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMAudioInputMixer</strong>](/windows/desktop/api/Strmif/nn-strmif-iamaudioinputmixer)</td>
<td>Controls audio capture properties.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMAudioRendererStats</strong>](/windows/desktop/api/Strmif/nn-strmif-iamaudiorendererstats)</td>
<td>Retrieves statistical performance information from an audio renderer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMBufferNegotiation</strong>](/windows/desktop/api/Strmif/nn-strmif-iambuffernegotiation)</td>
<td>Requests the number of buffers for a filter to create and size of each buffer.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMCameraControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iamcameracontrol)</td>
<td>Controls camera settings such as zoom, pan, aperture adjustment, or shutter speed.</td>
</tr>
<tr class="even">
<td>[<strong>IAMCertifiedOutputProtection</strong>](/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection)</td>
<td>Sends Certified Output Protection Protocol (COPP) messages to the graphics driver.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMChannelInfo</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iamchannelinfo)</td>
<td>Gets and sets channel information for Windows Media Station (.nsc) files.</td>
</tr>
<tr class="even">
<td>[<strong>IAMClockAdjust</strong>](/windows/desktop/api/Strmif/nn-strmif-iamclockadjust)</td>
<td>Adjusts the reference clock.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMClockSlave</strong>](/windows/desktop/api/Strmif/nn-strmif-iamclockslave)</td>
<td>Controls the tolerance of an audio renderer when it is matching rates with another clock.</td>
</tr>
<tr class="even">
<td>[<strong>IAMCopyCaptureFileProgress</strong>](/windows/desktop/api/Strmif/nn-strmif-iamcopycapturefileprogress)</td>
<td>Callback interface for the [<strong>ICaptureGraphBuilder2::CopyCaptureFile</strong>](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-copycapturefile) method.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMCrossbar</strong>](/windows/desktop/api/Strmif/nn-strmif-iamcrossbar)</td>
<td>Routes signals from an analog or digital source to a video capture filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMDecoderCaps</strong>](/windows/desktop/api/Strmif/nn-strmif-iamdecodercaps)</td>
<td>Returns capabilities information from an MPEG decoder filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMDeviceRemoval</strong>](/windows/desktop/api/Strmif/nn-strmif-iamdeviceremoval)</td>
<td>Provides a way for the Filter Graph Manager to register for device removal events for a capture device.</td>
</tr>
<tr class="even">
<td>[<strong>IAMDirectSound</strong>](/windows/desktop/api/Amaudio/nn-amaudio-iamdirectsound)</td>
<td>Specifies which window has focus for controlling DirectSound audio playback.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMDroppedFrames</strong>](/windows/desktop/api/Strmif/nn-strmif-iamdroppedframes)</td>
<td>Retrieves performance information from a video capture filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMExtDevice</strong>](/windows/desktop/api/Strmif/nn-strmif-iamextdevice)</td>
<td>Controls an external device, such as a DV camera or video tape recoder (VTR).</td>
</tr>
<tr class="odd">
<td>[<strong>IAMExtTransport</strong>](/windows/desktop/api/Strmif/nn-strmif-iamexttransport)</td>
<td>Controls the transport on a VTR or camcorder.</td>
</tr>
<tr class="even">
<td>[<strong>IAMExtendedSeeking</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iamextendedseeking)</td>
<td>Seeks to a marker in a Windows Media stream or changes the playback rate for a Windows Media file.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMFilterGraphCallback</strong>](/windows/desktop/api/Strmif/nn-strmif-iamfiltergraphcallback)</td>
<td>Callback interface for graph building.</td>
</tr>
<tr class="even">
<td>[<strong>IAMFilterMiscFlags</strong>](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags)</td>
<td>Queries whether a filter is a source filter or a renderer.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMGraphBuilderCallback</strong>](/windows/desktop/api/Strmif/nn-strmif-iamgraphbuildercallback)</td>
<td>Callback interface for graph building.</td>
</tr>
<tr class="even">
<td>[<strong>IAMGraphStreams</strong>](/windows/desktop/api/Strmif/nn-strmif-iamgraphstreams)</td>
<td>Controls a filter graph that renders a live source.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMLatency</strong>](/windows/desktop/api/Strmif/nn-strmif-iamlatency)</td>
<td>Reports the amount of latency that a filter introduces into the graph.</td>
</tr>
<tr class="even">
<td>[<strong>IAMLine21Decoder</strong>](/windows/desktop/api/il21dec/nn-il21dec-iamline21decoder)</td>
<td>Sets and retrieves information about closed captions.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMMediaContent</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent)</td>
<td>Retrieves metadata from a stream.</td>
</tr>
<tr class="even">
<td>[<strong>IAMNetShowConfig</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iamnetshowconfig)</td>
<td>Configures the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMNetShowExProps</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iamnetshowexprops)</td>
<td>Configures the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMNetShowPreroll</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iamnetshowpreroll)</td>
<td>Sets and retrieves the preroll settings for the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMNetworkStatus</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-iamnetworkstatus)</td>
<td>Reports the quality of the network connection for the legacy Windows Media Player 6.4 source filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMOpenProgress</strong>](/windows/desktop/api/Strmif/nn-strmif-iamopenprogress)</td>
<td>Reports the progress of a file-open operation.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMOverlayFX</strong>](/windows/desktop/api/Strmif/nn-strmif-iamoverlayfx)</td>
<td>Controls how the video overlay appears on the user's screen.</td>
</tr>
<tr class="even">
<td>[<strong>IAMParse</strong>](/windows/desktop/api/Amparse/nn-amparse-iamparse)</td>
<td>Sets and retrieves the parse time for an MPEG-2 stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMPushSource</strong>](/windows/desktop/api/Strmif/nn-strmif-iampushsource)</td>
<td>Synchronizes a filter graph that renders a live source.</td>
</tr>
<tr class="even">
<td>[<strong>IAMResourceControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iamresourcecontrol)</td>
<td>Opens and holds an audio device resource.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMStats</strong>](/windows/desktop/api/Control/nn-control-iamstats)</td>
<td>Retrieves performance data from the Filter Graph Manager.</td>
</tr>
<tr class="even">
<td>[<strong>IAMStreamConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig)</td>
<td>Sets the output format on certain capture and compression filters.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMStreamControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol)</td>
<td>Controls individual streams on a filter.</td>
</tr>
<tr class="even">
<td>[<strong>IAMStreamSelect</strong>](/windows/desktop/api/Strmif/nn-strmif-iamstreamselect)</td>
<td>selects from the available streams on a parser filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMTimecodeReader</strong>](/windows/desktop/api/Strmif/nn-strmif-iamtimecodereader)</td>
<td>Reads SMPTE or MIDI timecode from an external device.</td>
</tr>
<tr class="even">
<td>[<strong>IAMTuner</strong>](/windows/desktop/api/Strmif/nn-strmif-iamtuner)</td>
<td>Controls a TV tuner.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMTVAudio</strong>](/windows/desktop/api/Strmif/nn-strmif-iamtvaudio)</td>
<td>Controls audio from a television source.</td>
</tr>
<tr class="even">
<td>[<strong>IAMTVTuner</strong>](/windows/desktop/api/Strmif/nn-strmif-iamtvtuner)</td>
<td>Controls a TV tuner.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVfwCaptureDialogs</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvfwcapturedialogs)</td>
<td>Displays a dialog box provided by a Video for Windows (VFW) capture driver.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVfwCompressDialogs</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvfwcompressdialogs)</td>
<td>Displays a dialog box provided by a Video for Windows (VFW) codec.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoAccelerator</strong>](/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator)</td>
<td>Enables a video decoder filter to access DirectX Video Acceleration (DXVA) 1.0 functionality.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVideoAcceleratorNotify</strong>](/windows/desktop/api/videoacc/nn-videoacc-iamvideoacceleratornotify)</td>
<td>Callback interface for DXVA 1.0.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoCompression</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression)</td>
<td>Sets and retrieves video compression properties.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVideoControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvideocontrol)</td>
<td>Controls certain video capture operations such as enumerating available frame rates and image orientation.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoDecimationProperties</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvideodecimationproperties)</td>
<td>Controls how the Overlay Mixer performs video decimation.</td>
</tr>
<tr class="even">
<td>[<strong>IAMVideoProcAmp</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvideoprocamp)</td>
<td>Adjusts the qualities of an incoming video signal.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMWMBufferPass</strong>](/windows/desktop/api/Dshowasf/nn-dshowasf-iamwmbufferpass)</td>
<td>Gets or sets properties on individual samples in an ASF stream.</td>
</tr>
<tr class="even">
<td>[<strong>IAMWMBufferPassCallback</strong>](/windows/desktop/api/Dshowasf/nn-dshowasf-iamwmbufferpasscallback)</td>
<td>Callback interface used with the [<strong>IAMWMBufferPass</strong>](/windows/desktop/api/Dshowasf/nn-dshowasf-iamwmbufferpass) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IAMWstDecoder</strong>](/windows/desktop/api/Iwstdec/nn-iwstdec-iamwstdecoder)</td>
<td>Sets and retrieves information about World Standard Teletext (WST)</td>
</tr>
<tr class="even">
<td>[<strong>IAsyncReader</strong>](/windows/desktop/api/Strmif/nn-strmif-iasyncreader)</td>
<td>Performs an asynchronous data request on a filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IBaseFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)</td>
<td>Exposed by filters. This is the primary interface for all DirectShow filters.</td>
</tr>
<tr class="even">
<td>[<strong>IBasicAudio</strong>](/windows/desktop/api/Control/nn-control-ibasicaudio)</td>
<td>Controls the volume and balance of the audio stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IBasicVideo</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo)</td>
<td>Sets video properties such as the destination and source rectangles.</td>
</tr>
<tr class="even">
<td>[<strong>IBasicVideo2</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo2)</td>
<td>Extends the [<strong>IBasicVideo</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>ICameraControl</strong>](/windows/desktop/api/Vidcap/nn-vidcap-icameracontrol)</td>
<td>Controls the camera settings on a capture device.</td>
</tr>
<tr class="even">
<td>[<strong>ICaptureGraphBuilder2</strong>](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2)</td>
<td>Builds capture graphs and other custom filter graphs.</td>
</tr>
<tr class="odd">
<td>[<strong>ICodecAPI</strong>](/windows/desktop/api/Strmif/nn-strmif-icodecapi)</td>
<td>Configures an encoder or decoder.</td>
</tr>
<tr class="even">
<td>[<strong>IConfigAsfWriter</strong>](/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter)</td>
<td>Configures the [WM ASF Writer](wm-asf-writer-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IConfigAsfWriter2</strong>](/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter2)</td>
<td>Extends the [<strong>IConfigAsfWriter</strong>](/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IConfigAviMux</strong>](/windows/desktop/api/Strmif/nn-strmif-iconfigavimux)</td>
<td>Configures the [AVI Mux](avi-mux-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IConfigInterleaving</strong>](/windows/desktop/api/Strmif/nn-strmif-iconfiginterleaving)</td>
<td>Controls how the AVI Mux interleaves audio and video samples.</td>
</tr>
<tr class="even">
<td>[<strong>ICreateDevEnum</strong>](/windows/desktop/api/Strmif/nn-strmif-icreatedevenum)</td>
<td>Creates an enumerator for a category of filters.</td>
</tr>
<tr class="odd">
<td>[<strong>IDDrawExclModeVideo</strong>](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideo)</td>
<td>Enables video playback in DirectDraw exclusive full-screen mode.</td>
</tr>
<tr class="even">
<td>[<strong>IDDrawExclModeVideoCallback</strong>](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideocallback)</td>
<td>Callback interface for the [<strong>IDDrawExclModeVideoCallback</strong>](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideocallback) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IDecimateVideoImage</strong>](/windows/desktop/api/Strmif/nn-strmif-idecimatevideoimage)</td>
<td>Specifies decimation on a decoder filter.</td>
</tr>
<tr class="even">
<td>[<strong>IDeferredCommand</strong>](/windows/desktop/api/Control/nn-control-ideferredcommand)</td>
<td>Cancels or modifies graph-control commands that were queued using the [<strong>IQueueCommand</strong>](/windows/desktop/api/Control/nn-control-iqueuecommand) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawVideo</strong>](/windows/desktop/api/Amvideo/nn-amvideo-idirectdrawvideo)</td>
<td>Queries the [Video Renderer](video-renderer-filter.md) filter about DirectDraw surfaces and hardware capabilities.</td>
</tr>
<tr class="even">
<td>[<strong>IDirectDrawMediaSample</strong>](/windows/desktop/api/Amstream/nn-amstream-idirectdrawmediasample)</td>
<td>Provides access to DirectDraw surfaces allocated by the [Overlay Mixer](overlay-mixer-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawMediaSampleAllocator</strong>](/windows/desktop/api/Amstream/nn-amstream-idirectdrawmediasampleallocator)</td>
<td>Allocates samples that contain DirectDraw surfaces.</td>
</tr>
<tr class="even">
<td>[<strong>IDistributorNotify</strong>](/windows/desktop/api/Strmif/nn-strmif-idistributornotify)</td>
<td>Enables a plug-in distributor to be notified when the filter graph changes.</td>
</tr>
<tr class="odd">
<td>[<strong>IDMOWrapperFilter</strong>](/windows/desktop/api/Dmodshow/nn-dmodshow-idmowrapperfilter)</td>
<td>Enables an application to use a DirectX Media Object (DMO) inside a filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IDShowPlugin</strong>](/windows/desktop/api/Qnetwork/nn-qnetwork-idshowplugin)</td>
<td>Enables the Windows Media Source filter to communicate with the Windows Media Player 6.4 Plug-in for Netscape Navigator.</td>
</tr>
<tr class="odd">
<td>[<strong>IDvdCmd</strong>](/windows/desktop/api/Strmif/nn-strmif-idvdcmd)</td>
<td>Waits for DVD commands to start or end.</td>
</tr>
<tr class="even">
<td>[<strong>IDvdControl2</strong>](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2)</td>
<td>Navigates and plays DVD-Video titles.</td>
</tr>
<tr class="odd">
<td>[<strong>IDvdGraphBuilder</strong>](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder)</td>
<td>Builds a filter graph for DVD-Video playback.</td>
</tr>
<tr class="even">
<td>[<strong>IDvdInfo2</strong>](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2)</td>
<td>Reports attributes of a DVD disc or the current state of the DVD Navigator filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IDvdState</strong>](/windows/desktop/api/Strmif/nn-strmif-idvdstate)</td>
<td>Saves the current DVD playback location and state.</td>
</tr>
<tr class="even">
<td>[<strong>IDVEnc</strong>](/windows/desktop/api/Strmif/nn-strmif-idvenc)</td>
<td>Sets and retrieves properties on the [DV Video Encoder](dv-video-encoder-filter.md) filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IDVRGB219</strong>](/windows/desktop/api/Strmif/nn-strmif-idvrgb219)</td>
<td>Controls the dynamic range in the DV Video Encoder and [DV Video Decoder](dv-video-decoder-filter.md) filters.</td>
</tr>
<tr class="even">
<td>[<strong>IDVSplitter</strong>](/windows/desktop/api/Strmif/nn-strmif-idvsplitter)</td>
<td>Downgrades the frame rate on a digital video (DV) stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IEnumFilters</strong>](/windows/desktop/api/Strmif/nn-strmif-ienumfilters)</td>
<td>Enumerates the filters in a filter graph</td>
</tr>
<tr class="even">
<td>[<strong>IEnumMediaTypes</strong>](/windows/desktop/api/Strmif/nn-strmif-ienummediatypes)</td>
<td>Enumerates a pin's preferred media types</td>
</tr>
<tr class="odd">
<td>[<strong>IEnumPIDMap</strong>](/windows/desktop/api/Bdaiface/nn-bdaiface-ienumpidmap)</td>
<td>Enumerates the mappings of Packet IDs (PID) to output pins on the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) filter.</td>
</tr>
<tr class="even">
<td>[<strong>IEnumPins</strong>](/windows/desktop/api/Strmif/nn-strmif-ienumpins)</td>
<td>Enumerates pins on a filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IEnumStreamIdMap</strong>](/windows/desktop/api/Strmif/nn-strmif-ienumstreamidmap)</td>
<td>Enumerates the mappings of stream IDs to output pins on the MPEG-2 Demultiplexer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IFileSinkFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter)</td>
<td>Exposed by filters that write data to a file.</td>
</tr>
<tr class="odd">
<td>[<strong>IFileSinkFilter2</strong>](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter2)</td>
<td>Extends the [<strong>IFileSinkFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IFileSourceFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter)</td>
<td>Exposed by source filters.</td>
</tr>
<tr class="odd">
<td>[<strong>IFilterChain</strong>](/windows/desktop/api/Strmif/nn-strmif-ifilterchain)</td>
<td>Starting, stops, or removes chains of filters in a filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IFilterGraph</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph)</td>
<td>Builds a filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IFilterGraph2</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph2)</td>
<td>Extends the [<strong>IGraphBuilder</strong>](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IFilterGraph3</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph3)</td>
<td>Extends the [<strong>IFilterGraph2</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph2) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IFilterMapper2</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2)</td>
<td>Registers and unregisters filters, and locates filters in the registry.</td>
</tr>
<tr class="even">
<td>[<strong>IFilterMapper3</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper3)</td>
<td>Extends the [<strong>IFilterMapper2</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IFullScreenVideoEx</strong>](/windows/desktop/api/Amvideo/nn-amvideo-ifullscreenvideoex)</td>
<td>Exposed by the [Full Screen Renderer](full-screen-renderer-filter.md) filter.</td>
</tr>
<tr class="even">
<td>[<strong>IGetCapabilitiesKey</strong>](/windows/desktop/api/Strmif/nn-strmif-igetcapabilitieskey)</td>
<td>Retrieves the capabilities of a software or hardware encoder from the registry.</td>
</tr>
<tr class="odd">
<td>[<strong>IGraphBuilder</strong>](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder)</td>
<td>Extends the [<strong>IFilterGraph</strong>](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph) interface. This is the primary interface of the Filter Graph Manager.</td>
</tr>
<tr class="even">
<td>[<strong>IGraphConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-igraphconfig)</td>
<td>Reconfigures the filter graph while the graph is running.</td>
</tr>
<tr class="odd">
<td>[<strong>IGraphConfigCallback</strong>](/windows/desktop/api/Strmif/nn-strmif-igraphconfigcallback)</td>
<td>Callback interface for the [<strong>IGraphConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-igraphconfig) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IGraphVersion</strong>](/windows/desktop/api/Strmif/nn-strmif-igraphversion)</td>
<td>Retrieves the current version number of the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IIPDVDec</strong>](/windows/desktop/api/Strmif/nn-strmif-iipdvdec)</td>
<td>Configures the [DV Video Decoder](dv-video-decoder-filter.md) filter.</td>
</tr>
<tr class="even">
<td>[<strong>IKsNodeControl</strong>](/windows/desktop/api/Vidcap/nn-vidcap-iksnodecontrol)</td>
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
<td>[<strong>IKsTopologyInfo</strong>](/windows/desktop/api/Vidcap/nn-vidcap-ikstopologyinfo)</td>
<td>Enumerates the nodes in a stream class driver.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaControl</strong>](/windows/desktop/api/Control/nn-control-imediacontrol)</td>
<td>Controls the flow of data through the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaEvent</strong>](/windows/desktop/api/Control/nn-control-imediaevent)</td>
<td>Retrieves event notifications from the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaEventEx</strong>](/windows/desktop/api/Control/nn-control-imediaeventex)</td>
<td>Extends the [<strong>IMediaEvent</strong>](/windows/desktop/api/Control/nn-control-imediaevent) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaEventSink</strong>](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink)</td>
<td>Notifies the Filter Graph Manager of events that occur within the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-imediafilter)</td>
<td>Controls the streaming state of a filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaPosition</strong>](/windows/desktop/api/Control/nn-control-imediaposition)</td>
<td>Controls seeking in the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaPropertyBag</strong>](/windows/desktop/api/Strmif/nn-strmif-imediapropertybag)</td>
<td>Sets and retrieves INFO and DISP chunks in Audio-Video Interleaved (AVI) files.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaSample</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample)</td>
<td>Sets and retrieves properties on media samples.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaSample2</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample2)</td>
<td>Extends the [<strong>IMediaSample</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMediaSample2Config</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample2config)</td>
<td>Returns a pointer to a Direct3D surface representing a VRAM capture buffer.</td>
</tr>
<tr class="even">
<td>[<strong>IMediaSeeking</strong>](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)</td>
<td>Controls seeking in the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IMemAllocator</strong>](/windows/desktop/api/Strmif/nn-strmif-imemallocator)</td>
<td>Allocates media samples.</td>
</tr>
<tr class="even">
<td>[<strong>IMemAllocatorCallbackTemp</strong>](/windows/desktop/api/Strmif/nn-strmif-imemallocatorcallbacktemp)</td>
<td>Enables a filter to receive a callback notification from an allocator.
<blockquote>
[!Note]<br />
Deprecated.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMemAllocatorNotifyCallbackTemp</strong>](/windows/desktop/api/Strmif/nn-strmif-imemallocatornotifycallbacktemp)</td>
<td>Callback interface for the [<strong>IMemAllocatorCallbackTemp</strong>](/windows/desktop/api/Strmif/nn-strmif-imemallocatorcallbacktemp) interface.
<blockquote>
[!Note]<br />
Deprecated.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)</td>
<td>Delivers media data to an input pin.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerOCX</strong>](/windows/desktop/api/Mixerocx/nn-mixerocx-imixerocx)</td>
<td>Exposed by the Overlay Mixer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerOCXNotify</strong>](/windows/desktop/api/Mixerocx/nn-mixerocx-imixerocxnotify)</td>
<td>Callback interface for the [<strong>IMixerOCX</strong>](/windows/desktop/api/Mixerocx/nn-mixerocx-imixerocx) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerPinConfig</strong>](/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig)</td>
<td>Manipulates video streams on the Overlay Mixer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerPinConfig2</strong>](/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig2)</td>
<td>Extends the [<strong>IMixerPinConfig</strong>](/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IMpeg2Demultiplexer</strong>](/windows/desktop/api/Strmif/nn-strmif-impeg2demultiplexer)</td>
<td>Configures the MPEG-2 Demultiplexer filter.</td>
</tr>
<tr class="even">
<td>[<strong>IMPEG2PIDMap</strong>](/windows/desktop/api/Bdaiface/nn-bdaiface-impeg2pidmap)</td>
<td>Associates an output pin on the MPEG-2 Demultiplexer filter with one or more packet IDs (PIDs).</td>
</tr>
<tr class="odd">
<td>[<strong>IMPEG2StreamIdMap</strong>](/windows/desktop/api/Strmif/nn-strmif-impeg2streamidmap)</td>
<td>Associates an output pin on the MPEG-2 Demultiplexer filter with one or more stream IDs.</td>
</tr>
<tr class="even">
<td>[<strong>IMpegAudioDecoder</strong>](/windows/desktop/api/mpegtype/nn-mpegtype-impegaudiodecoder)</td>
<td>Configures the MPEG-1 Audio Decoder.</td>
</tr>
<tr class="odd">
<td>[<strong>IOverlay</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlay)</td>
<td>Enables a filter to write directly to video memory.</td>
</tr>
<tr class="even">
<td>[<strong>IOverlayNotify</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlaynotify)</td>
<td>Callback interface for the [<strong>IOverlay</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlay) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IOverlayNotify2</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlaynotify2)</td>
<td>Callback interface for the [<strong>IOverlay</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlay) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IPersistMediaPropertyBag</strong>](/windows/desktop/api/Strmif/nn-strmif-ipersistmediapropertybag)</td>
<td>Sets and retrieves INFO and DISP chunks in Audio-Video Interleaved (AVI) streams.</td>
</tr>
<tr class="odd">
<td>[<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin)</td>
<td>Exposed by all filter pins.</td>
</tr>
<tr class="even">
<td>[<strong>IPinConnection</strong>](/windows/desktop/api/Strmif/nn-strmif-ipinconnection)</td>
<td>Reconnects an input pin while the filter is still running.</td>
</tr>
<tr class="odd">
<td>[<strong>IPinFlowControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ipinflowcontrol)</td>
<td>Blocks data flow from an active output pin.</td>
</tr>
<tr class="even">
<td>[<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</td>
<td>Provides support for quality control in the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IQualProp</strong>](/windows/desktop/api/Amvideo/nn-amvideo-iqualprop)</td>
<td>Retrieves performance information from video renderers.</td>
</tr>
<tr class="even">
<td>[<strong>IQueueCommand</strong>](/windows/desktop/api/Control/nn-control-iqueuecommand)</td>
<td>Queues a command on the filter graph for processing at a designated time.</td>
</tr>
<tr class="odd">
<td>[<strong>IReferenceClock</strong>](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock)</td>
<td>Provides the reference time for the filter graph.</td>
</tr>
<tr class="even">
<td>[<strong>IReferenceClockTimerControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ireferenceclocktimercontrol)</td>
<td>Changes the timer period used by a reference clock.</td>
</tr>
<tr class="odd">
<td>[<strong>IRegisterServiceProvider</strong>](/windows/desktop/api/Strmif/nn-strmif-iregisterserviceprovider)</td>
<td>Registers an object as a service with the Filter Graph Manager.</td>
</tr>
<tr class="even">
<td>[<strong>IResourceConsumer</strong>](/windows/desktop/api/Strmif/nn-strmif-iresourceconsumer)</td>
<td>Callback interface for the [<strong>IResourceManager</strong>](/windows/desktop/api/Strmif/nn-strmif-iresourcemanager) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IResourceManager</strong>](/windows/desktop/api/Strmif/nn-strmif-iresourcemanager)</td>
<td>Resolves contentions for system resources.</td>
</tr>
<tr class="even">
<td>[<strong>ISeekingPassThru</strong>](/windows/desktop/api/Strmif/nn-strmif-iseekingpassthru)</td>
<td>Implements seeking for one-input filters.</td>
</tr>
<tr class="odd">
<td>[<strong>ISelector</strong>](/windows/desktop/api/Vidcap/nn-vidcap-iselector)</td>
<td>Selects source nodes in a stream class driver.</td>
</tr>
<tr class="even">
<td>[<strong>IStreamBuilder</strong>](/windows/desktop/api/Strmif/nn-strmif-istreambuilder)</td>
<td>Enables an output pin to build the downstream section of the filter graph.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoFrameStep</strong>](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep)</td>
<td>Steps through a video stream.</td>
</tr>
<tr class="even">
<td>[<strong>IVideoProcAmp</strong>](/windows/desktop/api/Vidcap/nn-vidcap-ivideoprocamp)</td>
<td>Controls the image adjustment (ProcAmp) settings on a capture device.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoWindow</strong>](/windows/desktop/api/Control/nn-control-ivideowindow)</td>
<td>Sets properties on the video window.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRAspectRatioControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmraspectratiocontrol)</td>
<td>controls whether the [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7) preserves the aspect ratio of the source video.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRAspectRatioControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmraspectratiocontrol9)</td>
<td>Controls whether the [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9) preserves the aspect ratio of the source video</td>
</tr>
<tr class="even">
<td>[<strong>IVMRDeinterlaceControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrdeinterlacecontrol)</td>
<td>Supports hardware-accelerated deinterlacing using the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRDeinterlaceControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9)</td>
<td>Supports hardware-accelerated deinterlacing using the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRFilterConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrfilterconfig)</td>
<td>Configures the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRFilterConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrfilterconfig9)</td>
<td>Configures the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImageCompositor</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagecompositor)</td>
<td>Exposed by VMR-7 compositors.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRImageCompositor9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagecompositor9)</td>
<td>Exposed by VMR-9 compositors.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImagePresenter</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenter)</td>
<td>Exposed by VMR-7 allocator-presenters.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRImagePresenter9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenter9)</td>
<td>Exposed by VMR-9 allocator-presenters.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImagePresenterConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenterconfig)</td>
<td>Sets the renderering preferences on the image presenter used by the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRImagePresenterConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenterconfig9)</td>
<td>Sets the renderering preferences on the image presenter used by the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRImagePresenterExclModeConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenterexclmodeconfig)</td>
<td>Setting and retrieves the renderering preferences on the Exclusive Mode Allocator-Presenter for the VMR-7</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRMixerBitmap</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmixerbitmap)</td>
<td>Blends a static image onto the video stream, when using the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRMixerBitmap9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixerbitmap9)</td>
<td>Blends a static image onto the video stream, when using the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRMixerControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmixercontrol)</td>
<td>Manipulates the incoming video streams on the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRMixerControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixercontrol9)</td>
<td>Manipulates the incoming video streams on the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRMonitorConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmonitorconfig)</td>
<td>Controls monitor usage by the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRMonitorConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmonitorconfig9)</td>
<td>Controls monitor usage by the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurface</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrsurface)</td>
<td>Exposed by media samples from the VMR-7.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRSurface9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurface9)</td>
<td>Exposed by media samples from the VMR-9.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurfaceAllocator</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocator)</td>
<td>Allocates the DirectDraw surfaces used by the VMR-7 allocator-presenter.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRSurfaceAllocator9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocator9)</td>
<td>Allocates the Direct3D surfaces used by the VMR-9 allocator-presenter.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurfaceAllocatorEx9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatorex9)</td>
<td>Extends the [<strong>IVMRSurfaceAllocator9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocator9) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRSurfaceAllocatorNotify</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocatornotify)</td>
<td>Enables the allocator-presenter to notify the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRSurfaceAllocatorNotify9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9)</td>
<td>Enables the allocator-presenter to notify the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRVideoStreamControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrvideostreamcontrol)</td>
<td>Controls input pins on the VMR-7.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRVideoStreamControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrvideostreamcontrol9)</td>
<td>Controls input pins on the VMR-9.</td>
</tr>
<tr class="even">
<td>[<strong>IVMRWindowlessControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol)</td>
<td>Controls how the VMR-7 renders a video stream.</td>
</tr>
<tr class="odd">
<td>[<strong>IVMRWindowlessControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9)</td>
<td>Controls how the VMR-9 renders a video stream.</td>
</tr>
<tr class="even">
<td>[<strong>IVPBaseConfig</strong>](/windows/desktop/api/Vpconfig/nn-vpconfig-ivpbaseconfig)</td>
<td>Base interface for the [<strong>IVPConfig</strong>](/windows/desktop/api/Vpconfig/nn-vpconfig-ivpconfig) interface.</td>
</tr>
<tr class="odd">
<td>[<strong>IVPBaseNotify</strong>](/windows/desktop/api/Vpnotify/nn-vpnotify-ivpbasenotify)</td>
<td>Base interface for the [<strong>IVPNotify</strong>](/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IVPConfig</strong>](/windows/desktop/api/Vpconfig/nn-vpconfig-ivpconfig)</td>
<td>Enables a video port to communicate with the Overlay Mixer filter.</td>
</tr>
<tr class="odd">
<td>[<strong>IVPManager</strong>](/windows/desktop/api/Strmif/nn-strmif-ivpmanager)</td>
<td>Exposed by the Video Port Manager filter.</td>
</tr>
<tr class="even">
<td>[<strong>IVPNotify</strong>](/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify)</td>
<td>Enables the Overlay Mixer to control the properties of a hardware device that uses a video port.</td>
</tr>
<tr class="odd">
<td>[<strong>IVPNotify2</strong>](/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify2)</td>
<td>Extends the [<strong>IVPNotify</strong>](/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify) interface.</td>
</tr>
<tr class="even">
<td>[<strong>IXMLGraphBuilder</strong>](/windows/desktop/api/amxmlgraphbuilder/nn-amxmlgraphbuilder-ixmlgraphbuilder)</td>
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

 

 




