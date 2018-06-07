---
Description: Video Capture Minidriver Enumerations and Structures
ms.assetid: 763f8328-268e-41ef-a2d3-51c585852151
title: Video Capture Minidriver Enumerations and Structures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Video Capture Minidriver Enumerations and Structures

## 

This section describes the enumerations and structures that video capture minidrivers use to pass property values, data format, data range, and general video capture information between the minidriver, the stream class driver, and user-mode applications.

Video capture minidrivers use the following structures:

<dl>

[**DEVCAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagdevcaps)  
[**KS\_ANALOGVIDEOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_analogvideoinfo)  
[**KS\_BITMAPINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_bitmapinfoheader)  
[**KS\_DATAFORMAT\_VBIINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_vbiinfoheader)  
[**KS\_DATAFORMAT\_VIDEOINFO\_PALETTE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_videoinfo_palette)  
[**KS\_DATAFORMAT\_VIDEOINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_videoinfoheader)  
[**KS\_DATAFORMAT\_VIDEOINFOHEADER2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_dataformat_videoinfoheader2)  
[**KS\_DATARANGE\_ANALOGVIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_analogvideo)  
[**KS\_DATARANGE\_MPEG1\_VIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_mpeg1_video)  
[**KS\_DATARANGE\_MPEG2\_VIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_mpeg2_video)  
[**KS\_DATARANGE\_VIDEO\_PALETTE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video_palette)  
[**KS\_DATARANGE\_VIDEO\_VBI**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video_vbi)  
[**KS\_DATARANGE\_VIDEO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video)  
[**KS\_DATARANGE\_VIDEO2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_datarange_video2)  
[**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_frame_info)  
[**KS\_RGBQUAD**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_rgbquad)  
[**KS\_TRUECOLORINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tag_ks_truecolorinfo)  
[**KS\_TVTUNER\_CHANGE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_tvtuner_change_info)  
[**KS\_VBI\_FRAME\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_vbi_frame_info)  
[**KS\_VBIINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_vbiinfoheader)  
[**KS\_VIDEOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_videoinfo)  
[**KS\_VIDEOINFOHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_videoinfoheader)  
[**KS\_VIDEOINFOHEADER2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_videoinfoheader2)  
[**KS\_VIDEO\_STREAM\_CONFIG\_CAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ks_video_stream_config_caps)  
[**KS\_MPEG1VIDEOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_mpeg1videoinfo)  
[**KS\_MPEGVIDEOINFO2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_mpegvideoinfo2)  
[**KS\_MPEGAUDIOINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagks_mpeaudioinfo)  
[**KSMPEGVID\_RECT**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksmpegvid_rect)  
[**MEDIUM\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-medium_info)  
[**TIMECODE\_SAMPLE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtimecode_sample)  
[**TRANSPORT\_STATE**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-transport_state)  
[**TRANSPORTSTATUS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportstatus)  
[**TRANSPORTAUDIOPARMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportaudioparms)  
[**TRANSPORTBASICPARMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportbasicparms)  
[**TRANSPORTVIDEOPARMS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagtransportvideoparms)  
[**TUNER\_ANALOG\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tuner_analog_caps_s)  
</dl>

The following structures are used by their respective properties and events. The appended "\_S" distinguishes a structure from its property or event.

<dl>

