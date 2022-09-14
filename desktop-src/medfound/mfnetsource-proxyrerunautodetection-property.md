---
description: Specifies whether the default proxy locator should force proxy auto-detection.
ms.assetid: ab547a92-94a2-482e-b7ac-aeb3fdfb6b91
title: MFNETSOURCE_PROXYRERUNAUTODETECTION property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PROXYRERUNAUTODETECTION property

Specifies whether the default proxy locator should force proxy auto-detection.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Boolean (**LONG**)

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_PROXYSETTINGS** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the proxy locator when creating the proxy locator object. To set the property, pass an **IPropertyStore** pointer in the *pProxyConfig* parameter of the [**MFCreateProxyLocator**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateproxylocator) function. In auto-detect mode, the proxy locator uses the WinInet proxy detection mechanism. To force auto-detection, set the value to 0.

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

 

 




