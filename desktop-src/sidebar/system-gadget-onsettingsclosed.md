---
title: System.Gadget.onSettingsClosed event
description: Event fired when the gadget Settings dialog is closed.
ms.assetid: 44963ae7-9621-41fb-834a-987aef7cbba1
keywords:
- onSettingsClosed event Windows Sidebar
- onSettingsClosed event Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , onSettingsClosed event
topic_type:
- apiref
api_name:
- System.Gadget.onSettingsClosed
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

# System.Gadget.onSettingsClosed event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget **Settings** dialog is closed.

## Syntax


```JScript
iRetVal = System.Gadget.onSettingsClosed(
  handler
)
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

The name of the function to call when the event is fired.

> [!Note]  
> The function takes a parameter of type [**System.Gadget.Settings.ClosingEvent**](system-gadget-settings-closingevent.md).

 

</dd> </dl>

## Remarks

Invoking the **OK** or **Cancel** button of the Settings dialog will close the dialog and fire this event.

## Examples

The following example demonstrates how to use the **onSettingsClosed** event to read values from controls in the Settings dialog.


```JScript
var userEntry = "";

System.Gadget.onSettingsClosed = SettingsClosed;

// --------------------------------------------------------------------
// Handle the Settings dialog closed event.
// event = System.Gadget.Settings.ClosingEvent argument.
// --------------------------------------------------------------------
function SettingsClosed(event)
{
    // User hit OK on the settings page.
    if (event.closeAction == event.Action.commit)
    {
        userEntry = 
            System.Gadget.Settings.readString("settingsUserEntry");
        SetContentText(userEntry);
    }
    // User hit Cancel on the settings page.
    else if (event.closeAction == event.Action.cancel)
    {
        SetContentText("Canceled");
    }
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

 

 





