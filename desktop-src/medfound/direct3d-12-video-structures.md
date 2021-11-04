---
description: This section contains reference information for the Microsoft Direct3D 12 video API structures.
ms.assetid: 
title: Direct3D 12 Video Structures
ms.topic: article
ms.date: 06/03/2019
---

# Direct3D 12 Video Structures

This section contains reference information for the Microsoft Direct3D 12 video API structures.

## In this section

| Topic                                                                                | Description                                                                                              |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_conversion_support)  | Retrieves the list of supported profiles.|
| [D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_formats)  | Retrieves the list of supported formats.|
| [D3D12_FEATURE_DATA_VIDEO_DECODE_HISTOGRAM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_histogram)  | Provides data for calls to ID3D12VideoDevice::CheckFeatureSupport when the feature specified is D3D12_FEATURE_VIDEO_DECODE_HISTOGRAM.|
| [D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_profiles)  | Retrieves the list of supported profiles.|
| [D3D12_FEATURE_DATA_VIDEO_DECODE_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_decode_support)  | Retrieves support information for video decoding.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_codec)  | Retrieves a value indicating if the specified codec is supported for video encoding.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_codec_configuration_support)  | Retrieves a value indicating if the specified codec configuration support parameters are supported for 
the provided HEVC encoding configuration or retrieves the supported configuration for H.264 encoding.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_codec_picture_control_support)  | Retrieves the picture control support for the specified codec and profile.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_frame_subregion_layout_mode)  | Retrieves a value indicating if the specified frame subregion layout mode is supported for the specified 
code, profile, and level.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_HEAP_SIZE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_heap_size)  | Retrieves a value indicating if the specified codec is supported for video encoding as well as the L0 and 
L1 sizes of the heap object.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_INPUT_FORMAT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_input_format)  | Retrieves a value indicating if the specified codec, profile, and format are supported for video encoding.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_INTRA_REFRESH_MODE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_intra_refresh_mode)  | Retrieves a value indicating if the specified intra refresh mode is supported for the specified codec, 
profile, and level.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_OUTPUT_RESOLUTION](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_output_resolution)  | Retrieves the list of supported resolutions for the specified codec.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_OUTPUT_RESOLUTION_RATIOS_COUNT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_output_resolution_ratios_count)  | |
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_PROFILE_LEVEL](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_profile_level)  | Retrieves a value indicating if the specified profile is supported for video encoding.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_RATE_CONTROL_MODE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_rate_control_mode)  | Retrieves a value indicating if the specified rate control mode is supported for video encoding with the 
specified codec|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOLUTION_SUPPORT_LIMITS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_resolution_support_limits)  | Represents the video encoder resolution support limits for a D3D12_FEATURE_DATA_VIDEO_ENCODER_SUPPORT 
structure.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOURCE_REQUIREMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_resource_requirements)  | Retrieves values indicating resource requirements for video encoding with the specified encoding 
configuration.|
| [D3D12_FEATURE_DATA_VIDEO_ENCODER_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_encoder_support)  | Retrieves values indicating support for the specified video encoding features and configuration values.|
| [D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_COUNT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_extension_command_count)  | Retrieves the number of video extension commands.|
| [D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_PARAMETER_COUNT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_extension_command_parameter_count)  | Retrieves the supported number of parameters for the specified parameter stage.|
| [D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_PARAMETERS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_extension_command_parameters)  | Retrieves the list of video extension command parameters for the specified parameter stage.|
| [D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_SIZE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_extension_command_size)  | Checks the allocation size of a video extension command.|
| [D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_extension_command_support)  | Retrieves video extension command support using command-defined input and output structures.|
| [D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMANDS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_extension_commands)  | Retrieves the list of video extension commands from the driver.|
| [D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_motion_estimator)  | Provides data for calls to ID3D12VideoDevice::CheckFeatureSupport when the feature specified is D3D12_FEATURE_VIDEO_MOTION_ESTIMATOR. Retrieves the motion estimation capabilities for a video encoder.|
| [D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR_PROTECTED_RESOURCES](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_motion_estimator_protected_resources)  | Provides data for calls to ID3D12VideoDevice::CheckFeatureSupport when the feature specified is D3D12_FEATURE_VIDEO_MOTION_ESTIMATOR_PROTECTED_RESOURCES. Retrieves the protected resources support for video motion estimation.|
| [D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR_SIZE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_motion_estimator_size)  | Describes the allocation size of a video motion estimator heap.|
| [D3D12_FEATURE_DATA_VIDEO_PROCESS_MAX_INPUT_STREAMS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_process_max_input_streams)  | Retrieves the maximum number of enabled input streams supported by the video processor.|
| [D3D12_FEATURE_DATA_VIDEO_PROCESS_REFERENCE_INFO](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_process_reference_info)  | Retrieves the number of past and future reference frames required for the specified deinterlace mode, filter, rate conversion, or auto processing features.|
| [D3D12_FEATURE_DATA_VIDEO_PROCESS_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_feature_data_video_process_support)  | Provides data for calls to ID3D12VideoDevice::CheckFeatureSupport when the feature specified is D3D12_FEATURE_VIDEO_PROCESS_SUPPORT.|
| [D3D12_QUERY_DATA_VIDEO_DECODE_STATISTICS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_query_data_video_decode_statistics)  | Represents data for a video decode statistics query invoked by calling ID3D12VideoDecodeCommandList::EndQuery.|
| [D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_INPUT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_resolve_video_motion_vector_heap_input)  | Provides input data for calls to ID3D12VideoEncodeCommandList::ResolveMotionVectorHeap.|
| [D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_OUTPUT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_resolve_video_motion_vector_heap_output)  | Receives output data from calls to ID3D12VideoEncodeCommandList::ResolveMotionVectorHeap.|
| [D3D12_RESOURCE_COORDINATE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_resource_coordinate)  | Describes the coordinates of a resource.|
| [D3D12_VIDEO_DECODER_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decoder_desc)  | Describes a ID3D12VideoDecoder.|
| [D3D12_VIDEO_DECODER_HEAP_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decoder_heap_desc)  | Describes a ID3D12VideoDecoderHeap.|
| [D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_compressed_bitstream)  | Represents a compressed bitstream from which video is decoded.|
| [D3D12_VIDEO_DECODE_CONFIGURATION](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_configuration)  | Describes the configuration for a video decoder.|
| [D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_conversion_arguments)  | Specifies the parameters for decode output conversion.|
| [D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_conversion_arguments1)  | Specifies the parameters for decode output conversion.|
| [D3D12_VIDEO_DECODE_FRAME_ARGUMENT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_frame_argument)  | Represents the decode parameters for a frame.|
| [D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_input_stream_arguments)  | Specifies the parameters for the input stream for a video decode operation.|
| [D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_output_histogram)  | Represents the histogram output buffer for a single component.|
| [D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_output_stream_arguments)  | Specifies the parameters for the output stream for a video decode operation.|
| [D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_output_stream_arguments1)  | Specifies the parameters for the output stream for a video decode operation.|
| [D3D12_VIDEO_DECODE_REFERENCE_FRAMES](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_reference_frames)  | Contains the list of reference frames for the current decode operation.|
| [D3D12_VIDEO_DECODE_SUB_SAMPLE_MAPPING_BLOCK](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_sub_sample_mapping_block)  | Defines the encryption byte mapping of sub samples for video decoding.|
| [D3D12_VIDEO_ENCODE_REFERENCE_FRAMES](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encode_reference_frames)  | Represents the reconstructed reference images for an encoding operation.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_configuration)  | Represents a codec configuration structure for video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_configuration_h264)  | Represents codec configuration for H.264 encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_configuration_hevc)  | Represents codec configuration for HEVC encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_configuration_support)  | Represents a codec configuration support structure for video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_configuration_support_h264)  | Represents encoder codec configuration support for H.264 encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_configuration_support_hevc)  | Represents encoder codec configuration support for HEVC encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_picture_control_support)  | Represents picture control support structure for multiple codecs.|
| [D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_H264](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_picture_control_support_h264)  | Represents picture control support settings for H.264 video encoding.|
| [D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_codec_picture_control_support_hevc)  | Represents picture control support settings for HEVC video encoding.|
| [D3D12_VIDEO_ENCODER_COMPRESSED_BITSTREAM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_compressed_bitstream)  | Encapsulates the compressed bitstream output for the encoding operation.|
| [D3D12_VIDEO_ENCODER_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_desc)  | Describes an ID3D12VideoEncoder.|
| [D3D12_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_encode_operation_metadata_buffer)  | Represents a buffer containing metadata about an ID3D12VideoEncodeCommandList2::EncodeFrame operation.|
| [D3D12_VIDEO_ENCODER_ENCODEFRAME_INPUT_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_encodeframe_input_arguments)  | Represents input arguments to ID3D12VideoEncodeCommandList2::EncodeFrame.|
| [D3D12_VIDEO_ENCODER_ENCODEFRAME_OUTPUT_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_encodeframe_output_arguments)  | Represents output arguments to ID3D12VideoEncodeCommandList2::EncodeFrame.|
| [D3D12_VIDEO_ENCODER_FRAME_SUBREGION_METADATA](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_frame_subregion_metadata)  | Represents video encoder frame subregion metadata.|
| [D3D12_VIDEO_ENCODER_HEAP_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_heap_desc)  | Describes a ID3D12VideoEncoderHeap.|
| [D3D12_VIDEO_ENCODER_INTRA_REFRESH](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_intra_refresh)  | Represents intra refresh settings for video encoding.|
| [D3D12_VIDEO_ENCODER_LEVEL_SETTING](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_level_setting)  | Represents a video encoder level setting.|
| [D3D12_VIDEO_ENCODER_LEVEL_TIER_CONSTRAINTS_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_level_tier_constraints_hevc)  | Associates a level and a tier for High Efficiency Video Coding (HEVC) level-setting configuration.|
| [D3D12_VIDEO_ENCODER_OUTPUT_METADATA](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_output_metadata)  | Represents metadata about an ID3D12VideoEncodeCommandList2::EncodeFrame operation.|
| [D3D12_VIDEO_ENCODER_OUTPUT_METADATA_STATISTICS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_output_metadata_statistics)  | Represents encoding statistics about a ID3D12VideoEncodeCommandList2::EncodeFrame operation.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_codec_data)  | Represents the picture level control elements for the associated EncodeFrame command for multiple codecs.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_codec_data_h264)  | Represents the picture level control elements for the associated EncodeFrame command for H.264 encoding.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_LIST_MODIFICATION_OPERATION](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_codec_data_h264_reference_picture_list_modification_operation)  | Represents a picture list modification operation for H264 video encoding.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_MARKING_OPERATION](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_codec_data_h264_reference_picture_marking_operation)  | Describes changes in the reference pictures as memory operations as a tuple of an operation identificator 
and associated parameters needed for the operation.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_codec_data_hevc)  | Represents the picture level control elements for the associated EncodeFrame command for HEVC encoding.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_desc)  | 06/30/2021|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_subregions_layout_data)  | Defines picture control subregions as slices for multiple codecs.|
| [D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_SLICES](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_control_subregions_layout_data_slices)  | Defines subregions as slices for codecs that support this partitioning mode.|
| [D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_resolution_desc)  | Defines a video encoder picture resolution.|
| [D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_RATIO_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_picture_resolution_ratio_desc)  | Defines a resolution ratio as an irreducible fraction.|
| [D3D12_VIDEO_ENCODER_PROFILE_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_profile_desc)  | Describes an encoder profile.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_rate_control)  | Represents a video encoder rate control configuration.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_CBR](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_rate_control_cbr)  | Represents a rate control structure definition for constant bitrate mode.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_rate_control_configuration_params)  | Represents video encoder rate control structure definitions for a D3D12_VIDEO_ENCODER_RATE_CONTROL 
structure.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_CQP](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_rate_control_cqp)  | Represents a rate control structure definition for constant quantization parameter mode.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_QVBR](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_rate_control_qvbr)  | Represents a rate control structure definition for constant quality target with constrained bitrate.|
| [D3D12_VIDEO_ENCODER_RATE_CONTROL_VBR](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_rate_control_vbr)  | Represents a rate control structure definition for variable bitrate mode.|
| [D3D12_VIDEO_ENCODER_RECONSTRUCTED_PICTURE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_reconstructed_picture)  | Represents the reconstructed picture generated from the input frame passed to the encode operation.|
| [D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_H264](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_reference_picture_descriptor_h264)  | Represents a reference picture descriptor for H.264 video encoding.|
| [D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_reference_picture_descriptor_hevc)  | Represents a reference picture descriptor for HEVC video encoding.|
| [D3D12_VIDEO_ENCODER_RESOLVE_METADATA_INPUT_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_resolve_metadata_input_arguments)  | Represents input arguments for a call to ID3D12VideoEncodeCommandList2::ResolveEncoderOutputMetadata.|
| [D3D12_VIDEO_ENCODER_RESOLVE_METADATA_OUTPUT_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_resolve_metadata_output_arguments)  | Represents output arguments for a call to ID3D12VideoEncodeCommandList2::ResolveEncoderOutputMetadata.|
| [D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_sequence_control_desc)  | |
| [D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_sequence_gop_structure)  | Represents the GOP structure for multiple video codecs.|
| [D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_H264](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_sequence_gop_structure_h264)  | Represents the GOP structure for H.264 video encoding.|
| [D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_HEVC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_encoder_sequence_gop_structure_hevc)  | Represents the GOP structure for HEVC video encoding.|
| [D3D12_VIDEO_EXTENSION_COMMAND_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_extension_command_desc)  | Describes a video extension command.|
| [D3D12_VIDEO_EXTENSION_COMMAND_INFO](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_extension_command_info)  | Describes a video extension command.|
| [D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_INFO](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_extension_command_parameter_info)  | Describes a video extension command parameter.|
| [D3D12_VIDEO_FORMAT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_format)  | Defines the combination of a pixel format and color space for a resource content description.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_motion_estimator_desc)  | Describes a ID3D12VideoMotionEstimator. Pass this structure into ID3D12VideoDevice1::CreateVideoMotionEstimator to create an instance of ID3D12VideoMotionEstimator.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_INPUT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_motion_estimator_input)  | Provides input data for calls to ID3D12VideoEncodeCommandList::EstimateMotion.|
| [D3D12_VIDEO_MOTION_ESTIMATOR_OUTPUT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_motion_estimator_output)  | Receives output data from calls to ID3D12VideoEncodeCommandList::EstimateMotion.|
| [D3D12_VIDEO_MOTION_VECTOR_HEAP_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_motion_vector_heap_desc)  | Describes a ID3D12VideoMotionEstimatorHeap. Pass this structure into ID3D12VideoDevice1::CreateVideoMotionEstimatorHeap to create an instance of ID3D12VideoMotionEstimatorHeap.|
| [D3D12_VIDEO_PROCESS_ALPHA_BLENDING](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_alpha_blending)  | Specifies alpha blending parameters for video processing.|
| [D3D12_VIDEO_PROCESS_FILTER_RANGE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_filter_range)  | Defines the range of supported values for an image filter.|
| [D3D12_VIDEO_PROCESS_INPUT_STREAM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream)  | Contains input information for the video processor blend functionality.|
| [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments)  | Specifies input stream arguments for an input stream passed to ID3D12VideoCommandList::ProcessFrames.|
| [D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_desc)  | Specifies the parameters for the input stream for a video process operation.|
| [D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_rate)  | Provides information about the stream rate.|
| [D3D12_VIDEO_PROCESS_LUMA_KEY](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_luma_key)  | Specifies the settings used for luma keying.|
| [D3D12_VIDEO_PROCESS_OUTPUT_STREAM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream)  | Represents the output stream for video processing commands.|
| [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_arguments)  | Specifies output stream arguments for the output passed to ID3D12VideoCommandList::ProcessFrames.|
| [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_desc)  | Specifies output stream arguments for the output passed to ID3D12VideoProcessCommandList::ProcessFrames.|
| [D3D12_VIDEO_PROCESS_REFERENCE_SET](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_reference_set)  | Contains the reference frames needed to perform video processing.|
| [D3D12_VIDEO_PROCESS_TRANSFORM](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_transform)  | Specifies transform parameters for video processing.|
| [D3D12_VIDEO_SAMPLE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_sample)  | Describes the width, height, format, and color space of a picture buffer.|
| [D3D12_VIDEO_SCALE_SUPPORT](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_scale_support)  | Describes the supported scaling range of output sizes for a video scaler.|
| [D3D12_VIDEO_SIZE_RANGE](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_size_range)  | Describes the range of supported sizes for a video scaler.|



## Related topics

<dl> <dt>

[Direct3D 12 Video APIs](direct3d-12-video-apis.md)
</dt> </dl>

 

 



