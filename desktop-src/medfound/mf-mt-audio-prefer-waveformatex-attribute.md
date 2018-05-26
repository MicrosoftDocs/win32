---
Description: Specifies the preferred legacy format structure to use when converting an audio media type.
ms.assetid: 9bb045a2-be5b-468b-b30b-aedcb7849945
title: MF\_MT\_AUDIO\_PREFER\_WAVEFORMATEX attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AUDIO\_PREFER\_WAVEFORMATEX attribute

Specifies the preferred legacy format structure to use when converting an audio media type.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute provides a hint to the [**MFCreateWaveFormatExFromMFMediaType**](/windows/win32/mfapi/nf-mfapi-mfcreatewaveformatexfrommfmediatype?branch=master) function. If the attribute is **TRUE**, the function converts the audio media type to a [**WAVEFORMATEX**](dshow.waveformatex) structure whenever possible, instead of converting it to a [**WAVEFORMATEXTENSIBLE**](dshow.waveformatextensible) structure.

The [**MFInitMediaTypeFromWaveFormatEx**](/windows/win32/mfapi/nf-mfapi-mfinitmediatypefromwaveformatex?branch=master) function sets this attribute. You can override the value of this attribute, but setting this attribute to **TRUE** does not guarantee that an audio media type can be converted to [**WAVEFORMATEX**](dshow.waveformatex) form.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




