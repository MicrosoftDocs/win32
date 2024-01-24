---
description: Specifies whether all streaming protocols are enabled.
ms.assetid: cf072572-58f7-429a-954a-8808d05248f0
title: MFNETSOURCE_ENABLE_STREAMING property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_ENABLE\_STREAMING property

Specifies whether all streaming protocols are enabled.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Boolean (**LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_ENABLE\_STREAMING** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the [Configuring a Media Source](configuring-a-media-source.md).

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
</dt> <dt>

[Supported Protocols](supported-protocols.md)
</dt> </dl>

 

 




