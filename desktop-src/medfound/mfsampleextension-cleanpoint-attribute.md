---
description: Indicates whether a sample is a random access point.
ms.assetid: 03d4bfd8-1148-4551-8e71-05cfba2e15fa
title: MFSampleExtension_CleanPoint attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_CleanPoint attribute

Indicates whether a sample is a random access point.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

This attribute applies to samples. If the attribute is **TRUE**, the sample is a random access point and decoding can begin from this sample. Otherwise, the sample is not a random access point.

If this attribute is not set, the default value is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples


```C++
inline BOOL IsRandomAccessPoint(IMFSample *pSample)
{
    // Check for the "clean point" attribute. Default to FALSE.
    return MFGetAttributeUINT32(pSample, MFSampleExtension_CleanPoint, FALSE);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 




