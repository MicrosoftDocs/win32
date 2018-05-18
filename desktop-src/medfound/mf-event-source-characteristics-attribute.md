---
Description: 'Specifies the current characteristics of the media source.'
ms.assetid: 'af2a2b75-cd4e-453c-876e-3be2db695e4e'
title: 'MF\_EVENT\_SOURCE\_CHARACTERISTICS attribute'
---

# MF\_EVENT\_SOURCE\_CHARACTERISTICS attribute

Specifies the current characteristics of the media source.

## Data type

**UINT32**

## Remarks

The value of this attribute is a bitwise **OR** of flags from the [**MFMEDIASOURCE\_CHARACTERISTICS**](mfmediasource-characteristics.md) enumeration.

This attribute is used with the [MESourceCharacteristicsChanged](mesourcecharacteristicschanged.md) event.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Event Attributes](event-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> </dl>

 

 




