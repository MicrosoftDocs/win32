---
description: Maximum amount of data the network source buffers, in milliseconds.
ms.assetid: bd776dc2-341a-4d87-8a06-8063daf53ede
title: MFNETSOURCE_MAXBUFFERTIMEMS property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_MAXBUFFERTIMEMS property

Maximum amount of data the network source buffers, in milliseconds.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**DWORD** (stored as **LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_MAXBUFFERTIMEMS** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

The default value of this property is 40,000 milliseconds.

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

 

 




