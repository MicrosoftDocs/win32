---
Description: 'Specifies the maximum video bit rate for the Digital Living Network Alliance (DLNA) media sink.'
ms.assetid: '5805f930-6cbd-4089-a052-522b4d152cc1'
title: 'MF\_MP2DLNA\_VIDEO\_BIT\_RATE attribute'
---

# MF\_MP2DLNA\_VIDEO\_BIT\_RATE attribute

Specifies the maximum video bit rate for the Digital Living Network Alliance (DLNA) media sink.

## Data type

**UINT32**

The value is the target maximum bit rate for the encoded video stream, in bits per second. The maximum value is 9800000 (9.8 Mbps), which is also the default value.

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

To set this attribute on the DLNA media sink, query the media sink for the [**IMFAttributes**](imfattributes.md) interface. Set the attribute before streaming begins.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmp2dlna.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




