---
description: Media Foundation Interfaces
ms.assetid: 3e367190-4c88-430e-adbf-9837e1bf0d2b
title: Media Foundation Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Interfaces

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/Mfmediacapture/nn-mfmediacapture-iadvancedmediacapture"><strong>IAdvancedMediaCapture</strong></a><br/></td>
<td>Enables advanced media capture.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediacapture/nn-mfmediacapture-iadvancedmediacaptureinitializationsettings"><strong>IAdvancedMediaCaptureInitializationSettings</strong></a><br/></td>
<td>Provides initialization settings for advanced media capture.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mfmediacapture/nn-mfmediacapture-iadvancedmediacapturesettings"><strong>IAdvancedMediaCaptureSettings</strong></a><br/></td>
<td>Provides settings for advanced media capture.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirect3ddevicemanager9"><strong>IDirect3DDeviceManager9</strong></a><br/></td>
<td>Enables two threads to share the same Direct3D 9 device, and provides access to the DirectX Video Acceleration (DXVA) features of the device.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoaccelerationservice"><strong>IDirectXVideoAccelerationService</strong></a><br/></td>
<td>Provides DirectX Video Acceleration (DXVA) services from a Direct3D device.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoder"><strong>IDirectXVideoDecoder</strong></a><br/></td>
<td>Represents a DirectX Video Acceleration (DXVA) video decoder device.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoderservice"><strong>IDirectXVideoDecoderService</strong></a><br/></td>
<td>Provides access to DirectX Video Acceleration (DXVA) decoder services.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration"><strong>IDirectXVideoMemoryConfiguration</strong></a><br/></td>
<td>Sets the type of video memory for uncompressed video surfaces.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoprocessor"><strong>IDirectXVideoProcessor</strong></a><br/></td>
<td>Represents a DirectX Video Acceleration (DXVA) video processor device.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoprocessorservice"><strong>IDirectXVideoProcessorService</strong></a><br/></td>
<td>Provides access to DirectX Video Acceleration (DXVA) video processing services.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-ievrfilterconfig"><strong>IEVRFilterConfig</strong></a><br/></td>
<td>Sets the number of input pins on the DirectShow <a href="/windows/desktop/DirectShow/enhanced-video-renderer-filter"><strong>Enhanced Video Renderer</strong></a> (EVR) filter.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr/nn-evr-ievrfilterconfigex"><strong>IEVRFilterConfigEx</strong></a><br/></td>
<td>Configures the DirectShow <a href="/windows/desktop/DirectShow/enhanced-video-renderer-filter"><strong>Enhanced Video Renderer</strong></a> (EVR) filter.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-ievrtrustedvideoplugin"><strong>IEVRTrustedVideoPlugin</strong></a><br/></td>
<td>Enables a plug-in component for the enhanced video renderer (EVR) to work with protected media.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr9/nn-evr9-ievrvideostreamcontrol"><strong>IEVRVideoStreamControl</strong></a><br/></td>
<td>This interface is not supported.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer"><strong>IMF2DBuffer</strong></a><br/></td>
<td>Represents a buffer that contains a two-dimensional surface, such as a video frame. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer2"><strong>IMF2DBuffer2</strong></a><br/></td>
<td>Represents a buffer that contains a two-dimensional surface, such as a video frame.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate"><strong>IMFActivate</strong></a><br/></td>
<td>Enables the application to defer the creation of an object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfcontentinfo"><strong>IMFASFContentInfo</strong></a><br/></td>
<td>Provides methods to work with the header section of files conforming to the Advanced Systems Format (ASF) specification. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfindexer"><strong>IMFASFIndexer</strong></a><br/></td>
<td>Provides methods to work with indexes in Systems Format (ASF) files.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfmultiplexer"><strong>IMFASFMultiplexer</strong></a><br/></td>
<td>Provides methods to create Advanced Systems Format (ASF) data packets.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfmutualexclusion"><strong>IMFASFMutualExclusion</strong></a><br/></td>
<td>Configures an Advanced Systems Format (ASF) mutual exclusion object, which manages information about a group of streams in an ASF profile that are mutually exclusive.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfprofile"><strong>IMFASFProfile</strong></a><br/></td>
<td>Manages an Advanced Systems Format (ASF) profile.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfsplitter"><strong>IMFASFSplitter</strong></a><br/></td>
<td>Provides methods to read data from an Advanced Systems Format (ASF) file.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig"><strong>IMFASFStreamConfig</strong></a><br/></td>
<td>Configures the settings of a stream in an ASF file.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamprioritization"><strong>IMFASFStreamPrioritization</strong></a><br/></td>
<td>Not implemented.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamselector"><strong>IMFASFStreamSelector</strong></a><br/></td>
<td>Selects streams in an Advanced Systems Format (ASF) file, based on the mutual exclusion information in the ASF header.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback"><strong>IMFAsyncCallback</strong></a><br/></td>
<td>Callback interface to notify the application when an asynchronous method completes. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mfobjects/nn-mfobjects-imfasynccallbacklogging"><strong>IMFAsyncCallbackLogging</strong></a><br/></td>
<td>Provides logging information about the parent object the async callback is associated with.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfasyncresult"><strong>IMFAsyncResult</strong></a><br/></td>
<td>Provides information about the result of an asynchronous operation. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes"><strong>IMFAttributes</strong></a><br/></td>
<td>Provides a generic way to store key/value pairs on an object.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfaudiomediatype"><strong>IMFAudioMediaType</strong></a><br/></td>
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfaudiomediatype"><strong>IMFAudioMediaType</strong></a> is no longer available for use as of Windows 7.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfaudiopolicy"><strong>IMFAudioPolicy</strong></a><br/></td>
<td>Configures the audio session that is associated with the streaming audio renderer (SAR).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfaudiostreamvolume"><strong>IMFAudioStreamVolume</strong></a><br/></td>
<td>Controls the volume levels of individual audio channels.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfbufferlistnotify"><strong>IMFBufferListNotify</strong></a><br/></td>
<td>Enables <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebufferlist"><strong>IMFSourceBufferList</strong></a> object to notify its clients of important state changes.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream"><strong>IMFByteStream</strong></a><br/></td>
<td>Represents a byte stream from some data source, which might be a local file, a network file, or some other source.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfbytestreambuffering"><strong>IMFByteStreamBuffering</strong></a><br/></td>
<td>Controls how a byte stream buffers data from a network. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamcachecontrol"><strong>IMFByteStreamCacheControl</strong></a><br/></td>
<td>Controls how a network byte stream transfers data to a local cache.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamcachecontrol2"><strong>IMFByteStreamCacheControl2</strong></a><br/></td>
<td>Controls how a network byte stream transfers data to a local cache.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamhandler"><strong>IMFByteStreamHandler</strong></a><br/></td>
<td>Creates a media source from a byte stream. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestreamproxyclassfactory"><strong>IMFByteStreamProxyClassFactory</strong></a><br/></td>
<td>Creates a proxy to a byte stream.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamtimeseek"><strong>IMFByteStreamTimeSeek</strong></a><br/></td>
<td>Seeks a byte stream by time position.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengine"><strong>IMFCaptureEngine</strong></a><br/></td>
<td>Controls one or more capture devices.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengineclassfactory"><strong>IMFCaptureEngineClassFactory</strong></a><br/></td>
<td>Creates an instance of the capture engine.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengineoneventcallback"><strong>IMFCaptureEngineOnEventCallback</strong></a><br/></td>
<td>Callback interface for receiving events from the capture engine.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengineonsamplecallback"><strong>IMFCaptureEngineOnSampleCallback</strong></a><br/></td>
<td>Callback interface to receive data from the capture engine.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengineonsamplecallback2"><strong>IMFCaptureEngineOnSampleCallback2</strong></a><br/></td>
<td>Extensions for the <a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengineonsamplecallback"><strong>IMFCaptureEngineOnSampleCallback</strong></a> callback interface that is used to receive data from the capture engine.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturephotosink"><strong>IMFCapturePhotoSink</strong></a><br/></td>
<td>Controls the photo sink.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturepreviewsink"><strong>IMFCapturePreviewSink</strong></a><br/></td>
<td>Controls the preview sink.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturerecordsink"><strong>IMFCaptureRecordSink</strong></a><br/></td>
<td>Controls the recording sink.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesink"><strong>IMFCaptureSink</strong></a><br/></td>
<td>Controls a capture sink, which is an object that receives one or more streams from a capture device.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesink2"><strong>IMFCaptureSink2</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesink"><strong>IMFCaptureSink</strong></a> interface to provide functionality for dynamically setting the output media type of the record sink or preview sink.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesource"><strong>IMFCaptureSource</strong></a><br/></td>
<td>Controls the capture source object. The capture source manages the audio and video capture devices.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfcdmsuspendnotify"><strong>IMFCdmSuspendNotify</strong></a><br/></td>
<td>Used to enable the client to notify the Content Decryption Module (CDM) when global resources should be brought into a consistent state prior to suspending. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfclock"><strong>IMFClock</strong></a><br/></td>
<td>Provides timing information from a clock in Microsoft Media Foundation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfclockconsumer"><strong>IMFClockConsumer</strong></a><br/></td>
<td>Implemented by an app in order to get access to the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfpresentationclock"><strong>IMFPresentationClock</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfclockstatesink"><strong>IMFClockStateSink</strong></a><br/></td>
<td>Receives state-change notifications from the presentation clock. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfcollection"><strong>IMFCollection</strong></a><br/></td>
<td>Represents a generic collection of <strong>IUnknown</strong> pointers. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfcontentdecryptorcontext"><strong>IMFContentDecryptorContext</strong></a><br/></td>
<td>Allows a decryptor to manage hardware keys and decrypt hardware samples.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler"><strong>IMFContentEnabler</strong></a><br/></td>
<td>Implements one step that must be performed for the user to access media content.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectiondevice"><strong>IMFContentProtectionDevice</strong></a><br/></td>
<td>Allows a decryptor to communicate with the security processor that implements the hardware decryption for a protection system. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectionmanager"><strong>IMFContentProtectionManager</strong></a><br/></td>
<td>Enables playback of protected content by providing the application with a pointer to a content enabler object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr/nn-evr-imfdesiredsample"><strong>IMFDesiredSample</strong></a><br/></td>
<td>Enables the presenter for the enhanced video renderer (EVR) to request a specific frame from the video mixer.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmp2dlna/nn-mfmp2dlna-imfdlnasinkinit"><strong>IMFDLNASinkInit</strong></a><br/></td>
<td>Initializes the Digital Living Network Alliance (DLNA) media sink. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcontainer/nn-wmcontainer-imfdrmnethelper"><strong>IMFDRMNetHelper</strong></a><br/></td>
<td>Configures Windows Media Digital Rights Management (DRM) for Network Devices on a network sink.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfdxgibuffer"><strong>IMFDXGIBuffer</strong></a><br/></td>
<td>Represents a buffer that contains a Microsoft DirectX Graphics Infrastructure (DXGI) surface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfdxgidevicemanager"><strong>IMFDXGIDeviceManager</strong></a><br/></td>
<td>Enables two threads to share the same Microsoft Direct3D 11 device.<br/></td>
</tr>
<tr class="odd">
<td><a href="imfdxgidevicemanagersource.md"><strong>IMFDXGIDeviceManagerSource</strong></a><br/></td>
<td>Provides functionality for getting the <a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfdxgidevicemanager"><strong>IMFDXGIDeviceManager</strong></a> from the Media Foundation video rendering sink.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock"><strong>IMFFieldOfUseMFTUnlock</strong></a><br/></td>
<td>Enables an application to use a Media Foundation transform (MFT) that has restrictions on its use.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imffinalizablemediasink"><strong>IMFFinalizableMediaSink</strong></a><br/></td>
<td>Optionally supported by media sinks to perform required tasks before shutdown.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfgetservice"><strong>IMFGetService</strong></a><br/></td>
<td>Queries an object for a specified service interface. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfhttpdownloadrequest"><strong>IMFHttpDownloadRequest</strong></a><br/></td>
<td>Applications implement this interface to override the default implementation of the HTTP and HTTPS protocols used by Microsoft Media Foundation. Applications provide the <strong>IMFHttpDownloadRequest</strong> interface to Media Foundation through the <a href="/windows/desktop/api/mfidl/nf-mfidl-imfhttpdownloadsession-createrequest"><strong>CreateRequest</strong></a> method on the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfhttpdownloadsession"><strong>IMFHttpDownloadSession</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfhttpdownloadsession"><strong>IMFHttpDownloadSession</strong></a><br/></td>
<td>Applications implement this interface to override the default implementation of the HTTP and HTTPS protocols used by Microsoft Media Foundation. Applications provide the <strong>IMFHttpDownloadSession</strong> interface to Media Foundation through the <a href="/windows/desktop/api/mfidl/nf-mfidl-imfhttpdownloadsessionprovider-createhttpdownloadsession"><strong>CreateHttpDownloadSession</strong></a> method on the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfhttpdownloadsessionprovider"><strong>IMFHttpDownloadSessionProvider</strong></a> interface. Microsoft Media Foundation uses this interface to perform a “streaming”, or “progressive”, download of a resource identified by a HTTP or HTTPS URL. Multiple HTTP requests may be sent to download the resource. The <strong>IMFHttpDownloadSession</strong> interface is used to create these individual HTTP requests.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfhttpdownloadsessionprovider"><strong>IMFHttpDownloadSessionProvider</strong></a><br/></td>
<td>Applications implement this interface in order to provide custom a custom HTTP or HTTPS download implementation. Use the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfsourceresolver"><strong>IMFSourceResolver</strong></a> interface to register the provider. For more information, see <a href="using-the-source-resolver.md">Using the Source Resolver</a>. Once registered, the Microsoft Media Foundation will invoke the <a href="/windows/desktop/api/mfidl/nf-mfidl-imfhttpdownloadsessionprovider-createhttpdownloadsession"><strong>CreateHttpDownloadSession</strong></a> method of the provider implementation to open HTTP or HTTPS URLs instead of using the default implementation.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfimagesharingengine"><strong>IMFImageSharingEngine</strong></a><br/></td>
<td>Enables image sharing.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfimagesharingengineclassfactory"><strong>IMFImageSharingEngineClassFactory</strong></a><br/></td>
<td>Creates an instance of the <a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfimagesharingengine"><strong>IMFImageSharingEngine</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfinputtrustauthority"><strong>IMFInputTrustAuthority</strong></a><br/></td>
<td>Enables other components in the protected media path (PMP) to use the input protection system provided by an input trust authorities (ITA).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imflocalmftregistration"><strong>IMFLocalMFTRegistration</strong></a><br/></td>
<td>Registers Media Foundation transforms (MFTs) in the caller's process.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer"><strong>IMFMediaBuffer</strong></a><br/></td>
<td>Represents a block of memory that contains media data.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengine"><strong>IMFMediaEngine</strong></a><br/></td>
<td>Enables an application to play audio or video files.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineclassfactory"><strong>IMFMediaEngineClassFactory</strong></a><br/></td>
<td>Creates an instance of the Media Engine.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineclassfactory2"><strong>IMFMediaEngineClassFactory2</strong></a><br/></td>
<td>Creates an instance of the <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeys"><strong>IMFMediaKeys</strong></a> object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineclassfactoryex"><strong>IMFMediaEngineClassFactoryEx</strong></a><br/></td>
<td>Extension for the <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineclassfactory"><strong>IMFMediaEngineClassFactory</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineeme"><strong>IMFMediaEngineEME</strong></a><br/></td>
<td>Implemented by the media engine to add encrypted media extensions methods.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineex"><strong>IMFMediaEngineEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengine"><strong>IMFMediaEngine</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineextension"><strong>IMFMediaEngineExtension</strong></a><br/></td>
<td>Enables an application to load media resources in the Media Engine.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineneedkeynotify"><strong>IMFMediaEngineNeedKeyNotify</strong></a><br/></td>
<td>Represents a callback to the media engine to notify key request data.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaenginenotify"><strong>IMFMediaEngineNotify</strong></a><br/></td>
<td>Callback interface for the <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengine"><strong>IMFMediaEngine</strong></a> interface. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineopminfo"><strong>IMFMediaEngineOPMInfo</strong></a><br/></td>
<td>Provides methods for getting information about the <a href="output-protection-manager.md">Output Protection Manager</a> (OPM).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineprotectedcontent"><strong>IMFMediaEngineProtectedContent</strong></a><br/></td>
<td>Enables the Media Engine to play protected video content.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaenginesrcelements"><strong>IMFMediaEngineSrcElements</strong></a><br/></td>
<td>Provides the Media Engine with a list of media resources.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaenginesrcelementsex"><strong>IMFMediaEngineSrcElementsEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaenginesrcelements"><strong>IMFMediaEngineSrcElements</strong></a> interface to provide additional capabilities.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaenginesupportssourcetransfer"><strong>IMFMediaEngineSupportsSourceTransfer</strong></a><br/></td>
<td>Enables the media source to be transferred between the media engine and the sharing engine for Play To.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaenginewebsupport"><strong>IMFMediaEngineWebSupport</strong></a><br/></td>
<td>Enables playback of web audio.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaerror"><strong>IMFMediaError</strong></a><br/></td>
<td>Provides the current error status for the Media Engine.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent"><strong>IMFMediaEvent</strong></a><br/></td>
<td>Represents an event generated by a Media Foundation object. Use this interface to get information about the event.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator"><strong>IMFMediaEventGenerator</strong></a><br/></td>
<td>Retrieves events from any Media Foundation object that generates events. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventqueue"><strong>IMFMediaEventQueue</strong></a><br/></td>
<td>Provides an event queue for applications that need to implement the <a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator"><strong>IMFMediaEventGenerator</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeys"><strong>IMFMediaKeys</strong></a><br/></td>
<td>Represents a media keys used for decrypting media data using a Digital Rights Management (DRM) key system. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeysession"><strong>IMFMediaKeySession</strong></a><br/></td>
<td>Represents a session with the Digital Rights Management (DRM) key system.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeysessionnotify"><strong>IMFMediaKeySessionNotify</strong></a><br/></td>
<td>Provides a mechanism for notifying the app about information regarding the media key session. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasession"><strong>IMFMediaSession</strong></a><br/></td>
<td>Provides playback controls for protected and unprotected content.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfmediasharingengine"><strong>IMFMediaSharingEngine</strong></a><br/></td>
<td>Enables media sharing.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfmediasharingengineclassfactory"><strong>IMFMediaSharingEngineClassFactory</strong></a><br/></td>
<td>Creates an instance of the <a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfmediasharingengine"><strong>IMFMediaSharingEngine</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasink"><strong>IMFMediaSink</strong></a><br/></td>
<td>Implemented by media sink objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasinkpreroll"><strong>IMFMediaSinkPreroll</strong></a><br/></td>
<td>Enables a media sink to receive samples before the presentation clock is started.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasource"><strong>IMFMediaSource</strong></a><br/></td>
<td>Implemented by media source objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasourceex"><strong>IMFMediaSourceEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasource"><strong>IMFMediaSource</strong></a> interface to provide additional capabilities for a media source.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediasourceextension"><strong>IMFMediaSourceExtension</strong></a><br/></td>
<td>Provides functionality for the Media Source Extension (MSE).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediasourceextensionnotify"><strong>IMFMediaSourceExtensionNotify</strong></a><br/></td>
<td>Provides functionality for raising events associated with <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediasourceextension"><strong>IMFMediaSourceExtension</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcepresentationprovider"><strong>IMFMediaSourcePresentationProvider</strong></a><br/></td>
<td>Provides notifications to the sequencer source.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcetopologyprovider"><strong>IMFMediaSourceTopologyProvider</strong></a><br/></td>
<td>Enables an application to get a topology from the sequencer source.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediastream"><strong>IMFMediaStream</strong></a><br/></td>
<td>Represents one stream in a media source. <br/></td>
</tr>
<tr class="odd">
<td><a href="imfmediastreamsourcesamplerequest.md"><strong>IMFMediaStreamSourceSampleRequest</strong></a><br/></td>
<td>Represents a request for a sample from a MediaStreamSource. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediatimerange"><strong>IMFMediaTimeRange</strong></a><br/></td>
<td>Represents a list of time ranges, where each range is defined by a start and end time.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype"><strong>IMFMediaType</strong></a><br/></td>
<td>Represents a description of a media format. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediatypehandler"><strong>IMFMediaTypeHandler</strong></a><br/></td>
<td>Gets and sets media types on an object, such as a media source or media sink. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmetadata"><strong>IMFMetadata</strong></a><br/></td>
<td>Manages metadata for an object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider"><strong>IMFMetadataProvider</strong></a><br/></td>
<td>Gets metadata from a media source or other object.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreamattributesmanager"><strong>IMFMuxStreamAttributesManager</strong></a><br/></td>
<td>Provides access to the <a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes"><strong>IMFAttributes</strong></a> of the substreams of a multiplexed media source.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreamsamplemanager"><strong>IMFMuxStreamSampleManager</strong></a><br/></td>
<td>Provides the ability to retrieve <a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfsample"><strong>IMFSample</strong></a> objects for individual substreams within the output of a multiplexed media source.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreammediatypemanager"><strong>IMFMuxStreamMediaTypeManager</strong></a><br/></td>
<td>Enables the management of stream configurations for a multiplexed media source. A stream configuration defines a set of substreams that can be included the multiplexed output.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetcredential"><strong>IMFNetCredential</strong></a><br/></td>
<td>Sets and retrieves user-name and password information for authentication purposes. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialcache"><strong>IMFNetCredentialCache</strong></a><br/></td>
<td>Gets credentials from the credential cache.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialmanager"><strong>IMFNetCredentialManager</strong></a><br/></td>
<td>Implemented by applications to provide user credentials for a network source.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetcrossoriginsupport"><strong>IMFNetCrossOriginSupport</strong></a><br/></td>
<td>Implemented by clients that want to enforce a cross origin policy for HTML5 media downloads. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetproxylocator"><strong>IMFNetProxyLocator</strong></a><br/></td>
<td>Determines the proxy to use when connecting to a server.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetproxylocatorfactory"><strong>IMFNetProxyLocatorFactory</strong></a><br/></td>
<td>Creates a proxy locator object, which determines the proxy to use.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetresourcefilter"><strong>IMFNetResourceFilter</strong></a><br/></td>
<td>Notifies the application when a byte stream requests a URL, and enables the application to block URL redirection.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfnetschemehandlerconfig"><strong>IMFNetSchemeHandlerConfig</strong></a><br/></td>
<td>Configures a network scheme plug-in. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfobjectreferencestream"><strong>IMFObjectReferenceStream</strong></a><br/></td>
<td>Marshals an interface pointer to and from a stream. <br/> Stream objects that support <strong>IStream</strong> can expose this interface to provide custom marshaling for interface pointers.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfoutputpolicy"><strong>IMFOutputPolicy</strong></a><br/></td>
<td>Encapsulates a usage policy from an input trust authority (ITA).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfoutputschema"><strong>IMFOutputSchema</strong></a><br/></td>
<td>Encapsulates information about an output protection system and its corresponding configuration data.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfoutputtrustauthority"><strong>IMFOutputTrustAuthority</strong></a><br/></td>
<td>Encapsulates the functionality of one or more output protection systems that a trusted output supports.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfplugincontrol"><strong>IMFPluginControl</strong></a><br/></td>
<td>Controls how media sources and transforms are enumerated in Media Foundation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfplugincontrol2"><strong>IMFPluginControl2</strong></a><br/></td>
<td>Controls how media sources and transforms are enumerated in Media Foundation.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfplay/nn-mfplay-imfpmediaitem"><strong>IMFPMediaItem</strong></a><br/></td>
<td>Represents a media item. (Deprecated.)<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayer"><strong>IMFPMediaPlayer</strong></a><br/></td>
<td>Contains methods to play media files. (Deprecated.)<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayercallback"><strong>IMFPMediaPlayerCallback</strong></a><br/></td>
<td>Callback interface for the <a href="/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayer"><strong>IMFPMediaPlayer</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpmpclient"><strong>IMFPMPClient</strong></a><br/></td>
<td>Enables a media source to receive a pointer to the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfpmphost"><strong>IMFPMPHost</strong></a> interface. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpmpclientapp"><strong>IMFPMPClientApp</strong></a><br/></td>
<td>Provides a mechanism for a media source to implement content protection functionality in a Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpmphost"><strong>IMFPMPHost</strong></a><br/></td>
<td>Enables a media source in the application process to create objects in the protected media path (PMP) process.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpmphostapp"><strong>IMFPMPHostApp</strong></a><br/></td>
<td>Allows a media source to create a <a href="/windows/desktop/WinRT/reference">Windows Runtime</a> object in the <a href="protected-media-path.md">Protected Media Path</a> (PMP) process. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpmpserver"><strong>IMFPMPServer</strong></a><br/></td>
<td>Enables two instances of the <a href="media-session.md">Media Session</a> to share the same protected media path (PMP) process. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpresentationclock"><strong>IMFPresentationClock</strong></a><br/></td>
<td>Represents a presentation clock, which is used to schedule when samples are rendered and to synchronize multiple streams.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor"><strong>IMFPresentationDescriptor</strong></a><br/></td>
<td>Describes the details of a presentation. A <em>presentation</em> is a set of related media streams that share a common presentation time. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfpresentationtimesource"><strong>IMFPresentationTimeSource</strong></a><br/></td>
<td>Provides the clock times for the presentation clock. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfprotectedenvironmentaccess"><strong>IMFProtectedEnvironmentAccess</strong></a><br/></td>
<td>Provides a method that allows content protection systems to perform a handshake with the protected environment. This is needed because the <strong>CreateFile</strong> and <strong>DeviceIoControl</strong> APIs are not available to Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise"><strong>IMFQualityAdvise</strong></a><br/></td>
<td>Enables the quality manager to adjust the audio or video quality of a component in the pipeline.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2"><strong>IMFQualityAdvise2</strong></a><br/></td>
<td>Enables a pipeline object to adjust its own audio or video quality, in response to quality messages.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfqualityadviselimits"><strong>IMFQualityAdviseLimits</strong></a><br/></td>
<td>Queries an object for the number of <em>quality modes</em> it supports.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfqualitymanager"><strong>IMFQualityManager</strong></a><br/></td>
<td>Adjusts playback quality. This interface is exposed by the quality manager. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol"><strong>IMFRateControl</strong></a><br/></td>
<td>Gets or sets the playback rate. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfratesupport"><strong>IMFRateSupport</strong></a><br/></td>
<td>Queries the range of playback rates that are supported, including reverse playback.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfreadwriteclassfactory"><strong>IMFReadWriteClassFactory</strong></a><br/></td>
<td>Creates an instance of either the sink writer or the source reader.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient"><strong>IMFRealTimeClient</strong></a><br/></td>
<td>Notifies a pipeline object to register itself with the Multimedia Class Scheduler Service (MMCSS).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclientex"><strong>IMFRealTimeClientEx</strong></a><br/></td>
<td>Notifies a pipeline object to register itself with the Multimedia Class Scheduler Service (MMCSS). <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfremoteasynccallback"><strong>IMFRemoteAsyncCallback</strong></a><br/></td>
<td>Used by the Media Foundation proxy/stub DLL to marshal certain asynchronous method calls across process boundaries.<br/> Applications do not use or implement this interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfremotedesktopplugin"><strong>IMFRemoteDesktopPlugin</strong></a><br/></td>
<td>Modifies a topology for use in a Terminal Services environment. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfremoteproxy"><strong>IMFRemoteProxy</strong></a><br/></td>
<td>Exposed by objects that act as a proxy for a remote object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsamistyle"><strong>IMFSAMIStyle</strong></a><br/></td>
<td>Sets and retrieves Synchronized Accessible Media Interchange (SAMI) styles on the <a href="sami-media-source.md">SAMI Media Source</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfsample"><strong>IMFSample</strong></a><br/></td>
<td>Represents a media sample, which is a container object for media data.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsamplegrabbersinkcallback"><strong>IMFSampleGrabberSinkCallback</strong></a><br/></td>
<td>Callback interface to get media data from the sample-grabber sink. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsamplegrabbersinkcallback2"><strong>IMFSampleGrabberSinkCallback2</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfsamplegrabbersinkcallback"><strong>IMFSampleGrabberSinkCallback</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfsampleoutputstream"><strong>IMFSampleOutputStream</strong></a><br/></td>
<td>Writes media samples to a byte stream.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsampleprotection"><strong>IMFSampleProtection</strong></a><br/></td>
<td>Provides encryption for media data inside the protected media path (PMP). <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsavejob"><strong>IMFSaveJob</strong></a><br/></td>
<td>Persists media data from a source byte stream to an application-provided byte stream.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfschemehandler"><strong>IMFSchemeHandler</strong></a><br/></td>
<td>Creates a media source or a byte stream from a URL. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsecurechannel"><strong>IMFSecureChannel</strong></a><br/></td>
<td>Establishes a one-way secure channel between two objects. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfseekinfo"><strong>IMFSeekInfo</strong></a><br/></td>
<td>For a particular seek position, gets the two nearest key frames.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensoractivitiesreport"><strong>IMFSensorActivitiesReport</strong></a><br/></td>
<td>Provides access to <a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensoractivityreport"><strong>IMFSensorActivityReport</strong></a> objects that describe the current activity of a sensor.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensoractivitiesreportcallback"><strong>IMFSensorActivitiesReportCallback</strong></a><br/></td>
<td>Interface implemented by the client to receive callbacks when sensor activity reports are available.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensoractivitymonitor"><strong>IMFSensorActivityMonitor</strong></a><br/></td>
<td>Provides methods for controlling a sensor activity monitor.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensoractivityreport"><strong>IMFSensorActivityReport</strong></a><br/></td>
<td>Represents an activity report for a sensor.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensordevice"><strong>IMFSensorDevice</strong></a><br/></td>
<td>Represents a sensor device that can belong to a sensor group, which is represented by the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensorgroup"><strong>IMFSensorGroup</strong></a> interface. The term &quot;device&quot; in this context could refer to a physical device, a custom media source, or a frame provider.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensorgroup"><strong>IMFSensorGroup</strong></a><br/></td>
<td>Represents a group of sensor devices from which an <a href="/windows/desktop/api/mfidl/nn-mfidl-imfmediasource"><strong>IMFMediaSource</strong></a> can be created. The term &quot;device&quot; in this context could refer to a physical device, a custom media source, or a frame provider. A sensor group may actually contain multiple sensor devices, or it could contain only a single device, but it still behaves as a sensor group.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensorprocessactivity"><strong>IMFSensorProcessActivity</strong></a><br/></td>
<td>Represents the activity of a process associated with a sensor.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensorprofilecollection"><strong>IMFSensorProfileCollection</strong></a><br/></td>
<td>Contains a collection of media foundation sensor profile objects.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensorprofile"><strong>IMFSensorProfile</strong></a><br/></td>
<td>Describes a media foundation sensor profile.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensorstream"><strong>IMFSensorStream</strong></a><br/></td>

