---
description: The number of times the network source tries to reconnect to the server and resume streaming if the connection is lost.
ms.assetid: 185e15c6-910b-4e27-9087-cfe30a174194
title: MFNETSOURCE_AUTORECONNECTLIMIT property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_AUTORECONNECTLIMIT property

The number of times the network source tries to reconnect to the server and resume streaming if the connection is lost.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**DWORD** (stored as **LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_AUTORECONNECTLIMIT** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** object to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

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

[Network Source Features](network-source-features.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




