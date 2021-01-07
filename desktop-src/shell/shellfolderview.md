---
description: Represents the objects in a view and provides properties and methods used to obtain information about the contents of the view.
ms.assetid: '3b866266-fee0-42f7-a1e0-9adb6cc2e23f'
title: ShellFolderView object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderView
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellFolderView object

Represents the objects in a view and provides properties and methods used to obtain information about the contents of the view.

## Members

The **ShellFolderView** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **ShellFolderView** object has these events.



| Event                                                        | Description                                                                              |
|:-------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**SelectionChanged**](shellfolderview-selectionchanged.md) | Occurs when the selection state of any item or items in the view has changed.<br/> |



 

### Methods

The **ShellFolderView** object has these methods.



| Method                                                 | Description                                                                                                        |
|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**PopupItemMenu**](shellfolderview-popupitemmenu.md) | Creates a shortcut menu for the specified item and returns the selected command string.<br/>                 |
| [**SelectedItems**](shellfolderview-selecteditems.md) | Gets a [**FolderItems**](folderitems.md) object that represents all of the selected items in the view.<br/> |
| [**SelectItem**](shellfolderview-selectitem.md)       | Sets the selection state of an item in the view.<br/>                                                        |



 

### Properties

The **ShellFolderView** object has these properties.



| Property                                                      | Access type          | Description                                                                                                  |
|:--------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------|
| [**Application**](shellfolderview-application.md)<br/> | Read-only<br/> | Contains the object's Application object.<br/>                                                         |
| [**FocusedItem**](shellfolderview-focuseditem.md)<br/> | Read-only<br/> | Gets a [**FolderItem**](folderitem.md) object that represents the item that has the input focus.<br/> |
| [**Folder**](shellfolderview-folder.md)<br/>           | Read-only<br/> | Gets a [**Folder**](folder.md) object that represents the view.<br/>                                  |
| [**Parent**](shellfolderview-parent.md)<br/>           | Read-only<br/> | Not implemented.<br/>                                                                                  |
| [**Script**](shellfolderview-script.md)<br/>           | Read-only<br/> | Deprecated.<br/>                                                                                       |
| [**ViewOptions**](shellfolderview-viewoptions.md)<br/> | Read-only<br/> | Gets a set of flags that indicate the current options of the view.<br/>                                |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |
| IID<br/>                      | CLSID\_ShellFolderView<br/>                                                                              |



## See also

<dl> <dt>

[**ShellFolderViewOptions Flags**](/windows/desktop/api/Shldisp/ne-shldisp-shellfolderviewoptions)
</dt> </dl>

 

 




