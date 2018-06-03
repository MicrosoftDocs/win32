---
Description: Extends the FolderItem object. In addition to the properties and methods supported by FolderItem, ShellFolderItem has two additional methods.
title: ShellFolderItem object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ShellFolderItem object

Extends the [**FolderItem**](folderitem.md) object. In addition to the properties and methods supported by **FolderItem**, **ShellFolderItem** has two additional methods.

## Members

The **ShellFolderItem** object has these types of members:

-   [Methods](#methods)

### Methods

The **ShellFolderItem** object has these methods.



| Method                                                       | Description                                                                                                                                                                                         |
|:-------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExtendedProperty**](shellfolderitem-extendedproperty.md) | Gets the value of a property from an item's property set. The property can be specified either by name or by the property set's format identifier (FMTID) and property identifier (PID).<br/> |
| [**InvokeVerbEx**](invokeverbex.md)                         | Executes a verb on a Shell item.<br/>                                                                                                                                                         |



 

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 




