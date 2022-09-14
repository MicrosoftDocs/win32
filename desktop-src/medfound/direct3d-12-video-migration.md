---
description: Describes equivalent Direct3D 12 video APIs to previous versions.
ms.assetid: 
title: Migrating to Direct3D 12 video
ms.topic: article
ms.date: 06/03/2019
---

# Migrating to Direct3D 12 video

This article describes the Direct3D 12 video APIs that are used to implement features available in previous versions. In the interest of improving the performance and usability of the highest priority video features, some features from Direct3D 11 are fully or partially unsupported in Direct3D 12. 

Note that, while most features from Direct3D 11 are available in Direct3D 12, the API design has changed, so in many cases there is not a one to one mapping of APIs between the two API sets. The tables below are intended to point you toward the most relevant APIs in Direct3D 12 for each Direct3D 11 API, but the way that you use the new APIs may be significantly different. For example:

- To decode a frame of video, the Direct3D 11 video APIs uses calls to [DecoderBeginFrame](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-decoderbeginframe), [GetDecoderBuffer](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-getdecoderbuffer), [SubmitDecoderBuffers](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-submitdecoderbuffers), and [DecoderEndFrame](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-decoderendframe). With Direct3D 12, a single method is used,  [ID3D12VideoDecodeCommandList::DecodeFrame](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-decodeframe).
- For video processing, Direct3D 11 provided individual methods for setting the various configuration values, such as [VideoProcessorSetOutputColorSpace](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputcolorspace) and [VideoProcessorSetOutputAlphaFillMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputalphafillmode). In Direct3D 12, these values are set when the video processor is created, in the call to [ID3D12VideoDevice::CreateVideoProcessor](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideoprocessor), or when the frame is processed with a call to [ID3D12VideoProcessCommandList1::ProcessFrames1](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videoprocesscommandlist1-processframes1).





## ID3D11VideoContext
Provides the video functionality of a Direct3D 11 device, including video decoding, video processing, GPU-based content protection and video encryption/decryption. This functionality is partially implemented for Direct3D 12.


| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| [ConfigureAuthenticatedChannel](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-configureauthenticatedchannel) | Not implemented |
| [DecoderBeginFrame](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-decoderbeginframe)| [ID3D12VideoDecodeCommandList::DecodeFrame](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-decodeframe),  [D3D12_VIDEO_DECODE_FRAME_ARGUMENT](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_frame_argument), [D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_compressed_bitstream), [D3D12_VIDEO_DECODE_REFERENCE_FRAMES](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_reference_frames) |
| [DecoderEndFrame](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-decoderendframe) | [ID3D12VideoDecodeCommandList](/windows/win32/api/d3d12video/nn-d3d12video-id3d12videodecodecommandlist) |
| [DecoderExtension](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-decoderextension) | Not implemented. |
| [DecryptionBlt](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-decryptionblt)  | Not implemented. |
| [EncryptionBlt](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-encryptionblt) | Not implemented. |
| [FinishSessionKeyRefresh](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-finishsessionkeyrefresh) | Not implemented. |
| [GetDecoderBuffer](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-getdecoderbuffer) | Not implemented. Compressed buffers are app-managed in Direct3D 12. |
| [GetEncryptionBltKey](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-getencryptionbltkey) | Not implemented. | 
| [NegotiateAuthenticatedChannelKeyExchange](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-negotiateauthenticatedchannelkeyexchange) | Not implemented. |
| [NegotiateCryptoSessionKeyExchange](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-negotiatecryptosessionkeyexchange) | Not implemented. |
| [QueryAuthenticatedChannel](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-queryauthenticatedchannel) | Not implemented. |
| [ReleaseDecoderBuffer](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-releasedecoderbuffer) | Not implemented. Compressed buffers are app-managed in Direct3D 12. |
| [StartSessionKeyRefresh](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-startsessionkeyrefresh) | Not implemented |
| [SubmitDecoderBuffers](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-submitdecoderbuffers) | [ID3D12VideoDecodeCommandList::DecodeFrame](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-decodeframe) |
| [VideoProcessorBlt](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorblt) | [ID3D12VideoProcessCommandList1::ProcessFrames1](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videoprocesscommandlist1-processframes1) |
| [VideoProcessorGetOutputAlphaFillMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputalphafillmode) [VideoProcessorSetOutputAlphaFillMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputalphafillmode) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC.AlphaFillMode](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc) |
| [VideoProcessorGetOutputBackgroundColor](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputbackgroundcolor) [VideoProcessorSetOutputBackgroundColor](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputbackgroundcolor) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC.BackgroundColor](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc)  |
| [VideoProcessorGetOutputColorSpace](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputcolorspace) [VideoProcessorSetOutputColorSpace](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputcolorspace) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC.ColorSpace](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc)  |
| [VideoProcessorGetOutputConstriction](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputconstriction) [VideoProcessorSetOutputConstriction](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputconstriction) | Not implemented. Software DRM is not supported. |
| [VideoProcessorGetOutputExtension](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputextension) [VideoProcessorSetOutputExtension](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputextension) | Not implemented. |
| [VideoProcessorGetOutputStereoMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputstereomode) [VideoProcessorSetOutputStereoMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputstereomode) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC.EnableStereo](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc) |
| [VideoProcessorGetOutputTargetRect](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetoutputtargetrect) [VideoProcessorSetOutputTargetRect](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetoutputtargetrect) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS.TargetRectangle](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_arguments) |
| [VideoProcessorGetStreamAlpha](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamalpha) [VideoProcessorSetStreamAlpha](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamalpha)  | [D3D12_VIDEO_PROCESS_ALPHA_BLENDING.Alpha](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_alpha_blending) |
| [VideoProcessorGetStreamAutoProcessingMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamautoprocessingmode) [VideoProcessorSetStreamAutoProcessingMode](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamautoprocessingmode) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC.EnableAutoProcessing](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamColorSpace](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamcolorspace) [VideoProcessorSetStreamColorSpace](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamcolorspace) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.ColorSpace](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamDestRect](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamdestrect) [VideoProcessorSetStreamDestRect](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamdestrect) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.DestinationRectangle](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamExtension](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamextension) [VideoProcessorSetStreamExtension](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamextension) | Not implemented. |
| [VideoProcessorGetStreamFilter](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamfilter) [VideoProcessorSetStreamFilter](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamfilter) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.FilterFlags](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamFrameFormat](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamframeformat) [VideoProcessorSetStreamFrameFormat](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamframeformat) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.Format](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamLumaKey](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamlumakey) [VideoProcessorSetStreamLumaKey](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamlumakey) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.LumaKey](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamOutputRate](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamoutputrate) [VideoProcessorSetStreamOutputRate](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamoutputrate) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC.FrameRate](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc) |
| [VideoProcessorGetStreamPalette](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreampalette) [VideoProcessorSetStreamPalette](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreampalette) | Not implemented |
| [VideoProcessorGetStreamPixelAspectRatio](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreampixelaspectratio) [VideoProcessorSetStreamPixelAspectRatio](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreampixelaspectratio) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.Transform](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments) |
| [VideoProcessorGetStreamRotation](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamrotation) [VideoProcessorSetStreamRotation](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamrotation) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.Transform](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments) |
| [VideoProcessorGetStreamSourceRect](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamsourcerect) [VideoProcessorSetStreamSourceRect](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamsourcerect) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.Transform](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments) |
| [VideoProcessorGetStreamStereoFormat](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorgetstreamstereoformat) [VideoProcessorSetStreamStereoFormat](/windows/win32/api/d3d11/nf-d3d11-id3d11videocontext-videoprocessorsetstreamstereoformat) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.Transform](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments) |

