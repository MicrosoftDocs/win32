---
Description: Enables two instances of the Media Session to share the same Protected Media Path (PMP) process.
ms.assetid: a922c79b-d6c1-447d-b6fa-993970169a3f
title: MF\_SESSION\_SERVER\_CONTEXT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SESSION\_SERVER\_CONTEXT attribute

Enables two instances of the Media Session to share the same Protected Media Path (PMP) process.

## Data type

**IUnknown\***

## Remarks

Use this attribute if you want to create the PMP Media Session in an existing PMP process. The value of the attribute is a pointer to the [**IMFPMPServer**](/windows/win32/mfidl/nn-mfidl-imfpmpserver?branch=master) interface.

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

[**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> </dl>

 

 




