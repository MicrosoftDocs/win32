---
Description: Profile flags that define the stream settings for the transcode topology. The flags are defined in the MF\_TRANSCODE\_ADJUST\_PROFILE\_FLAGS enumeration.
ms.assetid: 6782e080-284b-458d-8bc0-6e131a529e7b
title: MF\_TRANSCODE\_ADJUST\_PROFILE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TRANSCODE\_ADJUST\_PROFILE attribute

Profile flags that define the stream settings for the transcode topology. The flags are defined in the [**MF\_TRANSCODE\_ADJUST\_PROFILE\_FLAGS**](/windows/win32/mfidl/ne-mfidl-_mf_transcode_adjust_profile_flags?branch=master) enumeration.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

An application can set this attribute at the container level on the transcode profile. If this attribute is set, the [**MFCreateTranscodeTopology**](/windows/win32/mfidl/nf-mfidl-mfcreatetranscodetopology?branch=master) function changes the stream attributes during topology building, depending on the specified flag. For example, if the application specifies the **MF\_TRANSCODE\_ADJUST\_PROFILE\_DEFAULT** flag, the application-specified stream settings are used to create the profile.

For the video stream, the frame rate is updated based on the media source. If the application does not specify the interlaced mode, the profile is updated to use progressive frames by default.

If the application specifies the **MF\_TRANSCODE\_ADJUST\_PROFILE\_USE\_SOURCE\_ATTRIBUTES** flag, then missing stream attributes are copied from the input media source to the stream settings in the transcode profile.

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

[**IMFTranscodeProfile::SetContainerAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-setcontainerattributes?branch=master)
</dt> </dl>

 

 




