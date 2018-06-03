---
Description: Specifies the preferred legacy format structure to use when converting an audio media type.
ms.assetid: 9bb045a2-be5b-468b-b30b-aedcb7849945
title: MF\_MT\_AUDIO\_PREFER\_WAVEFORMATEX attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_AUDIO\_PREFER\_WAVEFORMATEX attribute

Specifies the preferred legacy format structure to use when converting an audio media type.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute provides a hint to the [**MFCreateWaveFormatExFromMFMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatewaveformatexfrommfmediatype) function. If the attribute is **TRUE**, the function converts the audio media type to a [**WAVEFORMATEX**](https://msdn.microsoft.com/windows/desktop/4f3bf6fb-b15f-43b3-82f1-e7a8a3007057) structure whenever possible, instead of converting it to a [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/windows/desktop/b16cdcab-fa4f-4c9a-b1f3-af459bd33245) structure.

The [**MFInitMediaTypeFromWaveFormatEx**](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromwaveformatex) function sets this attribute. You can override the value of this attribute, but setting this attribute to **TRUE** does not guarantee that an audio media type can be converted to [**WAVEFORMATEX**](https://msdn.microsoft.com/windows/desktop/4f3bf6fb-b15f-43b3-82f1-e7a8a3007057) form.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




