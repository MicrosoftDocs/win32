---
title: Windows Address Book Functions
description: This section describes the functions associated with WAB.
ms.assetid: 8748e2d7-72ff-4c21-bda1-7ed79c999b9c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Address Book Functions

New applications should not use these functions. These functions exist for backward compatibility with legacy applications. These functions will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

This section describes the functions associated with WAB.

### Functions



| Topic                               | Contents                                                                                                                                                                                                                                                        |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WABOpen**](/windows/previous-versions/Wabapi/nc-wabapi-wabopen?branch=master)     | Do not use. Provides access to the address book through a number of object interfaces. The root interface is [**IAddrBook**](/windows/previous-versions/Wabiab/?branch=master), which is a subset of the MAPI implementation of [IAddrBook](2681e3cf-a251-4c9d-9474-fc320fedede8).<br/> |
| [**WABOpenEx**](/windows/previous-versions/Wabapi/nc-wabapi-wabopenex?branch=master) | Do not use. Provides access to the WAB through a number of object interfaces. The root interface is [**IAddrBook**](/windows/previous-versions/Wabiab/?branch=master), which is a subset of the MAPI implementation of [IAddrBook](2681e3cf-a251-4c9d-9474-fc320fedede8). <br/>         |



 

 

 





