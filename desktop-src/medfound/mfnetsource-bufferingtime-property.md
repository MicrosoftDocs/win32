---
description: Number of seconds of data that the network source buffers at startup.
ms.assetid: 186b55fc-d1b1-4187-a748-efaee114eca9
title: MFNETSOURCE_BUFFERINGTIME property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_BUFFERINGTIME property

Number of seconds of data that the network source buffers at startup.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**DWORD** (stored as **LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_BUFFERINGTIME** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

The default value of this property is 5 seconds.

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

 

 




