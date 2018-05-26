---
title: System.Gadget.Sidebar.dockSide property
description: Gets the Windows Sidebar dock state.
ms.assetid: 1dad3291-5a0e-45f0-ba3d-df3831f413b6
keywords:
- dockSide property Windows Sidebar
- dockSide property Windows Sidebar , System.Gadget.Sidebar object
- System.Gadget.Sidebar object Windows Sidebar , dockSide property
topic_type:
- apiref
api_name:
- System.Gadget.Sidebar.dockSide
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

# System.Gadget.Sidebar.dockSide property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Windows Sidebar dock state.

This property is read-only.

## Syntax


```JScript
strdockSide = System.Gadget.Sidebar.dockSide
```



## Property value

A **String** that receives the dock state of the Sidebar.

<dt>



 (Right)


</dt> <dd>

The Sidebar is docked on the right side of the monitor.

</dd> <dt>



 (Left)


</dt> <dd>

The Sidebar is docked on the left side of the monitor.

</dd> </dl>

## Examples

The following example demonstrates how to get the dock state of the Sidebar.


```JScript
// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{
    // Initialize the gadget content.
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

[**onDockSideChanged**](system-gadget-sidebar-ondocksidechanged.md)
</dt> </dl>

 

 





