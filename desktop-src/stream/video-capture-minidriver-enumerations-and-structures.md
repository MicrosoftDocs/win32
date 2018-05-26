---
Description: Video Capture Minidriver Enumerations and Structures
ms.assetid: 763f8328-268e-41ef-a2d3-51c585852151
title: Video Capture Minidriver Enumerations and Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Capture Minidriver Enumerations and Structures

## 

This section describes the enumerations and structures that video capture minidrivers use to pass property values, data format, data range, and general video capture information between the minidriver, the stream class driver, and user-mode applications.

Video capture minidrivers use the following structures:

<dl>

[**DEVCAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagdevcaps?branch=master)  
[**KS\_ANALOGVIDEOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_analogvideoinfo?branch=master)  
[**KS\_BITMAPINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_bitmapinfoheader?branch=master)  
[**KS\_DATAFORMAT\_VBIINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_vbiinfoheader?branch=master)  
[**KS\_DATAFORMAT\_VIDEOINFO\_PALETTE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_videoinfo_palette?branch=master)  
[**KS\_DATAFORMAT\_VIDEOINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_videoinfoheader?branch=master)  
[**KS\_DATAFORMAT\_VIDEOINFOHEADER2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_videoinfoheader2?branch=master)  
[**KS\_DATARANGE\_ANALOGVIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_analogvideo?branch=master)  
[**KS\_DATARANGE\_MPEG1\_VIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_mpeg1_video?branch=master)  
[**KS\_DATARANGE\_MPEG2\_VIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_mpeg2_video?branch=master)  
[**KS\_DATARANGE\_VIDEO\_PALETTE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video_palette?branch=master)  
[**KS\_DATARANGE\_VIDEO\_VBI**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video_vbi?branch=master)  
[**KS\_DATARANGE\_VIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video?branch=master)  
[**KS\_DATARANGE\_VIDEO2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video2?branch=master)  
[**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_frame_info?branch=master)  
[**KS\_RGBQUAD**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_rgbquad?branch=master)  
[**KS\_TRUECOLORINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tag_ks_truecolorinfo?branch=master)  
[**KS\_TVTUNER\_CHANGE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_tvtuner_change_info?branch=master)  
[**KS\_VBI\_FRAME\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_vbi_frame_info?branch=master)  
[**KS\_VBIINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_vbiinfoheader?branch=master)  
[**KS\_VIDEOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_videoinfo?branch=master)  
[**KS\_VIDEOINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_videoinfoheader?branch=master)  
[**KS\_VIDEOINFOHEADER2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_videoinfoheader2?branch=master)  
[**KS\_VIDEO\_STREAM\_CONFIG\_CAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ks_video_stream_config_caps?branch=master)  
[**KS\_MPEG1VIDEOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_mpeg1videoinfo?branch=master)  
[**KS\_MPEGVIDEOINFO2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_mpegvideoinfo2?branch=master)  
[**KS\_MPEGAUDIOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_mpeaudioinfo?branch=master)  
[**KSMPEGVID\_RECT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksmpegvid_rect?branch=master)  
[**MEDIUM\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-medium_info?branch=master)  
[**TIMECODE\_SAMPLE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtimecode_sample?branch=master)  
[**TRANSPORT\_STATE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-transport_state?branch=master)  
[**TRANSPORTSTATUS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportstatus?branch=master)  
[**TRANSPORTAUDIOPARMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportaudioparms?branch=master)  
[**TRANSPORTBASICPARMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportbasicparms?branch=master)  
[**TRANSPORTVIDEOPARMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportvideoparms?branch=master)  
[**TUNER\_ANALOG\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tuner_analog_caps_s?branch=master)  
</dl>

The following structures are used by their respective properties and events. The appended "\_S" distinguishes a structure from its property or event.

<dl>

