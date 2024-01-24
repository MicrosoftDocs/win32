---
description: The value of the &\#0034;c-hostexever&\#0034; field that the network source uses for logging.
ms.assetid: eee93457-483d-41dc-91c5-c12382d03152
title: MFNETSOURCE_HOSTVERSION property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_HOSTVERSION property

The value of the "c-hostexever" field that the network source uses for logging. Applications can set this property to the version number of the host application. The host application is the .exe file identified by the c-hostexe field.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**LONGLONG**

VT\_I8

**hVal**



## Remarks

The constant **MFNETSOURCE\_HOSTVERSION** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the Source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

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

 

 




