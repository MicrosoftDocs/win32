---
description: Specifies a semicolon-delimited list of media servers that can accept connections from client applications without using a proxy server.
ms.assetid: 218883c5-9a26-4733-8308-1827cf1f2cd7
title: MFNETSOURCE_PROXYEXCEPTIONLIST property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PROXYEXCEPTIONLIST property

Specifies a semicolon-delimited list of media servers that can accept connections from client applications without using a proxy server.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Wide-character string (**WCHAR**\*)

VT\_LPWSTR

**pwszVal**



## Remarks

The constant **MFNETSOURCE\_PROXYEXCEPTIONLIST** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the proxy locator when creating the proxy locator object. To set the property, pass an **IPropertyStore** pointer in the *pProxyConfig* parameter of the [**MFCreateProxyLocator**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateproxylocator) function. The proxy locator does not perform proxy detection for these addresses.

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

 

 