## ID3D11VideoContext1

Provides extended video functionality of a Direct3D 11 device, including hardware DRM,  surface usage improvements, more video processing functionality. This functionality is implemented for Direct3D 12 via new interfaces.


| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| CheckCryptoSessionStatus | TBD | 
| [DecoderEnableDownsampling](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-checkcryptosessionstatus) | [D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_conversion_arguments) |
| [DecoderUpdateDownsampling](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-decoderenabledownsampling) | [D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_conversion_arguments) |
| [GetDataForNewHardwareKey](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-getdatafornewhardwarekey) | TBD |
| [SubmitDecoderBuffers1](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-submitdecoderbuffers1) | [ID3D12VideoDecodeCommandList::DecodeFrame](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-decodeframe) |
| [VideoProcessorGetBehaviorHints](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorgetbehaviorhints) | TBD |
| [VideoProcessorGetOutputColorSpace1](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorgetoutputcolorspace1) [VideoProcessorSetOutputColorSpace1](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorsetoutputcolorspace1) | [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC.ColorSpace](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc) |
| [VideoProcessorGetOutputShaderUsage](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorgetoutputshaderusage) [VideoProcessorSetOutputShaderUsage](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorsetoutputshaderusage) | TBD |
| [VideoProcessorGetStreamColorSpace1](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorgetstreamcolorspace1) [VideoProcessorSetStreamColorSpace1](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorsetstreamcolorspace1) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC.ColorSpace](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc) |
| [VideoProcessorGetStreamMirror](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorgetstreammirror) [VideoProcessorSetStreamMirror](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-videoprocessorsetstreammirror) | [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS.Transform](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments) |

## ID3D11VideoDecoder

Represents a hardware-accelerated video decoder for Direct3D 11. This is a wrapper interface around [ID3D11VideoContext](/windows/win32/api/d3d11/nn-d3d11-id3d11videocontext) which exposes the actual decoding functionality. There is no equivalent API for Direct3D 12 video.


## ID3D11VideoDecoderOutputView

Identifies the output surfaces that can be accessed during video decoding. In Direct3D 12, the [ID3D12VideoProcessor](/windows/win32/api/d3d12video/nn-d3d12video-id3d12videoprocessor) interface uses [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) objects directly.

## ID3D11VideoDevice

