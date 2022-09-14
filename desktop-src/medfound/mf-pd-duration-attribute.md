---
description: Specifies the duration of a presentation, in 100-nanosecond units.
ms.assetid: abc21696-ea97-41ff-9341-6d9e9dcb19ec
title: MF_PD_DURATION attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_DURATION attribute

Specifies the duration of a presentation, in 100-nanosecond units.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

Media sources can set this attribute on a presentation descriptor to indicate the duration of the presentation.

This attribute is a signed value, although it is stored as a **UINT64**. However, the attribute should never contain a negative value.

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples

The following example shows how to get the presentation duration from a media source.


```C++
HRESULT GetSourceDuration(IMFMediaSource *pSource, MFTIME *pDuration)
{
    *pDuration = 0;

    IMFPresentationDescriptor *pPD = NULL;

    HRESULT hr = pSource->CreatePresentationDescriptor(&pPD);
    if (SUCCEEDED(hr))
    {
        hr = pPD->GetUINT64(MF_PD_DURATION, (UINT64*)pDuration);
        pPD->Release();
    }
    return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




