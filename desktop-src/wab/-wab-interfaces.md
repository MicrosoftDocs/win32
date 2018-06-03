---
title: Windows Address Book Interfaces
description: This section describes the interfaces associated with WAB.
ms.assetid: 66ecba78-6fff-4570-b86c-6478ad1df38c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Address Book Interfaces

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](https://www.bing.com/search?q=Windows Contacts).

 

This section describes the interfaces associated with WAB.

### Interfaces



| Topic                                     | Contents                                                                                                                                                                                                                                                             |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IABContainer**](/previous-versions/windows/desktop/api/Wabdefs/) | Do not use. This interface provides access to address book containers. Applications call the methods of the interface to perform name resolution and to create, copy, and delete recipients.<br/>                                                              |
| [**IAddrBook**](/previous-versions/windows/desktop/api/Wabiab/)       | Do not use. This interface supports access to the WAB and includes operations such as displaying common dialog boxes, opening containers, messaging users (contacts) and distribution lists (groups) in the address book, and performing name resolution.<br/> |
| [**IDistList**](/previous-versions/windows/desktop/api/wabdefs/)       | Do not use. This interface is used to provide access to distribution lists in modifiable address book containers. The interface provides methods to create, copy, and delete distribution lists, in addition to performing name resolution.<br/>               |
| [**IMailUser**](/previous-versions/windows/desktop/api/wabdefs/)       | Do not use. This interface provides access to a mail user object.<br/>                                                                                                                                                                                         |
| [**IMAPITable**](/previous-versions/windows/desktop/api/Wabdefs/)     | Do not use. This interface is used for content tables of WAB containers and distribution lists.<br/>                                                                                                                                                           |
| [**IWABExtInit**](/previous-versions/windows/desktop/api/Wabapi/)   | Do not use. This interface ndicates which WAB object is being displayed (for example, a property sheet or context menu).<br/>                                                                                                                                  |
| [**IWABObject**](/previous-versions/windows/desktop/api/Wabapi/)     | Do not use. This interface provides access to the WAB object which contains function pointers to memory allocation functions and database maintenance functions. <br/>                                                                                         |



 

 

 





