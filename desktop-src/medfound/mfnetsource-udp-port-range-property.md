---
description: The range of valid UDP ports that the network source can use to receive streaming content.
ms.assetid: 97fe2d11-70f7-4baa-b49f-513d90146591
title: MFNETSOURCE_UDP_PORT_RANGE property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_UDP\_PORT\_RANGE property

The range of valid UDP ports that the network source can use to receive streaming content. The value of this property is a string with the form " *m*–*n* " where *m* and *n* are port numbers.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Wide-character string (**WCHAR**\*)

VT\_LPWSTR

**pwszVal**



## Remarks

The constant **MFNETSOURCE\_UDP\_PORT\_RANGE** defines the GUID for this property key. The property identifier (PID) is zero.

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

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




