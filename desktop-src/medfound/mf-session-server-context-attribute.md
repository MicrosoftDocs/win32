---
description: Enables two instances of the Media Session to share the same Protected Media Path (PMP) process.
ms.assetid: a922c79b-d6c1-447d-b6fa-993970169a3f
title: MF_SESSION_SERVER_CONTEXT attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SESSION\_SERVER\_CONTEXT attribute

Enables two instances of the Media Session to share the same Protected Media Path (PMP) process.

## Data type

**IUnknown\***

## Remarks

Use this attribute if you want to create the PMP Media Session in an existing PMP process. The value of the attribute is a pointer to the [**IMFPMPServer**](/windows/desktop/api/mfidl/nn-mfidl-imfpmpserver) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> </dl>

 

 




