---
Description: Specifies the nominal range of the color information in a video media type.
ms.assetid: 7b2b809e-aae4-401c-816a-626fb88f5f87
title: MF\_MT\_VIDEO\_NOMINAL\_RANGE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_VIDEO\_NOMINAL\_RANGE attribute

Specifies the nominal range of the color information in a video media type.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFNominalRange**](/windows/win32/mfobjects/ne-mfobjects-_mfnominalrange?branch=master) enumeration.

The GUID constant for this attribute is exported from mfuuid.lib.

**H.264/AVC encoders:**

On the output media type, MF\_MT\_VIDEO\_NOMINAL\_RANGE can be set with **MFNominalRange\_0\_255** and **MFNominalRange\_16\_235**.

H.264/AVC encoder shall treat **MFNominalRange\_Unknown** as **MFNominalRange\_16\_235**.

H.264/AVC encoder shall reject a output media type when MF\_MT\_VIDEO\_NOMINAL\_RANGE is set to **MFNominalRange\_48\_208**, **MFNominalRange\_64\_127**, or any other values not defined on [**MFNominalRange**](/windows/win32/mfobjects/ne-mfobjects-_mfnominalrange?branch=master).

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

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Extended Color Information](extended-color-information.md)
</dt> </dl>

 

 




