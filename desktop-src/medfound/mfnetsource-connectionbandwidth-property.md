---
description: Specifies the link bandwidth for the network source, in bits per second.
ms.assetid: 1b71dce1-8744-4114-9629-2a9d0afb7c43
title: MFNETSOURCE_CONNECTIONBANDWIDTH property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_CONNECTIONBANDWIDTH property

Specifies the link bandwidth for the network source, in bits per second.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**DWORD** (stored as **LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_CONNECTIONBANDWIDTH** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

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

 

 




