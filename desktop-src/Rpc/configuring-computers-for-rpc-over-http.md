---
title: Configuring Computers for RPC over HTTP
description: To use HTTP as a transport protocol for RPC, RPC Proxy running within Internet Information Server (IIS) must be configured on the server program's network.
ms.assetid: 5a67af51-924a-4f2b-b013-a4fd1bfaeddd
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Computers for RPC over HTTP

To use HTTP as a transport protocol for RPC, RPC Proxy running within Internet Information Server (IIS) must be configured on the server program's network. This section describes configuration options. For recommendations on best programming and configuration practices when using RPC over HTTP, see [RPC over HTTP Deployment Recommendations](rpc-over-http-deployment-recommendations.md). The primary task is configuring the RPC Proxy to accept and forward RPC over HTTP connections to an RPC over HTTP server program.

IIS must first be installed on the machine running the RPC Proxy. Once IIS is installed, the RPC Proxy is installed. Both IIS and the RPC Proxy can be installed simultaneously from **Add/Remove Windows Components** in the Control Panel. RPC Proxy is installed from **Networking Services**, and is called **RPC over HTTP Proxy** in Windows setup. If both IIS and RPC Proxy are installed at the same time, Windows ensures they are installed in the proper order.

> [!Note]  
> After installation is complete, IIS must be restarted if it was running during the installation process.

 

After installed of the RPC Proxy, some additional configuration tasks must be performed:

1.  Open the IIS MMC snap-in and configure the RPC Proxy virtual directory to require security, as explained in [RPC over HTTP Security](rpc-over-http-security.md). This step is required only if you plan to use RPC over HTTP v2.
2.  If IIS does not have a certificate installed, a valid certificate must be obtained and installed for that computer in order to use SSL when communicating with the RPC Proxy. This step is relevant only for RPC over HTTP v2. Since RPC over HTTP v1 does not support SSL, this step can be omitted for RPC over HTTP v1.
3.  Set the **ValidPorts** key as described in [RPC over HTTP Security](rpc-over-http-security.md).

When these configuration tasks are completed, the RPC over HTTP proxy is ready to forward requests from the RPC over HTTP client to the RPC over HTTP server.

## RPC over HTTP Registry Keys

This section explains additional registry keys used to configure the client, server or RPC Proxy in an RPC over HTTP connection. These keys are generally not required; they are provided here for completeness.

**HKLM\\Software\\Microsoft\\Rpc\\DefaultChannelLifetime**

DWORD. Overrides the default channel lifetime. Used on the client and the RPC Proxy. The channel lifetime is expressed in bytes. If not specified, 1GB is used. Used only in RPC over HTTP v2. When changed on RPC Proxy, IIS must be restarted for the change to take effect.

\-

**HKLM\\Software\\Microsoft\\Rpc\\ClientReceiveWindow**

DWORD. When present, specifies the receive window used by the client for data received from the RPC Proxy. The minimum valid value is 8K. The maximum is 1GB. If the value is not present, 64K is used. Used only in RPC over HTTP v2.

\-

**HKLM\\Software\\Microsoft\\Rpc\\InProxyReceiveWindow**

DWORD. When present, specifies the receive window used by the RPC Proxy for data received from the client. The minimum valid value is 8K. The maximum is 1GB. If the value is not present, 64K is used. Used only in RPC over HTTP v2. When changes are made to this value, IIS must be restarted for the change to take effect.

\-

**HKLM\\Software\\Microsoft\\Rpc\\OutProxyReceiveWindow**

DWORD. When present, specifies the receive window used by the RPC Proxy for data received from the server. The minimum valid value is 8K. The maximum is 1GB. If the value is not present, 64K is used. Used only in RPC over HTTP v2. When changes are made to this value, IIS must be restarted for the change to take effect.

\-

**HKLM\\Software\\Microsoft\\Rpc\\ServerReceiveWindow**

DWORD. When present, specifies the receive window used by the server for data received from the RPC Proxy. The minimum valid value is 8K. The maximum is 1GB. If the value is not present, 64K is used. Used only in RPC over HTTP v2. When changes are made to this value, IIS must be restarted for the change to take effect.

\-

**HKLM\\Software\\Policies\\Microsoft\\Windows NT\\Rpc\\MinimumConnectionTimeout**

DWORD. When present, specifies the minimum connection timeout used by the client and RPC Proxy, in seconds. The actual timeout used is the lower of this value and the IIS idle connection timeout. If zero, or the key is not present, the IIS idle connection timeout is used. Used only in RPC over HTTP v2. When changes are made to this value on the RPC Proxy, IIS must be restarted for the change to take effect.

\-

**HKLM\\Software\\Microsoft\\Rpc\\UseProxyForIPAddrIfRDNSFails**

When present and set to non-zero, and a numeric IP address is provided as the RPC Proxy address, an RPC over HTTP client will attempt reverse name resolution and, if that fails, will attempt connection to the RPC Proxy through an HTTP proxy. Can be used to emulate Windows NT behavior on installations that require such behavior. Ignored for RPC over HTTP v2. Used only when RPC over HTTP v1 is used. Supported only on Windows 2000 with Service Pack 3 (SP3) and later.

\-

**HKLM\\Software\\Microsoft\\Rpc\\RpcProxy\\AllowAnonymous**

DWORD. When not present or set to zero, the RPC Proxy checks whether the connection is authenticated, and whether it is secure (SSL or other form of encryption is used). If either is false, the connection is rejected. If this value contains non-zero, anonymous and non-encrypted connections are allowed. This setting is an addition to any virtual directory settings. For example, if anonymous access is disabled on the virtual directory level, but **AllowAnonymous** is non-zero, anonymous access will still be blocked at the IIS level. Used on the RPC Proxy only in RPC over HTTP v2. When changes are made to this value on the RPC Proxy, IIS must be restarted for the change to take effect.

> [!WARNING]
> Microsoft strongly recommends against setting the **AllowAnonymous** value on production systems for security considerations. The only reason this key should be set is for testing on closed networks without outside access. Any system connected to the Internet and running the RPC Proxy with the **AllowAnonymous** key set to a nonzero value may be vulnerable to attacks.

 

 

 




