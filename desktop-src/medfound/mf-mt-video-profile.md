---
Description: 'Specifies the profile of video encoding on the output media type. This is an alias of MF\_MT\_MPEG2\_PROFILE attribute.'
ms.assetid: '29D1CCCA-CC11-46F1-A094-8BA8F74F7EE9'
title: 'MF\_MT\_VIDEO\_PROFILE attribute'
---

# MF\_MT\_VIDEO\_PROFILE attribute

Specifies the profile of video encoding on the output media type. This is an alias of [MF\_MT\_MPEG2\_PROFILE](mf-mt-mpeg2-profile-attribute.md) attribute.

## Data type

**UINT32**

## Remarks

**H.264 encoders:**

Supported profiles are exceeded to include [**eAVEncH264VProfile\_ConstrainedBase**](eavench264vprofile.md) and **eAVEncH264VProfile\_ConstrainedHigh**.

Encoders shall support both [**GetValue**](imfmediaevent-getvalue.md) and [**SetValue**](dshow.icodecapi_setvalue) for this attribute.

This is static, so video encoders must be configured before the streaming starts. If the application sets a profile which the encoder does not support, the encoder shall reject the media type.

Recommended default: [**eAVEncH264VProfile\_Main**](eavench264vprofile.md) profile.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




