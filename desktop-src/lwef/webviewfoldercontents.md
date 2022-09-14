---
title: WebViewFolderContents object (Shldisp.h)
description: Implemented by the Shell for use inside a WebView.
ms.assetid: c9c46e21-2721-43c9-a6f4-38fafbda3798
keywords:
- WebViewFolderContents object Legacy Windows Environment Features
- WebViewFolderContents object Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- WebViewFolderContents
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WebViewFolderContents object

Implemented by the Shell for use inside a *WebView*. **WebViewFolderContents** automatically initializes itself to WebView's current folder. It creates a Shell folder view that displays the contents of the folder in one of five formats: Small Icon, Large Icon, List, Details, or Thumbnail. It is not valid outside of a WebView.

The methods and properties exposed by **WebViewFolderContents** are identical to those of the [**ShellFolderView**](/windows/desktop/shell/shellfolderview) object.

## Members

The **WebViewFolderContents** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **WebViewFolderContents** object has these events.



| Event                                                              | Description                                                                              |
|:-------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**SelectionChanged**](webviewfoldercontents-selectionchanged.md) | Occurs when the selection state of any item or items in the view has changed.<br/> |



 

### Methods

The **WebViewFolderContents** object has these methods.



| Method                                                       | Description                                                                                                          |
|:-------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**PopupItemMenu**](webviewfoldercontents-popupitemmenu.md) | Creates a shortcut menu for the specified item and returns the selected command string.<br/>                   |
| [**SelectedItems**](webviewfoldercontents-selecteditems.md) | Gets a [**FolderItems**](../shell/folderitems.md) object that represents all of the selected items in the view.<br/> |
| [**SelectItem**](webviewfoldercontents-selectitem.md)       | Sets the selection state of an item in the view.<br/>                                                          |



 

### Properties

The **WebViewFolderContents** object has these properties.



| Property                                                            | Access type          | Description                                                                                                                              |
|:--------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| [**Application**](webviewfoldercontents-application.md)<br/> | Read-only<br/> | Not implemented.<br/>                                                                                                              |
| [**FocusedItem**](webviewfoldercontents-focuseditem.md)<br/> | Read-only<br/> | Gets a [**FolderItem**](../shell/folderitem.md) object that represents the item that has the input focus.<br/>                           |
| [**Folder**](webviewfoldercontents-folder.md)<br/>           | Read-only<br/> | Gets a [**Folder**](../shell/folder.md) object that represents the view.<br/>                                                            |
| [**Parent**](webviewfoldercontents-parent.md)<br/>           | Read-only<br/> | Not implemented.<br/>                                                                                                              |
| [**Script**](webviewfoldercontents-script.md)<br/>           | Read-only<br/> | Gets the scripting object for the view.<br/>                                                                                       |
| [**ViewOptions**](webviewfoldercontents-viewoptions.md)<br/> | Read-only<br/> | Gets a set of [**ShellFolderViewOptions**](/windows/desktop/api/shldisp/ne-shldisp-shellfolderviewoptions) flags that indicate the current options of the view.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

