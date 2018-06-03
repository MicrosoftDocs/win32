---
title: System.Gadget.Settings.ClosingEvent.closeAction property
description: Gets the Settings dialog close request.
ms.assetid: 2e624513-0696-4754-8685-0eccc5403d1a
keywords:
- closeAction property Windows Sidebar
- closeAction property Windows Sidebar , System.Gadget.Settings.ClosingEvent object
- System.Gadget.Settings.ClosingEvent object Windows Sidebar , closeAction property
topic_type:
- apiref
api_name:
- System.Gadget.Settings.ClosingEvent.closeAction
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Gadget.Settings.ClosingEvent.closeAction property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the **Settings** dialog close request.

This property is read-only.

## Syntax


```JScript
closeAction = System.Gadget.Settings.ClosingEvent.closeAction
```



## Property value

[**Action**](system-gadget-settings-closingevent-action.md) that specifies the type of close request.

<dt>



 (commit)


</dt> <dd>

**OK** button is invoked. All modified settings are confirmed and stored.

</dd> <dt>



 (cancel)


</dt> <dd>

**Cancel** invoked. All modified settings are discarded.

</dd> </dl>

## Examples

The following example demonstrates how to store a Settings value when the Settings dialog closes.


```JScript
// --------------------------------------------------------------------
// Handle the Settings dialog closing event.
// Parameters:
// event - System.Gadget.Settings.ClosingEvent argument.
// --------------------------------------------------------------------
function SettingsClosing(event)
{
    // User hit OK on the settings page.
    if (event.closeAction == event.Action.commit)
    {
        System.Gadget.Settings.writeString(
        "settingsUserEntry", "OK");
    }
    // User hit Cancel on the settings page.
    else if (event.closeAction == event.Action.cancel)
    {
        System.Gadget.Settings.writeString(
                "settingsUserEntry", "CANCEL");
    }
    // Allow the Settings dialog to close.
    event.cancel = false;
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



 

 





