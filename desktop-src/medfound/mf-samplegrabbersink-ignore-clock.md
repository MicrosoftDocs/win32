---
description: Specifies whether the sample-grabber sink uses the presentation clock to schedule samples.
ms.assetid: 780ec4a6-8e14-4b81-9d50-82b2850c70ae
title: MF_SAMPLEGRABBERSINK_IGNORE_CLOCK attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SAMPLEGRABBERSINK\_IGNORE\_CLOCK attribute

Specifies whether the sample-grabber sink uses the presentation clock to schedule samples.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

You can set this attribute on the activation object created by the [**MFCreateSampleGrabberSinkActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesamplegrabbersinkactivate) function. Set the attribute before calling the [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) method on the activation object.

By default, when the sample-grabber sink receives a sample, it waits until the presentation time of the sample to invoke the application's callback. If the MF\_SAMPLEGRABBERSINK\_IGNORE\_CLOCK attribute is nonzero, the sample-grabber sink ignores the presentation clock and invokes the callback as soon as it receives each sample.

Recommended usage:

-   If you want to process samples as quickly as possible, set this attribute to **TRUE**.
-   If you want the calls to the callback method to be synchronized with the clock, either do not set this attribute or set it to **FALSE**. You can get samples slightly ahead of the clock, while still remaining synchronized, by setting the [**MF\_SAMPLEGRABBERSINK\_SAMPLE\_TIME\_OFFSET**](mf-samplegrabbersink-sample-time-offset-attribute.md) attribute.

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

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




