---
description: The following interface definition is provided as a standard that can be followed when developing a smart card service provider.
ms.assetid: 68cc0bbe-ce8e-4da1-b907-596caa95a39c
title: ISCardFileAccess interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess
api_type: 
- COM
api_location: 
---

# ISCardFileAccess interface

\[The **ISCardFileAccess** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The following interface definition is provided as a standard that can be followed when developing a [*smart card*](../secgloss/s-gly.md) [*service provider*](../secgloss/c-gly.md).

The **ISCardFileAccess** interface can be used to implement a high-level interface to a card-based file system with an underlying card file system based on the structure defined in ISO/IEC 7816-4. Other implementations are possible, but this is expected to be the most common.

The **ISCardFileAccess** interface can be used to expose file system entities in a manner very familiar to application developers in the PC environment. It provides mechanisms for locating specific files and performing common operations such as selecting, reading, writing, creating and deleting. It encapsulates and masks much of the low-level detail involved in performing these operations at the card level.

Following is a typical use of the **ISCardFileAccess** interface. In this case, the **ISCardFileAccess** interface is used to select, open, and write to a file.

**To write to a file**

1.  Call [**ISCardManage::CreateFileAccess**](iscardmanage-createfileaccess.md) to create an **ISCardFileAccess** interface.
2.  Call [**Open**](iscardfileaccess-open.md) to select and open the file.
3.  Call [**Write**](iscardfileaccess-write.md).
4.  Call [**Close**](iscardfileaccess-close.md).
5.  Release the **ISCardFileAccess** interface.

## Members

The **ISCardFileAccess** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCardFileAccess** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardFileAccess** interface has these methods.



| Method                                                              | Description                                                                                                                                  |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeDir**](iscardfileaccess-changedir.md)                     | Changes the current smart card directory to the new specified directory.<br/>                                                          |
| [**Close**](iscardfileaccess-close.md)                             | Closes the specified file.<br/>                                                                                                        |
| [**Create**](iscardfileaccess-create.md)                           | Creates a file at a given location within the ICC file system.<br/>                                                                    |
| [**Delete**](iscardfileaccess-delete.md)                           | Deletes a specified file.<br/>                                                                                                         |
| [**Directory**](iscardfileaccess-directory.md)                     | Retrieves a list of files.<br/>                                                                                                        |
| [**GetCurrentDir**](iscardfileaccess-getcurrentdir.md)             | Returns an absolute path to the currently selected directory.<br/>                                                                     |
| [**GetFileCapabilities**](iscardfileaccess-getfilecapabilities.md) | Retrieves file capabilities.<br/>                                                                                                      |
| [**GetProperties**](iscardfileaccess-getproperties.md)             | Retrieves the primitive data referred by tags for the specified object.<br/>                                                           |
| [**Invalidate**](iscardfileaccess-invalidate.md)                   | Makes the specified file not valid.<br/>                                                                                               |
| [**Open**](iscardfileaccess-open.md)                               | Opens the specified file for further use.<br/>                                                                                         |
| [**Read**](iscardfileaccess-read.md)                               | Reads and returns the specified data from a given file.<br/>                                                                           |
| [**Rehabilitate**](iscardfileaccess-rehabilitate.md)               | Makes a file (EF or DF), which has been previously made not valid by using the Invalidate command, accessible by the application.<br/> |
| [**Seek**](iscardfileaccess-seek.md)                               | Selects the object from which read/write permission will be done.<br/>                                                                 |
| [**SetProperties**](iscardfileaccess-setproperties.md)             | Sets the primitive data referred by tags for the specified object.<br/>                                                                |
| [**Write**](iscardfileaccess-write.md)                             | Writes data to a current opened file.<br/>                                                                                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



 

 
