---
description: Stores an array of bytes that represents the DRM license associated with the byte stream.
ms.assetid: 866a9706-0b0a-4675-af61-5f55a5a69014
title: MFNETSOURCE_DRMNET_LICENSE_REPRESENTATION property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_DRMNET\_LICENSE\_REPRESENTATION property

Stores an array of bytes that represents the DRM license associated with the byte stream.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Byte array (**BLOB**)

VT\_BLOB

**blob**



## Remarks

The constant **MFNETSOURCE\_DRMNET\_LICENSE\_REPRESENTATION** defines the GUID for this property key. The property identifier (PID) is zero.

This property is read-only. To get the property value from the network byte stream, call **IPropertyStore::GetValue** and pass the **PROPERTYKEY** structure in the *key* parameter. The **fmtid** member of **PROPERTYKEY** must be set to the property GUID.

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

 

 




