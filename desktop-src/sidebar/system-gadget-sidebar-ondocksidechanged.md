---
title: System.Gadget.Sidebar.onDockSideChanged event
description: Event fired when the Windows Sidebar dock state changes.
ms.assetid: 26ba45af-3dd3-4ba7-90cf-066b76d379cc
keywords:
- onDockSideChanged event Windows Sidebar
- onDockSideChanged event Windows Sidebar , System.Gadget.Sidebar object
- System.Gadget.Sidebar object Windows Sidebar , onDockSideChanged event
topic_type:
- apiref
api_name:
- System.Gadget.Sidebar.onDockSideChanged
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Gadget.Sidebar.onDockSideChanged event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the Windows Sidebar dock state changes.

## Syntax


```JScript
iRetVal = System.Gadget.Sidebar.onDockSideChanged(
  handler
)
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

The name of the function to call when the event is fired.

</dd> </dl>

## Remarks

The Sidebar can be docked on the left or the right side of the screen.

This event updates the [**dockSide**](system-gadget-sidebar-dockside.md) property.

Useful when changes to graphics alignment based on the Sidebar [**dockSide**](system-gadget-sidebar-dockside.md) property are necessary.

## Examples

The following example demonstrates how to listen for the **onDockSideChanged** event.


```JScript
// Enable the gadget Sidebar functionality. 
System.Gadget.Sidebar.onDockSideChanged = DockSideChanged;

// --------------------------------------------------------------------
// Handle the Sidebar dockside changed event.
// --------------------------------------------------------------------
function DockSideChanged()
{
    SetContentText(System.Gadget.Sidebar.dockSide);
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Gadget.Sidebar**](system-gadget-sidebar.md)
</dt> <dt>

[**dockSide**](system-gadget-sidebar-dockside.md)
</dt> </dl>

 

 





