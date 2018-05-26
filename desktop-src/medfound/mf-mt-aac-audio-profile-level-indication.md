---
Description: Specifies the audio profile and level of an Advanced Audio Coding (AAC) stream.
ms.assetid: 87fa1127-46ca-4b83-a3b5-99253af22ba0
title: MF\_MT\_AAC\_AUDIO\_PROFILE\_LEVEL\_INDICATION attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AAC\_AUDIO\_PROFILE\_LEVEL\_INDICATION attribute

Specifies the audio profile and level of an Advanced Audio Coding (AAC) stream.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies To

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)

## Remarks

This attribute contains the value of the **audioProfileLevelIndication** field, as defined by ISO/IEC 14496-3.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




