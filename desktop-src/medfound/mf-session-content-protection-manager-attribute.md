---
Description: 'Provides a callback interface for the application to receive a content enabler object from the protected media path (PMP) session.'
ms.assetid: '66482541-63d4-439b-862f-7507605af5d8'
title: 'MF\_SESSION\_CONTENT\_PROTECTION\_MANAGER attribute'
---

# MF\_SESSION\_CONTENT\_PROTECTION\_MANAGER attribute

Provides a callback interface for the application to receive a content enabler object from the protected media path (PMP) session.

## Data type

**IUnknown\***

## Remarks

The value of this attribute is a pointer to the application's [**IMFContentProtectionManager**](imfcontentprotectionmanager.md) interface.

Set this attribute on the PMP session by using the *pConfiguration* parameter of the [**MFCreatePMPMediaSession**](mfcreatepmpmediasession.md) function.

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

[**IMFAttributes::GetUnknown**](imfattributes-getunknown.md)
</dt> <dt>

[**IMFAttributes::SetUnknown**](imfattributes-setunknown.md)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> <dt>

[How to Play Protected Media Files](how-to-play-protected-media-files.md)
</dt> </dl>

 

 




