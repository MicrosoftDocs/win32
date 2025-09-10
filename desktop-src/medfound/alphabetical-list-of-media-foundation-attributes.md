---
description: This section contains an alphabetical list of Microsoft Media Foundation.
ms.assetid: 386ecdb9-dde5-470e-9ae8-d2e0acc065b1
title: Alphabetical List of Media Foundation Attributes
ms.topic: reference
ms.date: 05/31/2018
---

# Alphabetical List of Media Foundation Attributes

This section contains an alphabetical list of Microsoft Media Foundation attributes.

## In this section



| Topic                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EVRConfig\_AllowBatching](evrconfig-allowbatching.md) | Allows the Enhanced Video Renderer (EVR) to batch calls to the Microsoft Direct3D **IDirect3DDevice9::Present** method. |
| [EVRConfig\_AllowDropToBob](evrconfig-allowdroptobob.md) | Allows the EVR to improve performance by using bob deinterlacing. |
| [EVRConfig\_AllowDropToHalfInterlace](evrconfig-allowdroptohalfinterlace.md) | Allows the EVR to improve performance by skipping the second field of every interlaced frame. |
| [EVRConfig\_AllowDropToThrottle](evrconfig-allowdroptothrottle.md) | Allows the EVR to limit its output to match GPU bandwidth. |
| [EVRConfig\_AllowScaling](evrconfig-allowscaling.md) | Allows the EVR to mix the video within a rectangle that is smaller than the output rectangle, and then scale the result. |
| [EVRConfig\_ForceBatching](evrconfig-forcebatching.md) | Forces the EVR to batch calls to the [**IDirect3D9Device::Present**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-present) method. |
| [EVRConfig\_ForceBob](evrconfig-forcebob.md) | Forces the EVR to use bob deinterlacing. |
| [EVRConfig\_ForceHalfInterlace](evrconfig-forcehalfinterlace.md) | Forces the EVR to skip the second field of every interlaced frame. |
| [EVRConfig\_ForceScaling](evrconfig-forcescaling.md) | Forces the EVR to mix the video within a rectangle that is smaller than the output rectangle, and then scale the result. |
| [EVRConfig\_ForceThrottle](evrconfig-forcethrottle.md) | Forces the EVR to limit its output to match GPU bandwidth. |
| [MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE](mf-activate-custom-video-mixer-activate-attribute.md) | Specifies an activation object that creates a custom video mixer for the enhanced video renderer (EVR) media sink.  |
| [MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID](mf-activate-custom-video-mixer-clsid-attribute.md) | CLSID of a custom video mixer for the enhanced video renderer (EVR) media sink.  |
| [MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_FLAGS](mf-activate-custom-video-mixer-flags-attribute.md) | Specifies how to create a custom mixer for the enhanced video renderer (EVR).  |
| [MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_ACTIVATE](mf-activate-custom-video-presenter-activate-attribute.md) | Specifies an activation object that creates a custom video presenter for the enhanced video renderer (EVR) media sink.  |
| [MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_CLSID](mf-activate-custom-video-presenter-clsid-attribute.md) | CLSID of a custom video presenter for the enhanced video renderer (EVR) media sink.  |
| [MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_FLAGS](mf-activate-custom-video-presenter-flags-attribute.md) | Specifies how to create a custom presenter for the enhanced video renderer (EVR).  |
| [MF\_ACTIVATE\_MFT\_LOCKED](mf-activate-mft-locked-attribute.md) | Specifies whether the Topology Loader will change the media types on a Media Foundation transform (MFT). Applications typically do not use this attribute.  |
| [MF\_ACTIVATE\_VIDEO\_WINDOW](mf-activate-video-window-attribute.md) | Handle to the video clipping window.  |
| [MF\_ASFPROFILE\_MAXPACKETSIZE](mf-asfprofile-maxpacketsize-attribute.md) | Specifies the maximum packet size for an ASF file, in bytes.  |
| [MF\_ASFPROFILE\_MINPACKETSIZE](mf-asfprofile-minpacketsize-attribute.md) | Specifies the minimum packet size for an ASF file, in bytes.  |
| [MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1](mf-asfstreamconfig-leakybucket1-attribute.md) | Sets the average "leaky bucket" parameters (see Remarks) for encoding a Windows Media file. Set this attribute by using the [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) interface.  |
| [MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2](mf-asfstreamconfig-leakybucket2-attribute.md) | Sets the peak "leaky bucket" parameters (see Remarks) for encoding a Windows Media file. These parameters are used for the peak bit rate. Set this attribute by using the [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) interface.  |
| [MF\_AUDIO\_RENDERER\_ATTRIBUTE\_ENDPOINT\_ID](mf-audio-renderer-attribute-endpoint-id-attribute.md) | Specifies the identifier for the audio endpoint device.  |
| [MF\_AUDIO\_RENDERER\_ATTRIBUTE\_ENDPOINT\_ROLE](mf-audio-renderer-attribute-endpoint-role-attribute.md) | Specifies the audio endpoint role for the audio renderer.  |
| [MF\_AUDIO\_RENDERER\_ATTRIBUTE\_FLAGS](mf-audio-renderer-attribute-flags-attribute.md) | Contains flags to configure the audio renderer.  |
| [MF\_AUDIO\_RENDERER\_ATTRIBUTE\_SESSION\_ID](mf-audio-renderer-attribute-session-id-attribute.md) | Specifies the audio policy class for the audio renderer.  |
| [MF\_AUDIO\_RENDERER\_ATTRIBUTE\_STREAM\_CATEGORY](mf-audio-renderer-attribute-stream-category.md) | Specifies the audio stream category for the [Streaming Audio Renderer](streaming-audio-renderer.md) (SAR). |
| [MF\_BYTESTREAM\_CONTENT\_TYPE](mf-bytestream-content-type-attribute.md) | Specifies the MIME type of a byte stream.  |
| [MF\_BYTESTREAM\_DURATION](mf-bytestream-duration-attribute.md) | Specifies the duration of a byte stream, in 100-nanosecond units.  |
| [MF\_BYTESTREAM\_EFFECTIVE\_URL](mf-bytestream-effective-url.md) | Gets the effective URL of a byte stream. |
| [MF\_BYTESTREAM\_IFO\_FILE\_URI](mf-bytestream-ifo-file-uri.md) | Contains the URL of the IFO (DVD Information) file specified by the HTTP server in the HTTP header, "Pragma: ifoFileURI.dlna.org".  |
| [MF\_BYTESTREAM\_LAST\_MODIFIED\_TIME](mf-bytestream-last-modified-time-attribute.md) | Specifies when a byte stream was last modified.  |
| [MF\_BYTESTREAM\_ORIGIN\_NAME](mf-bytestream-origin-name-attribute.md) | Specifies the original URL for a byte stream.  |
| [MF\_BYTESTREAMHANDLER\_ACCEPTS\_SHARE\_WRITE](mf-bytestreamhandler-accepts-share-write.md) | Specifies whether a byte-stream handler can use a byte stream that is opened for writing by another thread. |
| [MF\_CAPTURE\_ENGINE\_CAMERA\_STREAM\_BLOCKED](mf-capture-engine-camera-stream-blocked.md) | Signals that video capture is being blocked by the driver. |
| [MF\_CAPTURE\_ENGINE\_CAMERA\_STREAM\_UNBLOCKED](mf-capture-engine-camera-stream-unblocked.md) | Signals that video capture is restored after being blocked. |
| [MF\_CAPTURE\_ENGINE\_D3D\_MANAGER Attribute](mf-capture-engine-d3d-manager.md) | Sets a pointer to the DXGI Device Manager on the capture engine. |
| [MF\_CAPTURE\_ENGINE\_DECODER\_MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mf-capture-engine-decoder-mft-fieldofuse-unlock-attribute.md) | Enables the capture engine to use a decoder that has field-of-use restrictions. |
| [MF\_CAPTURE\_ENGINE\_DISABLE\_DXVA Attribute](mf-capture-engine-disable-dxva.md) | Specifies whether the capture engine uses DirectX Video Acceleration (DXVA) for video decoding. |
| [MF\_CAPTURE\_ENGINE\_DISABLE\_HARDWARE\_TRANSFORMS Attribute](mf-capture-engine-disable-hardware-transforms.md) | Disables the use of hardware-based Media Foundation transforms (MFTs) in the capture engine.  |
| [MF\_CAPTURE\_ENGINE\_ENABLE\_CAMERA\_STREAMSTATE\_NOTIFICATION](mf-capture-engine-enable-camera-streamstate-notification.md) | Indicates whether stream state notifications should be enabled. |
| [MF\_CAPTURE\_ENGINE\_ENCODER\_MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mf-capture-engine-encoder-mft-fieldofuse-unlock-attribute.md) | Enables the capture engine to use an encoder that has field-of-use restrictions.  |
| [MF\_CAPTURE\_ENGINE\_EVENT\_GENERATOR\_GUID Attribute](mf-capture-engine-event-generator-guid.md) | Identifies the component that generated a capture event. |
| [MF\_CAPTURE\_ENGINE\_EVENT\_STREAM\_INDEX Attribute](mf-capture-engine-event-stream-index.md) | Identifies which stream generated a capture event. |
| [MF\_CAPTURE\_ENGINE\_MEDIASOURCE\_CONFIG Attribute](mf-capture-engine-mediasource-config.md) | Contains configuration properties for the capture source. |
| [MF\_CAPTURE\_ENGINE\_OUTPUT\_MEDIA\_TYPE\_SET](mf-capture-engine-output-media-type-set.md) | Indicates that the output type has been set on the capture engine in response to [**IMFCaptureSink2::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype). |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_PROCESSED\_SAMPLES Attribute](mf-capture-engine-record-sink-audio-max-processed-samples.md) | Sets the maximum number of processed samples that can be buffered in the record sink audio path.  |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_UNPROCESSED\_SAMPLES Attribute](mf-capture-engine-record-sink-audio-max-unprocessed-samples.md) | Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink audio path.  |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_PROCESSED\_SAMPLES Attribute](mf-capture-engine-record-sink-video-max-processed-samples.md) | Sets the maximum number of processed samples that can be buffered in the record sink video path.  |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_UNPROCESSED\_SAMPLES Attribute](mf-capture-engine-record-sink-video-max-unprocessed-samples.md) | Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink video path. |
| [MF\_CAPTURE\_ENGINE\_USE\_AUDIO\_DEVICE\_ONLY Attribute](mf-capture-engine-use-audio-device-only.md) | Specifies whether the capture engine captures audio but not video. |
| [MF\_CAPTURE\_ENGINE\_USE\_VIDEO\_DEVICE\_ONLY Attribute](mf-capture-engine-use-video-device-only.md) | Specifies whether the capture engine captures video but not audio. |
| [MF\_CAPTURE\_METADATA\_FRAME\_BACKGROUND\_MASK](mf-capture-metadata-frame-background-mask.md) | Reports the metadata and mask buffer for a background segmentation mask that distinguishes between the background and foreground of a video frame. |
| [MF\_CAPTURE\_METADATA\_FRAME\_ILLUMINATION](mf-capture-metadata-frame-illumination.md) | A value indicating whether a frame was captured using active infrared (IR) illumination. |
| [MF\_CAPTURE\_METADATA\_PHOTO\_FRAME\_FLASH](mf-capture-metadata-photo-frame-flash.md) | Indicates if a flash was triggered for the captured frame. |
| [MF\_DEVICE\_THERMAL\_STATE\_CHANGED](mf-device-thermal-state-changed.md) | Represents an event that signals a thermal state change in the device.  |
| [MF\_DECODER\_FWD\_CUSTOM\_SEI\_DECODE\_ORDER](mf-decoder-fwd-custom-set-decode-order.md) | Specifies that the SEI unit type to forward on output samples of the decoder shall be sent out in decode order. |
| [MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES](mf-devicestream-attribute-framesource-types.md) | Represents the frame source type. |
| [MF\_DEVICESTREAM\_EXTENSION\_PLUGIN\_CONNECTION\_POINT](mf-devicestream-extension-plugin-connection-point.md) | Represents a extension plugin connection point. |
| [MF\_DEVICESTREAM\_EXTENSION\_PLUGIN\_CLSID](mf-devicestream-extension-plugin-clsid.md) | Specifies the CLSID of a post-processing plug-in for a video capture device. |
| [MF\_DEVICESTREAM\_FRAMESERVER\_HIDDEN](mf-devicestream-frameserver-hidden.md) | This attribute, when set on a stream, marks the stream as being hidden from the client. |
| [MF\_DEVICESTREAM\_FRAMESERVER\_SHARED](mf-devicestream-frameserver-shared.md) | This attribute, when set on a stream, explicitly marks the stream as shared by the frame server. |
| [MF\_DEVICESTREAM\_IMAGE\_STREAM](mf-devicestream-image-stream.md) | Specifies whether a stream on a video capture source is a still-image stream. |
| [MF\_DEVICESTREAM\_INDEPENDENT\_IMAGE\_STREAM](mf-devicestream-independent-image-stream.md) | Specifies whether the image stream on a video capture source is independent of the video stream. |
| [MF\_DEVICESTREAM\_MAX\_FRAME\_BUFFERS](mf-devicestream-max-frame-buffers.md) | Specifies the maximum number of frames that the video capture source will buffer for this stream. |
| [MF\_DEVICESTREAM\_MULTIPLEXED\_MANAGER](mf-devicestream-multiplexed-manager.md) | Provides an instance of [**IMFMuxStreamAttributesManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreamattributesmanager) which manages the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) describing the substreams of a multiplexed media source. |
| [MF\_DEVICESTREAM\_REQUIRED\_CAPABILITIES](mf-devicestream-required-capabilities.md) | Specifies a list of unicode strings representing the device capabilities required by the sensor transform. |
| [MF\_DEVICESTREAM\_STREAM\_CATEGORY](mf-devicestream-stream-category.md) | Represents the stream category. |
| [MF\_DEVICESTREAM\_STREAM\_ID](mf-devicestream-stream-id.md) | Specifies the kernel streaming (KS) identifier for a stream on a video capture device. |
| [MF\_DEVICESTREAM\_TAKEPHOTO\_TRIGGER](mf-devicestream-takephoto-trigger.md) | Specifies if the take photo trigger is encapsulated into the device source. |
| [MF\_DEVICESTREAM\_TRANSFORM\_STREAM\_ID](mf-devicestream-transform-stream-id.md) | Represents the Media Foundation Transform (MFT) stream id of the stream. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_ENABLE\_MS\_CAMERA\_EFFECTS](mf-devsource-attribute-enable-ms-camera-effects.md) | Specifies whether Windows Camera Effects are enabled for a capture device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_FRAMESERVER\_SHARE\_MODE](mf-devsource-attribute-frameserver-share-mode.md) | Configures a camera device source represented by an instance of [IMFMEdiaSource](/windows/win32/api/mfidl/nn-mfidl-imfmediasource) to be in either controlling mode or sharing mode. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_FRIENDLY\_NAME](mf-devsource-attribute-friendly-name.md) | Specifies the display name for a device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_MEDIA\_TYPE](mf-devsource-attribute-media-type.md) | Specifies the output format of a device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md) | Specifies a device's type, such as audio capture or video capture. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ENDPOINT\_ID](mf-devsource-attribute-source-type-audcap-endpoint-id.md) | Specifies the endpoint ID for an audio capture device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ROLE](mf-devsource-attribute-source-type-audcap-role.md) | Specifies the device role for an audio capture device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_CATEGORY](mf-devsource-attribute-source-type-vidcap-category.md) | Specifies the device category for a video capture device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_HW\_SOURCE](mf-devsource-attribute-source-type-vidcap-hw-source.md) | Specifies whether a video capture source is a hardware device or a software device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_MAX\_BUFFERS](mf-devsource-attribute-source-type-vidcap-max-buffers.md) | Specifies the maximum number of frames that the video capture source will buffer. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK](mf-devsource-attribute-source-type-vidcap-symbolic-link.md) | Contains the symbolic link for a video capture driver. |
| [MF\_DMFT\_FRAME\_BUFFER\_INFO](mf-dmft-frame-buffer-info.md) | Contains information about system-allocated frame buffers sent to the device driver. |
| [MF\_DISABLE\_LOCALLY\_REGISTERED\_PLUGINS](mf-disable-locally-registered-plugins.md) | Specifies if locally registered plugins are disabled. |
| [MF\_ENABLE\_3DVIDEO\_OUTPUT](mf-enable-3dvideo-output.md) | Specifies how a Media Foundation transform (MFT) should output a 3D stereoscopic video stream. |
| [MF\_EVENT\_DO\_THINNING](mf-event-do-thinning-attribute.md) | When a media source requests a new playback rate, this attribute specifies whether the source also requests thinning. For a definition of thinning, see [About Rate Control](about-rate-control.md).  |
| [MF\_EVENT\_MFT\_CONTEXT](mf-event-mft-context.md) | Contains a caller-defined value for an [METransformMarker](metransformmarker.md) event. |
| [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md) | Specifies an input stream on a Media Foundation transform (MFT). |
| [MF\_EVENT\_OUTPUT\_NODE](mf-event-output-node-attribute.md) | Identifies the topology node for a stream sink. |
| [MF\_EVENT\_PRESENTATION\_TIME\_OFFSET](mf-event-presentation-time-offset-attribute.md) | Offset between the presentation time and the media source's time stamps.  |
| [MF\_EVENT\_SCRUBSAMPLE\_TIME](mf-event-scrubsample-time-attribute.md) | Presentation time for a sample that was rendered while scrubbing.  |
| [MF\_EVENT\_SESSIONCAPS](mf-event-sessioncaps-attribute.md) | Contains flags that define the capabilities of the Media Session, based on the current presentation.  |
| [MF\_EVENT\_SESSIONCAPS\_DELTA](mf-event-sessioncaps-delta-attribute.md) | Contains flags that indicate which capabilities have changed in the Media Session, based on the current presentation.  |
| [MF\_EVENT\_SOURCE\_ACTUAL\_START](mf-event-source-actual-start-attribute.md) | Contains the start time at which a media source restarts from its current position.  |
| [MF\_EVENT\_SOURCE\_CHARACTERISTICS](mf-event-source-characteristics-attribute.md) | Specifies the current characteristics of the media source.  |
| [MF\_EVENT\_SOURCE\_CHARACTERISTICS\_OLD](mf-event-source-characteristics-old-attribute.md) | Specifies the previous characteristics of the media source. |
| [MF\_EVENT\_SOURCE\_FAKE\_START](mf-event-source-fake-start-attribute.md) | Specifies whether the current segment topology is empty.  |
| [MF\_EVENT\_SOURCE\_PROJECTSTART](mf-event-source-projectstart-attribute.md) | Specifies the start time for a segment topology.  |
| [MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED](mf-event-source-topology-canceled-attribute.md) | Specifies whether the [Sequencer Source](sequencer-source.md) canceled a topology.  |
| [MF\_EVENT\_START\_PRESENTATION\_TIME](mf-event-start-presentation-time-attribute.md) | The starting time for the presentation, in 100-nanosecond units, as measured by the presentation clock.  |
| [MF\_EVENT\_START\_PRESENTATION\_TIME\_AT\_OUTPUT](mf-event-start-presentation-time-at-output-attribute.md) | The presentation time at which the media sinks will render the first sample of the new topology.  |
| [MF\_EVENT\_STREAM\_METADATA\_CONTENT\_KEYIDS](mf-event-stream-metadata-content-keyids.md) | Specifies the content key IDs. |
| [MF\_EVENT\_STREAM\_METADATA\_KEYDATA](mf-event-stream-metadata-keydata.md) | Specifies protection system specific data. |
| [MF\_EVENT\_STREAM\_METADATA\_SYSTEMID](mf-event-stream-metadata-systemid.md) | Specifies the system ID for which the key data is intended.  |
| [MF\_EVENT\_TOPOLOGY\_STATUS](mf-event-topology-status-attribute.md) | Specifies the status of a topology during playback.  |
| [MF\_LOCAL\_PLUGIN\_CONTROL\_POLICY](mf-local-plugin-control-policy.md) | Specifies a local plugin control policy. |
| [MF\_LOW\_LATENCY](mf-low-latency.md) | Enables low-latency processing in the Media Foundation pipeline. |
| [MF\_MEDIA\_ENGINE\_AUDIO\_CATEGORY](mf-media-engine-audio-category.md) | Specifies the category of the audio stream. |
| [MF\_MEDIA\_ENGINE\_AUDIO\_ENDPOINT\_ROLE](mf-media-engine-audio-endpoint-role.md) | Specifies the device role for the audio stream. |
| [MF\_MEDIA\_ENGINE\_BROWSER\_COMPATIBILITY\_MODE](mf-media-engine-browser-compatibility-mode.md) | Specifies the browser compatibility mode. |
| [MF\_MEDIA\_ENGINE\_CALLBACK](mf-media-engine-callback.md) | Contains a pointer to the callback interface for the Media Engine.  |
| [MF\_MEDIA\_ENGINE\_CONTENT\_PROTECTION\_FLAGS](mf-media-engine-content-protection-flags.md) | Specifies whether the Media Engine will play protected content. |
| [MF\_MEDIA\_ENGINE\_CONTENT\_PROTECTION\_MANAGER](mf-media-engine-content-protection-manager.md) | Enables the Media Engine to play protected content. |
| [MF\_MEDIA\_ENGINE\_COREWINDOW](mf-media-engine-corewindow.md) | Core window. |
| [MF\_MEDIA\_ENGINE\_DXGI\_MANAGER](mf-media-engine-dxgi-manager.md) | Sets the Microsoft DirectX Graphics Infrastructure (DXGI) Device Manager on the Media Engine. |
| [MF\_MEDIA\_ENGINE\_EXTENSION](mf-media-engine-extension.md) | Contains a pointer to the [**IMFMediaEngineExtension**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineextension) interface. |
| [MF\_MEDIA\_ENGINE\_NEEDKEY\_CALLBACK](mf-media-engine-needkey-callback.md) | Attribute which is passed in the [**IMFMediaEngineNeedKeyNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineneedkeynotify) to the media engine on creation. |
| [MF\_MEDIA\_ENGINE\_OPM\_HWND](mf-media-engine-opm-hwnd.md) | Specifies a window for the Media Engine to apply [Output Protection Manager](output-protection-manager.md) (OPM) protections. |
| [MF\_MEDIA\_ENGINE\_PLAYBACK\_HWND](mf-media-engine-playback-hwnd.md) | Sets a handle to a video playback window for the Media Engine. |
| [MF\_MEDIA\_ENGINE\_PLAYBACK\_VISUAL](mf-media-engine-playback-visual.md) | Sets a Microsoft DirectComposition visual as the playback region for the Media Engine. |
| [MF\_MEDIA\_ENGINE\_SOURCE\_RESOLVER\_CONFIG\_STORE](mf-media-engine-source-resolver-config-store.md) | Gets the source resolver config store. |
| [MF\_MEDIA\_ENGINE\_STREAM\_CONTAINS\_ALPHA\_CHANNEL](mf-media-engine-stream-contains-alpha-channel.md) | Specifies if the stream contains an alpha channel. |
| [MF\_MEDIA\_ENGINE\_TRACK\_ID](mf-media-engine-track-id.md) | Specifies the track id. |
| [MF\_MEDIA\_ENGINE\_VIDEO\_OUTPUT\_FORMAT](mf-media-engine-video-output-format.md) | Sets the render-target format for the Media Engine. |
| [MF\_MEDIATYPE\_MULTIPLEXED\_MANAGER](mf-mediatype-multiplexed-manager.md) | Provides an instance of [**IMFMuxStreamMediaTypeManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreammediatypemanager) which can be used to get the media types of the substreams of a multiplexed media source as well as control the combination of substreams that are multiplexed by the source. |
| [MF\_MP2DLNA\_AUDIO\_BIT\_RATE](mf-mp2dlna-audio-bit-rate.md) | Specifies the maximum audio bit rate for the Digital Living Network Alliance (DLNA) media sink. |
| [MF\_MP2DLNA\_ENCODE\_QUALITY](mf-mp2dlna-encode-quality.md) | Specifies the encoding quality for the DLNA media sink. |
| [MF\_MP2DLNA\_STATISTICS](mf-mp2dlna-statistics.md) | Gets statistics from the DLNA media sink. |
| [MF\_MP2DLNA\_USE\_MMCSS](mf-mp2dlna-use-mmcss.md) | Specifies whether the DLNA media sink uses the Multimedia Class Scheduler Service (MMCSS) |
| [MF\_MP2DLNA\_VIDEO\_BIT\_RATE](mf-mp2dlna-video-bit-rate.md) | Specifies the maximum video bit rate for the DLNA media sink. |
| [MF\_MPEG4SINK\_MOOV\_BEFORE\_MDAT](mf-mpeg4sink-moov-before-mdat.md) | Indicates that 'moov' will be written before 'mdat' box in the generated file. |
| [MF\_MPEG4SINK\_SPSPPS\_PASSTHROUGH](mf-mpeg4sink-spspps-passthrough.md) | Specifies whether the [**MPEG-4 File Sink**](mpeg-4-file-sink.md) filters out sequence parameter set (SPS) and picture parameter set (PPS) NALUs. |
| [MF\_MSE\_ACTIVELIST\_CALLBACK](mf-mse-activelist-callback.md) | Contains a pointer to the application's callback interface for the [**IMFBufferListNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfbufferlistnotify) interface for the active buffer list. |
| [MF\_MSE\_BUFFERLIST\_CALLBACK](mf-mse-bufferlist-callback.md) | Contains a pointer to the application's callback interface for the [**IMFBufferListNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfbufferlistnotify). |
| [MF\_MSE\_CALLBACK](mf-mse-callback.md) | Contains a pointer to the application's callback interface for the [**IMFMediaSourceExtensionNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediasourceextensionnotify). |
| [MF\_MT\_AAC\_AUDIO\_PROFILE\_LEVEL\_INDICATION](mf-mt-aac-audio-profile-level-indication.md) | Specifies the audio profile and level of an Advanced Audio Coding (AAC) stream. |
| [MF\_MT\_AAC\_PAYLOAD\_TYPE](mf-mt-aac-payload-type.md) | Specifies the payload type of an Advanced Audio Coding (AAC) stream. |
| [MF\_MT\_ALL\_SAMPLES\_INDEPENDENT](mf-mt-all-samples-independent-attribute.md) | Specifies for a media type whether each sample is independent of the other samples in the stream.  |
| [MF\_MT\_ALPHA\_MODE](mf-mt-alpha-mode.md) | Specifies whether the alpha mode for color media video types is premultiplied or straight. |
| [MF\_MT\_AM\_FORMAT\_TYPE](mf-mt-am-format-type-attribute.md) | Contains a DirectShow format GUID for a media type.  |
| [MF\_MT\_ARBITRARY\_FORMAT](mf-mt-arbitrary-format.md) | Additional format data for a binary stream in an Advanced Systems Format (ASF) file. |
| [MF\_MT\_ARBITRARY\_HEADER](mf-mt-arbitrary-header.md) | Type-specific data for a binary stream in an Advanced Systems Format (ASF) file. |
| [MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND](mf-mt-audio-avg-bytes-per-second-attribute.md) | Average number of bytes per second in an audio media type.  |
| [MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE](mf-mt-audio-bits-per-sample-attribute.md) | Number of bits per audio sample in an audio media type.  |
| [MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT](mf-mt-audio-block-alignment-attribute.md) | Block alignment, in bytes, for an audio media type. The block alignment is the minimum atomic unit of data for the audio format.  |
| [MF\_MT\_AUDIO\_CHANNEL\_MASK](mf-mt-audio-channel-mask-attribute.md) | In an audio media type, specifies the assignment of audio channels to speaker positions.  |
| [MF\_MT\_AUDIO\_FLOAT\_SAMPLES\_PER\_SECOND](mf-mt-audio-float-samples-per-second-attribute.md) | Number of audio samples per second in an audio media type.  |
| [MF\_MT\_AUDIO\_FOLDDOWN\_MATRIX](mf-mt-audio-folddown-matrix-attribute.md) | Specifies how an audio decoder should transform multichannel audio to stereo output. This process is also called *fold-down*.  |
| [MF\_MT\_AUDIO\_NUM\_CHANNELS](mf-mt-audio-num-channels-attribute.md) | Number of audio channels in an audio media type.  |
| [MF\_MT\_AUDIO\_PREFER\_WAVEFORMATEX](mf-mt-audio-prefer-waveformatex-attribute.md) | Specifies the preferred legacy format structure to use when converting an audio media type.  |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_BLOCK](mf-mt-audio-samples-per-block-attribute.md) | Number of audio samples contained in one compressed block of audio data. This attribute can be used in compressed audio formats that have a fixed number of samples within each block.  |
| [MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND](mf-mt-audio-samples-per-second-attribute.md) | Number of audio samples per second in an audio media type.  |
| [MF\_MT\_AUDIO\_VALID\_BITS\_PER\_SAMPLE](mf-mt-audio-valid-bits-per-sample-attribute.md) | Number of valid bits of audio data in each audio sample.  |
| [MF\_MT\_AUDIO\_WMADRC\_AVGREF](mf-mt-audio-wmadrc-avgref-attribute.md) | Reference average volume level of a Windows Media Audio file.  |
| [MF\_MT\_AUDIO\_WMADRC\_AVGTARGET](mf-mt-audio-wmadrc-avgtarget-attribute.md) | Target average volume level of a Windows Media Audio file.  |
| [MF\_MT\_AUDIO\_WMADRC\_PEAKREF](mf-mt-audio-wmadrc-peakref-attribute.md) | Reference peak volume level of a Windows Media Audio file.  |
| [MF\_MT\_AUDIO\_WMADRC\_PEAKTARGET](mf-mt-audio-wmadrc-peaktarget-attribute.md) | Target peak volume level of a Windows Media Audio file.  |
| [MF\_MT\_AVG\_BIT\_ERROR\_RATE](mf-mt-avg-bit-error-rate-attribute.md) | Data error rate, in bit errors per second, for a video media type.  |
| [MF\_MT\_AVG\_BITRATE](mf-mt-avg-bitrate-attribute.md) | Approximate data rate of the video stream, in bits per second, for a video media type.  |
| [MF\_MT\_COMPRESSED](mf-mt-compressed-attribute.md) | Specifies for a media type whether the media data is compressed.  |
| [MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES](mf-mt-custom-video-primaries-attribute.md) | Specifies custom color primaries for a video media type.  |
| [MF_MT_D3D_RESOURCE_VERSION](mf-mt-d3d-resource-version.md) | Specifies the Direct3D version of the resources stored in the data stream associated with the media type.  |
| [MF_MT_D3D12_CPU_READBACK](mf-mt-d3d12-cpu-readback.md) | Indicates whether CPU access is required for the associated Direct3D resources. |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_CROSS_ADAPTER](mf-mt-d3d12-resource-flag-allow-cross-adapter.md) | Indicates whether the resources in the stream can be used for cross-adapter data.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL](mf-mt-d3d12-resource-flag-allow-depth-stencil.md) | Indicates whether depth stencil view can be created for the Direct3D resources in the stream associated with the media type.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_RENDER_TARGET](mf-mt-d3d12-resource-flag-allow-render-target.md) | Indicates whether a render target view can be created for the Direct3D resources in the stream associated with the media type.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS](mf-mt-d3d12-resource-flag-allow-simultaneous-access.md) | Indicates whether the Direct3D resources in the stream can be simultaneously accessed by multiple different command queues.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS](mf-mt-d3d12-resource-flag-allow-unordered-access.md) | Indicates whether an unordered access view can be created for the Direct3D resources in the stream associated with the media type.   |
| [MF_MT_D3D12_RESOURCE_FLAG_DENY_SHADER_RESOURCE](mf-mt-d3d12-resource-flag-deny-shader-resource.md) | Indicates whether shader resource view creation is disallowed for the Direct3D resources in the stream associated with the media type.  |
| [MF_MT_D3D12_TEXTURE_LAYOUT](mf-mt-d3d12-texture-layout.md) | Indicates the texture layout options that were used to create the associated Direct3D resources.  |
| [MF\_MT\_DEFAULT\_STRIDE](mf-mt-default-stride-attribute.md) | Default surface stride, for an uncompressed video media type. Stride is the number of bytes needed to go from one row of pixels to the next. |
| [MF\_MT\_DEPTH\_MEASUREMENT](mf-mt-depth-measurement.md) | A value that defines the measurement system for a depth value in a video frame. |
| [MF\_MT\_DEPTH\_VALUE\_UNIT](mf-mt-depth-value-unit.md) | A value that defines the units for a depth value in a video frame. |
| [MF\_MT\_DRM\_FLAGS](mf-mt-drm-flags-attribute.md) | Specifies whether a video media type requires the enforcement of copy protection.  |
| [MF\_MT\_DV\_AAUX\_CTRL\_PACK\_0](mf-mt-dv-aaux-ctrl-pack-0-attribute.md) | Audio auxiliary (AAUX) source control pack for the first audio block in a digital video (DV) media type.  |
| [MF\_MT\_DV\_AAUX\_CTRL\_PACK\_1](mf-mt-dv-aaux-ctrl-pack-1-attribute.md) | Audio auxiliary (AAUX) source control pack for the second audio block in a digital video (DV) media type.  |
| [MF\_MT\_DV\_AAUX\_SRC\_PACK\_0](mf-mt-dv-aaux-src-pack-0-attribute.md) | Audio auxiliary (AAUX) source pack for the first audio block in a digital video (DV) media type.  |
| [MF\_MT\_DV\_AAUX\_SRC\_PACK\_1](mf-mt-dv-aaux-src-pack-1-attribute.md) | Audio auxiliary (AAUX) source pack for the second audio block in a digital video (DV) media type.  |
| [MF\_MT\_DV\_VAUX\_CTRL\_PACK](mf-mt-dv-vaux-ctrl-pack-attribute.md) | Video auxiliary (VAUX) source control pack in a digital video (DV) media type.  |
| [MF\_MT\_DV\_VAUX\_SRC\_PACK](mf-mt-dv-vaux-src-pack-attribute.md) | Video auxiliary (VAUX) source pack in a digital video (DV) media type.  |
| [MF\_MT\_FIXED\_SIZE\_SAMPLES](mf-mt-fixed-size-samples-attribute.md) | Specifies for a media type whether the samples have a fixed size.  |
| [MF\_MT\_FORWARD\_CUSTOM\_NALU](mf-mt-forward-custom-nalu.md) | Specifies that network abstraction layer (NAL) unit types should be forwarded on output samples by the decoder. |
| [MF\_MT\_FORWARD\_CUSTOM\_SEI](mf-mt-forward-custom-sei.md) | Specifies that Supplemental Enhancement Information (SEI) unit types should be forwarded on output samples by the decoder. |
| [MF\_MT\_FRAME\_RATE](mf-mt-frame-rate-attribute.md) | Frame rate of a video media type, in frames per second.  |
| [MF\_MT\_FRAME\_RATE\_RANGE\_MAX](mf-mt-frame-rate-range-max.md) | The maximum frame rate that is supported by a video capture device, in frames per second. |
| [MF\_MT\_FRAME\_RATE\_RANGE\_MIN](mf-mt-frame-rate-range-min.md) | The minimum frame rate that is supported by a video capture device, in frames per second. |
| [MF\_MT\_FRAME\_SIZE](mf-mt-frame-size-attribute.md) | Width and height of a video frame, in pixels.  |
| [MF\_MT\_FRAMESOURCE\_TYPES](mf-mt-framesource-types.md) | A value that indicates the type of sensor provided by a frame source, such as color, infrared, or depth. |
| [MF\_MT\_GEOMETRIC\_APERTURE](mf-mt-geometric-aperture-attribute.md) | Defines the geometric aperture for a video media type.  |
| [MF\_MT\_H264\_CAPABILITIES](mf-mt-h264-capabilities.md) | Specifies the capabilities flags for an H.264 video stream. |
| [MF\_MT\_H264\_MAX\_CODEC\_CONFIG\_DELAY](mf-mt-h264-max-codec-config-delay.md) | The maximum number of frames the H.264 encoder takes to respond to a command.  |
| [MF\_MT\_H264\_MAX\_MB\_PER\_SEC](mf-mt-h264-max-mb-per-sec.md) | Specifies the maximum macroblock processing rate for an H.264 video stream. |
| [MF\_MT\_H264\_RATE\_CONTROL\_MODES](mf-mt-h264-rate-control-modes.md) | Specifies the rate-control mode for an H.264 video stream. |
| [MF\_MT\_H264\_SIMULCAST\_SUPPORT](mf-mt-h264-simulcast-support.md) | Specifies the number of streaming endpoints and the number of supported streams for a UVC H.264 encoder. |
| [MF\_MT\_H264\_SUPPORTED\_RATE\_CONTROL\_MODES](mf-mt-h264-supported-rate-control-modes.md) | Specifies the supported rate-control modes for an H.264 video stream. |
| [MF\_MT\_H264\_SUPPORTED\_SLICE\_MODES](mf-mt-h264-supported-slice-modes.md) | Specifies the supported slice modes for an H.264 video stream. |
| [MF\_MT\_H264\_SUPPORTED\_SYNC\_FRAME\_TYPES](mf-mt-h264-supported-sync-frame-types.md) | Specifies the types of synchronization frame that are supported for an H.264 video stream. |
| [MF\_MT\_H264\_SUPPORTED\_USAGES](mf-mt-h264-supported-usages.md) | Specifies the supported usage modes for an H.264 video stream. |
| [MF\_MT\_H264\_SVC\_CAPABILITIES](mf-mt-h264-svc-capabilities.md) | Specifies the SVC capabilities of an H.264 video stream. |
| [MF\_MT\_H264\_USAGE](mf-mt-h264-usage.md) | Specifies the usage mode for a UVC H.264 encoder. |
| [MF\_MT\_IMAGE\_LOSS\_TOLERANT](mf-mt-image-loss-tolerant.md) | Specifies whether an ASF image stream is a degradable JPEG type. |
| [MF\_MT\_INTERLACE\_MODE](mf-mt-interlace-mode-attribute.md) | Describes how the frames in a video media type are interlaced.  |
| [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md) | Major type GUID for a media type.  |
| [MF\_MT\_MAX\_KEYFRAME\_SPACING](mf-mt-max-keyframe-spacing-attribute.md) | Maximum number of frames from one key frame to the next, in a video media type.  |
| [MF\_MT\_MAX\_LUMINANCE\_LEVEL](mf-mt-max-luminance-level.md) | Specifies the maximum luminance level of the content in Nits. This attribute has the same semantics as **MaxCLL** as defined in the CEA-861.3 standard. |
| [MF\_MT\_MAX\_FRAME\_AVERAGE\_LUMINANCE\_LEVEL](mf-mt-max-frame-average-luminance-level.md) | Specifies the maximum average per-frame luminance level of the content in Nits. This attribute has the same semantics as **MaxFALL** as defined in the CEA-861.3 standard. |
| [MF\_MT\_MAX\_MASTERING\_LUMINANCE](mf-mt-max-mastering-luminance.md) | Specifies the maximum luminance of the display on which the content was authored, in Nits. This attribute has the same semantics as **max\_display\_mastering\_luminance** as defined in the CEA-861.3 standard.  |
| [MF\_MT\_MIN\_MASTERING\_LUMINANCE](mf-mt-min-mastering-luminance.md) | Specifies the maximum luminance of the display on which the content was authored, in Nits. This attribute has the same semantics as **min\_display\_mastering\_luminance** as defined in the CEA-861.3 standard.  |
| [MF\_MT\_MINIMUM\_DISPLAY\_APERTURE](mf-mt-minimum-display-aperture-attribute.md) | Defines the display aperture, which is the region of a video frame that contains valid image data.  |
| [MF\_MT\_MPEG\_SEQUENCE\_HEADER](mf-mt-mpeg-sequence-header-attribute.md) | Contains the MPEG-1 or MPEG-2 sequence header for a video media type.  |
| [MF\_MT\_MPEG\_START\_TIME\_CODE](mf-mt-mpeg-start-time-code-attribute.md) | Group-of-pictures (GOP) start time code, for an MPEG-1 or MPEG-2 video media type.  |
| [MF\_MT\_MPEG2\_CONTENT\_PACKET Attribute](mf-mt-mpeg2-content-packet.md) | For a media type that describes an MPEG-2 transport stream (TS), specifies whether the transport packets contain Content Packet headers. |
| [MF\_MT\_MPEG2\_FLAGS](mf-mt-mpeg2-flags-attribute.md) | Contains miscellaneous flags for an MPEG-2 video media type.  |
| [MF\_MT\_MPEG2\_LEVEL](mf-mt-mpeg2-level-attribute.md) | Specifies the MPEG-2 or H.264 level in a video media type.  |
| [MF\_MT\_MPEG2\_PROFILE](mf-mt-mpeg2-profile-attribute.md) | Specifies the MPEG-2 or H.264 profile in a video media type.  |
| [MF\_MT\_MPEG2\_STANDARD Attribute](mf-mt-mpeg2-standard.md) | For a media type that describes an MPEG-2 program stream (PS) or transport stream (TS), specifies the standard that is used to multiplex the stream. |
| [MF\_MT\_MPEG2\_TIMECODE Attribute](mf-mt-mpeg2-timecode.md) | For a media type that describes an MPEG-2 transport stream (TS), specifies the transport packets contain a 4-byte time code. |
| [MF\_MT\_MPEG4\_CURRENT\_SAMPLE\_ENTRY](mf-mt-mpeg4-current-sample-entry.md) | Specifies the current entry in the sample description box for an MPEG-4 media type. |
| [MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION](mf-mt-mpeg4-sample-description.md) | Contains the sample description box for an MP4 or 3GP file. |
| [MF\_MT\_ORIGINAL\_4CC](mf-mt-original-4cc.md) | Contains the original codec FOURCC for a video stream. |
| [MF\_MT\_ORIGINAL\_WAVE\_FORMAT\_TAG](mf-mt-original-wave-format-tag.md) | Contains the original WAVE format tag for an audio stream. |
| [MF\_MT\_PAD\_CONTROL\_FLAGS](mf-mt-pad-control-flags-attribute.md) | Specifies the aspect ratio of the output rectangle for a video media type.  |
| [MF\_MT\_PALETTE](mf-mt-palette-attribute.md) | Contains the palette entries for a video media type. Use this attribute for palettized video formats, such as RGB 8.  |
| [MF\_MT\_PAN\_SCAN\_APERTURE](mf-mt-pan-scan-aperture-attribute.md) | Defines the pan/scan aperture, which is the 4 3 region of video that should be displayed in pan/scan mode.  |
| [MF\_MT\_PAN\_SCAN\_ENABLED](mf-mt-pan-scan-enabled-attribute.md) | Specifies whether pan/scan mode is enabled.  |
| [MF\_MT\_PIXEL\_ASPECT\_RATIO](mf-mt-pixel-aspect-ratio-attribute.md) | Pixel aspect ratio for a video media type.  |
| [MF\_MT\_REALTIME\_CONTENT](mf-mt-realtime-content.md) | Specifies the real time media content type.  |
| [MF\_MT\_SAMPLE\_SIZE](mf-mt-sample-size-attribute.md) | Specifies the size of each sample, in bytes, in a media type.  |
| [MF\_MT\_SOURCE\_CONTENT\_HINT](mf-mt-source-content-hint-attribute.md) | Describes the intended aspect ratio for a video media type.  |
| [MF\_MT\_SPATIAL\_AUDIO\_MAX\_DYNAMIC\_OBJECTS](mf-mt-spatial-audio-max-dynamic-objects.md) | Specifies the maximum number of dynamic audio objects that can be rendered by the audio endpoint simulataneously. |
| [MF\_MT\_SPATIAL\_AUDIO\_OBJECT\_METADATA\_FORMAT\_ID](mf-mt-spatial-audio-object-metadata-format-id.md) | A decoder-defined GUID that identifies the spatial audio metadata format, notifying downstream components of the metadata object type that the decoder will output. |
| [MF\_MT\_SPATIAL\_AUDIO\_OBJECT\_METADATA\_LENGTH](mf-mt-spatial-audio-object-metadata-length.md) | A value specifying the size, in bytes, of the spatial audio metadata object type that the decoder will output. |
| [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md) | Subtype GUID for a media type.  |
| [MF\_MT\_TIMESTAMP\_CAN\_BE\_DTS Attribute](mf-mt-timestamp-can-be-dts.md) | Specifies whether a decoder can use decode time stamps (DTS) when setting time stamps. |
| [MF\_MT\_TRANSFER\_FUNCTION](mf-mt-transfer-function-attribute.md) | Specifies the conversion function from RGB to R'G'B' for a video media type.  |
| [MF\_MT\_USER\_DATA](mf-mt-user-data-attribute.md) | Contains additional format data for a media type.  |
| [MF\_MT\_VIDEO\_3D](mf-mt-video-3d.md) | Specifies whether a video stream contains 3D content. |
| [MF\_MT\_VIDEO\_3D\_FIRST\_IS\_LEFT](mf-mt-video-3d-first-is-left.md) | For a 3D video format, specifies which view is the left view. |
| [MF\_MT\_VIDEO\_3D\_FORMAT](mf-mt-video-3d-format.md) | For a video media type, specifies how 3D video frames are stored in memory. |
| [MF\_MT\_VIDEO\_3D\_LEFT\_IS\_BASE](mf-mt-video-3d-left-is-base.md) | For a 3D video format, specifies which view is the base view. |
| [MF\_MT\_VIDEO\_3D\_NUM\_VIEWS](mf-mt-video-3d-num-views.md) | The number of views in a 3D video sequence. |
| [MF\_MT\_VIDEO\_CHROMA\_SITING](mf-mt-video-chroma-siting-attribute.md) | Describes how chroma was sampled for a Y'Cb'Cr' video media type.  |
| [MF\_MT\_VIDEO\_LEVEL](mf-mt-video-level.md) | Specifies the MPEG-2 or H.264 level in a video media type. This is an alias of [MF\_MT\_MPEG2\_LEVEL](mf-mt-mpeg2-level-attribute.md). |
| [MF\_MT\_VIDEO\_LIGHTING](mf-mt-video-lighting-attribute.md) | Specifies the optimal lighting conditions for a video media type.  |
| [MF\_MT\_VIDEO\_NOMINAL\_RANGE](mf-mt-video-nominal-range-attribute.md) | Specifies the nominal range of the color information in a video media type.  |
| [MF\_MT\_VIDEO\_PRIMARIES](mf-mt-video-primaries-attribute.md) | Specifies the color primaries for a video media type.  |
| [MF\_MT\_VIDEO\_PROFILE](mf-mt-video-profile.md) | Specifies the profile of video encoding on the output media type. This is an alias of [MF\_MT\_MPEG2\_PROFILE](mf-mt-mpeg2-profile-attribute.md) attribute. |
| [MF\_MT\_VIDEO\_RENDERER\_EXTENSION\_PROFILE](mf-mt-video-renderer-extension-profile.md) | Contains a string that matches an entry in a UWP app manifest's **VideoRendererExtensionProfiles** list to select which effect to load. |
| [MF\_MT\_VIDEO\_ROTATION](mf-mt-video-rotation.md) | Specifies the rotation of a video frame in the counter-clockwise direction. |
| [MF\_MT\_WRAPPED\_TYPE](mf-mt-wrapped-type-attribute.md) | Contains a media type that has been wrapped in another media type.  |
| [MF\_MT\_YUV\_MATRIX](mf-mt-yuv-matrix-attribute.md) | For YUV media types, defines the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space.  |
| [MF\_NALU\_LENGTH\_INFORMATION](mf-nalu-length-information.md) | Indicates the lengths of NALUs in the sample. This is a MF **BLOB** that is set on compressed input samples to the H.264 decoder.  |
| [MF\_NALU\_LENGTH\_SET](mf-nalu-length-set.md) | Indicates that NALU length information will be sent as a **BLOB** with each compressed H.264 sample. |
| [MF\_PD\_APP\_CONTEXT](mf-pd-app-context-attribute.md) | Contains a pointer to the presentation descriptor from the Protected Media Path (PMP).  |
| [MF\_PD\_ASF\_CODECLIST](mf-pd-asf-codeclist-attribute.md) | Contains information about the codecs and formats that were used to encode the content in an Advanced Systems Format (ASF) file. This attribute corresponds to the Codec List Object in the ASF header, defined in the ASF specification.  |
| [MF\_PD\_ASF\_CONTENTENCRYPTION\_KEYID](mf-pd-asf-contentencryption-keyid-attribute.md) | Specifies the key identifier for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the Key ID field of the Content Encryption Header, defined in the ASF specification.  |
| [MF\_PD\_ASF\_CONTENTENCRYPTION\_LICENSE\_URL](mf-pd-asf-contentencryption-license-url-attribute.md) | Specifies the license acquisition URL for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the License URL field of the Content Encryption Header, defined in the ASF specification.  |
| [MF\_PD\_ASF\_CONTENTENCRYPTION\_SECRET\_DATA](mf-pd-asf-contentencryption-secret-data-attribute.md) | Contains secret data for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the Secret Data field of the Content Encryption Header, defined in the ASF specification.  |
| [MF\_PD\_ASF\_CONTENTENCRYPTION\_TYPE](mf-pd-asf-contentencryption-type-attribute.md) | Specifies the type of protection mechanism used in an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_CONTENTENCRYPTIONEX\_ENCRYPTION\_DATA](mf-pd-asf-contentencryptionex-encryption-data-attribute.md) | Contains encryption data for an Advanced Systems Format (ASF) file. This attribute corresponds to the Extended Content Encryption Object in the ASF header, defined in the ASF specification.  |
| [MF\_PD\_ASF\_DATA\_LENGTH](mf-pd-asf-data-length-attribute.md) | Specifies the size, in bytes, of the data section of an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_DATA\_START\_OFFSET](mf-pd-asf-data-start-offset-attribute.md) | Specifies the offset, in bytes, from the start of an Advanced Systems Format (ASF) file to the start of the first data packet.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_CREATION\_TIME](mf-pd-asf-fileproperties-creation-time-attribute.md) | Specifies the date and time when an Advanced Systems Format (ASF) file was created.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_FILE\_ID](mf-pd-asf-fileproperties-file-id-attribute.md) | Specifies the file identifier of an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_FLAGS](mf-pd-asf-fileproperties-flags-attribute.md) | Specifies whether an Advanced Systems Format (ASF) file is broadcast or seekable. This value corresponds to the Flags field of the File Properties Object, defined in the ASF specification.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_BITRATE](mf-pd-asf-fileproperties-max-bitrate-attribute.md) | Specifies the maximum instantaneous bit rate, in bits per second, for an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_PACKET\_SIZE](mf-pd-asf-fileproperties-max-packet-size-attribute.md) | Specifies the maximum packet size, in bytes, of an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_MIN\_PACKET\_SIZE](mf-pd-asf-fileproperties-min-packet-size-attribute.md) | Specifies the minimum packet size, in bytes, for an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_PACKETS](mf-pd-asf-fileproperties-packets-attribute.md) | Specifies the number of packets in the data section of an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_PLAY\_DURATION](mf-pd-asf-fileproperties-play-duration-attribute.md) | Specifies the time needed to play an Advanced Systems Format (ASF) file, in 100-nanosecond units. |
| [MF\_PD\_ASF\_FILEPROPERTIES\_PREROLL](mf-pd-asf-fileproperties-preroll-attribute.md) | Specifies the amount of time, in milliseconds, to buffer data before playing an Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_FILEPROPERTIES\_SEND\_DURATION](mf-pd-asf-fileproperties-send-duration-attribute.md) | Specifies the time, in 100-nanosecond units, needed to send an Advanced Systems Format (ASF) file. A packet's *send time* is the time when the packet should be delivered over the network. It is not the presentation time of the packet.  |
| [MF\_PD\_ASF\_INFO\_HAS\_AUDIO](mf-pd-asf-info-has-audio-attribute.md) | Specifies whether an Advanced Systems Format (ASF) file contains any audio streams.  |
| [MF\_PD\_ASF\_INFO\_HAS\_NON\_AUDIO\_VIDEO](mf-pd-asf-info-has-non-audio-video-attribute.md) | Specifies whether an Advanced Systems Format (ASF) file contains any streams that are not audio or video.  |
| [MF\_PD\_ASF\_INFO\_HAS\_VIDEO](mf-pd-asf-info-has-video-attribute.md) | Specifies whether an Advanced Systems Format (ASF) file contains at least one video stream.  |
| [MF\_PD\_ASF\_LANGLIST](mf-pd-asf-langlist-attribute.md) | Specifies a list of language identifiers which specifies the languages contained in an Advanced Systems Format (ASF) file. This attribute corresponds to the Language List Object, defined in the ASF specification.  |
| [MF\_PD\_ASF\_LANGLIST\_LEGACYORDER](mf-pd-asf-langlist-legacyorder.md) | Contains a list of RFC 1766 languages used in the current presentation. |
| [MF\_PD\_ASF\_MARKER](mf-pd-asf-marker-attribute.md) | Specifies the markers in an Advanced Systems Format (ASF) file. This attribute corresponds to the Marker Object in the ASF header, defined in the ASF specification.  |
| [MF\_PD\_ASF\_METADATA\_IS\_VBR](mf-pd-asf-metadata-is-vbr-attribute.md) | Specifies whether an Advanced Systems Format (ASF) file uses variable bit rate (VBR) encoding.  |
| [MF\_PD\_ASF\_METADATA\_LEAKY\_BUCKET\_PAIRS](mf-pd-asf-metadata-leaky-bucket-pairs-attribute.md) | Specifies a list of bit rates and corresponding buffer windows for a variable bit rate (VBR) Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_METADATA\_V8\_BUFFERAVERAGE](mf-pd-asf-metadata-v8-bufferaverage-attribute.md) | Specifies the average buffer size needed for a variable bit rate (VBR) Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_METADATA\_V8\_VBRPEAK](mf-pd-asf-metadata-v8-vbrpeak-attribute.md) | Specifies the highest momentary bit rate in a variable bit rate (VBR) Advanced Systems Format (ASF) file.  |
| [MF\_PD\_ASF\_SCRIPT](mf-pd-asf-script-attribute.md) | Specifies a list of script commands and the parameters for an Advanced Systems Format (ASF) file. This attribute corresponds to the Script Command Object in the ASF header, defined in the ASF specification.  |
| [MF\_PD\_AUDIO\_ENCODING\_BITRATE](mf-pd-audio-encoding-bitrate-attribute.md) | Specifies the audio encoding bit rate for the presentation, in bits per second. This attribute applies to presentation descriptors.  |
| [MF\_PD\_AUDIO\_ISVARIABLEBITRATE](mf-pd-audio-isvariablebitrate.md) | Specifies whether the audio streams in a presentation have a variable bit rate. |
| [MF\_PD\_DURATION](mf-pd-duration-attribute.md) | Specifies the duration of a presentation, in 100-nanosecond units.  |
| [MF\_PD\_LAST\_MODIFIED\_TIME](mf-pd-last-modified-time-attribute.md) | Specifies when a presentation was last modified.  |
| [MF\_PD\_MIME\_TYPE](mf-pd-mime-type-attribute.md) | Specifies the MIME type of the content.  |
| [MF\_PD\_PLAYBACK\_BOUNDARY\_TIME](mf-pd-playback-boundary-time.md) | Stores the time (in 100-nanoseconds units) at which the presentation must begin, relative to the start of the media source. |
| [MF\_PD\_PLAYBACK\_ELEMENT\_ID](mf-pd-playback-element-id.md) | Contains the identifier of the playlist element in the presentation. |
| [MF\_PD\_PMPHOST\_CONTEXT](mf-pd-pmphost-context-attribute.md) | Contains a pointer to the proxy object for the application's presentation descriptor.  |
| [MF\_PD\_PREFERRED\_LANGUAGE](mf-pd-preferred-language.md) | Contains the preferred RFC 1766 language of the media source. |
| [MF\_PD\_SAMI\_STYLELIST](mf-pd-sami-stylelist-attribute.md) | Contains the friendly names of the Synchronized Accessible Media Interchange (SAMI) styles defined in the SAMI file. |
| [MF\_PD\_TOTAL\_FILE\_SIZE](mf-pd-total-file-size-attribute.md) | Specifies the total size of the source file, in bytes. This attribute applies to presentation descriptors. A media source can optionally set this attribute.  |
| [MF\_PD\_VIDEO\_ENCODING\_BITRATE](mf-pd-video-encoding-bitrate-attribute.md) | Specifies the video encoding bit rate for the presentation, in bits per second. This attribute applies to presentation descriptors.  |
| [MF\_READWRITE\_D3D\_OPTIONAL](mf-readwrite-d3d-optional.md) | Specifies whether the application requires Microsoft Direct3D support in the [Source Reader](source-reader.md) or [Sink Writer](sink-writer.md). |
| [MF\_READWRITE\_DISABLE\_CONVERTERS](mf-readwrite-disable-converters.md) | Enables or disables format conversions by the source reader or sink writer. |
| [MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS](mf-readwrite-enable-hardware-transforms.md) | Enables the source reader or sink writer to use hardware-based Media Foundation transforms (MFTs). |
| [MF\_READWRITE\_MMCSS\_CLASS](mf-readwrite-mmcss-class.md) | Specifies a [Multimedia Class Scheduler Service](/windows/desktop/ProcThread/multimedia-class-scheduler-service) (MMCSS) class for the Source Reader or Sink Writer. |
| [MF\_READWRITE\_MMCSS\_CLASS\_AUDIO](mf-readwrite-mmcss-class-audio.md) | Specifies a [Multimedia Class Scheduler Service](/windows/desktop/ProcThread/multimedia-class-scheduler-service) (MMCSS) class for audio-processing threads in the Source Reader or Sink Writer. |
| [MF\_READWRITE\_MMCSS\_PRIORITY](mf-readwrite-mmcss-priority.md) | Sets the base thread priority for the Source Reader or Sink Writer. |
| [MF\_READWRITE\_MMCSS\_PRIORITY\_AUDIO](mf-readwrite-mmcss-priority-audio.md) | Sets the base priority for audio-processing threads created by the Source Reader or Sink Writer. |
| [MF\_READWRITE\_USE\_ONLY\_HARDWARE\_TRANSFORMS](mf-readwrite-use-only-hardware-transforms.md) | Specifies that the Source Reader or Sink Writer should load only hardware-based Media Foundation transforms (MFTs) that match the passed-in D3D device manager. |
| [MF\_SA\_D3D\_ALLOCATE\_DISPLAYABLE\_RESOURCES](mf-sa-d3d11-allocate-displayable-resources.md) | Specifies if the MFT’s Sample Allocator (SA) should allocate the underlying Direct3D Texture using the D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE flag. |
| [MF\_SA\_BUFFERS\_PER\_SAMPLE](mf-sa-buffers-per-sample.md) | Specifies how many buffers the video-sample allocator creates for each video sample.  |
| [MF\_SA\_D3D\_AWARE](mf-sa-d3d-aware-attribute.md) | Specifies whether a Media Foundation transform (MFT) supports DirectX Video Acceleration (DXVA). This attribute applies only to video MFTs.  |
| [MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md) | Specifies whether a Media Foundation transform (MFT) supports Microsoft Direct3D 11. |
| [MF\_SA\_D3D11\_BINDFLAGS](mf-sa-d3d11-bindflags.md) | Specifies the binding flags to use when allocating Direct3D 11 surfaces for media samples. |
| [MF\_SA\_D3D11\_SHARED](mf-sa-d3d11-shared.md) | Indicates to the video sample allocator to create textures as shareable using keyed-mutex. |
| [MF\_SA\_D3D11\_SHARED\_WITHOUT\_MUTEX](mf-sa-d3d11-shared-without-mutex.md) | Indicates to the video sample allocator to create textures as shareable using the legacy mechanism. |
| [MF\_SA\_D3D11\_USAGE](mf-sa-d3d11-usage.md) | Specifies how to allocate Direct3D 11 surfaces for media samples. |
| [MF_SA_D3D12_CLEAR_VALUE](mf-sa-d3d12-clear-value.md) | Contains a blob with the information used to optimize clear operations for the Direct3D resources in the stream. |
| [MF_SA_D3D12_HEAP_FLAGS](mf-sa-d3d12-heap-flags.md) | Contains a value specifying the heap options used for the Direct3D resources in the stream. |
| [MF_SA_D3D12_HEAP_TYPE](mf-sa-d3d12-heap-type.md) | Contains a value specifying the type of heap used for the Direct3D resources in the stream. |
| [MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT](mf-sa-minimum-output-sample-count.md) | Specifies the maximum number of output samples that a Media Foundation transform (MFT) will have outstanding in the pipeline at any time. |
| [MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT\_PROGRESSIVE](mf-sa-minimum-output-sample-count-progressive.md) | Indicates the minimum number of progressive samples that the Media Foundation transform (MFT) should allow to be oustanding at any given time. |
| [MF\_SA\_REQUIRED\_SAMPLE\_COUNT](mf-sa-required-sample-count-attribute.md) | Indicates the number of uncompressed buffers that the enhanced video renderer (EVR) media sink requires for deinterlacing.  |
| [MF\_SA\_REQUIRED\_SAMPLE\_COUNT\_PROGRESSIVE](mf-sa-required-sample-count-progressive.md) | Indicates the number of samples that a Media Foundation transform (MFT) requires to be allocated for progressive content. |
| [MF\_SAMPLEGRABBERSINK\_IGNORE\_CLOCK](mf-samplegrabbersink-ignore-clock.md) | Specifies whether the sample-grabber sink uses the presentation clock to schedule samples. |
| [MF\_SAMPLEGRABBERSINK\_SAMPLE\_TIME\_OFFSET](mf-samplegrabbersink-sample-time-offset-attribute.md) | Offset between the time stamp on each sample received by the sample grabber, and the time when the sample grabber presents the sample.  |
| [MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_BUFFERSIZE](mf-sd-asf-extstrmprop-avg-buffersize-attribute.md) | Specifies the average buffer size, in bytes, needed for a stream in an Advanced Systems Format (ASF) file.  |
| [MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_DATA\_BITRATE](mf-sd-asf-extstrmprop-avg-data-bitrate-attribute.md) | Specifies the average data bit rate, in bits per second, of a stream in an Advanced Systems Format (ASF) file.  |
| [MF\_SD\_ASF\_EXTSTRMPROP\_LANGUAGE\_ID\_INDEX](mf-sd-asf-extstrmprop-language-id-index-attribute.md) | Specifies the language used by a stream in an Advanced Systems Format (ASF) file.  |
| [MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_BUFFERSIZE](mf-sd-asf-extstrmprop-max-buffersize-attribute.md) | Specifies the maximum buffer size, in bytes, needed for a stream in an Advanced Systems Format (ASF) file.  |
| [MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_DATA\_BITRATE](mf-sd-asf-extstrmprop-max-data-bitrate-attribute.md) | Specifies the maximum data bit rate, in bits per second, of a stream in an Advanced Systems Format (ASF) file.  |
| [MF\_SD\_ASF\_METADATA\_DEVICE\_CONFORMANCE\_TEMPLATE](mf-sd-asf-metadata-device-conformance-template-attribute.md) | Specifies the device conformance template for a stream in an Advanced Systems Format (ASF) file.  |
| [MF\_SD\_ASF\_STREAMBITRATES\_BITRATE](mf-sd-asf-streambitrates-bitrate-attribute.md) | Specifies the average bit rate, in bits per second, of a stream in an Advanced Systems Format (ASF) file. This attribute corresponds to the Stream Bitrate Properties Object defined in the ASF specification.  |
| [MF\_SD\_LANGUAGE](mf-sd-language-attribute.md) | Specifies the language for a stream.  |
| [MF\_SD\_MUTUALLY\_EXCLUSIVE](mf-sd-mutually-exclusive.md) | Specifies whether a stream is mutually exclusive with other streams of the same type. |
| [MF\_SD\_PROTECTED](mf-sd-protected-attribute.md) | Indicates whether a stream contains protected content.  |
| [MF\_SD\_SAMI\_LANGUAGE](mf-sd-sami-language-attribute.md) | Contains the Synchronized Accessible Media Interchange (SAMI) language name that is defined for the stream.  |
| [MF\_SD\_STREAM\_NAME](mf-sd-stream-name.md) | Contains the name of a stream. |
| [MF\_SENSORSTREAM\_REQUIRED\_SDDL](mf-sensorstream-required-sddl.md) | This attribute is used to specify a Security Descriptor Definition Language (SDDL) on the stream in order to specify fine grained access rights for a given sensor.  |
| [MF\_SENSORSTREAM\_REQUIRED\_CAPABILITIES](mf-sensorstream-required-capabilities.md) | This attribute contains a semi-colon delimited list of capability strings which specifies the capabilities required for a specific stream. For the list of capability strings that can be included in this attribute, see [DeviceCapability](/uwp/schemas/appxpackage/appxmanifestschema/element-devicecapability). |
| [MF\_SESSION\_APPROX\_EVENT\_OCCURRENCE\_TIME](mf-session-approx-event-occurrence-time-attribute.md) | The approximate time when the Media Session raised an event.  |
| [MF\_SESSION\_CONTENT\_PROTECTION\_MANAGER](mf-session-content-protection-manager-attribute.md) | Provides a callback interface for the application to receive a content enabler object from the protected media path (PMP) session.  |
| [MF\_SESSION\_GLOBAL\_TIME](mf-session-global-time-attribute.md) | Specifies whether topologies have a global start and stop time.  |
| [MF\_SESSION\_QUALITY\_MANAGER](mf-session-quality-manager-attribute.md) | Contains the CLSID of a quality manager for the Media Session.  |
| [MF\_SESSION\_REMOTE\_SOURCE\_MODE](mf-session-remote-source-mode-attribute.md) | Specifies that the media source will be created in a remote process.  |
| [MF\_SESSION\_SERVER\_CONTEXT](mf-session-server-context-attribute.md) | Enables two instances of the Media Session to share the same Protected Media Path (PMP) process.  |
| [MF\_SESSION\_TOPOLOADER](mf-session-topoloader-attribute.md) | Contains the CLSID of a topology loader for the Media Session.  |
| [MF\_SINK\_WRITER\_ASYNC\_CALLBACK](mf-sink-writer-async-callback.md) | Contains a pointer to the application's callback interface for the sink writer. |
| [MF\_SINK\_WRITER\_D3D\_MANAGER](mf-sink-writer-d3d-manager.md) | Contains a pointer to the DXGI Device Manager for the [Sink Writer](sink-writer.md). |
| [MF\_SINK\_WRITER\_DISABLE\_THROTTLING](mf-sink-writer-disable-throttling.md) | Specifies whether the sink writer limits the rate of incoming data. |
| [MF\_SINK\_WRITER\_ENCODER\_CONFIG](mf-sink-writer-encoder-config.md) | Contains a pointer to a property store with encoding properties. |
| [MF\_SOURCE\_READER\_ASYNC\_CALLBACK](mf-source-reader-async-callback.md) | Contains a pointer to the application's callback interface for the [Source Reader](source-reader.md). |
| [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md) | Contains a pointer to the Microsoft [Direct3D Device Manager](direct3d-device-manager.md) for the [Source Reader](source-reader.md). |
| [MF\_SOURCE\_READER\_DISABLE\_CAMERA\_PLUGINS](mf-source-reader-disable-camera-plugins.md) | Disables the use of post-processing camera plug-ins by the [Source Reader](source-reader.md). |
| [MF\_SOURCE\_READER\_DISABLE\_DXVA](mf-source-reader-disable-dxva.md) | Specifies whether the [Source Reader](source-reader.md) enables DirectX Video Acceleration (DXVA) on the video decoder. |
| [MF\_SOURCE\_READER\_DISCONNECT\_MEDIASOURCE\_ON\_SHUTDOWN](mf-source-reader-disconnect-mediasource-on-shutdown.md) | Specifies whether the [Source Reader](source-reader.md) shuts down the media source. |
| [MF\_SOURCE\_READER\_ENABLE\_ADVANCED\_VIDEO\_PROCESSING](mf-source-reader-enable-advanced-video-processing.md) | Enables advanced video processing by the [Source Reader](source-reader.md), including color space conversion, deinterlacing, video resizing, and frame-rate conversion. |
| [MF\_SOURCE\_READER\_ENABLE\_TRANSCODE\_ONLY\_TRANSFORMS](mf-source-reader-enable-transcode-only-transforms.md) | Enables the [Source Reader](source-reader.md) to use Media Foundation transforms (MFTs) that are optimized for transcoding. |
| [MF\_SOURCE\_READER\_ENABLE\_VIDEO\_PROCESSING](mf-source-reader-enable-video-processing.md) | Enables video processing by the [Source Reader](source-reader.md). |
| [MF\_SOURCE\_READER\_MEDIASOURCE\_CHARACTERISTICS](mf-source-reader-mediasource-characteristics.md) | Gets the characteristics of the media source from the [Source Reader](source-reader.md). |
| [MF\_SOURCE\_READER\_MEDIASOURCE\_CONFIG](mf-source-reader-mediasource-config.md) | Contains configuration properties for the [Source Reader](source-reader.md). |
| [MF\_SOURCE\_READER\_PASSTHROUGH\_MODE](mf-source-reader-passthrough-mode.md) | When this attribute is set, the [Source Reader](source-reader.md) passes through video samples backed by the system memory to internal MFTs without automatically copying them into a DirectX texture, even if a Direct3D device manager is present. |
| [MF\_SOURCE\_STREAM\_SUPPORTS\_HW\_CONNECTION](mf-source-stream-supports-hw-connection.md) | Indicates whether a media source supports hardware data flow. |
| [MF\_STF\_VERSION\_DATE](mf-stf-version-date.md) | This attribute stores a [FILETIME](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) representing the date/time stamp of a sensor transform factory. |
| [MF\_STF\_VERSION\_INFO](mf-stf-version-info.md) | This attribute represents the version information sensor transform factory. This is the only attribute that is required for sensor transforms. The value is defined by the sensor transform developer and is treated as opaque by the media pipeline. |
| [MF\_STREAM\_SINK\_SUPPORTS\_HW\_CONNECTION](mf-stream-sink-supports-hw-connection.md) | Indicates whether a media sink supports hardware data flow. |
| [MF\_STREAM\_SINK\_SUPPORTS\_ROTATION](mf-stream-sink-supports-rotation.md) | Indicates whether the stream sink supports video rotation. |
| [MF\_TOPOLOGY\_DXVA\_MODE](mf-topology-dxva-mode.md) | Specifies whether the topology loader enables Microsoft DirectX Video Acceleration (DXVA) in the topology. |
| [MF\_TOPOLOGY\_DYNAMIC\_CHANGE\_NOT\_ALLOWED](mf-topology-dynamic-change-not-allowed.md) | Specifies whether the Media Session attempts to modify the topology when the format of a stream changes.  |
| [MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES](mf-topology-enumerate-source-types.md) | Specifies whether the topology loader enumerates the media types provided by the media source. |
| [MF\_TOPOLOGY\_HARDWARE\_MODE](mf-topology-hardware-mode.md) | Specifies whether to load hardware-based Media Foundation transforms (MFTs) in the topology. |
| [MF\_TOPOLOGY\_NO\_MARKIN\_MARKOUT](mf-topology-no-markin-markout-attribute.md) | Specifies whether the pipeline trims samples.  |
| [MF\_TOPOLOGY\_PLAYBACK\_FRAMERATE](mf-topology-playback-framerate.md) | Specifies the monitor refresh rate. |
| [MF\_TOPOLOGY\_PLAYBACK\_MAX\_DIMS](mf-topology-playback-max-dims.md) | Specifies the size of the destination window for video playback. |
| [MF\_TOPOLOGY\_PROJECTSTART](mf-topology-projectstart-attribute.md) | Specifies the stop time for a topology, relative to the start of the first topology in the sequence. |
| [MF\_TOPOLOGY\_PROJECTSTOP](mf-topology-projectstop-attribute.md) | Specifies the start time for a topology, relative to the start of the first topology in the sequence. |
| [MF\_TOPOLOGY\_RESOLUTION\_STATUS](mf-topology-resolution-status-attribute.md) | Specifies the status of an attempt to resolve a topology.  |
| [MF\_TOPOLOGY\_START\_TIME\_ON\_PRESENTATION\_SWITCH](mf-topology-start-time-on-presentation-switch.md) | Specifies the start time for presentations that are queued after the first presentation. |
| [MF\_TOPOLOGY\_STATIC\_PLAYBACK\_OPTIMIZATIONS](mf-topology-static-playback-optimizations.md) | Enables static optimizations in the video pipeline. |
| [MF\_TOPONODE\_CONNECT\_METHOD](mf-toponode-connect-method-attribute.md) | Specifies how the topology loader connects this topology node, and whether this node is optional.  |
| [MF\_TOPONODE\_D3DAWARE](mf-toponode-d3daware-attribute.md) | Specifies whether the transform associated with a topology node supports DirectX Video Acceleration (DXVA).  |
| [MF\_TOPONODE\_DECODER](mf-toponode-decoder-attribute.md) | Specifies whether a topology node's underlying object is a decoder.  |
| [MF\_TOPONODE\_DECRYPTOR](mf-toponode-decryptor-attribute.md) | Specifies whether a toplogy node's underlying object is a decrypter.  |
| [MF\_TOPONODE\_DISABLE\_PREROLL](mf-toponode-disable-preroll-attribute.md) | Specifies whether the Media Session uses preroll on the media sink represented by this topology node.  |
| [MF\_TOPONODE\_DISCARDABLE](mf-toponode-discardable-attribute.md) | Specifies whether the pipeline can drop samples from a topology node.  |
| [MF\_TOPONODE\_DRAIN](mf-toponode-drain-attribute.md) | Specifies when a transform is drained.  |
| [MF\_TOPONODE\_ERROR\_MAJORTYPE](mf-toponode-error-majortype-attribute.md) | Contains the major media type for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.  |
| [MF\_TOPONODE\_ERROR\_SUBTYPE](mf-toponode-error-subtype-attribute.md) | Contains the media subtype for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.  |
| [MF\_TOPONODE\_ERRORCODE](mf-toponode-errorcode-attribute.md) | Contains the error code from the most recent connection failure for this toplogy node.  |
| [MF\_TOPONODE\_FLUSH](mf-toponode-flush-attribute.md) | Specifies when a transform is flushed.  |
| [MF\_TOPONODE\_LOCKED](mf-toponode-locked-attribute.md) | Specifies whether the media types can be changed on this topology node.  |
| [MF\_TOPONODE\_MARKIN\_HERE](mf-toponode-markin-here-attribute.md) | Specifies whether the pipeline applies mark-in at this node. |
| [MF\_TOPONODE\_MARKOUT\_HERE](mf-toponode-markout-here-attribute.md) | Specifies whether the pipeline applies mark-out at this node. Mark-out is the point where a presentation ends. If pipeline components generate data past the mark-out point, the data is not rendered.  |
| [MF\_TOPONODE\_MEDIASTART](mf-toponode-mediastart-attribute.md) | Specifies the start time of the presentation. |
| [MF\_TOPONODE\_MEDIASTOP](mf-toponode-mediastop-attribute.md) | Specifies the stop time of the presentation. |
| [MF\_TOPONODE\_NOSHUTDOWN\_ON\_REMOVE](mf-toponode-noshutdown-on-remove-attribute.md) | Specifies how the Media Session shuts down an object in the topology. |
| [MF\_TOPONODE\_PRESENTATION\_DESCRIPTOR](mf-toponode-presentation-descriptor-attribute.md) | Contains a pointer to the presentation descriptor for the media source.  |
| [MF\_TOPONODE\_PRIMARYOUTPUT](mf-toponode-primaryoutput-attribute.md) | Indicates which output is the primary output on a tee node.  |
| [MF\_TOPONODE\_RATELESS](mf-toponode-rateless-attribute.md) | Specifies whether the media sink associated with this topology node is rateless.  |
| [MF\_TOPONODE\_SEQUENCE\_ELEMENTID](mf-toponode-sequence-elementid-attribute.md) | Specifies the element that contains this source node.  |
| [MF\_TOPONODE\_SOURCE](mf-toponode-source-attribute.md) | Contains a pointer to the media source associated with a topology node.  |
| [MF\_TOPONODE\_STREAM\_DESCRIPTOR](mf-toponode-stream-descriptor-attribute.md) | Contains a pointer to the stream descriptor for the media source.  |
| [MF\_TOPONODE\_STREAMID](mf-toponode-streamid-attribute.md) | The stream identifier of the stream sink associated with this topology node.  |
| [MF\_TOPONODE\_TRANSFORM\_OBJECTID](mf-toponode-transform-objectid-attribute.md) | The class identifier (CLSID) of the Media Foundation transform (MFT) associated with this topology node.  |
| [MF\_TOPONODE\_WORKQUEUE\_ID](mf-toponode-workqueue-id-attribute.md) | Specifies a work queue for a topology branch. |
| [MF\_TOPONODE\_WORKQUEUE\_ITEM\_PRIORITY](mf-toponode-workqueue-item-priority.md) | Specifies the work-item priority for a branch of the topology. |
| [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS](mf-toponode-workqueue-mmcss-class-attribute.md) | Specifies a [Multimedia Class Scheduler Service](/windows/desktop/ProcThread/multimedia-class-scheduler-service) (MMCSS) task for a topology branch.  |
| [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_PRIORITY](mf-toponode-workqueue-mmcss-priority.md) | Specifies the relative thread priority for a branch of the topology. |
| [MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID](mf-toponode-workqueue-mmcss-taskid-attribute.md) | Specifies a Multimedia Class Scheduler Service (MMCSS) task identifier for a topology branch.  |
| [MF\_TRANSCODE\_ADJUST\_PROFILE](mf-transcode-adjust-profile.md) | Profile flags that define the stream settings for the transcode topology. The flags are defined in the [**MF\_TRANSCODE\_ADJUST\_PROFILE\_FLAGS**](/windows/desktop/api/mfidl/ne-mfidl-mf_transcode_adjust_profile_flags) enumeration. |
| [MF\_TRANSCODE\_CONTAINERTYPE](mf-transcode-containertype.md) | Specifies the container type of an encoded file. |
| [MF\_TRANSCODE\_DONOT\_INSERT\_ENCODER](mf-transcode-donot-insert-encoder.md) | Specifies whether an encoder must be included in the transcode topology. |
| [MF\_TRANSCODE\_ENCODINGPROFILE](mf-transcode-encodingprofile.md) | Specifies the device conformance profile for encoding Advanced Streaming Format (ASF) files. |
| [MF\_TRANSCODE\_QUALITYVSSPEED](mf-transcode-qualityvsspeed.md) | Specifies a number between 0 and 100 that indicates the tradeoff between encoding quality and encoding speed. |
| [MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER](mf-transcode-skip-metadata-transfer.md) | Specifies whether metadata is written to the transcoded file. |
| [MF\_TRANSCODE\_TOPOLOGYMODE](mf-transcode-topologymode.md) | Specifies for a transcode topology whether the topology loader will load hardware-based transforms. |
| [MF\_TRANSFORM\_ASYNC](mf-transform-async.md) | Specifies whether a Media Foundation transform (MFT) performs asynchronous processing. |
| [MF\_TRANSFORM\_ASYNC\_UNLOCK](mf-transform-async-unlock.md) | Enables the use of an asynchronous Media Foundation transform (MFT). |
| [MF\_TRANSFORM\_CATEGORY\_Attribute](mf-transform-category-attribute.md) | Specifies the category for a Media Foundation transform (MFT). |
| [MF\_TRANSFORM\_FLAGS\_Attribute](mf-transform-flags-attribute.md) | Contains flags for a Media Foundation transform (MFT) activation object. |
| [MF\_USER\_DATA\_PAYLOAD](mf-user-data-payload.md) | Sets whether to include a user data payload with the output sample. |
| [MF\_VIDEO\_RENDERER\_EFFECT\_APP\_SERVICE\_NAME](mf-video-renderer-effect-app-service-name.md) | Specifies the name of the video renderer effect app service with which a communication channel will be opened. |
| [MF\_VIDEO\_MAX\_MB\_PER\_SEC](mf-video-max-mb-per-sec.md) | Specifies, on [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform), the maximum macroblock processing rate, in macroblocks per second, that is supported by the hardware encoder. |
| [MF\_VIDEO\_PROCESSOR\_ALGORITHM](mf-video-processor-algorithm.md) | Sets the algorithm used by the video processor.  |
| [MF\_VIDEODSP\_MODE](mf-videodsp-mode.md) | Sets the processing mode of the [**Video Stabilization MFT**](video-stabilization-mft.md). |
| [MF\_VIRTUALCAMERA\_ASSOCIATED\_CAMERA\_SOURCES](mf-virtualcamera-associated-camera-sources.md) | Contains an IMFCollection object containing the IMFMediaSourceEx representing the physical cameras associated with a virtual camera. |
| [MF\_VIRTUALCAMERA\_APP\_PACKAGE\_FAMILY\_NAME](mf-virtualcamera-configuration-app-package-family-name.md) | Specifies the app package family name for a virtual camera configuration application. |
| [MF\_VIRTUALCAMERA\_PROVIDE\_ASSOCIATED\_CAMERA\_SOURCES](mf-virtualcamera-provide-associated-camera-sources.md) | Specifies that the pipeline should provide the list of physical camera sources associated with a virtual camera. |
| [MF\_XVP\_CALLER\_ALLOCATES\_OUTPUT](mf-xvp-caller-allocates-output.md) | Specifies whether that the caller will allocate the textures used for output. |
| [MF\_XVP\_DISABLE\_FRC](mf-xvp-disable-frc.md) | Disables frame-rate conversion in the [**Video Processor MFT**](video-processor-mft.md). |
| [MF\_XVP\_SAMPLE\_LOCK\_TIMEOUT](mf-xvp-sample-lock-timeout.md) | Specifies the timeout value used for sample locking operations in XVP. |
| [MFASFSPLITTER\_PACKET\_BOUNDARY](mfasfsplitter-packet-boundary-attribute.md) | Specifies whether a buffer contains the start of an Advanced Systems Format (ASF) packet.  |
| [MFPROTECTION\_ACP](mfprotection-acp.md) | Specifies Analog Copy Protection (ACP) protection. |
| [MFPROTECTION\_CGMSA](mfprotection-cgmsa.md) | Specifies Copy Generational Management System - A (CGMS-A) protection.  |
| [MFPROTECTION\_CONSTRICTAUDIO](mfprotection-constrictaudio.md) | Specifies to constrict audio. |
| [MFPROTECTION\_CONSTRICTVIDEO](mfprotection-constrictvideo.md) | Specifies to constrict video. |
| [MFPROTECTION\_CONSTRICTVIDEO\_NOOPM](mfprotection-constrictvideo-noopm.md) | This attribute specifies additional protection offered by a video output trust authority(OTA) when a connector does not offer output protection. |
| [MFPROTECTION\_DISABLE](mfprotection-disable.md) | Specifies protection is disabled. |
| [MFPROTECTION\_DISABLE\_SCREEN\_SCRAPE](mfprotection-disable-screen-scrape.md) | Specifies disable screen scrap protection. |
| [MFPROTECTION\_FFT](mfprotection-fft.md) | Specifies FFT protection.  |
| [MFPROTECTION\_GRAPHICS\_TRANSFER\_AES\_ENCRYPTION](mfprotection-graphics-transfer-aes-encryption.md) | Specifies AES DXVA encryption for DXVA decoders. |
| [MFPROTECTION\_HDCP](mfprotection-hdcp.md) | Specifies HDCP High-Bandwidth Digital Content Protection (HDCP) protection. |
| [MFPROTECTION\_PROTECTED\_SURFACE](mfprotection-protected-surface.md) | Specifies a protected surface. |
| [MFPROTECTION\_TRUSTEDAUDIODRIVERS](mfprotection-trustedaudiodrivers.md) | Specifies trusted audio drivers. |
| [MFPROTECTION\_VIDEO\_FRAMES](mfprotection-video-frames.md) | Specifies if an application is allowed access to uncompressed video frames. |
| [MFPROTECTION\_WMDRMOTA](mfprotection-wmdrmota.md) | Specifies Windows Media Digital Rights Management (WMDRM) Output Trust Authority (OTA). |
| [MFPROTECTIONATTRIBUTE\_BEST\_EFFORT](mfprotectionattribute-best-effort.md) | Set as an attribute for an [**IMFOutputSchema**](/windows/desktop/api/mfidl/nn-mfidl-imfoutputschema) object. If this attribute is present, a failed attempt to apply the protection is ignored. If the associated attribute value is **TRUE**, the protection schema with the [MFPROTECTIONATTRIBUTE\_FAIL\_OVER](mfprotectionattribute-fail-over.md) attribute should be applied. |
| [MFPROTECTIONATTRIBUTE\_FAIL\_OVER](mfprotectionattribute-fail-over.md) | Indicates whether the protection fails over to this if the best effort fails. This attribute can be used with [**IMFOutputSchema**](/windows/desktop/api/mfidl/nn-mfidl-imfoutputschema) objects.  |
| [MFSampleExtension\_3DVideo](mfsampleextension-3dvideo.md) | Specifies whether a media sample contains a 3D video frame. |
| [MFSampleExtension\_3DVideo\_SampleFormat](mfsampleextension-3dvideo-sampleformat.md) | Specifies how a 3D video frame is stored in a media sample. |
| [MFSampleExtension\_BottomFieldFirst](mfsampleextension-bottomfieldfirst-attribute.md) | Specifies the field dominance for an interlaced video frame. |
| [MFSampleExtension\_CameraExtrinsics](mfsampleextension-cameraextrinsics.md) | Contains the camera extrinsics for the sample. |
| [MFSampleExtension\_CaptureMetadata](mfsampleextension-capturemetadata.md) | The [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) store for all the metadata related to the capture pipeline. |
| [MFSampleExtension\_CleanPoint](mfsampleextension-cleanpoint-attribute.md) | Indicates whether a sample is a random access point.  |
| [MFSampleExtension\_Content\_KeyID](mfsampleextension-content-keyid.md) | Sets the Key ID for the sample. |
| [MFSampleExtension\_DecodeTimestamp Attribute](mfsampleextension-decodetimestamp.md) | Contains the decode time stamp (DTS) for the sample. |
| [MFSampleExtension\_DerivedFromTopField](mfsampleextension-derivedfromtopfield-attribute.md) | Specifies whether a deinterlaced video frame was derived from the upper field or the lower field. |
| [MFSampleExtension\_DeviceReferenceSystemTime](mfsampleextension-devicereferencesystemtime.md) | Specifies the original device timestamp on the sample. |
| [MFSampleExtension\_DeviceTimestamp](mfsampleextension-devicetimestamp.md) | Contains the time stamp from the device driver. |
| [MFSampleExtension\_Discontinuity](mfsampleextension-discontinuity-attribute.md) | Specifies whether a media sample is the first sample after a gap in the stream.  |
| [MFSampleExtension\_Encryption\_CryptByteBlock](mfsampleextension-encryption-cryptbyteblock.md) | Specifies the encrypted byte block size for sample-based pattern encryption. |
| [MFSampleExtension\_Encryption\_HardwareProtection](mfsampleextension-encryption-hardwareprotection.md) | Specifies whether a media sample is hardware protected.  |
| [MFSampleExtension\_Encryption\_ProtectionScheme](mfsampleextension-encryption-protectionscheme.md) | Specifies the protection scheme for encrypted samples. |
| [MFSampleExtension\_Encryption\_SampleID](mfsampleextension-encryption-sampleid.md) | Specifies the ID of an encrypted sample. |
| [MFSampleExtension\_Encryption\_SkipByteBlock](mfsampleextension-encryption-skipbyteblock.md) | Specifies the clear (non-encrypted) byte block size for sample-based pattern encryption. |
| [MFSampleExtension\_Encryption\_SubSampleMappingSplit](mfsampleextension-encryption-subsamplemappingsplit.md) | Sets the sub-sample mapping for the sample indicating the clear and encrypted bytes in the sample data.  |
| [MFSampleExtension\_FeatureMap](mfsampleextension-featuremap.md) | Contains one MACROBLOCK_DATA structure for each macroblock in the input frame.  |
| [MFSampleExtension\_ForwardedDecodeUnits](mfsampleextension-forwardeddecodeunits.md) | Gets an object of type [**IMFCollection**](/windows/desktop/api/mfobjects/nn-mfobjects-imfcollection) containing [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) objects which contain network abstraction layer units (NALUs) and Supplemental Enhancement Information (SEI) units forwarded by a decoder.  |
| [MFSampleExtension\_ForwardedDecodeUnitType](mfsampleextension-forwardeddecodeunittype.md) | Specifies the type, NALU or SEI, of a unit attached to an [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) in a [MFSampleExtension\_ForwardedDecodeUnits](mfsampleextension-forwardeddecodeunits.md) collection. |
| [MFSampleExtension\_FrameCorruption](mfsampleextension-framecorruption.md) | Specifies whether a video frame is corrupted. |
| [MFSampleExtension\_FramePsnrYuv](mfsampleextension-framepsnryuv.md) | Stores Peak Signal-to-Noise Ratio (PSNR) values for the Y, U, and V planes of an encoded video frame. |
| [MFSampleExtension\_Interlaced](mfsampleextension-interlaced-attribute.md) | Indicates whether a video frame is interlaced or progressive. |
| [MFSampleExtension\_LongTermReferenceFrameInfo](mfsampleextension-longtermreferenceframeinfo.md) | Specifies Long Term Reference (LTR) frame info and is returned on the output sample.  |
| [MFSampleExtension\_MeanAbsoluteDifference](mfsampleextension-meanabsolutedifference.md) | This attribute returns the mean absolute difference (MAD) across all macro-blocks in the Y plane.  |
| [MFSampleExtension\_MULTIPLEXED\_MANAGER](mfsampleextension-multiplexed-manager.md) | Provides an instance of [**IMFMuxStreamSampleManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmuxstreamsamplemanager) which is used to access the collection of samples from the substreams of a multiplexed media source. |
| [MFSampleExtension\_PacketCrossOffsets](mfsampleextension-packetcrossoffsets-attribute.md) | Specifies the offsets to the payload boundaries in a frame for protected samples.  |
| [MFSampleExtension\_PhotoThumbnail](mfsampleextension-photothumbnail.md) | Contains the photo thumbnail of a [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample). |
| [MFSampleExtension\_PhotoThumbnailMediaType](mfsampleextension-photothumbnailmediatype.md) | Contains the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) which describes the image format type contained in the [MFSampleExtension\_PhotoThumbnail](mfsampleextension-photothumbnail.md) attribute. |
| [MFSampleExtension\_PinholeCameraIntrinsics](mfsampleextension-pinholecameraintrinsics.md) | Contains the pinhole camera intrinsics for the sample. |
| [MFSampleExtension\_RepeatFirstField](mfsampleextension-repeatfirstfield-attribute.md) | Specifies whether to repeat the first field in an interlaced frame. This attribute applies to media samples.  |
| [MFSampleExtension\_ROIRectangle](mfsampleextension-roirectangle.md) | Specifies the bounds of the region of interest which indicates the region of the frame that requires different quality.  |
| [MFSampleExtension\_SingleField](mfsampleextension-singlefield-attribute.md) | Specifies whether a video sample contains a single field or two interleaved fields. This attribute applies to media samples.  |
| [MFSampleExtension\_SpatialLayerId](mfsampleextension-spatiallayerid.md) | The spatial layer ID of the data contained in an [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample).  |
| [MFSampleExtension\_TargetGlobalLuminance](mfsampleextension-targetgloballuminance.md) | The value in Nits that specifies the targeted global backlight luminance for the associated video frame.  |
| [MFSampleExtension\_TemporalLayerId](mfsampleextension-temporallayerid.md) | The temporal layer ID of the data contained in an [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample).  |
| [MFSampleExtension\_Token](mfsampleextension-token-attribute.md) | Contains a pointer to the token that was provided to the [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method.  |
| [MFSampleExtension\_VideoDSPMode](mfsampleextension-videodspmode.md) | Indicates whether video stabilization was applied to a video frame. |
| [MFSampleExtension\_VideoEncodeBitsUsedMap](mfsampleextension-videoencodebitsusedmap.md) | Stores a map of the number of bits used for encoding each block in an encoded video frame. |
| [MFSampleExtension\_VideoEncodePictureType](mfsampleextension-videoencodepicturetype.md) | Specifies the type of picture that is output by a video encoder. |
| [MFSampleExtension\_VideoEncodeQP](mfsampleextension-videoencodeqp.md) | Specifies the quantization parameter (QP) that was used to encode a video sample. |
| [MFSampleExtension\_VideoEncodeQPMap](mfsampleextension-videoencodeqpmap.md) | Stores a map of the Quantization Parameter (QP) values used for each block in an encoded video frame. |
| [MFStreamExtension\_CameraExtrinsics](mfstreamextension-cameraextrinsics.md) | Contains the camera extrinsics for the stream. |
| [MFStreamExtension\_PinholeCameraIntrinsics](mfstreamextension-pinholecameraintrinsics.md) | Contains the pinhole camera intrinsics for the stream. |
| [MFT\_CODEC\_MERIT\_Attribute](mft-codec-merit-attribute.md) | Contains the merit value of a hardware codec. |
| [MFT\_AUDIO\_DECODER\_AUDIO\_ENDPOINT\_FORMFACTOR](mft-audio-decoder-audio-endpoint-formfactor-attribute.md) | Specifies the form factor for the audio endpoint device associated with an audio decoder MFT. |
| [MFT\_AUDIO\_DECODER\_AUDIO\_ENDPOINT\_ID](mft-audio-decoder-audio-endpoint-id-attribute.md) | Specifies the identifier for the audio endpoint device associated with an audio decoder MFT. |
| [MFT\_AUDIO\_DECODER\_AUDIO\_ENDPOINT\_DIGITAL\_STEREO\_ONLY](mft-audio-decoder-audio-endpoint-is-digital-stereo-only-attribute.md) | Specifies whether the audio endpoint device associated with an audio decoder MFT only supports uncompressed stereo signals. |
| [MFT\_CONNECTED\_STREAM\_ATTRIBUTE](mft-connected-stream-attribute.md) | Contains a pointer to the stream attributes of the connected stream on a hardware-based Media Foundation transform (MFT). |
| [MFT\_CONNECTED\_TO\_HW\_STREAM](mft-connected-to-hw-stream.md) | Specifies whether a hardware-based Media Foundation transform (MFT) is connected to another hardware-based MFT. |
| [MFT\_DECODER\_EXPOSE\_OUTPUT\_TYPES\_IN\_NATIVE\_ORDER](mft-decoder-expose-output-types-in-native-order.md) | Specifies whether a decoder exposes IYUV/I420 output types (suitable for transcoding) before other formats. |
| [MFT\_DECODER\_FINAL\_VIDEO\_RESOLUTION\_HINT](mft-decoder-final-video-resolution-hint.md) | Specifies the final output resolution of the decoded image, after video processing. |
| [MFT\_DECODER\_OPERATING\_POINT](mft-decoder-operating-point.md) | Specify the decoder’s “operating point”, the scalability layer that the decoder should be operating at when it supports spatial or temporal scalability. |
| [MFT\_ENCODER\_SUPPORTS\_CONFIG\_EVENT](mft-encoder-supports-config-event.md) | Specifies that the MFT encoder supports receiving [MEEncodingParameter](meencodingparameters.md) events while streaming. |
| [MFT\_ENUM\_ADAPTER\_LUID](mft-enum-adapter-luid.md) | Specifies the unique identifier for a video adapter. Use this attribute when calling [**MFTEnum2**](/windows/desktop/api/mfapi/nf-mfapi-mftenum2) to enumerate MFTs associated with a specific adapter.  |
| [MFT\_ENUM\_HARDWARE\_URL\_Attribute](mft-enum-hardware-url-attribute.md) | Contains the symbolic link for a hardware-based Media Foundation transform (MFT). |
| [MFT\_ENUM\_HARDWARE\_VENDOR\_ID\_Attribute](mft-enum-hardware-vendor-id-attribute.md) | Specifies the vendor ID for a hardware-based Media Foundation |
| [MFT\_ENUM\_TRANSCODE\_ONLY\_ATTRIBUTE](mft-enum-transcode-only-attribute.md) | Specifies whether a decoder is optimized for transcoding rather than for playback. |
| [MFT\_ENUM\_VIDEO\_RENDERER\_EXTENSION\_PROFILE](mft-enum-video-renderer-extension-profile.md) | Contains a list of all **VideoRendererExtensionProfile** entries in the **VideoRendererExtensionProfiles** tag of a UWP app manifest file. [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) stores this on the attribute store of the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) object that **MFTEnumEx** creates for MFTs that have an associated UWP manifest containing the **VideoRendererExtensionProfiles** tag.  |
| [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) | Contains an [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) pointer, which can be used to unlock a Media Foundation transform (MFT). The **IMFFieldOfUseMFTUnlock** interface is used to unlock an MFT that has field-of-use restrictions. |
| [MFT\_FRIENDLY\_NAME\_Attribute](mft-friendly-name-attribute.md) | Contains the display name for a hardware-based Media Foundation transform (MFT). |
| [MFT\_HW\_TIMESTAMP\_WITH\_QPC\_Attribute](mft-hw-timestamp-with-qpc-attribute.md) | Specifies whether a hardware device source uses the system time for time stamps. |
| [MFT\_INPUT\_TYPES\_Attributes](mft-input-types-attributes.md) | Contains the registered input types for a Media Foundation transform (MFT). |
| [MFT\_OUTPUT\_TYPES\_Attributes](mft-output-types-attributes.md) | Contains the registered output types for a Media Foundation transform (MFT). |
| [MFT\_PREFERRED\_ENCODER\_PROFILE](mft-preferred-encoder-profile.md) | Contains configuration properties for an encoder. |
| [MFT\_PREFERRED\_OUTPUTTYPE\_Attribute](mft-preferred-outputtype-attribute.md) | Specifies the preferred output format for an encoder. |
| [MFT\_PROCESS\_LOCAL\_Attribute](mft-process-local-attribute.md) | Specifies whether a Media Foundation transform (MFT) is registered only in the application's process. |
| [MFT\_REMUX\_MARK\_I\_PICTURE\_AS\_CLEAN\_POINT](mft-remux-mark-i-picture-as-clean-point.md) | Specifies whether the H.264 video remux MFT should mark I pictures as clean point for better seek-ability. This has the potential for corruptions on seeks in non-conforming final MP4 files.  |
| [MFT\_SUPPORT\_3DVIDEO](mft-support-3dvideo.md) | Specifies whether a Media Foundation transform (MFT) supports 3D stereoscopic video. |
| [MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE](mft-support-dynamic-format-change-attribute.md) | Specifies whether a Media Foundation transform (MFT) supports dynamic format changes.  |
| [MFT\_TRANSFORM\_CLSID\_Attribute](mft-transform-clsid-attribute.md) | Contains the class identifier (CLSID) of a Media Foundation transform (MFT). |
| [VIDEO\_ZOOM\_RECT](video-zoom-rect-attribute.md) | Specifies the source rectangle for video mixer of the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR). The source rectangle is the portion of the video frame that the mixer blits to the destination surface.  |



 

## Related topics

<dl> <dt>

[**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

