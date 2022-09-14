---
description: Offset between the time stamp on each sample received by the sample grabber, and the time when the sample grabber presents the sample.
ms.assetid: 8d06b415-aafc-4276-9a88-4b7262df62f1
title: MF_SAMPLEGRABBERSINK_SAMPLE_TIME_OFFSET attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SAMPLEGRABBERSINK\_SAMPLE\_TIME\_OFFSET attribute

Offset between the time stamp on each sample received by the sample grabber, and the time when the sample grabber presents the sample.

## Data type

**UINT64**

## Remarks

You can set this attribute on the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) object that is returned by the [**MFCreateSampleGrabberSinkActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesamplegrabbersinkactivate) function. This attribute enables the sample grabber's callback function to receive samples earlier than the presentation time.

When the sample grabber receives a new sample, it presents the sample at time *t* − *offset*, where *t* is the time stamp on the sample and *offset* is the value of this attribute. If this attribute is not set, the default value is zero.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64)
</dt> <dt>

[**IMFSampleGrabberSinkCallback**](/windows/desktop/api/mfidl/nn-mfidl-imfsamplegrabbersinkcallback)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




