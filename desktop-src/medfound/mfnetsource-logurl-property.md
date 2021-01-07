---
description: List of URLs to which the network source will send logging information.
ms.assetid: 772c5b57-273d-4289-9229-ef7a199c6473
title: MFNETSOURCE_LOGURL property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_LOGURL property

List of URLs to which the network source will send logging information.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Array of wide-character strings (**CALPWSTR**)

VT\_VECTOR \| VT\_LPWSTR

**calpwstr**



## Remarks

The constant **MFNETSOURCE\_LOGURL** defines the GUID for this property key. The property identifier (PID) is zero.

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

 

 




