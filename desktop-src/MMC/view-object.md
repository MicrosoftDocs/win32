---
title: View Object object
description: The View object encapsulates a single MDI child window in the MMC console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 004043d1-c7c3-4385-a4f5-a7fbf616d05c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- View Object object MMC
- View Object object MMC , described
topic_type:
- apiref
api_name:
- View Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# View Object object

The **View** object encapsulates a single MDI child window in the MMC console.

Additionally, the **View** object serves as the [**external object**](_inet_external_object_scr) when an MMC snap-in hosts Microsoft Internet Explorer browser components.

## Members

The **View Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **View Object** object has these methods.



| Method                                                                      | Description                                                                              |
|:----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**Back**](view-back.md)                                                   | Moves to the previous view.<br/>                                                   |
| [**Close**](view-close.md)                                                 | Closes the view.<br/>                                                              |
| [**CopyScopeNode**](view-copyscopenode.md)                                 | Copies the data object of the specified scope node to the clipboard.<br/>          |
| [**CopySelection**](view-copyselection.md)                                 | Copies the data object of the current selection to the clipboard.<br/>             |
| [**DeleteScopeNode**](view-deletescopenode.md)                             | Deletes the specified scope node.<br/>                                             |
| [**DeleteSelection**](view-deleteselection.md)                             | Deletes the selected items.<br/>                                                   |
| [**Deselect**](view-deselect.md)                                           | Clears a single node.<br/>                                                         |
| [**DisplayScopeNodePropertySheet**](view-displayscopenodepropertysheet.md) | Displays the property sheet for a specified scope node.<br/>                       |
| [**DisplaySelectionPropertySheet**](view-displayselectionpropertysheet.md) | Displays the property sheet for the current selection.<br/>                        |
| [**ExecuteScopeNodeMenuItem**](view-executescopenodemenuitem.md)           | Executes a menu item for the specified scope item.<br/>                            |
| [**ExecuteSelectionMenuItem**](view-executeselectionmenuitem.md)           | Executes a menu item for the current selection.<br/>                               |
| [**ExecuteShellCommand**](view-executeshellcommand.md)                     | Executes a shell command in a window.<br/>                                         |
| [**ExportList**](view-exportlist.md)                                       | Exports the view list to a specified file.<br/>                                    |
| [**Forward**](view-forward.md)                                             | Moves to the next view.<br/>                                                       |
| [**Is**](view-is.md)                                                       | Returns whether this view is the same as a specified view.<br/>                    |
| [**IsSelected**](view-isselected.md)                                       | Returns whether a single node is selected.<br/>                                    |
| [**RefreshScopeNode**](view-refreshscopenode.md)                           | Refreshes the display of the specified scope node.<br/>                            |
| [**RefreshSelection**](view-refreshselection.md)                           | Refreshes the display of the selected items.<br/>                                  |
| [**RenameScopeNode**](view-renamescopenode.md)                             | Renames a specified scope node.<br/>                                               |
| [**RenameSelectedItem**](view-renameselecteditem.md)                       | Renames the selected item.<br/>                                                    |
| [**Select**](view-select.md)                                               | Selects a single item in the result pane.<br/>                                     |
| [**SelectAll**](view-selectall.md)                                         | Selects all items in the result pane.<br/>                                         |
| [**SnapinScopeObject**](view-snapinscopeobject.md)                         | Returns the automation interface of the snap-in for the specified scope node.<br/> |
| [**SnapinSelectionObject**](view-snapinselectionobject.md)                 | Returns the automation interface of the snap-in selection.<br/>                    |
| [**ViewMemento**](view-viewmemento.md)                                     | Restores the view to a previously recorded state.<br/>                             |



 

### Properties

The **View Object** object has these properties.



| Property                                                             | Access type           | Description                                                                                                                                                              |
|:---------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActiveScopeNode**](view-activescopenode.md)<br/>           | Read/write<br/> | The active scope node, which owns the view.<br/>                                                                                                                   |
| [**CellContents**](view-cellcontents.md)<br/>                 | Read-only<br/>  | Returns the contents of a cell referenced by a [**Node**](node-object.md) object and a column.<br/>                                                               |
| [**Columns**](view-columns.md)<br/>                           | Read-only<br/>  | Returns the [**Columns**](columns-collection.md) object for the list view.<br/>                                                                                   |
| [**ControlObject**](view-controlobject.md)<br/>               | Read-only<br/>  | Returns the automation interface supplied by the control in the result pane. This property is valid only when an OCX control is displayed in the result view.<br/> |
| [**Document**](view-document.md)<br/>                         | Read-only<br/>  | The [**Document**](document-object.md) object that represents the parent of the view.<br/>                                                                        |
| [**Frame**](view-frame.md)<br/>                               | Read-only<br/>  | The [**Frame**](frame-object.md) object for the view.<br/>                                                                                                        |
| [**ListItems**](view-listitems.md)<br/>                       | Read-only<br/>  | Returns a [**Nodes**](nodes-collection.md) object that represents all items in the list.<br/>                                                                     |
| [**ListViewMode**](view-listviewmode.md)<br/>                 | Read/write<br/> | Returns the mode of the list view; applies only if a list view is being displayed.<br/>                                                                            |
| [**Memento**](view-memento.md)<br/>                           | Read-only<br/>  | Returns a string that represents the current view.<br/>                                                                                                            |
| [**ScopeNodeContextMenu**](view-scopenodecontextmenu.md)<br/> | Read/write<br/> | The [**ContextMenu**](contextmenu-object.md) object for a given node.<br/>                                                                                        |
| [**ScopeTreeVisible**](view-scopetreevisible.md)<br/>         | Read/write<br/> | The visible state for the scope tree.<br/>                                                                                                                         |
| [**Selection**](view-selection.md)<br/>                       | Read-only<br/>  | The set of selected result nodes.<br/>                                                                                                                             |
| [**SelectionContextMenu**](view-selectioncontextmenu.md)<br/> | Read-only<br/>  | The [**ContextMenu**](contextmenu-object.md) object for the selected node.<br/>                                                                                   |
| [**StatusBarText**](view-statusbartext.md)<br/>               | Write-only<br/> | The text in the status bar.<br/>                                                                                                                                   |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>                 |



 

 





