---
title: System.Gadget.Sidebar object
description: Defines the properties and events that provide basic Windows Sidebar functionality.
ms.assetid: 74d7ae80-73b8-4088-a496-1c49bec20316
keywords:
- System.Gadget.Sidebar object Windows Sidebar
- System.Gadget.Sidebar object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Gadget.Sidebar
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Gadget.Sidebar object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and events that provide basic Windows Sidebar functionality.

## Members

The **System.Gadget.Sidebar** object has these types of members:

-   [Events](#events)
-   [Properties](#properties)

### Events

The **System.Gadget.Sidebar** object has these events.



| Event                                                                | Description                                                  |
|:---------------------------------------------------------------------|:-------------------------------------------------------------|
| [**onDockSideChanged**](system-gadget-sidebar-ondocksidechanged.md) | Event fired when the Sidebar dock state changes. <br/> |



 

### Properties

The **System.Gadget.Sidebar** object has these properties.



| Property                                                      | Access type          | Description                              |
|:--------------------------------------------------------------|:---------------------|:-----------------------------------------|
| [**dockSide**](system-gadget-sidebar-dockside.md)<br/> | Read-only<br/> | Gets the Sidebar dock state. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





