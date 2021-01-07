---
description: If your network provider needs to support browsing of its network resources, it should implement the following functions. MPR calls these functions to enumerate the resources.
ms.assetid: 9f7c0e5b-1358-43f8-84e4-26e84a2275ba
title: Enumeration Functions
ms.topic: article
ms.date: 05/31/2018
---

# Enumeration Functions

If your network provider needs to support browsing of its network resources, it should implement the following functions. MPR calls these functions to enumerate the resources.

A network provider is not required to implement any of the enumeration functions. If, however, a network provider implements either [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum), [**NPEnumResource**](/windows/desktop/api/Npapi/nf-npapi-npenumresource), or [**NPCloseEnum**](/windows/desktop/api/Npapi/nf-npapi-npcloseenum), it must also implement the other two enumeration functions.



| Function                                                     | Description                                                                                                                                                         |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum)                             | Opens an enumeration of network resources or existing connections.                                                                                                  |
| [**NPEnumResource**](/windows/desktop/api/Npapi/nf-npapi-npenumresource)                     | Performs an enumeration on a handle returned by [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum).                                                                                   |
| [**NPCloseEnum**](/windows/desktop/api/Npapi/nf-npapi-npcloseenum)                           | Closes an enumeration.                                                                                                                                              |
| [**NPGetResourceInformation**](/windows/desktop/api/Npapi/nf-npapi-npgetresourceinformation) | Determines whether the provider is the correct provider to respond to a request for a specified network resource and returns information about the resource's type. |
| [**NPGetResourceParent**](/windows/desktop/api/Npapi/nf-npapi-npgetresourceparent)           | Returns the parent of a specified network resource in the browse hierarchy.                                                                                         |



 

 

 



