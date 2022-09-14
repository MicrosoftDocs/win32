---
title: RPC over HTTP Deployment Recommendations
description: This section documents best practices and recommended deployment configurations for achieving maximum security and performance when using RPC over HTTP.
ms.assetid: 83938a7d-77d0-45e8-b0a3-7b32ef768d83
ms.topic: article
ms.date: 05/31/2018
---

# RPC over HTTP Deployment Recommendations

This section documents best practices and recommended deployment configurations for achieving maximum security and performance when using RPC over HTTP. The various configurations found herein apply do different organizations based on various size, budget, and security requirements. Each configuration also provides deployment considerations useful in determining which is best for a given scenario.

For information regarding high volume RPC over HTTP scenarios, please see [Microsoft RPC Load Balancing](rpc-load-balancing.md).

The following recommendations apply to all configurations:

-   Use versions of Windows that support RPC over HTTP v2.
-   Put IIS on the machine that runs the RPC Proxy in IIS 6.0 mode.
-   Disallow anonymous access to the RPC Proxy virtual directory.
-   Never enable the AllowAnonymous registry key.
-   Make your RPC over HTTP clients use the **CertificateSubjectField** (see [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) for more information) to verify that the RPC Proxy you connected to is the RPC Proxy you expect.
-   Configure the **ValidPorts** registry key to contain only machines to which the RPC over HTTP clients will connect.
-   Do not use wildcards in the **ValidPorts** key; doing so can save time, but a completely unexpected machine may fit the wildcard as well.
-   Use SSL on RPC over HTTP clients. If the guidelines set forth in these sections are followed, the RPC over HTTP client will not be able to connect without using SSL.
-   Configure RPC over HTTP clients to use RPC Encryption in addition to using SSL. If the RPC over HTTP client cannot reach the KDC, it can use only Negotiate and NTLM.
-   Configure client machines to use NTLMv2. Set the **LMCompatibilityLevel** registry key to 2 or higher. See **msdn.microsoft.com** for more information on the **LMCompatibilityLevel** key.
-   Run a web farm of RPC Proxy machines with the configuration outlined above.
-   Deploy a firewall between the Internet and the RPC Proxy.
-   For optimal performance, configure IIS to send a short response for non-success error codes. Because the consumer of the IIS response is an automated process, there is no need for user friendly explanations to be sent to the client; they will simply be ignored by the RPC over HTTP client.

The basic goals of the RPC Proxy from a security, performance and manageability perspective are the following:

-   Provide a single point of entry for RPC over HTTP traffic into the server network. Having a single point of entry for RPC over HTTP traffic into a server network has two main benefits. First, since the RPC Proxy is facing the Internet, most organizations isolate such machines in a special network called an untrusted perimeter network which is separate from the normal organizational network. Servers in an untrusted perimeter network are very carefully managed, configured and monitored to be able to withstand attacks from the Internet. The fewer machines in an untrusted perimeter network, the easier it is to configure, manage, monitor and keep them secure. Second, since a single Web Farm with RPC Proxies installed can service any number of RPC over HTTP Servers residing on the corporate network, it makes a lot of sense to separate the RPC Proxy from the RPC over HTTP Server and have the RPC Proxy reside in an untrusted perimeter network. If the RPC Proxy was on the same machine as the RPC over HTTP Server, organizations would be forced to put all of their back end servers into an untrusted perimeter network, which would make it much harder to keep the untrusted perimeter network secure. Separating the role of the RPC Proxy and the RPC over HTTP server helps organizations keep the number of machines in an untrusted perimeter network manageable and therefore, more secure.
-   Serve as a safety fuse for the server network. The RPC Proxy is designed as an expendable fuse for the server network – if something goes wrong on the RPC Proxy, it simply goes out and thus protects the real RPC over HTTP server. If the outlined best practices outlined in this section have been followed thus far, the RPC over HTTP traffic is encrypted with RPC encryption in addition to SSL. The RPC Encryption itself is between the client and the server, not between the client and the proxy. This means the proxy does not understand and cannot decrypt the RPC traffic it receives. It only understands some control sequences sent to it by the client dealing with connection establishment, flow control and other tunneling details. It has no access to the data the RPC over HTTP client sends to the server. Furthermore, the RPC over HTTP client must independently authenticate to both the RPC Proxy and the RPC over HTTP server. This provides defense in depth. If the RPC Proxy machine becomes compromised, due to some configuration error or a security breach of some sort, the data that pass through it are still secure from tampering. An attacker that would gain control of the RPC Proxy can at most interrupt the traffic, but not read it or tamper with it. This is where the fuse role of the RPC Proxy comes into play – it is expendable without the security of the RPC over HTTP traffic being compromised.
-   Distribute some of the access checks and decryption work among multiple machines running RPC Proxy in a Web Farm. By functioning well in a Web Farm, the RPC Proxy enables organizations to offload SSL decryption and some of the access checks, thus freeing more capacity on the back end server for processing. Using a Web Farm of RPC Proxy machines also enables an organization to increase its ability to withstand Denial of Service (DoS) attacks by increasing the capacity on its front end servers.

Within the guidelines set forth thus far, organizations still have choices. Each organization has choices and compromises between user inconvenience, security and cost:

-   **Use Basic Authentication or Windows Integrated Authentication to authenticate to the RPC Proxy?** RPC over HTTP currently supports only NTLM – it doesn't support Kerberos. Also, if there is an HTTP Proxy or a firewall between the RPC over HTTP client and the RPC Proxy which inserts the *via* pragma in the HTTP header, NTLM authentication will not work. When that is not the case, organizations can choose between Basic and NTLM authentication. The advantage of Basic authentication is that it is faster and simpler, and therefore offers less opportunity for denial of service attacks. But NTLM is more secure. Depending on an organization's priorities, it can choose Basic, NTLM, or allow its users to choose between the two. If only one is chosen, it is best to turn off the other from the RPC Proxy virtual directory to reduce risk of attack.
-   **Use the same set of credentials for both the RPC Proxy and the RPC over HTTP Server, or use different credentials for each?** The tradeoff for this decision is between user's convenience and security. Few users like to enter multiple credentials. However, if a security breach occurs in an untrusted perimeter network, having separate sets of credentials for the RPC Proxy and the RPC over HTTP Server provides additional protection. Note that if separate credentials are used, and one set of credentials is the user's domain credentials, it is advisable to use the user's domain credentials for the RPC over HTTP Server and not for the RPC Proxy.

 

 




