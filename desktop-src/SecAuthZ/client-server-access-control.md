---
Description: A server application provides services to clients.
ms.assetid: 8301ed4f-9458-410b-af19-4f055656005a
title: Client/Server Access Control
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client/Server Access Control

A server application provides services to clients. For example, a server could perform the following services on behalf of a client:

-   Save and retrieve information from a private database
-   Access network resources
-   Start [*processes*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly) in the client's [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) on the server's computer

A protected server controls access to its services. Windows provides security support that enables a server to do the following:

-   Impersonate a client's [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly), which causes the system to perform most access and [*privilege*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-privilege-gly) checks against the client's [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly) rather than the server's
-   Log a client on to the server's computer
-   Connect to network resources using the client's security context
-   Create [*security descriptors*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) to protect private objects
-   Determine whether a security descriptor allows access to a client
-   Determine whether a set of privileges are enabled in a client's token
-   Generate audit messages in the security event log to record attempts by a client to access objects or use privileges

 

 



