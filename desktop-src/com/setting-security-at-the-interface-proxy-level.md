---
title: Setting Security at the Interface Proxy Level
description: Sometimes the client needs fine-grained control over the security on calls to particular interfaces.
ms.assetid: '72925ca2-78c9-47d9-8760-63f6379326d2'
---

# Setting Security at the Interface Proxy Level

Sometimes the client needs fine-grained control over the security on calls to particular interfaces. For example, security might be set at a low level for the process but calls to a particular interface might require a higher authentication level, such as encryption. The methods of the [**IClientSecurity**](iclientsecurity.md) interface allow the client to change the security settings associated with calls to a particular interface by controlling the security settings at the interface-proxy level.

The client can query an existing object for [**IClientSecurity**](iclientsecurity.md) and then call the [**IClientSecurity::QueryBlanket**](iclientsecurity-queryblanket.md) method to find out what the current security settings are for a particular interface proxy. The [**IClientSecurity::SetBlanket**](iclientsecurity-setblanket.md) method can be used to modify the security settings for an individual interface proxy on the object before calling one of the interface's methods. The new settings apply to any future callers of this particular interface. The [**IClientSecurity::CopyProxy**](iclientsecurity-copyproxy.md) method provides a way for the client to copy an interface proxy so that subsequent calls to **SetBlanket** on the copy do not affect callers of the original proxy.

[**SetBlanket**](iclientsecurity-setblanket.md) is commonly used to raise the authentication level for a particular interface proxy to a higher level of security protection. However, in some situations, it might also be helpful to lower the authentication level for a particular interface proxy. For instance, suppose the default authentication level for the process is some value other than RPC\_C\_AUTHN\_LEVEL\_NONE and the client and server are in separate domains that do not trust each other. In this case, calls to the server will fail unless the client calls **SetBlanket** to lower the authentication level to RPC\_C\_AUTHN\_LEVEL\_NONE.

Clients using the default implementation of [**IClientSecurity**](iclientsecurity.md) provided by the proxy manager can call the [**CoQueryProxyBlanket**](coqueryproxyblanket.md), [**CoSetProxyBlanket**](cosetproxyblanket.md), and [**CoCopyProxy**](cocopyproxy.md) helper functions instead of calling **IClientSecurity** methods directly. The helper functions simplify the code but are slightly less efficient than calling the corresponding **IClientSecurity** methods directly.

The [**IClientSecurity**](iclientsecurity.md) interface is implemented locally for the client by the proxy manager. Some custom marshaled objects might not support **IClientSecurity**.

[**IClientSecurity**](iclientsecurity.md) works with all supported authentication services (currently NTLMSSP, Schannel, and the Kerberos v5 protocol).

## Related topics

<dl> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




