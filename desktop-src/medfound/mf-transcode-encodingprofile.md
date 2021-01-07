---
description: Specifies the device conformance profile for encoding Advanced Streaming Format (ASF) files.
ms.assetid: 9a6b6402-ff53-4399-8616-06b7768a8737
title: MF_TRANSCODE_ENCODINGPROFILE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TRANSCODE\_ENCODINGPROFILE attribute

Specifies the device conformance profile for encoding Advanced Streaming Format (ASF) files.

## Data type

**LPWSTR**

## Get/set

To get this attribute, call [**IMFAttributes::GetAllocatedString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getallocatedstring).

To set this attribute, call [**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring).

## Remarks

Use this attribute when transcoding to a device that supports Windows Media. If this attribute is set, the encoder will use the device conformance profile, or template, for Windows Media codecs. Set the attribute on the transcode profile before building the transcode topology.

The value of this attribute can be any of the conformance template strings listed in the following topics:

-   [Audio Device Conformance Templates](../wmformat/audio-device-conformance-templates.md)
-   [Video Device Conformance Templates](../wmformat/video-device-conformance-templates.md)

For Windows Media Video encoding, the topology builder uses this attribute to set the [**MFPKEY\_DECODERCOMPLEXITYREQUESTED**](mfpkey-decodercomplexityrequestedproperty.md) property on the encoder. The encoder will attempt to use the specified template to encode the content. To get the actual template, traverse the nodes of the transcode topology to get a pointer to the encoder node. Then get the value of the [**MFPKEY\_DECODERCOMPLEXITYPROFILE**](mfpkey-decodercomplexityprofileproperty.md) property from the encoder.

The topology builder also uses the value of this attribute to set the "DeviceConformanceTemplate" property on the ASF media sink.

If this attribute is set, the metadata object of the ASF file is always generated irrespective of the application-specified value of the [MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER](mf-transcode-skip-metadata-transfer.md) attribute.

Typical values for this attribute include the following:



| Value   | Description                      |
|---------|----------------------------------|
| "AP"    | Advanced profile video           |
| "MP"    | Main profile video               |
| "SP"    | Simple profile video             |
| "MP@LL" | Main profile, medium level video |
| "L2"    | Audio profile, <= 160 Kbps    |



 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transcode API](transcode-api.md)
</dt> <dt>

[**IMFTranscodeProfile::GetAudioAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-getaudioattributes)
</dt> <dt>

[**IMFTranscodeProfile::SetAudioAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setaudioattributes)
</dt> <dt>

[**IMFTranscodeProfile::SetVideoAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-getvideoattributes)
</dt> <dt>

[**IMFTranscodeProfile::GetVideoAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setvideoattributes)
</dt> </dl>

 

 
