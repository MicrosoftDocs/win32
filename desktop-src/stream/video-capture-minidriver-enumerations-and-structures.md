---
Description: Video Capture Minidriver Enumerations and Structures
ms.assetid: '763f8328-268e-41ef-a2d3-51c585852151'
title: Video Capture Minidriver Enumerations and Structures
---

# Video Capture Minidriver Enumerations and Structures

## 

This section describes the enumerations and structures that video capture minidrivers use to pass property values, data format, data range, and general video capture information between the minidriver, the stream class driver, and user-mode applications.

Video capture minidrivers use the following structures:

<dl>

[**DEVCAPS**](devcaps.md)  
[**KS\_ANALOGVIDEOINFO**](ks-analogvideoinfo.md)  
[**KS\_BITMAPINFOHEADER**](ks-bitmapinfoheader.md)  
[**KS\_DATAFORMAT\_VBIINFOHEADER**](ks-dataformat-vbiinfoheader.md)  
[**KS\_DATAFORMAT\_VIDEOINFO\_PALETTE**](ks-dataformat-videoinfo-palette.md)  
[**KS\_DATAFORMAT\_VIDEOINFOHEADER**](ks-dataformat-videoinfoheader.md)  
[**KS\_DATAFORMAT\_VIDEOINFOHEADER2**](ks-dataformat-videoinfoheader2.md)  
[**KS\_DATARANGE\_ANALOGVIDEO**](ks-datarange-analogvideo.md)  
[**KS\_DATARANGE\_MPEG1\_VIDEO**](ks-datarange-mpeg1-video.md)  
[**KS\_DATARANGE\_MPEG2\_VIDEO**](ks-datarange-mpeg2-video.md)  
[**KS\_DATARANGE\_VIDEO\_PALETTE**](ks-datarange-video-palette.md)  
[**KS\_DATARANGE\_VIDEO\_VBI**](ks-datarange-video-vbi.md)  
[**KS\_DATARANGE\_VIDEO**](ks-datarange-video.md)  
[**KS\_DATARANGE\_VIDEO2**](ks-datarange-video2.md)  
[**KS\_FRAME\_INFO**](ks-frame-info.md)  
[**KS\_RGBQUAD**](ks-rgbquad.md)  
[**KS\_TRUECOLORINFO**](ks-truecolorinfo.md)  
[**KS\_TVTUNER\_CHANGE\_INFO**](ks-tvtuner-change-info.md)  
[**KS\_VBI\_FRAME\_INFO**](ks-vbi-frame-info.md)  
[**KS\_VBIINFOHEADER**](ks-vbiinfoheader.md)  
[**KS\_VIDEOINFO**](ks-videoinfo.md)  
[**KS\_VIDEOINFOHEADER**](ks-videoinfoheader.md)  
[**KS\_VIDEOINFOHEADER2**](ks-videoinfoheader2.md)  
[**KS\_VIDEO\_STREAM\_CONFIG\_CAPS**](ks-video-stream-config-caps.md)  
[**KS\_MPEG1VIDEOINFO**](ks-mpeg1videoinfo.md)  
[**KS\_MPEGVIDEOINFO2**](ks-mpegvideoinfo2.md)  
[**KS\_MPEGAUDIOINFO**](ks-mpegaudioinfo.md)  
[**KSMPEGVID\_RECT**](ksmpegvid-rect.md)  
[**MEDIUM\_INFO**](medium-info.md)  
[**TIMECODE\_SAMPLE**](timecode-sample.md)  
[**TRANSPORT\_STATE**](transport-state.md)  
[**TRANSPORTSTATUS**](transportstatus.md)  
[**TRANSPORTAUDIOPARMS**](transportaudioparms.md)  
[**TRANSPORTBASICPARMS**](transportbasicparms.md)  
[**TRANSPORTVIDEOPARMS**](transportvideoparms.md)  
[**TUNER\_ANALOG\_CAPS\_S**](tuner-analog-caps-s.md)  
</dl>

The following structures are used by their respective properties and events. The appended "\_S" distinguishes a structure from its property or event.

<dl>