Provides the video decoding and video processing capabilities of a Direct3D 11 device. This is the main entry point to create the video decoder device and crypto session, and for video processing, capabilities, profiles, etc. This functionality is partially implemented for Direct3D 12.


| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| [CheckCryptoKeyExchange](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-checkcryptokeyexchange) | Not implemented. |
| [CheckVideoDecoderFormat](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-checkvideodecoderformat) | [D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_formats) |
| [CreateAuthenticatedChannel](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createauthenticatedchannel) | Not implemented. |
| [CreateCryptoSession](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createcryptosession) | Not implemented. |
| [CreateVideoDecoder](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createvideodecoder) | [ID3D12VideoDevice::CreateVideoDecoder](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideodecoder)  [ID3D12VideoDevice::CreateVideoDecoderHeap](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideodecoderheap) |
| [CreateVideoDecoderOutputView](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createvideodecoderoutputview) | [ID3D12Texture2D](/windows/win32/api/d3d11/nn-d3d11-id3d11texture2d) |
| [CreateVideoProcessor](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createvideoprocessor) | [ID3D12VideoDevice::CreateVideoProcessor](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideoprocessor)  |
| [CreateVideoProcessorEnumerator](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createvideoprocessorenumerator) | N/A |
| [CreateVideoProcessorInputView](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createvideoprocessorinputview) | [ID3D12Texture2D](/windows/win32/api/d3d11/nn-d3d11-id3d11texture2d) |
| [CreateVideoProcessorOutputView](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-createvideoprocessoroutputview) | [ID3D12Texture2D](/windows/win32/api/d3d11/nn-d3d11-id3d11texture2d) |
| [GetContentProtectionCaps](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-getcontentprotectioncaps) | TBD
| [GetVideoDecoderConfig](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-getvideodecoderconfig) | Only VLD mode is supported in Direct3D 12. [D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_profiles) [D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_formats) |
| [GetVideoDecoderConfigCount](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-getvideodecoderconfigcount) | N/A |
| [GetVideoDecoderProfile](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-getvideodecoderprofile) | [D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_profiles) |
| [GetVideoDecoderProfileCount](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-getvideodecoderprofilecount) | [D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES.ProfileCount](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_profiles) |
| [SetPrivateData](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-setprivatedata) | [ID3D12Object::SetPrivateData](/windows/win32/api/d3d12/nf-d3d12-id3d12object-setprivatedata) |
| [SetPrivateDataInterface](/windows/win32/api/d3d11/nf-d3d11-id3d11videodevice-setprivatedatainterface) | [ID3D12Object::SetPrivateDataInterface](/windows/win32/api/d3d12/nf-d3d12-id3d12object-setprivatedatainterface) |

## ID3D11VideoDevice1

Provides extended video decoding and video processing capabilities of a Direct3D 11 device, including more extensions, hardware DRM, decode downsampling, video decoder capabilities, etc. This functionality is implemented for Direct3D 12.

| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| [CheckVideoDecoderDownsampling](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videodevice1-checkvideodecoderdownsampling) | [D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_conversion_support) |
| [GetCryptoSessionPrivateDataSize](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videodevice1-getcryptosessionprivatedatasize) | TBD |
| [GetVideoDecoderCaps](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videodevice1-getvideodecodercaps) | [D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_conversion_support) |
| [RecommendVideoDecoderDownsampleParameters](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videodevice1-recommendvideodecoderdownsampleparameters) | [D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_conversion_support) |


## ID3D11VideoProcessor

Represents a video processor for Direct3D 11. This functionality is implemented for Direct3D 12 in the [ID3D12VideoProcessor](/windows/win32/api/d3d12video/nn-d3d12video-id3d12videoprocessor)

| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| [GetContentDesc](/windows/win32/api/d3d11/nf-d3d11-id3d11videoprocessor-getcontentdesc)| Not implemented |
| [GetRateConversionCaps](/windows/win32/api/d3d11/nf-d3d11-id3d11videoprocessor-getrateconversioncaps) | Not implemented |


## ID3D11VideoProcessorEnumerator and ID3D11VideoProcessorEnumerator1

Enumerates the video processor capabilities of a Direct3D 11 device.
In Direct3D 12, enumeration functionality is replaced by [ID3D12VideoDevice::CheckFeatureSupport](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice-checkfeaturesupport). 

##	ID3D11VideoProcessorInputView

Identifies the input surfaces that can be accessed during video processing.
In Direct3D 12, this is replaced by ID3D12Texture2D.

##	ID3D11VideoProcessorOutputView

Identifies the output surfaces that can be accessed during video processing.
In Direct3D 12, this is replaced by ID3D12Texture2D.

## ID3D11AuthenticatedChannel

Provides a secure communication channel with the graphics driver or the Microsoft Direct3D runtime. This functionality is not implemented for Direct3D 12 video.

##	ID3D11CryptoSession

Represents a cryptographic session. Used for software and hardware DRM scenarios. There is no equivalent public API for Direct3D 12 video.

## Related topics

[Direct3D 12 Video APIs](direct3d-12-video-apis.md)


 

 




