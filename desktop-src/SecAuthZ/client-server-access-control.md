---
description: A server application provides services to clients.
ms.assetid: 8301ed4f-9458-410b-af19-4f055656005a
title: Client/Server Access Control
ms.topic: article
ms.date: 05/31/2018
---

# Client/Server Access Control

A server application provides services to clients. For example, a server could perform the following services on behalf of a client:

-   Save and retrieve information from a private database
-   Access network resources
-   Start [*processes*](/windows/desktop/SecGloss/p-gly) in the client's [*security context*](/windows/desktop/SecGloss/s-gly) on the server's computer

A protected server controls access to its services. Windows provides security support that enables a server to do the following:

-   Impersonate a client's [*security context*](/windows/desktop/SecGloss/s-gly), which causes the system to perform most access and [*privilege*](/windows/desktop/SecGloss/p-gly) checks against the client's [*access token*](/windows/desktop/SecGloss/a-gly) rather than the server's
-   Log a client on to the server's computer
-   Connect to network resources using the client's security context
-   Create [*security descriptors*](/windows/desktop/SecGloss/s-gly) to protect private objects
-   Determine whether a security descriptor allows access to a client
-   Determine whether a set of privileges are enabled in a client's token
-   Generate audit messages in the security event log to record attempts by a client to access objects or use privileges

 

 
