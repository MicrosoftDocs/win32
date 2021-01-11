---
description: Stores the host name and the port of the proxy server used by the network source.
ms.assetid: 164f8ac3-08ce-40a8-ac8d-4c2a267d9db5
title: MFNETSOURCE_PROXYINFO property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PROXYINFO property

Stores the host name and the port of the proxy server used by the network source.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Wide-character string (**WCHAR**\*)

VT\_LPWSTR

**pwszVal**



## Remarks

The constant **MFNETSOURCE\_PROXYINFO** defines the GUID for this property key. The property identifier (PID) is zero.

This property is read-only. To get the property value from the network source, call **IPropertyStore::GetValue** and pass the **PROPERTYKEY** structure in the *key* parameter. The **fmtid** member of **PROPERTYKEY** must be set to the property GUID.

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

[Proxy Support for Network Sources](proxy-support-for-network-sources.md)
</dt> </dl>

 

 




