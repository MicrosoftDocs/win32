---
description: Profile flags that define the stream settings for the transcode topology. The flags are defined in the MF\_TRANSCODE\_ADJUST\_PROFILE\_FLAGS enumeration.
ms.assetid: 6782e080-284b-458d-8bc0-6e131a529e7b
title: MF_TRANSCODE_ADJUST_PROFILE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TRANSCODE\_ADJUST\_PROFILE attribute

Profile flags that define the stream settings for the transcode topology. The flags are defined in the [**MF\_TRANSCODE\_ADJUST\_PROFILE\_FLAGS**](/windows/desktop/api/mfidl/ne-mfidl-mf_transcode_adjust_profile_flags) enumeration.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

An application can set this attribute at the container level on the transcode profile. If this attribute is set, the [**MFCreateTranscodeTopology**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetranscodetopology) function changes the stream attributes during topology building, depending on the specified flag. For example, if the application specifies the **MF\_TRANSCODE\_ADJUST\_PROFILE\_DEFAULT** flag, the application-specified stream settings are used to create the profile.

For the video stream, the frame rate is updated based on the media source. If the application does not specify the interlaced mode, the profile is updated to use progressive frames by default.

If the application specifies the **MF\_TRANSCODE\_ADJUST\_PROFILE\_USE\_SOURCE\_ATTRIBUTES** flag, then missing stream attributes are copied from the input media source to the stream settings in the transcode profile.

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

[**IMFTranscodeProfile::SetContainerAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setcontainerattributes)
</dt> </dl>

 

 




