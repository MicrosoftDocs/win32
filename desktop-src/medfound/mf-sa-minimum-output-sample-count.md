---
Description: 'Specifies the maximum number of output samples that a Microsoft Media Foundation transform (MFT) will have outstanding in the pipeline at any time.'
ms.assetid: '53D393B4-BFF1-430F-9CD1-5071336E6F04'
title: 'MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT attribute'
---

# MF\_SA\_MINIMUM\_OUTPUT\_SAMPLE\_COUNT attribute

Specifies the maximum number of output samples that a Microsoft Media Foundation transform (MFT) will have outstanding in the pipeline at any time.

## Data type

**UINT32**

## Remarks

This attribute applies only to MFTs that use a circular buffer to allocate their own output samples. Other MFTs ignore this attribute.

To set this attribute:

1.  Call [**IMFTransform::GetAttributes**](imftransform-getattributes.md) on the decoder to get an [**IMFAttributes**](imfattributes.md) pointer.
2.  Call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md) to add the attribute.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




