---
description: The value of the &\#0034;c-playerversion&\#0034; field that the network source uses for logging.
ms.assetid: 7bc485de-345b-475c-bbae-0776aa63c93a
title: MFNETSOURCE_PLAYERVERSION property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PLAYERVERSION property

The value of the "c-playerversion" field that the network source uses for logging. Applications can set this property to the version number of the application.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**LONGLONG**

VT\_I8

**hVal**



## Remarks

The constant **MFNETSOURCE\_PLAYERVERSION** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Source Resolver](source-resolver.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Client Logging](client-logging.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




