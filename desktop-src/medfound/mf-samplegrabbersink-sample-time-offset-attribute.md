---
Description: Offset between the time stamp on each sample received by the sample grabber, and the time when the sample grabber presents the sample.
ms.assetid: 8d06b415-aafc-4276-9a88-4b7262df62f1
title: MF\_SAMPLEGRABBERSINK\_SAMPLE\_TIME\_OFFSET attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SAMPLEGRABBERSINK\_SAMPLE\_TIME\_OFFSET attribute

Offset between the time stamp on each sample received by the sample grabber, and the time when the sample grabber presents the sample.

## Data type

**UINT64**

## Remarks

You can set this attribute on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) object that is returned by the [**MFCreateSampleGrabberSinkActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatesamplegrabbersinkactivate?branch=master) function. This attribute enables the sample grabber's callback function to receive samples earlier than the presentation time.

When the sample grabber receives a new sample, it presents the sample at time *t* − *offset*, where *t* is the time stamp on the sample and *offset* is the value of this attribute. If this attribute is not set, the default value is zero.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint64?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint64?branch=master)
</dt> <dt>

[**IMFSampleGrabberSinkCallback**](/windows/win32/mfidl/nn-mfidl-imfsamplegrabbersinkcallback?branch=master)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




