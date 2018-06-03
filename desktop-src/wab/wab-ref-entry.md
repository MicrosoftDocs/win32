---
title: Windows Address Book API Reference
description: The following reference articles are available for the WAB \ 160;API.
ms.assetid: 117050b9-e331-4ed1-b632-a6ff418bc83a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Address Book API Reference

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](https://www.bing.com/search?q=Windows Contacts).

 

The following reference articles are available for the WAB API.

### Functions



| Topic                               | Contents                                                                                                                                                                                                                                                        |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WABOpen**](/previous-versions/windows/desktop/api/Wabapi/nc-wabapi-wabopen)     | Do not use. Provides access to the address book through a number of object interfaces. The root interface is [**IAddrBook**](/previous-versions/windows/desktop/api/Wabiab/), which is a subset of the MAPI implementation of [IAddrBook](https://msdn.microsoft.com/windows/desktop/2681e3cf-a251-4c9d-9474-fc320fedede8).<br/> |
| [**WABOpenEx**](/previous-versions/windows/desktop/api/Wabapi/nc-wabapi-wabopenex) | Do not use. Provides access to the WAB through a number of object interfaces. The root interface is [**IAddrBook**](/previous-versions/windows/desktop/api/Wabiab/), which is a subset of the MAPI implementation of [IAddrBook](https://msdn.microsoft.com/windows/desktop/2681e3cf-a251-4c9d-9474-fc320fedede8). <br/>         |



 

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



 

### Enumerations



| Topic                         | Contents                                                                                                                        |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**Gender**](/previous-versions/windows/desktop/api/Wabtags/ne-wabtags-gender) | Do not use. The [**Gender**](/previous-versions/windows/desktop/api/Wabtags/ne-wabtags-gender) enumeration specifies the possible values for the PR\_GENDER property.<br/> |



 

### Structures



| Topic                                               | Contents                                                                                                                                                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADRENTRY**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrentry)                   | Do not use. Describes zero or more properties belonging to one or more recipients.<br/>                                                                                            |
| [**ADRLIST**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrlist)                     | Do not use. Describes zero or more properties belonging to one or more recipients. <br/>                                                                                           |
| [**ADRPARM**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrparm)                     | Do not use. Describes the display and behavior of the common address dialog box. <br/>                                                                                             |
| [**ENTRYID**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-entryid)                     | Do not use. Contains the entry identifier information for a MAPI object.<br/>                                                                                                      |
| [**ENTRYLIST**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_sbinaryarray)                 | Do not use. An array of entry identifiers representing MAPI objects. Uses the same implementation as [SBinaryArray](https://msdn.microsoft.com/windows/desktop/31fc6e1b-c2c1-4e74-a760-957a60005d1e).<br/>                    |
| [**SPropProblem**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropproblem)           | Do not use. Describes an error relating to an operation involving a property.<br/>                                                                                                 |
| [**SPropProblemArray**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropproblemarray) | Do not use. Contains an array of one or more [**SPropProblem**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropproblem) structures.<br/>                                                                            |
| [**SPropTagArray**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_sproptagarray)         | Do not use. Contains an array of property tags.<br/>                                                                                                                               |
| [**SPropValue**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropvalue)               | Do not use. Contains the property tag values.<br/>                                                                                                                                 |
| [**SRestriction**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_srestriction)           | Do not use. Describes a filter for limiting the view of a table to particular rows.<br/>                                                                                           |
| [**SRow**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_srow)                           | Do not use. Describes a row from a table containing selected properties for a specific object.<br/>                                                                                |
| [**SRowSet**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_srowset)                     | Do not use. Contains an array of [**SRow**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_srow) structures. Each **SRow** structure describes a row from a table.<br/>                                                  |
| [**SSortOrder**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_ssortorder)               | Do not use. Defines how to sort rows of a table, describing both the column to use as the sort key and the direction of the sort.<br/>                                             |
| [**SSortOrderSet**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_ssortorderset)         | Do not use. Defines a collection of keys for a table to be used for standard or categorized sorting.<br/>                                                                          |
| [**WAB\_PARAM**](/previous-versions/windows/desktop/api/Wabapi/ns-wabapi-_tagwab_param)                | Do not use. Contains the input information to pass to [**WABOpen**](/previous-versions/windows/desktop/api/Wabapi/nc-wabapi-wabopen).<br/>                                                                                        |
| [**WABEXTDISPLAY**](/previous-versions/windows/desktop/api/Wabapi/ns-wabapi-_wabextdisplay)         | Do not use. Used by the WAB to initialize user's [IContextMenu Interface](https://www.bing.com/search?q=IContextMenu Interface) and [IShellPropSheetExt Interface](https://www.bing.com/search?q=IShellPropSheetExt Interface) implementations.<br/> |
| [**WABIMPORTPARAM**](/previous-versions/windows/desktop/api/Wabapi/ns-wabapi-_wabimportparam)       | Do not use. Structure passed to [**Import**](/previous-versions/windows/desktop/api/Wabapi/) that gives information about importing .wab files.<br/>                                                   |



 

 

 





