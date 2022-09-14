---
description: An AppContainer is implemented by adding new information to the process token, changing SeAccessCheck() so that all legacy, unmodified access control list (ACL) objects block access requests from AppContainer processes by default, and re-ACL objects that should be available to AppContainers.
ms.assetid: C70A2F8C-27CB-4298-AA31-8F5099616625
title: Implementing an AppContainer
ms.topic: article
ms.date: 05/31/2018
---

# Implementing an AppContainer

An AppContainer is implemented by adding new information to the process token, changing [**SeAccessCheck()**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-seaccesscheck) so that all legacy, unmodified access control list (ACL) objects block access requests from AppContainer processes by default, and re-ACL objects that should be available to AppContainers.

## The process

Begin by adding new information for the process token. Then change **SeAccessCheck()** so that all legacy, unmodified ACLs will block access requests from AppContainer processes by default. Finally, re-ACL resources that should be available to AppContainers

The AppContainer SID is a persistent unique identifier for the appcontainer. Capability SIDs grant access to groups of resources to groups of AppContainers. An AppContainerNumber is a transient **DWORD** used to distinguish between AppContainers. However, it should not be used as an identity for the AppContainer.

To allow a single AppContainer to access a resource, add its AppContainerSID to the ACL for that resource.

To allow several specific AppContainers to access a resource, add all of their AppContainerSIDs to the ACL for that resource.

To manage groups of permissions, create a Capability SID (a GUID) and put that Capability SID on all of the resources to be granted. Then add the Capability SID to your process token.

To allow all AppContainers to access a resource, add the **ALL APPLICATION PACKAGES** SID to the ACL for that resource. This acts like a wildcard.

Both AppContainerSID and CapabilitySID support access masks in Access Control Entries (ACE). Set as appropriate.

 

 
