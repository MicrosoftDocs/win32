---
description: This section contains reference information for the Microsoft Direct3D 12 video API enumerations.
ms.assetid: 
title: Direct3D 12 Video Enumerations
ms.topic: article
ms.date: 06/03/2019
---

# Direct3D 12 Video Enumerations

This section contains reference information for the Microsoft Direct3D 12 video API enumerations.

## In this section

| Topic                                                                                | Description                                                                                              |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [D3D12_BITSTREAM_ENCRYPTION_TYPE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_bitstream_encryption_type)  | Specifies a bitstream encryption type.|
| [D3D12_FEATURE_VIDEO](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_feature_video)  | Specifies a Direct3D 12 video feature or feature set to query about.|
| [D3D12_VIDEO_DECODE_ARGUMENT_TYPE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_argument_type)  | Specifies the argument type of a D3D12_VIDEO_DECODE_FRAME_ARGUMENT|
| [D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_configuration_flags)  | Specifies the configuration for video decoding.|
| [D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_conversion_support_flags)  | Specifies whether a video decode conversion operation is supported.|
| [D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_histogram_component)  | Specifies indices for arrays of per component histogram information.|
| [D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_histogram_component_flags)  | Flags for indicating a subset of components used with video decode histogram.|
| [D3D12_VIDEO_DECODE_STATUS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_status)  | Specifes the status of a video decode operation.|
| [D3D12_VIDEO_DECODE_SUPPORT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_support_flags)  | Specifies whether a video decoding operation is supported.|
| [D3D12_VIDEO_DECODE_TIER](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_tier)  | Specifies the decoding tier of a hardware video decoder, which determines the required format of application-defined textures and buffers.|
| [D3D12_VIDEO_ENCODER_CODEC](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec)  | Specifies codecs for Direct3D 12 video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_h264_direct_modes)  | Specifies direct modes for H.264 video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_h264_flags)  | Specifies configuration flags for H.264 video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_h264_slices_deblocking_mode_flags)  | A flags enumeration allowing bitwise OR combinations of values from the 
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_h264_slices_deblocking_modes)  | Specifies the slice deblocking mode as defined by the *disable_deblocking_filter_idc* syntax in the H.264 
specification.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_hevc_cusize)  | Specifies possible values for luma coding block sizes for HEVC.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_hevc_flags)  | Specifies configuration flags for HEVC video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_hevc_tusize)  | Specifies possible values for luma transform block sizes for HEVC.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_support_h264_flags)  | Specifies configuration support flags for H.264 video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_codec_configuration_support_hevc_flags)  | Specifies configuration support flags for HEVC video encoding.|
| [D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_encode_error_flags)  | Specifies errors encountered during the ID3D12VideoEncodeCommandList2::EncodeFrame operation.|
| [D3D12_VIDEO_ENCODER_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_flags)  | Specifies flags for video encoder creation.|
| [D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_frame_subregion_layout_mode)  | Specifies video encoder frame subregion layout modes.|
| [D3D12_VIDEO_ENCODER_FRAME_TYPE_H264](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_frame_type_h264)  | Specifies the type of an H.264 video frame.|
| [D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_frame_type_hevc)  | Specifies the type of an HEVC video frame.|
| [D3D12_VIDEO_ENCODER_HEAP_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_heap_flags)  | Specifies heap options for video encoding.|
| [D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_intra_refresh_mode)  | Specifies video encoder intra refresh modes.|
| [D3D12_VIDEO_ENCODER_LEVELS_H264](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_levels_h264)  | Specifies the encoder levels for H.264 encoding.|
| [D3D12_VIDEO_ENCODER_LEVELS_HEVC](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_levels_hevc)  | Specifies the encoder levels for High Efficiency Video Coding (HEVC) encoding.|
| [D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_motion_estimation_precision_mode)  | Specifies motion estimation precision modes for video encoding.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_picture_control_codec_data_h264_flags)  | Specifies flags for the H.264-specific picture control properties.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_picture_control_codec_data_hevc_flags)  | Specifies flags for the HEVC-specific picture control properties.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_picture_control_flags)  | Specifies video encoder picture control flags.|
| [D3D12_VIDEO_ENCODER_PROFILE_H264](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_profile_h264)  | Specifies the encoder profiles for H.264 encoding.|
| [D3D12_VIDEO_ENCODER_PROFILE_HEVC](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_profile_hevc)  | Specifies the encoder profiles for High Efficiency Video Coding (HEVC) encoding.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_rate_control_flags)  | Specifies flags for a 3D12_VIDEO_ENCODER_RATE_CONTROL structure.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_rate_control_mode)  | Specifies video encoder rate control modes.|
| [D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_sequence_control_flags)  | Specifies flags for video encoder sequence control properties.|
| [D3D12_VIDEO_ENCODER_SUPPORT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_support_flags)  | Specifies flags for video encoder features.|
| [D3D12_VIDEO_ENCODER_TIER_HEVC](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_tier_hevc)  | Specifies the encoder tiers for High Efficiency Video Coding (HEVC) encoding.|
| [D3D12_VIDEO_ENCODER_VALIDATION_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_encoder_validation_flags)  | Flags specifying unsupported encoder features.|
| [D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_extension_command_parameter_flags)  | Specifies the usage of the associated video extension command parameter.|
| [D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_extension_command_parameter_stage)  | Specifies the parameter stages for video extension commands.|
| [D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_extension_command_parameter_type)  | Specifies the types of parameters for video extension commands.|
| [D3D12_VIDEO_FIELD_TYPE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_field_type)  | Specifies how a video frame is interlaced.|
| [D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_frame_coded_interlace_type)  | |
| [D3D12_VIDEO_FRAME_STEREO_FORMAT](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_frame_stereo_format)  | Defines the layout in memory of a stereo 3D video frame.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_motion_estimator_search_block_size)  | Defines supported search block sizes for video motion estimation.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_motion_estimator_search_block_size_flags)  | Specifies the motion estimation search block sizes that a video encoder can support.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_motion_estimator_vector_precision)  | Defines vector precision values for video motion estimation.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_motion_estimator_vector_precision_flags)  | Specifies the motion estimation vector precision that a video encoder supports.|
| [D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_alpha_fill_mode)  | Specifies the alpha fill mode for video processing.|
| [D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_auto_processing_flags)  | Specifies the automatic processing features that a video processor can support.|
| [D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_deinterlace_flags)  | Specifies the deinterlacing video processor capabilities.|
| [D3D12_VIDEO_PROCESS_FEATURE_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_feature_flags)  | Specifies the features that a video processor can support.|
| [D3D12_VIDEO_PROCESS_FILTER_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_filter_flags)  | Specifies support for the image filters defined by the D3D12_VIDEO_PROCESS_FILTER enumeration.|
| [D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_input_stream_flags)  | Specifies flags for video processing input streams.|
| [D3D12_VIDEO_PROCESS_ORIENTATION](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_orientation)  | Specifies an orientation operation to be performed by a video processor.|
| [D3D12_VIDEO_PROCESS_SUPPORT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_support_flags)  | Specifies whether a video format and colorspace conversion operation is supported.|
| [D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_protected_resource_support_flags)  | Specifies support for protected resources in video operations.|
| [D3D12_VIDEO_SCALE_SUPPORT_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_scale_support_flags)  | Specifies the scaling capabilities of the video scaler.|


## Related topics

<dl> <dt>

[Direct3D 12 Video APIs](direct3d-12-video-apis.md)
</dt> </dl>

 

 



