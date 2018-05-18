---
Description: 'Contains a caller-defined value for an METransformMarker event.'
ms.assetid: 'c6ab20d9-c2bc-43ba-a018-2c6682bf0485'
title: 'MF\_EVENT\_MFT\_CONTEXT attribute'
---

# MF\_EVENT\_MFT\_CONTEXT attribute

Contains a caller-defined value for an [METransformMarker](metransformmarker.md) event.

## Data type

**ULONG\_PTR** stored as **UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](imfattributes-getuint64.md).

To set this attribute, call [**IMFAttributes::SetUINT64**](imfattributes-setuint64.md).

## Applies to

[**IMFMediaEvent**](imfmediaevent.md)

## Remarks

This attribute is used with the [METransformMarker](metransformmarker.md) event. The value of the attribute is taken from the *ulParam* parameter of the [**IMFTransform::ProcessMessage**](imftransform-processmessage.md) method.

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

 

 




