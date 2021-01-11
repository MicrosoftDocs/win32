---
description: Specifies the host name of the proxy server.
ms.assetid: e53c86e9-c326-41c9-aa86-c80a750b9ce3
title: MFNETSOURCE_PROXYHOSTNAME property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PROXYHOSTNAME property

Specifies the host name of the proxy server.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Wide-character string (**WCHAR**\*)

VT\_LPWSTR

**pwszVal**



## Remarks

The constant **MFNETSOURCE\_PROXYHOSTNAME** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the default proxy locator when creating the proxy locator object. To set the property, pass an **IPropertyStore** pointer in the *pProxyConfig* parameter of the [**MFCreateProxyLocator**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateproxylocator) function. This property must be set by the application when the proxy locator is configured to operate in the manual mode.

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

 

 




