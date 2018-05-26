---
Description: Contains a caller-defined value for an METransformMarker event.
ms.assetid: c6ab20d9-c2bc-43ba-a018-2c6682bf0485
title: MF\_EVENT\_MFT\_CONTEXT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_EVENT\_MFT\_CONTEXT attribute

Contains a caller-defined value for an [METransformMarker](metransformmarker.md) event.

## Data type

**ULONG\_PTR** stored as **UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint64?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint64?branch=master).

## Applies to

[**IMFMediaEvent**](/windows/win32/mfobjects/nn-mfobjects-imfmediaevent?branch=master)

## Remarks

This attribute is used with the [METransformMarker](metransformmarker.md) event. The value of the attribute is taken from the *ulParam* parameter of the [**IMFTransform::ProcessMessage**](/windows/win32/mftransform/nf-mftransform-imftransform-processmessage?branch=master) method.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
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

 

 