[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](ksevent-tuner-initiate-scan-s.md)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS\_S**](ksproperty-allocator-control-capture-caps-s.md)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE\_S**](ksproperty-allocator-control-capture-interleave-s.md)  
[**KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE\_S**](ksproperty-allocator-control-surface-size-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_S**](ksproperty-cameracontrol-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_S2**](ksproperty-cameracontrol-s2.md)  
[**KSPROPERTY\_CAMERACONTROL\_S\_EX**](ksproperty-cameracontrol-s-ex.md)  
[**KSPROPERTY\_CAMERACONTROL\_FLASH\_S**](ksproperty-cameracontrol-flash-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](ksproperty-cameracontrol-focal-length-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](ksproperty-cameracontrol-image-pin-capability-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](ksproperty-cameracontrol-node-focal-length-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](ksproperty-cameracontrol-node-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_NODE\_S2**](ksproperty-cameracontrol-node-s2.md)  
[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](ksproperty-cameracontrol-region-of-interest-s.md)  
[**KSPROPERTY\_CAMERACONTROL\_VIDEOSTABILIZATION\_MODE\_S**](ksproperty-cameracontrol-videostabilization-mode-s.md)  
[**KSPROPERTY\_CROSSBAR\_CAPS\_S**](ksproperty-crossbar-caps-s.md)  
[**KSPROPERTY\_CROSSBAR\_PININFO\_S**](ksproperty-crossbar-pininfo-s.md)  
[**KSPROPERTY\_CROSSBAR\_ROUTE\_S**](ksproperty-crossbar-route-s.md)  
[**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](ksproperty-droppedframes-current-s.md)  
[**KSPROPERTY\_EXTDEVICE\_S**](ksproperty-extdevice-s.md)  
[**KSPROPERTY\_EXTXPORT\_S**](ksproperty-extxport-s.md)  
[**KSPROPERTY\_EXTXPORT\_NODE\_S**](ksproperty-extxport-node-s.md)  
[**KSPROPERTY\_TIMECODE\_S**](ksproperty-timecode-s.md)  
[**KSPROPERTY\_TIMECODE\_NODE\_S**](ksproperty-timecode-node-s.md)  
[**KSPROPERTY\_TUNER\_CAPS\_S**](ksproperty-tuner-caps-s.md)  
[**KSPROPERTY\_TUNER\_IF\_MEDIUM\_S**](ksproperty-tuner-if-medium-s.md)  
[**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](ksproperty-tuner-mode-caps-s.md)  
[**KSPROPERTY\_TUNER\_MODE\_S**](ksproperty-tuner-mode-s.md)  
[**KSPROPERTY\_TUNER\_FREQUENCY\_S**](ksproperty-tuner-frequency-s.md)  
[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](ksproperty-tuner-networktype-scan-caps-s.md)  
[**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](ksproperty-tuner-scan-caps-s.md)  
[**KSPROPERTY\_TUNER\_SCAN\_STATUS\_S**](ksproperty-tuner-scan-status-s.md)  
[**KSPROPERTY\_TUNER\_STANDARD\_MODE\_S**](ksproperty-tuner-standard-mode-s.md)  
[**KSPROPERTY\_TUNER\_STANDARD\_S**](ksproperty-tuner-standard-s.md)  
[**KSPROPERTY\_TUNER\_INPUT\_S**](ksproperty-tuner-input-s.md)  
[**KSPROPERTY\_TUNER\_STATUS\_S**](ksproperty-tuner-status-s.md)  
[**KSPROPERTY\_TVAUDIO\_CAPS\_S**](ksproperty-tvaudio-caps-s.md)  
[**KSPROPERTY\_TVAUDIO\_S**](ksproperty-tvaudio-s.md)  
[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](ksproperty-videocompression-getinfo-s.md)  
[**KSPROPERTY\_VIDEOCOMPRESSION\_S**](ksproperty-videocompression-s.md)  
[**KSPROPERTY\_VIDEOCONTROL\_ACTUAL\_FRAME\_RATE\_S**](ksproperty-videocontrol-actual-frame-rate-s.md)  
[**KSPROPERTY\_VIDEOCONTROL\_CAPS\_S**](ksproperty-videocontrol-caps-s.md)  
[**KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES\_S**](ksproperty-videocontrol-frame-rates-s.md)  
[**KSPROPERTY\_VIDEOCONTROL\_MODE\_S**](ksproperty-videocontrol-mode-s.md)  
[**KSPROPERTY\_VIDEODECODER\_CAPS\_S**](ksproperty-videodecoder-caps-s.md)  
[**KSPROPERTY\_VIDEODECODER\_S**](ksproperty-videodecoder-s.md)  
[**KSPROPERTY\_VIDEODECODER\_STATUS\_S**](ksproperty-videodecoder-status-s.md)  
[**KSPROPERTY\_VIDEOPROCAMP\_S**](ksproperty-videoprocamp-s.md)  
[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S**](ksproperty-videoprocamp-node-s.md)  
[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S2**](ksproperty-videoprocamp-node-s2.md)  
[**KSPROPERTY\_SELECTOR\_S**](ksproperty-selector-s.md)  
[**KSPROPERTY\_SELECTOR\_NODE\_S**](ksproperty-selector-node-s.md)  
</dl>

Video capture minidrivers use the following enumerations:

<dl>

