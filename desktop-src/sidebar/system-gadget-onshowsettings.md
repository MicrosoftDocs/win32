---
title: System.Gadget.onShowSettings event
description: Event fired when the gadget Settings dialog is requested.
ms.assetid: c844ed9c-3a05-4053-9851-4434983c0b37
keywords:
- onShowSettings event Windows Sidebar
- onShowSettings event Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , onShowSettings event
topic_type:
- apiref
api_name:
- System.Gadget.onShowSettings
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

# System.Gadget.onShowSettings event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget **Settings** dialog is requested.

## Syntax


```JScript
iRetVal = System.Gadget.onShowSettings(
  handler
)
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

The name of the function to call when the event is fired.

</dd> </dl>

## Examples

The following example demonstrates how to use the **onShowSettings** event.


```JScript
// Delegate for the show settings event. 
System.Gadget.onShowSettings = SettingsShow;

// --------------------------------------------------------------------
// Handle the Settings dialog show event.
// --------------------------------------------------------------------
function SettingsShow()
{
    SetContentText("Settings opening.");
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

[**System.Gadget**](system-gadget.md)
</dt> </dl>

 

 





