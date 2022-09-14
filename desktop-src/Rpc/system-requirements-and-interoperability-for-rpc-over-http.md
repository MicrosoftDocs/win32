---
title: RPC over HTTP system requirements, interoperability
description: Microsoft RPC supports RPC over HTTP as shown in the following table.
ms.assetid: 1815315c-1286-4e60-b3a2-a02cb3016fca
ms.topic: article
ms.date: 05/31/2018
---

# RPC over HTTP system requirements, interoperability

Microsoft RPC supports RPC over HTTP as shown in the following table.



| Platform                             | Supports                       | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Server 2003                  | Clients, servers and RPC Proxy | Supports RPC over HTTP v1 and RPC over HTTP v2 client and server. RPC Proxy supports RPC over HTTP v2 when IIS is running in IIS 6.0 mode. RPC Proxy supports RPC over HTTP v1 and RPC over HTTP v2 when IIS is running in IIS 5.0 mode. However, running in IIS 5.0 mode is not recommended. See [RPC over HTTP Deployment Recommendations](rpc-over-http-deployment-recommendations.md) for more information. RPC over HTTP server and the RPC Proxy can be on different machines. |
| Windows XP with Service Pack 1 (SP1) | Clients and servers            | Supports RPC over HTTP v1 and RPC over HTTP v2 client and server. Does not support RPC Proxy.                                                                                                                                                                                                                                                                                                                                                                                         |
| Windows XP                           | Clients and servers            | Supports RPC over HTTP v1 client and server only. Does not support RPC Proxy.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Windows 2000                         | Clients, servers and RPC Proxy | RPC over HTTP server program and the RPC Proxy can be running on different computers. RPC over HTTP client, server and the RPC Proxy support RPC over HTTP v1 only.                                                                                                                                                                                                                                                                                                                   |



 

In addition, the following requirements apply:

-   Windows 2000 and later requires the use of IIS 4.0 or later.
-   The RPC over HTTP proxy runs on Windows server editions only.
-   If IIS is running on a server version of Windows, the RPC over HTTP server program can run on any computer to which the RPC Proxy is configured to forward traffic. Therefore, it can run on the same computer as the RPC Proxy, or a different computer.

For an RPC over HTTP connection to be established, all of the RPC over HTTP client, RPC over HTTP server and the RPC Proxy must agree on which version of RPC over HTTP is used. If there is no common version of RPC over HTTP that all three support (client, server and RPC Proxy), an RPC over HTTP connection cannot be established. The following table summarizes this interoperability for different versions of RPC over HTTP.



| RPC over HTTP Client | RPC Proxy      | RPC over HTTP Server | Works?                                      | Version used     |
|----------------------|----------------|----------------------|---------------------------------------------|------------------|
| v1 only              | v1 only        | v1 only              | Yes, with v1 limitations                    | RPC over HTTP v1 |
| v1 only              | v1 only        | Both v1 and v2       | Yes, with v1 limitations                    | RPC over HTTP v1 |
| v1 only              | Both v1 and v2 | v1 only              | Yes, with v1 limitations                    | RPC over HTTP v1 |
| v1 only              | Both v1 and v2 | Both v1 and v2       | Yes, with v1 limitations                    | RPC over HTTP v1 |
| v1 only              | v2 only        | v1 only              | No                                          |                  |
| v1 only              | v2 only        | Both v1 and v2       | No                                          |                  |
| Both v1 and v2       | v1 only        | v1 only              | Yes, with v1 limitations                    | RPC over HTTP v1 |
| Both v1 and v2       | v1 only        | Both v1 and v2       | Yes, with v1 limitations                    | RPC over HTTP v1 |
| Both v1 and v2       | Both v1 and v2 | v1 only              | Yes, with v1 limitations                    | RPC over HTTP v1 |
| Both v1 and v2       | Both v1 and v2 | Both v1 and v2       | Yes                                         | RPC over HTTP v2 |
| Both v1 and v2       | v2 only        | v1 only              | No                                          |                  |
| Both v1 and v2       | v2 only        | Both v1 and v2       | Yes. This is the recommended configuration. | RPC over HTTP v2 |



 

For example, imagine a Windows 2000 client, a Windows Server 2003 proxy with IIS running in IIS 6.0 mode, and a Windows Server 2003 RPC over HTTP server. The first table on this reference page shows that Windows 2000 supports only RPC over HTTP v1. The same table reveals that a Windows Server 2003 with IIS running in IIS 6.0 mode supports only RPC over HTTP v2, and that a Windows Server 2003 RPC over HTTP server supports both RPC over HTTP v1 and RPC over HTTP v2. This scenario is described in row 6 of the second table on this reference page, where it shows that an RPC over HTTP connection cannot be established. Furthermore, the second table reveals that two choices exist for that scenario:

-   If security and robustness are not a consideration, IIS can be switched to IIS 5.0 mode where it supports both RPC over HTTP v1 and RPC over HTTP v2. Doing so would enable establishment of an RPC over HTTP v1 connection.
-   Upgrade the Windows 98 client to Windows XP with SP1 and obtain the power, security and robustness of an RPC over HTTP v2 connection.

 

 