[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_caps_s)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_interleave_s)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_allocator_control_surface_size_s)  
[**KSPROPERTY\_CAMERACONTROL\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)  
[**KSPROPERTY\_CAMERACONTROL\_S2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2)  
[**KSPROPERTY\_CAMERACONTROL\_S\_EX**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_s_ex)  
[**KSPROPERTY\_CAMERACONTROL\_FLASH\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_flash_s)  
[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_focal_length_s)  
[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_focal_length_s)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2)  
[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s)  
[**KSPROPERTY\_CAMERACONTROL\_VIDEOSTABILIZATION\_MODE\_S**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s)  
[**KSPROPERTY\_CROSSBAR\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_caps_s)  
[**KSPROPERTY\_CROSSBAR\_PININFO\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_pininfo_s)  
[**KSPROPERTY\_CROSSBAR\_ROUTE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_route_s)  
[**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_droppedframes_current_s)  
[**KSPROPERTY\_EXTDEVICE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_extdevice_s)  
[**KSPROPERTY\_EXTXPORT\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_extxport_s)  
[**KSPROPERTY\_EXTXPORT\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_extxport_node_s)  
[**KSPROPERTY\_TIMECODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_timecode_s)  
[**KSPROPERTY\_TIMECODE\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_timecode_node_s)  
[**KSPROPERTY\_TUNER\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_caps_s)  
[**KSPROPERTY\_TUNER\_IF\_MEDIUM\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_if_medium_s)  
[**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_mode_caps_s)  
[**KSPROPERTY\_TUNER\_MODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_mode_s)  
[**KSPROPERTY\_TUNER\_FREQUENCY\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_frequency_s)  
[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_networktype_scan_caps_s)  
[**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_scan_caps_s)  
[**KSPROPERTY\_TUNER\_SCAN\_STATUS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_scan_status_s)  
[**KSPROPERTY\_TUNER\_STANDARD\_MODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_standard_mode_s)  
[**KSPROPERTY\_TUNER\_STANDARD\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_standard_s)  
[**KSPROPERTY\_TUNER\_INPUT\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_input_s)  
[**KSPROPERTY\_TUNER\_STATUS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_status_s)  
[**KSPROPERTY\_TVAUDIO\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tvaudio_caps_s)  
[**KSPROPERTY\_TVAUDIO\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tvaudio_s)  
[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocompression_getinfo_s)  
[**KSPROPERTY\_VIDEOCOMPRESSION\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocompression_s)  
[**KSPROPERTY\_VIDEOCONTROL\_ACTUAL\_FRAME\_RATE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_actual_frame_rate_s)  
[**KSPROPERTY\_VIDEOCONTROL\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_caps_s)  
[**KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_frame_rates_s)  
[**KSPROPERTY\_VIDEOCONTROL\_MODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videocontrol_mode_s)  
[**KSPROPERTY\_VIDEODECODER\_CAPS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videodecoder_caps_s)  
[**KSPROPERTY\_VIDEODECODER\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videodecoder_s)  
[**KSPROPERTY\_VIDEODECODER\_STATUS\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videodecoder_status_s)  
[**KSPROPERTY\_VIDEOPROCAMP\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videoprocamp_s)  
[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videoprocamp_node_s)  
[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S2**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_videoprocamp_node_s2)  
[**KSPROPERTY\_SELECTOR\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_selector_s)  
[**KSPROPERTY\_SELECTOR\_NODE\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_selector_node_s)  
</dl>

Video capture minidrivers use the following enumerations:

<dl>

[**KS\_AnalogVideoStandard**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_analogvideostandard)  
[**KS\_CameraControlAsyncOperation**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-ks_cameracontrolasyncoperation)  
[**KS\_MPEG2Profile**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_mpeg2profile)  
[**KS\_MPEG2Level**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_mpeg2level)  
[**KS\_TUNER\_TUNING\_FLAGS**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_tuner_tuning_flags)  
[**KS\_TUNER\_STRATEGY**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_tuner_strategy)  
[**KS\_VIDEODECODER\_FLAGS**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_videodecoder_flags)  
[**KS\_CompressionCaps**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_compressioncaps)  
[**KS\_VideoStreamingHints**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_videostreaminghints)  
[**KS\_VideoControlFlags**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_videocontrolflags)  
[**KS\_AMPixAspectRatio**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_ampixaspectratio)  
[**KS\_AMVP\_SELECTFORMATBY**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_amvp_selectformatby)  
[**KS\_AMVP\_MODE**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_amvp_mode)  
[**KSEVENT\_DEVICE**](/windows-hardware/drivers/ddi/content/Ks/ne-ks-ksevent_device)  
[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s)  
</dl>

This following camera driver enumerations are new for Windows 10.

<dl>

