---
Description: 'Specifies the configuration setting for the default proxy locator.'
ms.assetid: '85f2bd02-8a2f-46b5-b765-1a0bc5b6ccc3'
title: 'MFNETSOURCE\_PROXYSETTINGS property'
---

# MFNETSOURCE\_PROXYSETTINGS property

Specifies the configuration setting for the default proxy locator. The value of this property is a member of the [**MFNET\_PROXYSETTINGS**](mfnet-proxysettings.md) enumeration.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**LONG**

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_PROXYSETTINGS** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the proxy locator when creating the default proxy locator object. To set the property, pass an **IPropertyStore** pointer in the *pProxyConfig* parameter of the [**MFCreateProxyLocator**](mfcreateproxylocator.md) function.

## Requirements



|                                     |                                                                                    |
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

 

 




