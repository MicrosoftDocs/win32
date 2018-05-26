---
title: Windows Address Book Structures
description: This section describes the structures associated with WAB.
ms.assetid: 16c36aa6-a973-44b6-82ad-40343b093836
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Address Book Structures

New applications should not use these structures. These structures exist for backward compatibility with legacy applications. These structures will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

This section describes the structures associated with WAB.

### Structures



| Topic                                               | Contents                                                                                                                                                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADRENTRY**](/windows/previous-versions/Wabdefs/ns-wabdefs-_adrentry?branch=master)                   | Do not use. Describes zero or more properties belonging to one or more recipients.<br/>                                                                                            |
| [**ADRLIST**](/windows/previous-versions/Wabdefs/ns-wabdefs-_adrlist?branch=master)                     | Do not use. Describes zero or more properties belonging to one or more recipients. <br/>                                                                                           |
| [**ADRPARM**](/windows/previous-versions/Wabdefs/ns-wabdefs-_adrparm?branch=master)                     | Do not use. Describes the display and behavior of the common address dialog box. <br/>                                                                                             |
| [**ENTRYID**](/windows/previous-versions/Wabdefs/ns-wabdefs-entryid?branch=master)                     | Do not use. Contains the entry identifier information for a MAPI object.<br/>                                                                                                      |
| [**ENTRYLIST**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sbinaryarray?branch=master)                 | Do not use. An array of entry identifiers representing MAPI objects. Uses the same implementation as [SBinaryArray](31fc6e1b-c2c1-4e74-a760-957a60005d1e).<br/>                    |
| [**SPropProblem**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropproblem?branch=master)           | Do not use. Describes an error relating to an operation involving a property.<br/>                                                                                                 |
| [**SPropProblemArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropproblemarray?branch=master) | Do not use. Contains an array of one or more [**SPropProblem**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropproblem?branch=master) structures.<br/>                                                                            |
| [**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master)         | Do not use. Contains an array of property tags.<br/>                                                                                                                               |
| [**SPropValue**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropvalue?branch=master)               | Do not use. Contains the property tag values.<br/>                                                                                                                                 |
| [**SRestriction**](/windows/previous-versions/Wabdefs/ns-wabdefs-_srestriction?branch=master)           | Do not use. Describes a filter for limiting the view of a table to particular rows.<br/>                                                                                           |
| [**SRow**](/windows/previous-versions/Wabdefs/ns-wabdefs-_srow?branch=master)                           | Do not use. Describes a row from a table containing selected properties for a specific object.<br/>                                                                                |
| [**SRowSet**](/windows/previous-versions/Wabdefs/ns-wabdefs-_srowset?branch=master)                     | Do not use. Contains an array of [**SRow**](/windows/previous-versions/Wabdefs/ns-wabdefs-_srow?branch=master) structures. Each **SRow** structure describes a row from a table.<br/>                                                  |
| [**SSortOrder**](/windows/previous-versions/Wabdefs/ns-wabdefs-_ssortorder?branch=master)               | Do not use. Defines how to sort rows of a table, describing both the column to use as the sort key and the direction of the sort.<br/>                                             |
| [**SSortOrderSet**](/windows/previous-versions/Wabdefs/ns-wabdefs-_ssortorderset?branch=master)         | Do not use. Defines a collection of keys for a table to be used for standard or categorized sorting.<br/>                                                                          |
| [**WAB\_PARAM**](/windows/previous-versions/Wabapi/ns-wabapi-_tagwab_param?branch=master)                | Do not use. Contains the input information to pass to [**WABOpen**](/windows/previous-versions/Wabapi/nc-wabapi-wabopen?branch=master).<br/>                                                                                        |
| [**WABEXTDISPLAY**](/windows/previous-versions/Wabapi/ns-wabapi-_wabextdisplay?branch=master)         | Do not use. Used by the WAB to initialize user's [IContextMenu Interface](_win32_IContextMenu) and [IShellPropSheetExt Interface](_win32_IShellPropSheetExt) implementations.<br/> |
| [**WABIMPORTPARAM**](/windows/previous-versions/Wabapi/ns-wabapi-_wabimportparam?branch=master)       | Do not use. Structure passed to [**Import**](/windows/previous-versions/Wabapi/?branch=master) that gives information about importing .wab files.<br/>                                                   |



 

 

 





