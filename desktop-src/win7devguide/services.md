---
title: Services (Windows 7 Developer Guide)
description: Windows 7 provides a powerful, highly extensible, and manageable platform for building and integrating the web services and applications of the future.Windows 7 offers both managed-code APIs and native APIs for building and running web services.
ms.assetid: 6a027e0c-28a0-41cf-b96f-ed988c64c92a
ms.topic: article
ms.date: 05/31/2018
---

# Services (Windows 7 Developer Guide)

Windows 7 provides a powerful, highly extensible, and manageable platform for building and integrating the web services and applications of the future.

Windows 7 offers both managed-code APIs and native APIs for building and running web services. A variety of new features are built on top of a new extensibility layer that allows developers to extend all APIs, in native code or within the Microsoft .NET Framework.

Windows 7 also lets developers take advantage of better caching and searching capabilities. With these enhancements, developers can retrieve data faster and reduce network bandwidth usage.

## Windows Web Services

With [Windows Web Services](/windows/desktop/wsw/portal), you can create applications that communicate easily with a local computer or a remote web service. Windows Web Services is a native-code implementation of SOAP and provides core network communication by supporting a broad set of the web services (*WS*) family of protocols. Windows Web Services is a peer to [Windows Communication Foundation](/previous-versions/windows/desktop/cc907054(v=vs.85)) (*WCF*, managed-code web services), and provides a high-performance subset of *WCF* functionality. Windows Web Services provides the following benefits:

-   The ability to build native code web services in C/C++ in Windows client and server.
-   Extensive integration with [Windows Communication Foundation](/previous-versions/windows/desktop/cc907054(v=vs.85)) services.
-   The ability to build web services with minimal startup time.
-   The ability to build services based on the core *WS* family of protocols and *W3C* standards.
-   The ability to use web services in resource-constrained environments.

For more information, see [Windows Web Services API](../wsw/portal.md) and [Implement Web Services with the Windows Web Services API](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/web/WWSAPI).

## Distributed Routing Table

Windows 7 makes it easier to build sophisticated peer-to-peer applications like distributed file systems and content distribution networks with the [Distributed Routing Table](/windows/desktop/P2PSdk/distributed-routing-table-api-reference). The Distributed Routing Table provides a secure, scalable mechanism for publishing and searching for keys in a peer-to-peer system. It can be used to build distributed hash tables and construct topologies for overlay networks. (See [Distributed Routing Table API](../p2psdk/distributed-routing-table-api.md).)

## **Windows BranchCache**

Windows 7 improves application responsiveness between central servers and branch-office computers. In today's networks, communication between central servers and branch offices is often congested, which leads to slower performance for applications in the branch office. With Windows BranchCache, clients can retrieve data from other clients in their own branch that have already downloaded the data, instead of having to retrieve the data over remote servers. As a result, wide area network (WAN) link traffic decreases and application responsiveness improves. The cache keeps a copy of all content that clients in the branch have requested and ensures that only the clients that are authorized by the content server can access the requested data, while preserving end-to-end encryption of the data.

Windows BranchCache is already integrated with HTTP and Server Message Block (SMB). If an application uses the WindowsAPIs for either of these protocols, Windows BranchCache can help increase the performance of this application on Windows 7 without making any changes to it.

If your application retrieves the same data multiple times from a server over a WAN link and is not automatically optimized using Windows 7, it is easy for you to use the Windows BranchCacheAPIs to optimize your application to work faster on Windows 7 and satisfy your branch users.

These new features help reduce WAN traffic and latency while ensuring compliance with security mandates. (See [Peer Distribution](../p2psdk/peer-distribution.md).)

 

 
