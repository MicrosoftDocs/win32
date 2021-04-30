---
description: The following GUIDs define the types for the mutual exclusion object for Advanced Systems Format (ASF) streams.
ms.assetid: 3db8eebd-2e26-4c77-8f66-7d08436c9e42
title: ASF Mutual Exclusion Type GUIDs (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ASF Mutual Exclusion Type GUIDs

The following GUIDs define the types for the mutual exclusion object for Advanced Systems Format (ASF) streams.



| Constant                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MFASFMutexType_Language"></span><span id="mfasfmutextype_language"></span><span id="MFASFMUTEXTYPE_LANGUAGE"></span><dl> <dt>**MFASFMutexType\_Language**</dt> </dl>                 | The streams are mutually exclusive by language. This type of mutual exclusion is similar to the audio tracks on a DVD.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="MFASFMutexType_Bitrate"></span><span id="mfasfmutextype_bitrate"></span><span id="MFASFMUTEXTYPE_BITRATE"></span><dl> <dt>**MFASFMutexType\_Bitrate**</dt> </dl>                     | The streams are mutually exclusive by bit rate. This type of mutual exclusion is also called multiple bit rate (MBR) exclusion.<br/>                                                                                                                                                                                                                                                                                                                                                        |
| <span id="MFASFMutexType_Presentation"></span><span id="mfasfmutextype_presentation"></span><span id="MFASFMUTEXTYPE_PRESENTATION"></span><dl> <dt>**MFASFMutexType\_Presentation**</dt> </dl> | The streams are mutually exclusive by presentation. This type can be used for many scenarios, but it should only be used when the content is the same but takes a different form. For example, two streams containing the same video, one formatted to fill the screen and the other maintaining the original widescreen aspect ratio, should be made mutually exclusive by using this type. Another example is streams containing video of the same scene shot from different angles.<br/> |
| <span id="MFASFMutexType_Unknown"></span><span id="mfasfmutextype_unknown"></span><span id="MFASFMUTEXTYPE_UNKNOWN"></span><dl> <dt>**MFASFMutexType\_Unknown**</dt> </dl>                     | The streams are mutually exclusive based on custom criteria.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                           |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[**IMFASFMutualExclusion::GetType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-gettype)
</dt> <dt>

[**IMFASFMutualExclusion::SetType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-settype)
</dt> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> </dl>

 

 




