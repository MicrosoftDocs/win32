---
Description: If your network provider needs to support browsing of its network resources, it should implement the following functions. MPR calls these functions to enumerate the resources.
ms.assetid: 9f7c0e5b-1358-43f8-84e4-26e84a2275ba
title: Enumeration Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumeration Functions

If your network provider needs to support browsing of its network resources, it should implement the following functions. MPR calls these functions to enumerate the resources.

A network provider is not required to implement any of the enumeration functions. If, however, a network provider implements either [**NPOpenEnum**](/windows/win32/Npapi/nf-npapi-npopenenum?branch=master), [**NPEnumResource**](/windows/win32/Npapi/nf-npapi-npenumresource?branch=master), or [**NPCloseEnum**](/windows/win32/Npapi/nf-npapi-npcloseenum?branch=master), it must also implement the other two enumeration functions.



| Function                                                     | Description                                                                                                                                                         |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPOpenEnum**](/windows/win32/Npapi/nf-npapi-npopenenum?branch=master)                             | Opens an enumeration of network resources or existing connections.                                                                                                  |
| [**NPEnumResource**](/windows/win32/Npapi/nf-npapi-npenumresource?branch=master)                     | Performs an enumeration on a handle returned by [**NPOpenEnum**](/windows/win32/Npapi/nf-npapi-npopenenum?branch=master).                                                                                   |
| [**NPCloseEnum**](/windows/win32/Npapi/nf-npapi-npcloseenum?branch=master)                           | Closes an enumeration.                                                                                                                                              |
| [**NPGetResourceInformation**](/windows/win32/Npapi/nf-npapi-npgetresourceinformation?branch=master) | Determines whether the provider is the correct provider to respond to a request for a specified network resource and returns information about the resource's type. |
| [**NPGetResourceParent**](/windows/win32/Npapi/nf-npapi-npgetresourceparent?branch=master)           | Returns the parent of a specified network resource in the browse hierarchy.                                                                                         |



 

 

 



