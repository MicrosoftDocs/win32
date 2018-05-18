---
Description: 'If your network provider needs to support browsing of its network resources, it should implement the following functions. MPR calls these functions to enumerate the resources.'
ms.assetid: '9f7c0e5b-1358-43f8-84e4-26e84a2275ba'
title: Enumeration Functions
---

# Enumeration Functions

If your network provider needs to support browsing of its network resources, it should implement the following functions. MPR calls these functions to enumerate the resources.

A network provider is not required to implement any of the enumeration functions. If, however, a network provider implements either [**NPOpenEnum**](npopenenum.md), [**NPEnumResource**](npenumresource.md), or [**NPCloseEnum**](npcloseenum.md), it must also implement the other two enumeration functions.



| Function                                                     | Description                                                                                                                                                         |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPOpenEnum**](npopenenum.md)                             | Opens an enumeration of network resources or existing connections.                                                                                                  |
| [**NPEnumResource**](npenumresource.md)                     | Performs an enumeration on a handle returned by [**NPOpenEnum**](npopenenum.md).                                                                                   |
| [**NPCloseEnum**](npcloseenum.md)                           | Closes an enumeration.                                                                                                                                              |
| [**NPGetResourceInformation**](npgetresourceinformation.md) | Determines whether the provider is the correct provider to respond to a request for a specified network resource and returns information about the resource's type. |
| [**NPGetResourceParent**](npgetresourceparent.md)           | Returns the parent of a specified network resource in the browse hierarchy.                                                                                         |



 

 

 



