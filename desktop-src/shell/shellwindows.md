---
Description: Represents a collection of the open windows that belong to the Shell. Methods associated with this objects can control and execute commands within the Shell, and obtain other Shell-related objects.
ms.assetid: e609c8b6-2b2e-4188-894c-5c85960206ea
title: ShellWindows object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ShellWindows object

Represents a collection of the open windows that belong to the Shell. Methods associated with this objects can control and execute commands within the Shell, and obtain other Shell-related objects.

## Members

The **ShellWindows** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ShellWindows** object has these methods.



| Method                                                 | Description                                                                                                         |
|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](shellwindows--newenum-method-7ral.md) | Creates and returns a new **ShellWindows** object that is a copy of this **ShellWindows** object.<br/>        |
| [**Item**](shellwindows-item.md)                      | Retrieves an [**InternetExplorer**](https://msdn.microsoft.com/windows/desktop/4f59dc39-4fa5-46ac-a572-0d0b36876f54) object that represents the Shell window.<br/> |



 

### Properties

The **ShellWindows** object has these properties.



| Property                                       | Access type          | Description                                                |
|:-----------------------------------------------|:---------------------|:-----------------------------------------------------------|
| [**Count**](shellwindows-count.md)<br/> | Read-only<br/> | Contains the number of items in the collection.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




