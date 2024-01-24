---
description: Duration of accelerated streaming for the network source, in milliseconds.
ms.assetid: 3f9cd762-f393-4130-ba25-d16da0642093
title: MFNETSOURCE_ACCELERATEDSTREAMINGDURATION property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_ACCELERATEDSTREAMINGDURATION property

Duration of accelerated streaming for the network source, in milliseconds.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**DWORD** (stored as **LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_ACCELERATEDSTREAMINGDURATION** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** object to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

This property applies to the Fast Start feature of Windows Media Services, which plays content quickly without waiting for lengthy initial buffering. When using Fast Start, the server running Windows Media Services will send some data at the beginning of the content at a faster rate than that specified by the bit rate of the content.

The default value of this property is 10,000 milliseconds.

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

 

 




