---
Description: Describes equivalent Direct3D 12 video APIs to previous versions.
ms.assetid: 
title: Migrating to Direct3D 12 video
ms.topic: article
ms.date: 06/03/2019
---

# Migrating to Direct3D 12 video

This article describes equivalent Direct3D 12 video APIs to previous versions. In the interest of improving the performance and usability of the highest priority video features, some features from Direct3D 11 are fully or partially unsupported in Direct3D 12. Feature support is organized by interface identifies cases where there is a one to one mapping of APIs between the two API sets.

## ID3D11AuthenticatedChannel

Provides a secure communication channel with the graphics driver or the Microsoft Direct3D runtime. This functionality is not implemented for Direct3D 12 video.

##	ID3D11CryptoSession

Represents a cryptographic session. Used for software and hardware DRM scenarios. There is no equivalent public API for Direct3D 12 video.

## ID3D11VideoContext
Provides the video functionality of a Direct3D 11 device, including video decoding, video processing, GPU-based content protection and video encryption/decryption. This functionality is partially implemented for Direct3D 12.

| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| ConfigureAuthenticatedChannel | Not implemented |
| DecoderBeginFrame | See Interface: ID3D12VideoCommandList, DecodeFrame,  Struct: D3D12_VIDEO_DECODE_FRAME_ARGUMENT, Struct: D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM and Struct: D3D12_VIDEO_DECODE_REFERENCE_FRAMES. |
| DecoderEndFrame | See Interface: ID3D12VideoCommandList EndFrame is not applicable. |
| DecoderExtension | Not implemented |
| DecryptionBlt  | Not implemented |
| EncryptionBlt | Not implemented |
| FinishSessionKeyRefresh | Not implemented |
| GetDecoderBuffer | Not implemented. Compressed buffers are app managed instead. |
| GetEncryptionBltKey | Not implemented | 
| NegotiateAuthenticatedChannelKeyExchange | Not implemented |
| NegotiateCryptoSessionKeyExchange | See ID3D12CryptoSession for HW DRM. Other Key exchange functionality not implemented. |
| QueryAuthenticatedChannel | Not implemented |
| ReleaseDecoderBuffer | Not implemented. Compressed buffers are app managed instead. |
| StartSessionKeyRefresh | Not implemented |
| SubmitDecoderBuffers | See Method: DecodeFrame |
| VideoProcessorBlt | See Method: ProcessFrames |
| VideoProcessorGetOutputAlphaFillMode | N/A |
| VideoProcessorGetOutputBackgroundColor | N/A |
| VideoProcessorGetOutputColorSpace | N/A |
| VideoProcessorGetOutputConstriction | N/A |
| VideoProcessorGetOutputExtension | N/A |
| VideoProcessorGetOutputStereoMode | N/A |
| VideoProcessorGetOutputTargetRect  | N/A |
| VideoProcessorGetStreamAlpha | N/A |
| VideoProcessorGetStreamAutoProcessingMode | N/A |
| VideoProcessorGetStreamColorSpace | N/A |
| VideoProcessorGetStreamDestRect | N/A |
| VideoProcessorGetStreamExtension | N/A |
| VideoProcessorGetStreamFilter | N/A |
| VideoProcessorGetStreamFrameFormat | N/A |
| VideoProcessorGetStreamLumaKey | N/A |
| VideoProcessorGetStreamOutputRate | N/A |
| VideoProcessorGetStreamPalette | N/A |
| VideoProcessorGetStreamPixelAspectRatio | N/A |
| VideoProcessorGetStreamRotation | N/A |
| VideoProcessorGetStreamSourceRect | N/A |
| VideoProcessorGetStreamStereoFormat | N/A |
| VideoProcessorSetOutputAlphaFillMode | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS AlphaFillMode |
| VideoProcessorSetOutputBackgroundColor | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS BackgroundColor |
| VideoProcessorSetOutputColorSpace | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS ColorSpace |
| VideoProcessorSetOutputConstriction | Not implemented. Software DRM is not supported. |
| VideoProcessorSetOutputExtension | Not implemented. |
| VideoProcessorSetOutputStereoMode | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS StereoEnable |
| VideoProcessorSetOutputTargetRect | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS TargetRectangle |
| VideoProcessorSetStreamAlpha | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS Alpha |
| VideoProcessorSetStreamAutoProcessingMode | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS EnableAutoProcessing |
| VideoProcessorSetStreamColorSpace | SeeStruct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS ColorSpace |
| VideoProcessorSetStreamDestRect | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS DestinationRectangle |
| VideoProcessorSetStreamExtension | Not implemented. |
| VideoProcessorSetStreamFilter | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS FilterFlags/FilterLevels |
| VideoProcessorSetStreamFrameFormat | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS FrameFormat |
| VideoProcessorSetStreamLumaKey | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS LumaKey |
| VideoProcessorSetStreamOutputRate | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS FrameRate |
| VideoProcessorSetStreamPalette | Cut: No use. |
| VideoProcessorSetStreamPixelAspectRatio | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS SourceAspectRatio/DestinationAspectRatio |
| VideoProcessorSetStreamRotation | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS Orientation |
| VideoProcessorSetStreamSourceRect | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS SourceRectangle |
| VideoProcessorSetStreamStereoFormat | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS SourceAspectRatio/DestinationAspectRatio |

