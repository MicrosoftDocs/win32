---
description: The notion of blocking in a Windows environment has historically been a very important one.
ms.assetid: bd2ede96-34a4-4912-b9d2-ef11d37d2292
title: Blocking Operations
ms.topic: article
ms.date: 05/31/2018
---

# Blocking Operations

The notion of blocking in a Windows environment has historically been a very important one. In Windows Sockets 1.1 environments, blocking calls were discouraged since they tended to disable ongoing interaction with the system. Additionally, they employ a pseudoblocking technique which, for a variety of reasons, does not always work as intended. However, in preemptively scheduled Windows environments, blocking calls make much more sense, can be implemented by native operating system services, and are in fact a generally preferred mechanism. The Winsock 2 API no longer supports psuedoblocking, but because the Windows Sockets 1.1 compatibility shims must continue to emulate this behavior, service providers must support this as described in the following.

 

 



