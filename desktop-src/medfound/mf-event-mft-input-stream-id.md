---
description: Specifies an input stream on a Media Foundation transform (MFT).
ms.assetid: 2922af62-3fcc-4153-a26a-aba3c4121a0b
title: MF_EVENT_MFT_INPUT_STREAM_ID attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_MFT\_INPUT\_STREAM\_ID attribute

Specifies an input stream on a Media Foundation transform (MFT).

## Data type

**UINT32**

The value is an input stream identifier.

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFMediaEvent**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent)

## Remarks

This attribute is used with the following events:

-   [METransformDrainComplete](metransformdraincomplete.md)
-   [METransformNeedInput](metransformneedinput.md)

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Asynchronous MFTs](asynchronous-mfts.md)
</dt> <dt>

[Event Attributes](event-attributes.md)
</dt> </dl>

 

 




