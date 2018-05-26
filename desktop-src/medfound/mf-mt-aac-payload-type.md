---
Description: Specifies the payload type of an Advanced Audio Coding (AAC) stream.
ms.assetid: a032fcf4-2584-4047-adbd-d94d4fc4e841
title: MF\_MT\_AAC\_PAYLOAD\_TYPE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AAC\_PAYLOAD\_TYPE attribute

Specifies the payload type of an Advanced Audio Coding (AAC) stream.

## Data type

**UINT32**

The following values are possible.



| Value                                                                        | Meaning                                                                                                                           |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The stream contains raw\_data\_block elements only.<br/>                                                                    |
| <dl> <dt>1</dt> </dl> | Audio Data Transport Stream (ADTS). The stream contains an adts\_sequence, as defined by MPEG-2.<br/>                       |
| <dl> <dt>2</dt> </dl> | Audio Data Interchange Format (ADIF). The stream contains an adif\_sequence, as defined by MPEG-2.<br/>                     |
| <dl> <dt>3</dt> </dl> | The stream contains an MPEG-4 audio transport stream with a synchronization layer (LOAS) and a multiplex layer (LATM).<br/> |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies To

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)

## Remarks

MF\_MT\_AAC\_PAYLOAD\_TYPE is optional. If this attribute is not specified, the default value 0 is used, which specifies the stream contains raw\_data\_block elements only.

Applies only to **MFAudioFormat\_AAC**.

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

 

 




