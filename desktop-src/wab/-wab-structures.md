---
title: Windows Address Book Structures
description: This section describes the structures associated with WAB.
ms.assetid: '16c36aa6-a973-44b6-82ad-40343b093836'
---

# Windows Address Book Structures

New applications should not use these structures. These structures exist for backward compatibility with legacy applications. These structures will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

This section describes the structures associated with WAB.

### Structures



| Topic                                               | Contents                                                                                                                                                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADRENTRY**](-wab-adrentry.md)                   | Do not use. Describes zero or more properties belonging to one or more recipients.<br/>                                                                                            |
| [**ADRLIST**](-wab-adrlist.md)                     | Do not use. Describes zero or more properties belonging to one or more recipients. <br/>                                                                                           |
| [**ADRPARM**](-wab-adrparm.md)                     | Do not use. Describes the display and behavior of the common address dialog box. <br/>                                                                                             |
| [**ENTRYID**](-wab-entryid.md)                     | Do not use. Contains the entry identifier information for a MAPI object.<br/>                                                                                                      |
| [**ENTRYLIST**](-wab-entrylist.md)                 | Do not use. An array of entry identifiers representing MAPI objects. Uses the same implementation as [SBinaryArray](31fc6e1b-c2c1-4e74-a760-957a60005d1e).<br/>                    |
| [**SPropProblem**](-wab-spropproblem.md)           | Do not use. Describes an error relating to an operation involving a property.<br/>                                                                                                 |
| [**SPropProblemArray**](-wab-spropproblemarray.md) | Do not use. Contains an array of one or more [**SPropProblem**](-wab-spropproblem.md) structures.<br/>                                                                            |
| [**SPropTagArray**](-wab-sproptagarray.md)         | Do not use. Contains an array of property tags.<br/>                                                                                                                               |
| [**SPropValue**](-wab-spropvalue.md)               | Do not use. Contains the property tag values.<br/>                                                                                                                                 |
| [**SRestriction**](-wab-srestriction.md)           | Do not use. Describes a filter for limiting the view of a table to particular rows.<br/>                                                                                           |
| [**SRow**](-wab-srow.md)                           | Do not use. Describes a row from a table containing selected properties for a specific object.<br/>                                                                                |
| [**SRowSet**](-wab-srowset.md)                     | Do not use. Contains an array of [**SRow**](-wab-srow.md) structures. Each **SRow** structure describes a row from a table.<br/>                                                  |
| [**SSortOrder**](-wab-ssortorder.md)               | Do not use. Defines how to sort rows of a table, describing both the column to use as the sort key and the direction of the sort.<br/>                                             |
| [**SSortOrderSet**](-wab-ssortorderset.md)         | Do not use. Defines a collection of keys for a table to be used for standard or categorized sorting.<br/>                                                                          |
| [**WAB\_PARAM**](-wab-wab-param.md)                | Do not use. Contains the input information to pass to [**WABOpen**](-wab-wabopen.md).<br/>                                                                                        |
| [**WABEXTDISPLAY**](-wab-wabextdisplay.md)         | Do not use. Used by the WAB to initialize user's [IContextMenu Interface](_win32_IContextMenu) and [IShellPropSheetExt Interface](_win32_IShellPropSheetExt) implementations.<br/> |
| [**WABIMPORTPARAM**](-wab-wabimportparam.md)       | Do not use. Structure passed to [**Import**](-wab-iwabobject-import.md) that gives information about importing .wab files.<br/>                                                   |



 

 

 





