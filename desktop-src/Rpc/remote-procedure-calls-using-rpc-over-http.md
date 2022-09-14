---
title: Remote Procedure Calls Using RPC over HTTP
description: Internet browser programs commonly employ the Hypertext Transport Protocol (HTTP) as the primary means of browsing the World Wide Web.
ms.assetid: f87262f6-fd82-4e8c-bf83-8f93791deec0
keywords:
- Remote Procedure Call RPC , tasks, using RPC/http
ms.topic: article
ms.date: 05/31/2018
---

# Remote Procedure Calls Using RPC over HTTP

Internet browser programs commonly employ the Hypertext Transport Protocol (HTTP) as the primary means of browsing the World Wide Web. HTTP, therefore, sees extensive usage on most computers today. Microsoft has extended the capabilities of its Internet Information Server (IIS) to provide remote procedure call services using HTTP.

The Microsoft RPC-over-HTTP implementation (RPC over HTTP) allows RPC clients to securely and efficiently connect across the Internet to RPC server programs and execute remote procedure calls. This is accomplished with the help of an intermediary known as the RPC-over-HTTP Proxy, or simply the RPC Proxy.

The RPC Proxy runs on an IIS computer. It accepts RPC requests coming from the Internet, performs authentication, validation, and access checks on those requests, and if the request passes all tests, RPC Proxy forwards the request to the RPC server that performs the actual processing. With RPC over HTTP the RPC client and server do not communicate directly; rather, they use the RPC Proxy as intermediary. This model was chosen for many reasons. For more information, see [RPC over HTTP Security](rpc-over-http-security.md).

This section provides an overview of RPC over HTTP in the following topics:

-   [Using HTTP as an RPC Transport](using-http-as-an-rpc-transport.md)
-   [RPC over HTTP Security](rpc-over-http-security.md)
-   [System Requirements and Interoperability for RPC over HTTP](system-requirements-and-interoperability-for-rpc-over-http.md)
-   [Configuring Computers for RPC over HTTP](configuring-computers-for-rpc-over-http.md)
-   [RPC over HTTP Deployment Recommendations](rpc-over-http-deployment-recommendations.md)

For information regarding high volume RPC over HTTP scenarios, please see [Microsoft RPC Load Balancing](rpc-load-balancing.md).

 

 




