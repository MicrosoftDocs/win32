---
Description: Specifies the device conformance profile for encoding Advanced Streaming Format (ASF) files.
ms.assetid: 9a6b6402-ff53-4399-8616-06b7768a8737
title: MF\_TRANSCODE\_ENCODINGPROFILE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TRANSCODE\_ENCODINGPROFILE attribute

Specifies the device conformance profile for encoding Advanced Streaming Format (ASF) files.

## Data type

**LPWSTR**

## Get/set

To get this attribute, call [**IMFAttributes::GetAllocatedString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getallocatedstring?branch=master).

To set this attribute, call [**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master).

## Remarks

Use this attribute when transcoding to a device that supports Windows Media. If this attribute is set, the encoder will use the device conformance profile, or template, for Windows Media codecs. Set the attribute on the transcode profile before building the transcode topology.

The value of this attribute can be any of the conformance template strings listed in the following topics:

-   [Audio Device Conformance Templates](wmformat.audio_device_conformance_templates)
-   [Video Device Conformance Templates](wmformat.video_device_conformance_templates)

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
| "L2"    | Audio profile, &lt;= 160 Kbps    |



 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
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

[**IMFTranscodeProfile::GetAudioAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-getaudioattributes?branch=master)
</dt> <dt>

[**IMFTranscodeProfile::SetAudioAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-setaudioattributes?branch=master)
</dt> <dt>

[**IMFTranscodeProfile::SetVideoAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-getvideoattributes?branch=master)
</dt> <dt>

[**IMFTranscodeProfile::GetVideoAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-setvideoattributes?branch=master)
</dt> </dl>

 

 




