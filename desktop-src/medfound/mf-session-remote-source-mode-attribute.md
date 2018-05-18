---
Description: 'Specifies that the media source will be created in a remote process.'
ms.assetid: '3a2f9ff5-1780-40f3-b36b-3a7cccb47d05'
title: 'MF\_SESSION\_REMOTE\_SOURCE\_MODE attribute'
---

# MF\_SESSION\_REMOTE\_SOURCE\_MODE attribute

Specifies that the media source will be created in a remote process.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

You can set this attribute on the protected media path (PMP) session by using the *pConfiguration* parameter of the [**MFCreatePMPMediaSession**](mfcreatepmpmediasession.md) function.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> <dt>

[PMP Media Session](pmp-media-session.md)
</dt> </dl>

 

 




