---
description: Specifies the packet-pair bandwidth and run-time bandwidth detected by the network source.
ms.assetid: 430de7fc-fe62-4b89-b3fc-7cd956e40892
title: MFNETSOURCE_PPBANDWIDTH property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PPBANDWIDTH property

Specifies the packet-pair bandwidth and run-time bandwidth detected by the network source. The property value is a array of two values:

-   Packet-pair bandwidth, in bits per second.
-   Run-time bandwidth, in bits per second.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Array of **ULONG** values (**CAUL**)

VT\_VECTOR \| VT\_UI4

**caul**



## Remarks

The constant **MFNETSOURCE\_PPBANDWIDTH** defines the GUID for this property key. The property identifier (PID) is zero.

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

[Network Source Features](network-source-features.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




