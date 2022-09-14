---
description: TLS is a standard closely related to SSL 3.0, and is sometimes referred to as &\#0034;SSL 3.1&\#0034;.
ms.assetid: 92b1b486-7e10-48a2-b1d2-56d4e472dbe4
title: TLS vs. SSL
ms.topic: article
ms.date: 05/31/2018
---

# TLS vs. SSL

TLS is a standard closely related to SSL 3.0, and is sometimes referred to as "SSL 3.1". TLS supersedes SSL 2.0 and should be used in new development. Beginning with Windows 10, version 1607 and Windows Server 2016, SSL 2.0 has been removed and is no longer supported.

Applications that require a high level of interoperability should support SSL 3.0 and TLS. Because of the similarities between these two protocols, SSL details are not included in this documentation, except where they differ from TLS. The following is from [RFC 2246](https://www.ietf.org/rfc/rfc2246.txt):

"The differences between this protocol and SSL 3.0 are not dramatic, but they are significant enough that TLS 1.0 and SSL 3.0 do not interoperate (although TLS 1.0 does incorporate a mechanism by which a TLS implementation can back down to SSL 3.0)."

 

 