[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s?branch=master)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_caps_s?branch=master)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_interleave_s?branch=master)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_allocator_control_surface_size_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_S2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_S\_EX**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_s_ex?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_FLASH\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_flash_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_focal_length_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_focal_length_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_VIDEOSTABILIZATION\_MODE\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s?branch=master)  
[**KSPROPERTY\_CROSSBAR\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_caps_s?branch=master)  
[**KSPROPERTY\_CROSSBAR\_PININFO\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_pininfo_s?branch=master)  
[**KSPROPERTY\_CROSSBAR\_ROUTE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s?branch=master)  
[**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_droppedframes_current_s?branch=master)  
[**KSPROPERTY\_EXTDEVICE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_extdevice_s?branch=master)  
[**KSPROPERTY\_EXTXPORT\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_extxport_s?branch=master)  
[**KSPROPERTY\_EXTXPORT\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_extxport_node_s?branch=master)  
[**KSPROPERTY\_TIMECODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_timecode_s?branch=master)  
[**KSPROPERTY\_TIMECODE\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_timecode_node_s?branch=master)  
[**KSPROPERTY\_TUNER\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_caps_s?branch=master)  
[**KSPROPERTY\_TUNER\_IF\_MEDIUM\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_if_medium_s?branch=master)  
[**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_mode_caps_s?branch=master)  
[**KSPROPERTY\_TUNER\_MODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_mode_s?branch=master)  
[**KSPROPERTY\_TUNER\_FREQUENCY\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_frequency_s?branch=master)  
[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_networktype_scan_caps_s?branch=master)  
[**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_scan_caps_s?branch=master)  
[**KSPROPERTY\_TUNER\_SCAN\_STATUS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_scan_status_s?branch=master)  
[**KSPROPERTY\_TUNER\_STANDARD\_MODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_standard_mode_s?branch=master)  
[**KSPROPERTY\_TUNER\_STANDARD\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_standard_s?branch=master)  
[**KSPROPERTY\_TUNER\_INPUT\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_input_s?branch=master)  
[**KSPROPERTY\_TUNER\_STATUS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_status_s?branch=master)  
[**KSPROPERTY\_TVAUDIO\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tvaudio_caps_s?branch=master)  
[**KSPROPERTY\_TVAUDIO\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tvaudio_s?branch=master)  
[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocompression_getinfo_s?branch=master)  
[**KSPROPERTY\_VIDEOCOMPRESSION\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocompression_s?branch=master)  
[**KSPROPERTY\_VIDEOCONTROL\_ACTUAL\_FRAME\_RATE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_actual_frame_rate_s?branch=master)  
[**KSPROPERTY\_VIDEOCONTROL\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s?branch=master)  
[**KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_frame_rates_s?branch=master)  
[**KSPROPERTY\_VIDEOCONTROL\_MODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_mode_s?branch=master)  
[**KSPROPERTY\_VIDEODECODER\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videodecoder_caps_s?branch=master)  
[**KSPROPERTY\_VIDEODECODER\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videodecoder_s?branch=master)  
[**KSPROPERTY\_VIDEODECODER\_STATUS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videodecoder_status_s?branch=master)  
[**KSPROPERTY\_VIDEOPROCAMP\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videoprocamp_s?branch=master)  
[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videoprocamp_node_s?branch=master)  
[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videoprocamp_node_s2?branch=master)  
[**KSPROPERTY\_SELECTOR\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_selector_s?branch=master)  
[**KSPROPERTY\_SELECTOR\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_selector_node_s?branch=master)  
</dl>

Video capture minidrivers use the following enumerations:

<dl>

