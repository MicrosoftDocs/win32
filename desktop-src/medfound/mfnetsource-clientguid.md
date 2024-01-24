---
description: Unique identifier by which the server identifies the client.
ms.assetid: 490a2b03-aba8-4510-80c5-ca12f4037747
title: MFNETSOURCE_CLIENTGUID property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_CLIENTGUID property

Unique identifier by which the server identifies the client.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**GUID**

VT\_CLSID

**puuid**



## Remarks

The **MFNETSOURCE\_CLIENTGUID** constant defines the GUID for the property key. The property identifier (PID) is zero. To set this property on the network source, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

If not set or set as **GUID\_NULL**, Microsoft Media Foundation generates an anonymous GUID per session that ensures the user's privacy.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




