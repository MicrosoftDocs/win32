---
title: System.Shell object
description: Defines the properties and methods used to expose Windows Shell characteristics.
ms.assetid: 79b04a71-3bff-4832-b7c6-c7c3b72fdb84
keywords:
- System.Shell object Windows Sidebar
- System.Shell object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Shell
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Shell object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods used to expose [Windows Shell](http://msdn.microsoft.com/library/bb773177.aspx) characteristics.

## Members

The **System.Shell** object has these types of members:

-   [Methods](#methods)

### Methods

The **System.Shell** object has these methods.



| Method                                                    | Description                                                                                                                                                                                                                                    |
|:----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**chooseFile**](system-shell-choosefile.md)             | Displays a file picker dialog box and retrieves a [**System.Shell.Item**](system-shell-item.md) object that represents the selected file. <br/>                                                                                         |
| [**chooseFolder**](system-shell-choosefolder.md)         | Displays a folder picker dialog box and retrieves a [**System.Shell.Item**](system-shell-item.md) object that represents the selected folder. <br/>                                                                                     |
| [**drive**](system-shell-drive-method.md)                | Retrieves a [**System.Shell.Drive**](system-shell-drive.md) object that represents the specified drive. <br/>                                                                                                                           |
| [**execute**](system-shell-execute.md)                   | Launches an application. <br/>                                                                                                                                                                                                           |
| [**itemFromFileDrop**](system-shell-itemfromfiledrop.md) | Retrieves an [**System.Shell.Item**](system-shell-item.md) from the [**Items**](system-shell-folder-items.md) collection that represents the object(s) dropped on a gadget during a drag-and-drop operation (copying or moving). <br/> |
| [**itemFromPath**](system-shell-itemfrompath.md)         | Retrieves a [**System.Shell.Item**](system-shell-item.md) that represents an object at the specified UNC path. <br/>                                                                                                                    |
| [**knownFolder**](system-shell-knownfolder.md)           | Returns an instance of a [**System.Shell.Folder**](system-shell-folder.md) based on a "well-known folder" name as defined within the user profile (for example, Documents or ProgramFiles). <br/>                                       |
| [**knownFolderPath**](system-shell-knownfolderpath.md)   | Retrieves a **Known Folder** UNC path. <br/>                                                                                                                                                                                             |
| [**refreshDesktop**](system-shell-refreshdesktop.md)     | Refreshes the desktop after adding or removing files. <br/>                                                                                                                                                                              |
| [**saveFileDialog**](system-shell-savefiledialog.md)     | Displays a standard Windows **File Save** dialog box. <br/>                                                                                                                                                                              |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





