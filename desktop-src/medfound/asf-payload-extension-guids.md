---
description: The following GUIDs define payload extensions for Advanced Systems Format (ASF) streams.
ms.assetid: db973b41-1e5c-4bc8-921d-5e9312eb21cb
title: ASF Payload Extension GUIDs (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ASF Payload Extension GUIDs

The following GUIDs define payload extensions for Advanced Systems Format (ASF) streams.



| Constant                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                      |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MFASFSampleExtension_SampleDuration"></span><span id="mfasfsampleextension_sampleduration"></span><span id="MFASFSAMPLEEXTENSION_SAMPLEDURATION"></span><dl> <dt>**MFASFSampleExtension\_SampleDuration**</dt> </dl>         | The data indicates the duration, in milliseconds, of the sample contained in the buffer object.<br/>                                                                       |
| <span id="MFASFSampleExtension_OutputCleanPoint"></span><span id="mfasfsampleextension_outputcleanpoint"></span><span id="MFASFSAMPLEEXTENSION_OUTPUTCLEANPOINT"></span><dl> <dt>**MFASFSampleExtension\_OutputCleanPoint**</dt> </dl> | The data indicates whether the sample is a key frame. A value of zero indicates that the sample is not a key frame. A nonzero value indicates that it is a key frame.<br/> |
| <span id="MFASFSampleExtension_SMPTE"></span><span id="mfasfsampleextension_smpte"></span><span id="MFASFSAMPLEEXTENSION_SMPTE"></span><dl> <dt>**MFASFSampleExtension\_SMPTE**</dt> </dl>                                             | The data is a SMPTE time code.<br/>                                                                                                                                        |
| <span id="MFASFSampleExtension_FileName"></span><span id="mfasfsampleextension_filename"></span><span id="MFASFSAMPLEEXTENSION_FILENAME"></span><dl> <dt>**MFASFSampleExtension\_FileName**</dt> </dl>                                 | The data in the sample extension specifies the name of the file from which the content in the sample was taken.<br/>                                                       |
| <span id="MFASFSampleExtension_ContentType"></span><span id="mfasfsampleextension_contenttype"></span><span id="MFASFSAMPLEEXTENSION_CONTENTTYPE"></span><dl> <dt>**MFASFSampleExtension\_ContentType**</dt> </dl>                     | The data identifies the type of content that the sample contains.<br/>                                                                                                     |
| <span id="MFASFSampleExtension_PixelAspectRatio"></span><span id="mfasfsampleextension_pixelaspectratio"></span><span id="MFASFSAMPLEEXTENSION_PIXELASPECTRATIO"></span><dl> <dt>**MFASFSampleExtension\_PixelAspectRatio**</dt> </dl> | The data indicates the pixel aspect ratio of the content in the sample.<br/>                                                                                               |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[**IMFASFStreamConfig::AddPayloadExtension**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-addpayloadextension)
</dt> <dt>

[**IMFASFStreamConfig::GetPayloadExtension**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getpayloadextension)
</dt> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> </dl>

 

 