## ID3D11VideoContext1

Provides extended video functionality of a Direct3D 11 device, including hardware DRM,  surface usage improvements, more VP functionality. This functionality is implemented for Direct3D 12 via new interfaces.


| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| CheckCryptoSessionStatus | GetStatus | 
| DecoderEnableDownsampling | D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS |
| DecoderUpdateDownsampling | D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS |
| GetDataForNewHardwareKey | SetupHardwareKey |
| SubmitDecoderBuffers1 | See Method: DecodeFrame and Struct: D3D12_VIDEO_DECODE_DECRYPTION_ARGUMENTS. |
| VideoProcessorGetBehaviorHints | TODO |
| VideoProcessorGetOutputColorSpace1 | N/A |
| VideoProcessorGetOutputShaderUsage | N/A |
| VideoProcessorGetStreamColorSpace1 | N/A |
| VideoProcessorGetStreamMirror | N/A |
| VideoProcessorSetOutputColorSpace1 | See Struct: D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS ColorSpace |
| VideoProcessorSetOutputShaderUsage | TODO |
| VideoProcessorSetStreamColorSpace1 | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS ColorSpace |
| VideoProcessorSetStreamMirror | See Struct: D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS Orientation |

## ID3D11VideoDecoder

Represents a hardware-accelerated video decoder for Direct3D 11. This is a wrapper interface. All video decoder functionality is in ID3D11VideoContext instead. There is no equivalent API for Direct3D 12 video.


## ID3D11VideoDecoderOutputView

Identifies the output surfaces that can be accessed during video decoding. In Direct3D 12, the ID3D12VideoProcessor interface uses ID3D12Resources directly.

## ID3D11VideoDevice

Provides the video decoding and video processing capabilities of a Direct3D 11 device. This is the main entry point to create the video decoder device and crypto session, and for video processing, capabilities, profiles, etc. This functionality is partially implemented for Direct3D 12.


| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| CheckCryptoKeyExchange | Not implemented |
| CheckVideoDecoderFormat | See Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS |
| CreateAuthenticatedChannel | Not implemented |
| CreateCryptoSession | Not implemented. HW DRM functionality provided via CreateCryptoSession |
| CreateVideoDecoder | See Method: CreateVideoDecoder and Method: CreateVideoDecodeStream. |
| CreateVideoDecoderOutputView | Replaced by ID3D12Texture2D |
| CreateVideoProcessor | See Method: CreateVideoProcessor and Method: CreateVideoProcessStream |
| CreateVideoProcessorEnumerator | Enumeration doesn’t exist any longer. See Video Processing Support. |
| CreateVideoProcessorInputView | Replaced by ID3D12Texture2D |
| CreateVideoProcessorOutputView | Replaced by ID3D12Texture2D |
| GetContentProtectionCaps | See Content Protection Support.
| GetVideoDecoderConfig | Only VLD mode supported in DX12. Other functionality via Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES and Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS. |
| GetVideoDecoderConfigCount | N/A |
| GetVideoDecoderProfile | See Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES |
| GetVideoDecoderProfileCount | See Method: GetVideoDecodeProfileCount |
| SetPrivateData | See ID3D12Object’s SetPrivateData |
| SetPrivateDataInterface | See ID3D12Object’s SetPrivateDataInterface |

## ID3D11VideoDevice1

Provides extended video decoding and video processing capabilities of a Direct3D 11 device, including more extensions, HWDRM, decode downsampling, video decoder caps, etc. This functionality is implemented for Direct3D 12

| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| CheckVideoDecoderDownsampling | See Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT. |
| GetCryptoSessionPrivateDataSize | See Struct: D3D12_FEATURE_DATA_CRYPTO_SESSION_SUPPORT |
| GetVideoDecoderCaps | See Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_SUPPORT |
| RecommendVideoDecoderDownsampleParameters | See Struct: D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT |


## ID3D11VideoProcessor
Represents a video processor for Direct3D 11
•	Main functionality: vpblit
•	A video driver can implement more than one video proc device. If it does, it implements at least:
o	DXVA2_VideoProcBobDevice.  
o	DXVA2_VideoProcProgressiveDevice.

DX12: Functionality implemented.

| Direct3D 11 |	Direct3D 12 |
|-------------|----------------|
| GetContentDesc | Not implemented |
| GetRateConversionCaps | Not implemented |

See Interface: ID3D12VideoProcessor.

## ID3D11VideoProcessorEnumerator and ID3D11VideoProcessorEnumerator1

Enumerates the video processor capabilities of a Direct3D 11 device.
In Direct3D 12, enumeration functionality is replaced by CheckFeatureSupport. See Video Processing Support.

##	ID3D11VideoProcessorInputView

Identifies the input surfaces that can be accessed during video processing.
In Direct3D 12, this is replaced by ID3D12Texture2D.

##	ID3D11VideoProcessorOutputView

Identifies the output surfaces that can be accessed during video processing.
In Direct3D 12, this is replaced by ID3D12Texture2D.



## Related topics

<dl> <dt>

[Direct3D 12 Video APIs](direct3d-12-video-apis.md)
</dt> </dl>

 

 