[**KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_extendedprop_focusstate)  
[**KSCAMERA\_EXTENDEDPROP\_MetadataAlignment**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_extendedprop_metadataalignment)  
[**KSCAMERA\_EXTENDEDPROP\_ROITYPE**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_extendedprop_roitype)  
[**KSCAMERA\_MetadataId**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_metadataid)  
[**KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-kscamera_perframesetting_item_type)  
[**KSEVENT\_CAMERAEVENT**](/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksevent_cameraevent)  
[**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property)  
[**KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY**](/windows-hardware/drivers/ddi/content/Ksmedia/ne-ksmedia-ksproperty_cameracontrol_perframesetting_property)  
</dl>

The following camera driver structures are new for Windows 10.

<dl>

[**CapturedMetadataExposureCompensation**](https://www.bing.com/search?q=**CapturedMetadataExposureCompensation**)  
[**CapturedMetadataISOGains**](https://www.bing.com/search?q=**CapturedMetadataISOGains**)  
[**CapturedMetadataWhiteBalanceGains**](https://www.bing.com/search?q=**CapturedMetadataWhiteBalanceGains**)  
[**FaceCharacterization**](https://www.bing.com/search?q=**FaceCharacterization**)  
[**FaceCharacterizationBlobHeader**](https://www.bing.com/search?q=**FaceCharacterizationBlobHeader**)  
[**FaceRectInfo**](https://www.bing.com/search?q=**FaceRectInfo**)  
[**FaceRectInfoBlobHeader**](https://www.bing.com/search?q=**FaceRectInfoBlobHeader**)  
[**HistogramBlobHeader**](https://www.bing.com/search?q=**HistogramBlobHeader**)  
[**HistogramDataHeader**](https://www.bing.com/search?q=**HistogramDataHeader**)  
[**HistogramGrid**](https://www.bing.com/search?q=**HistogramGrid**)  
[**HistogramHeader**](https://www.bing.com/search?q=**HistogramHeader**)  
[**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/)  
[**KSCAMERA\_EXTENDEDPROP\_METADATAINFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_metadatainfo)  
[**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)  
[**KSCAMERA\_EXTENDEDPROP\_PROFILE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_kscamera_extendedprop_profile)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPS**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcaps)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPSHEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcapsheader)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_EXPOSURE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_exposure)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_FOCUS**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_focus)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_INFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_info)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrol)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROLHEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrolheader)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_WHITEBALANCE**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_whitebalance)  
[**KSCAMERA\_METADATA\_ITEMHEADER**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_metadata_itemheader)  
[**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-tagkscamera_metadata_photoconfirmation)  
[**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header)  
[**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_cap_item_header)  
[**KSCAMERA\_PERFRAMESETTING\_CUSTOM\_ITEM**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_custom_item)  
[**KSCAMERA\_PERFRAMESETTING\_FRAME\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_frame_header)  
[**KSCAMERA\_PERFRAMESETTING\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_header)  
[**KSCAMERA\_PERFRAMESETTING\_ITEM\_HEADER**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-kscamera_perframesetting_item_header)  
[**KSCAMERA\_PROFILE\_CONCURRENCYINFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_kscamera_profile_concurrencyinfo)  
[**KSCAMERA\_PROFILE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_kscamera_profile_info)  
[**KSCAMERA\_PROFILE\_MEDIAINFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_kscamera_profile_mediainfo)  
[**KSCAMERA\_PROFILE\_PININFO**](/windows-hardware/drivers/ddi/content/Ksmedia/ns-ksmedia-_kscamera_profile_pininfo)  
[**KSDEVICE\_PROFILE\_INFO**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-_ksdevice_profile_info)  
[**KSPROPERTY\_STEPPING\_LONG**](/windows-hardware/drivers/ddi/content/Ks/)  
[**KSPROPERTY\_STEPPING\_LONGLONG**](/windows-hardware/drivers/ddi/content/Ks/)  
[**KSSTREAM\_METADATA\_INFO**](/windows-hardware/drivers/ddi/content/Ks/ns-ks-ksstream_metadata_info)  
[**MetadataTimeStamps**](https://www.bing.com/search?q=**MetadataTimeStamps**)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Minidriver%20Enumerations%20and%20Structures%20%20RELEASE:%20%285/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