[**KS\_AnalogVideoStandard**](ks-analogvideostandard.md)  
[**KS\_CameraControlAsyncOperation**](ks-cameracontrolasyncoperation.md)  
[**KS\_MPEG2Profile**](ks-mpeg2profile.md)  
[**KS\_MPEG2Level**](ks-mpeg2level.md)  
[**KS\_TUNER\_TUNING\_FLAGS**](ks-tuner-tuning-flags.md)  
[**KS\_TUNER\_STRATEGY**](ks-tuner-strategy.md)  
[**KS\_VIDEODECODER\_FLAGS**](ks-videodecoder-flags.md)  
[**KS\_CompressionCaps**](ks-compressioncaps.md)  
[**KS\_VideoStreamingHints**](ks-videostreaminghints.md)  
[**KS\_VideoControlFlags**](ks-videocontrolflags.md)  
[**KS\_AMPixAspectRatio**](ks-ampixaspectratio.md)  
[**KS\_AMVP\_SELECTFORMATBY**](ks-amvp-selectformatby.md)  
[**KS\_AMVP\_MODE**](ks-amvp-mode.md)  
[**KSEVENT\_DEVICE**](ksevent-device.md)  
[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](ksevent-tuner-initiate-scan-s.md)  
</dl>

This following camera driver enumerations are new for Windows 10.

<dl>

[**KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE**](kscamera-extendedprop-focusstate.md)  
[**KSCAMERA\_EXTENDEDPROP\_MetadataAlignment**](kscamera-extendedprop-metadataalignment.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROITYPE**](kscamera-extendedprop-roitype.md)  
[**KSCAMERA\_MetadataId**](kscamera-metadataid.md)  
[**KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE**](kscamera-perframesetting-item-type.md)  
[**KSEVENT\_CAMERAEVENT**](ksevent-cameraevent.md)  
[**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](ksproperty-cameracontrol-extended-property.md)  
[**KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY**](ksproperty-cameracontrol-perframesetting-property.md)  
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
[**KSCAMERA\_EXTENDEDPROP\_HEADER**](kscamera-extendedprop-header2.md)  
[**KSCAMERA\_EXTENDEDPROP\_METADATAINFO**](kscamera-extendedprop-metadatainfo.md)  
[**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](kscamera-extendedprop-photomode.md)  
[**KSCAMERA\_EXTENDEDPROP\_PROFILE**](kscamera-extendedprop-profile.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPS**](kscamera-extendedprop-roi-configcaps.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPSHEADER**](kscamera-extendedprop-roi-configcapsheader.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_EXPOSURE**](kscamera-extendedprop-roi-exposure.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_FOCUS**](kscamera-extendedprop-roi-focus.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_INFO**](kscamera-extendedprop-roi-info.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL**](kscamera-extendedprop-roi-ispcontrol.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROLHEADER**](kscamera-extendedprop-roi-ispcontrolheader.md)  
[**KSCAMERA\_EXTENDEDPROP\_ROI\_WHITEBALANCE**](kscamera-extendedprop-roi-whitebalance.md)  
[**KSCAMERA\_METADATA\_ITEMHEADER**](kscamera-metadata-itemheader.md)  
[**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](kscamera-metadata-photoconfirmation.md)  
[**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](kscamera-perframesetting-cap-header.md)  
[**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](kscamera-perframesetting-cap-item-header.md)  
[**KSCAMERA\_PERFRAMESETTING\_CUSTOM\_ITEM**](kscamera-perframesetting-custom-item.md)  
[**KSCAMERA\_PERFRAMESETTING\_FRAME\_HEADER**](kscamera-perframesetting-frame-header.md)  
[**KSCAMERA\_PERFRAMESETTING\_HEADER**](kscamera-perframesetting-header.md)  
[**KSCAMERA\_PERFRAMESETTING\_ITEM\_HEADER**](kscamera-perframesetting-item-header.md)  
[**KSCAMERA\_PROFILE\_CONCURRENCYINFO**](kscamera-profile-concurrencyinfo.md)  
[**KSCAMERA\_PROFILE\_INFO**](kscamera-profile-info.md)  
[**KSCAMERA\_PROFILE\_MEDIAINFO**](kscamera-profile-mediainfo.md)  
[**KSCAMERA\_PROFILE\_PININFO**](kscamera-profile-pininfo.md)  
[**KSDEVICE\_PROFILE\_INFO**](ksdevice-profile-info.md)  
[**KSPROPERTY\_STEPPING\_LONG**](ksproperty-stepping-long2.md)  
[**KSPROPERTY\_STEPPING\_LONGLONG**](ksproperty-stepping-longlong2.md)  
[**KSSTREAM\_METADATA\_INFO**](ksstream-metadata-info.md)  
[**MetadataTimeStamps**](metadatatimestamps.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Minidriver%20Enumerations%20and%20Structures%20%20RELEASE:%20%285/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



