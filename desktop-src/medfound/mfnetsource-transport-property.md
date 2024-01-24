---
description: Specifies the transport protocol used by the network source.
ms.assetid: 7c8598ff-f408-42d0-9eee-3ef1e82f0466
title: MFNETSOURCE_TRANSPORT property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_TRANSPORT property

Specifies the transport protocol used by the network source. The value of this property is a member of the [**MFNETSOURCE\_TRANSPORT\_TYPE**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_transport_type) enumeration.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**LONG**

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_TRANSPORT** defines the GUID for this property key. The property identifier (PID) is zero.

This property is read-only. To retrieve this property, query the network source for the **IPropertyStore** interface and call **IPropertyStore::GetValue**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> <dt>

[Supported Protocols](supported-protocols.md)
</dt> </dl>

 

 




