---
title: System.Shell.Folder object
description: Defines the properties and methods for performing file management operations as well as the properties for the Items collection.
ms.assetid: '62d32b81-6055-45b6-ba17-eaf7bdd7cc0a'
keywords: ["System.Shell.Folder object Windows Sidebar", "System.Shell.Folder object Windows Sidebar , described"]
topic_type:
- apiref
api_name:
- System.Shell.Folder
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Folder object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods for performing file management operations as well as the properties for the [**Items**](system-shell-folder-items.md) collection.

> [!Note]  
> Objects of type [**System.Shell.Item**](system-shell-item.md) can only be accessed through the [**Items**](system-shell-folder-items.md) collection. This collection is a member of **System.Shell.Folder**.

 

## Members

The **System.Shell.Folder** object has these types of members:

-   [Collections](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Collections

The **System.Shell.Folder** object has these collections.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Collection</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>Items</strong>](system-shell-folder-items.md)</td>
<td style="text-align: left;">A collection of [<strong>System.Shell.Item</strong>](system-shell-item.md) objects. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Shell.Item</strong>](system-shell-item.md) can only be accessed through the [<strong>Items</strong>](system-shell-folder-items.md) collection. This collection is a member of <strong>System.Shell.Folder</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Methods

The **System.Shell.Folder** object has these methods.



| Method                                             | Description                                                                                                      |
|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**copyHere**](system-shell-folder-copyhere.md)   | Copies a [**System.Shell.Item**](system-shell-item.md) to a folder. <br/>                                 |
| [**moveHere**](system-shell-folder-movehere.md)   | Moves a [**System.Shell.Item**](system-shell-item.md) to a folder. <br/>                                  |
| [**newFolder**](system-shell-folder-newfolder.md) | Creates a new folder. <br/>                                                                                |
| [**parse**](system-shell-folder-parse.md)         | Retrieves a **System.Shell.Folder** object that represents the folder containing the specified file. <br/> |



 

### Properties

The **System.Shell.Folder** object has these properties.



| Property                                                | Access type          | Description                                                                                                 |
|:--------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------|
| [**Parent**](system-shell-folder-parent.md)<br/> | Read-only<br/> | Gets a [**System.Shell.Item**](system-shell-item.md) object that represents the parent folder. <br/> |
| [**Self**](system-shell-folder-self.md)<br/>     | Read-only<br/> | Gets a duplicate **System.Shell.Folder** object. <br/>                                                |



 

## Remarks

Each [**System.Shell.Item**](system-shell-item.md) in the [**Items**](system-shell-folder-items.md) collection corresponds to a file system object present on the machine.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





