---
description: Forwards the events fired by a specified ShellFolderView object to corresponding ShellFolderViewOC event handlers.
title: ShellFolderViewOC object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderViewOC
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: b50f549c-a79d-4411-a18e-a181b4b924e3

---

# ShellFolderViewOC object

Forwards the events fired by a specified [**ShellFolderView**](shellfolderview.md) object to corresponding **ShellFolderViewOC** event handlers.

## Members

The **ShellFolderViewOC** object has these types of members:

- [Events](#events)
- [Methods](#methods)

### Events

The **ShellFolderViewOC** object has these events.



| Event                                                          | Description                                                                                                                     |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDone**](shellfolderviewoc-enumdone.md)                 | Indicates that the [**ShellFolderView**](shellfolderview.md) object has finished enumerating the folder's contents.<br/> |
| [**SelectionChanged**](shellfolderviewoc-selectionchanged.md) | Indicates that the selection state of one or more items in the view has changed.<br/>                                     |



 

### Methods

The **ShellFolderViewOC** object has these methods.



| Method                                                   | Description                                                                                                                                                 |
|:---------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetFolderView**](shellfolderviewoc-setfolderview.md) | Forwards the events of the specified [**ShellFolderView**](shellfolderview.md) object to the corresponding **ShellFolderViewOC** event handler.<br/> |



 

## Remarks

The [**ShellFolderView**](shellfolderview.md) object fires two events, [**EnumDone**](shellfolderviewoc-enumdone.md) and [**SelectionChanged**](shellfolderviewoc-selectionchanged.md), that are typically handled by applications. However, some applications must handle events from a series of **ShellFolderView** objects. For example, an application might host a WebBrowser control that allows users to navigate through a series of folders. Each folder has its own **ShellFolderView** object with its associated events. Handling these events can be difficult.

The **ShellFolderViewOC** object simplifies event handling for such scenarios. It allows applications to handle events for all [**ShellFolderView**](shellfolderview.md) objects with a single pair of **ShellFolderViewOC** event handlers. Each time the user navigates to a new folder, the application passes the associated **ShellFolderView** object to the **ShellFolderViewOC** object by calling [**SetFolderView**](shellfolderviewoc-setfolderview.md). Then, when an [**EnumDone**](shellfolderviewoc-enumdone.md) or [**SelectionChanged**](shellfolderviewoc-selectionchanged.md) event is fired, the **ShellFolderViewOC** object forwards the event to its own handler for processing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**ShellFolderView**](shellfolderview.md)
</dt> </dl>

 

 