</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsensortransformfactory"><strong>IMFSensorTransformFactory</strong></a><br/></td>
<td>The interface implemented by sensor transforms to allow the media pipeline to query requirements of the sensor transform and to create a runtime instance of the sensor transform.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsequencersource"><strong>IMFSequencerSource</strong></a><br/></td>
<td>Implemented by the <a href="sequencer-source.md">Sequencer Source</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-imfsharingengineclassfactory"><strong>IMFSharingEngineClassFactory</strong></a><br/></td>
<td>Creates an instance of the media sharing engine.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfshutdown"><strong>IMFShutdown</strong></a><br/></td>
<td>Exposed by some Media Foundation objects that must be explicitly shut down. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsignedlibrary"><strong>IMFSignedLibrary</strong></a><br/></td>
<td>Provides a method that allows content protection systems to get the procedure address of a function in the signed library. This method provides the same functionality as <strong>GetProcAddress</strong> which is not available to Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsimpleaudiovolume"><strong>IMFSimpleAudioVolume</strong></a><br/></td>
<td>Controls the master volume level of the audio session associated with the streaming audio renderer (SAR) and the audio capture source.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriter"><strong>IMFSinkWriter</strong></a><br/></td>
<td>Implemented by the Media Foundation sink writer object.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback"><strong>IMFSinkWriterCallback</strong></a><br/></td>
<td>Callback interface for the Media Foundation sink writer. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback2"><strong>IMFSinkWriterCallback2</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback"><strong>IMFSinkWriterCallback</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriterencoderconfig"><strong>IMFSinkWriterEncoderConfig</strong></a><br/></td>
<td>Provides additional functionality on the sink writer for dynamically changing the media type and encoder configuration. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriterex"><strong>IMFSinkWriterEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriter"><strong>IMFSinkWriter</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffer"><strong>IMFSourceBuffer</strong></a><br/></td>
<td>Represents a buffer which contains media data for a <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediasourceextension"><strong>IMFMediaSourceExtension</strong></a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebufferlist"><strong>IMFSourceBufferList</strong></a><br/></td>
<td>Represents a collection of <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffer"><strong>IMFSourceBuffer</strong></a> objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffernotify"><strong>IMFSourceBufferNotify</strong></a><br/></td>
<td>Provides functionality for raising events associated with <a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffer"><strong>IMFSourceBuffer</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsourceopenmonitor"><strong>IMFSourceOpenMonitor</strong></a><br/></td>
<td>Callback interface to receive notifications from a network source on the progress of an asynchronous open operation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereader"><strong>IMFSourceReader</strong></a><br/></td>
<td>Implemented by the Media Foundation source reader object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback"><strong>IMFSourceReaderCallback</strong></a><br/></td>
<td>Callback interface for the Media Foundation source reader.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback2"><strong>IMFSourceReaderCallback2</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback"><strong>IMFSourceReaderCallback</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereaderex"><strong>IMFSourceReaderEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereader"><strong>IMFSourceReader</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsourceresolver"><strong>IMFSourceResolver</strong></a><br/></td>
<td>Creates a media source from a URL or a byte stream.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudioobjectbuffer"><strong>IMFSpatialAudioObjectBuffer</strong></a><br/></td>
<td>Represents a section of audio data with associated positional and rendering metadata. Spatial audio objects are stored in <a href="/windows/desktop/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudiosample"><strong>IMFSpatialAudioSample</strong></a> instances, and allow passing of spatial audio information between Media Foundation components.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudiosample"><strong>IMFSpatialAudioSample</strong></a><br/></td>
<td>Represents a multimedia sample with spatial sound information. Every <a href="/windows/desktop/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudiosample"><strong>IMFSpatialAudioSample</strong></a> contains one or more <a href="/windows/desktop/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudioobjectbuffer"><strong>IMFSpatialAudioObjectBuffer</strong></a> objects.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsslcertificatemanager"><strong>IMFSSLCertificateManager</strong></a><br/></td>
<td>Implemented by a client and called by Media Foundation to get the client Secure Sockets Layer (SSL) certificate requested by the server. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor"><strong>IMFStreamDescriptor</strong></a><br/></td>
<td>Gets information about one stream in a media source. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfstreamingsinkconfig"><strong>IMFStreamingSinkConfig</strong></a><br/></td>
<td>Passes configuration information to the media sinks that are used for streaming the content.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfstreamsink"><strong>IMFStreamSink</strong></a><br/></td>
<td>Represents a stream on a media sink object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfsystemid"><strong>IMFSystemId</strong></a><br/></td>
<td>Provides a method that retireves system id data.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftimecodetranslate"><strong>IMFTimecodeTranslate</strong></a><br/></td>
<td>Converts between Society of Motion Picture and Television Engineers (SMPTE) time codes and 100-nanosecond time units.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtext"><strong>IMFTimedText</strong></a><br/></td>
<td>A timed-text object represents a component of timed text.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtextbinary"><strong>IMFTimedTextBinary</strong></a><br/></td>
<td>Represents the data content of a timed-text object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtextcue"><strong>IMFTimedTextCue</strong></a><br/></td>
<td>Represents the timed-text-cue object. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtextformattedtext"><strong>IMFTimedTextFormattedText</strong></a><br/></td>
<td>Represents a block of formatted timed-text.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtextnotify"><strong>IMFTimedTextNotify</strong></a><br/></td>
<td>Interface that defines callbacks for Media Foundation Timed Text notifications.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtextregion"><strong>IMFTimedTextRegion</strong></a><br/></td>
<td>Represents the display region of a timed-text object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtextstyle"><strong>IMFTimedTextStyle</strong></a><br/></td>
<td>Represents the style for timed text.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtexttrack"><strong>IMFTimedTextTrack</strong></a><br/></td>
<td>Represents a track of timed text.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imftimedtexttracklist"><strong>IMFTimedTextTrackList</strong></a><br/></td>
<td>Represents a list of timed-text tracks.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftimer"><strong>IMFTimer</strong></a><br/></td>
<td>Provides a timer that invokes a callback at a specified time.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftopoloader"><strong>IMFTopoLoader</strong></a><br/></td>
<td>Converts a partial topology into a full topology.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftopology"><strong>IMFTopology</strong></a><br/></td>
<td>Represents a topology. A <em>topology</em> describes a collection of media sources, sinks, and transforms that are connected in a certain order.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftopologynode"><strong>IMFTopologyNode</strong></a><br/></td>
<td>Represents a node in a topology.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftopologynodeattributeeditor"><strong>IMFTopologyNodeAttributeEditor</strong></a><br/></td>
<td>Updates the attributes of one or more nodes in the Media Session's current topology.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr/nn-evr-imftopologyservicelookup"><strong>IMFTopologyServiceLookup</strong></a><br/></td>
<td>Enables a custom video mixer or video presenter to get interface pointers from the <a href="enhanced-video-renderer.md">Enhanced Video Renderer</a> (EVR).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-imftopologyservicelookupclient"><strong>IMFTopologyServiceLookupClient</strong></a><br/></td>
<td>Initializes a video mixer or presenter.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftrackedsample"><strong>IMFTrackedSample</strong></a><br/></td>
<td>Tracks the reference counts on a video media sample.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftranscodeprofile"><strong>IMFTranscodeProfile</strong></a><br/></td>
<td>Implemented by the transcode profile object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftranscodesinkinfoprovider"><strong>IMFTranscodeSinkInfoProvider</strong></a><br/></td>
<td>Implemented by the transcode sink activation object.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mftransform/nn-mftransform-imftransform"><strong>IMFTransform</strong></a><br/></td>
<td>Implemented by all <a href="media-foundation-transforms.md">Media Foundation Transforms</a> (MFTs).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftrustedinput"><strong>IMFTrustedInput</strong></a><br/></td>
<td>Implemented by components that provide input trust authorities (ITAs). This interface is used to get the ITA for each of the component's streams. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imftrustedoutput"><strong>IMFTrustedOutput</strong></a><br/></td>
<td>Implemented by components that provide output trust authorities (OTAs).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideodeviceid"><strong>IMFVideoDeviceID</strong></a><br/></td>
<td>Returns the device identifier supported by a video renderer component.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol"><strong>IMFVideoDisplayControl</strong></a><br/></td>
<td>Controls how the <a href="enhanced-video-renderer.md">Enhanced Video Renderer</a> (EVR) displays video.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfobjects/nn-mfobjects-imfvideomediatype"><strong>IMFVideoMediaType</strong></a><br/></td>
<td>Represents a description of a video format.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr9/nn-evr9-imfvideomixerbitmap"><strong>IMFVideoMixerBitmap</strong></a><br/></td>
<td>Alpha-blends a static bitmap image with the video displayed by the <a href="enhanced-video-renderer.md">Enhanced Video Renderer</a> (EVR).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideomixercontrol"><strong>IMFVideoMixerControl</strong></a><br/></td>
<td>Controls how the <a href="enhanced-video-renderer.md">Enhanced Video Renderer</a> (EVR) mixes video substreams.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideomixercontrol2"><strong>IMFVideoMixerControl2</strong></a><br/></td>
<td>Controls preferences for video deinterlacing.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideopositionmapper"><strong>IMFVideoPositionMapper</strong></a><br/></td>
<td>Maps a position on an input video stream to the corresponding position on an output video stream.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideopresenter"><strong>IMFVideoPresenter</strong></a><br/></td>
<td>Represents a video presenter. A <em>video presenter</em> is an object that receives video frames, typically from a video mixer, and presents them in some way, typically by rendering them to the display.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/evr9/nn-evr9-imfvideoprocessor"><strong>IMFVideoProcessor</strong></a><br/></td>
<td>Controls video processing in the <a href="enhanced-video-renderer.md">Enhanced Video Renderer</a> (EVR).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideoprocessorcontrol"><strong>IMFVideoProcessorControl</strong></a><br/></td>
<td>Configures the <a href="video-processor-mft.md"><strong>Video Processor MFT</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideoprocessorcontrol2"><strong>IMFVideoProcessorControl2</strong></a><br/></td>
<td>Configures the <a href="video-processor-mft.md"><strong>Video Processor MFT</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/evr/nn-evr-imfvideorenderer"><strong>IMFVideoRenderer</strong></a><br/></td>
<td>Sets a new mixer or presenter for the <a href="enhanced-video-renderer.md">Enhanced Video Renderer</a> (EVR).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocator"><strong>IMFVideoSampleAllocator</strong></a><br/></td>
<td>Allocates video samples for a video media sink.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorcallback"><strong>IMFVideoSampleAllocatorCallback</strong></a><br/></td>
<td>Enables an application to track video samples allocated by the enhanced video renderer (EVR).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorex"><strong>IMFVideoSampleAllocatorEx</strong></a><br/></td>
<td>Allocates video samples that contain Direct3D 11 texture surfaces.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatornotify"><strong>IMFVideoSampleAllocatorNotify</strong></a><br/></td>
<td>The callback for the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorcallback"><strong>IMFVideoSampleAllocatorCallback</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatornotifyex"><strong>IMFVideoSampleAllocatorNotifyEx</strong></a><br/></td>
<td>The callback for the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorcallback"><strong>IMFVideoSampleAllocatorCallback</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfworkqueueservices"><strong>IMFWorkQueueServices</strong></a><br/></td>
<td>Controls the work queues created by the <a href="media-session.md">Media Session</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfworkqueueservicesex"><strong>IMFWorkQueueServicesEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfworkqueueservices"><strong>IMFWorkQueueServices</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-iplaytocontrol"><strong>IPlayToControl</strong></a><br/></td>
<td>Enables the <strong>PlayToConnection</strong> object to connect to a media element.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-iplaytocontrolwithcapabilities"><strong>IPlayToControlWithCapabilities</strong></a><br/></td>
<td>Provides functionality for the <a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-iplaytosourceclassfactory"><strong>IPlayToSource</strong></a> to determine the capabilities of the content.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/mfsharingengine/nn-mfsharingengine-iplaytosourceclassfactory"><strong>IPlayToSourceClassFactory</strong></a><br/></td>
<td>Creates an instance of the <a href="/uwp/api/Windows.Media.PlayTo.PlayToSource"><strong>PlayToSource</strong></a> object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecleakybucket"><strong>IWMCodecLeakyBucket</strong></a><br/></td>
<td>Configures the &quot;leaky bucket&quot; parameters on a video encoder.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecoutputtimestamp"><strong>IWMCodecOutputTimestamp</strong></a><br/></td>
<td>Gets the time stamp of the next video frame to be decoded.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecprivatedata"><strong>IWMCodecPrivateData</strong></a><br/></td>
<td>Gets the private codec data that must be appended to the output media type. This codec data is required for properly decoding Windows Media Video content.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecprops"><strong>IWMCodecProps</strong></a><br/></td>
<td>Provides methods that retrieve format-specific codec properties.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecstrings"><strong>IWMCodecStrings</strong></a><br/></td>
<td>Retrieves names and descriptive strings for codecs and formats.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcolorconvprops"><strong>IWMColorConvProps</strong></a><br/></td>
<td>Sets properties on the color converter DSP. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmresamplerprops"><strong>IWMResamplerProps</strong></a><br/></td>
<td>Sets properties on the audio resampler DSP. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmresizerprops"><strong>IWMResizerProps</strong></a><br/></td>
<td>Sets properties on the video resizer DSP.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmsampleextensionsupport"><strong>IWMSampleExtensionSupport</strong></a><br/></td>
<td>Configures codec support for sample extensions. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmvideodecoderhurryup"><strong>IWMVideoDecoderHurryup</strong></a><br/></td>
<td>Controls the speed of the video decoder.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmvideodecoderreconbuffer"><strong>IWMVideoDecoderReconBuffer</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
This interface is obsolete and should not be used.
</blockquote>
<br/> Manages reconstructed video frames.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmvideoforcekeyframe"><strong>IWMVideoForceKeyFrame</strong></a><br/></td>
<td>Forces the encoder to encode the current frame as a key frame. <br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Media Foundation Programming Reference](media-foundation-programming-reference.md)
</dt> </dl>

 

 