[**KS\_AnalogVideoStandard**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_analogvideostandard?branch=master)  
[**KS\_CameraControlAsyncOperation**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-ks_cameracontrolasyncoperation?branch=master)  
[**KS\_MPEG2Profile**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_mpeg2profile?branch=master)  
[**KS\_MPEG2Level**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_mpeg2level?branch=master)  
[**KS\_TUNER\_TUNING\_FLAGS**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_tuner_tuning_flags?branch=master)  
[**KS\_TUNER\_STRATEGY**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_tuner_strategy?branch=master)  
[**KS\_VIDEODECODER\_FLAGS**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_videodecoder_flags?branch=master)  
[**KS\_CompressionCaps**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_compressioncaps?branch=master)  
[**KS\_VideoStreamingHints**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_videostreaminghints?branch=master)  
[**KS\_VideoControlFlags**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_videocontrolflags?branch=master)  
[**KS\_AMPixAspectRatio**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_ampixaspectratio?branch=master)  
[**KS\_AMVP\_SELECTFORMATBY**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_amvp_selectformatby?branch=master)  
[**KS\_AMVP\_MODE**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_amvp_mode?branch=master)  
[**KSEVENT\_DEVICE**](/windows-hardware/drivers/ddi/content/Ks/ne-ks-ksevent_device?branch=master)  
[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s?branch=master)  
</dl>

This following camera driver enumerations are new for Windows 10.

<dl>

[**KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_extendedprop_focusstate?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_MetadataAlignment**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_extendedprop_metadataalignment?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROITYPE**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_extendedprop_roitype?branch=master)  
[**KSCAMERA\_MetadataId**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_metadataid?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_perframesetting_item_type?branch=master)  
[**KSEVENT\_CAMERAEVENT**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksevent_cameraevent?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property?branch=master)  
[**KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-ksproperty_cameracontrol_perframesetting_property?branch=master)  
</dl>

The following camera driver structures are new for Windows 10.

<dl>

[**CapturedMetadataExposureCompensation**](capturedmetadataexposurecompensation.md)  
[**CapturedMetadataISOGains**](capturedmetadataisogains.md)  
[**CapturedMetadataWhiteBalanceGains**](capturedmetadatawhitebalancegains.md)  
[**FaceCharacterization**](facecharacterization.md)  
[**FaceCharacterizationBlobHeader**](facecharacterizationblobheader.md)  
[**FaceRectInfo**](facerectinfo.md)  
[**FaceRectInfoBlobHeader**](facerectinfoblobheader.md)  
[**HistogramBlobHeader**](histogramblobheader.md)  
[**HistogramDataHeader**](histogramdataheader.md)  
[**HistogramGrid**](histogramgrid.md)  
[**HistogramHeader**](histogramheader.md)  
[**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_METADATAINFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_metadatainfo?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_PROFILE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_kscamera_extendedprop_profile?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPS**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcaps?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPSHEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcapsheader?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_EXPOSURE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_exposure?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_FOCUS**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_focus?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_INFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_info?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrol?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROLHEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrolheader?branch=master)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_WHITEBALANCE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_whitebalance?branch=master)  
[**KSCAMERA\_METADATA\_ITEMHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_metadata_itemheader?branch=master)  
[**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_metadata_photoconfirmation?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_cap_item_header?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_CUSTOM\_ITEM**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_custom_item?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_FRAME\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_frame_header?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_header?branch=master)  
[**KSCAMERA\_PERFRAMESETTING\_ITEM\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_item_header?branch=master)  
[**KSCAMERA\_PROFILE\_CONCURRENCYINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_kscamera_profile_concurrencyinfo?branch=master)  
[**KSCAMERA\_PROFILE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_kscamera_profile_info?branch=master)  
[**KSCAMERA\_PROFILE\_MEDIAINFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_kscamera_profile_mediainfo?branch=master)  
[**KSCAMERA\_PROFILE\_PININFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_kscamera_profile_pininfo?branch=master)  
[**KSDEVICE\_PROFILE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksdevice_profile_info?branch=master)  
[**KSPROPERTY\_STEPPING\_LONG**](/windows-hardware/drivers/ddi/content/Ks/?branch=master)  
[**KSPROPERTY\_STEPPING\_LONGLONG**](/windows-hardware/drivers/ddi/content/Ks/?branch=master)  
[**KSSTREAM\_METADATA\_INFO**](/windows-hardware/drivers/ddi/content/Ks/ns-ks-ksstream_metadata_info?branch=master)  
[**MetadataTimeStamps**](metadatatimestamps.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Minidriver%20Enumerations%20and%20Structures%20%20RELEASE:%20%285/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



