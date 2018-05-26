---
title: System.Gadget.Settings.ClosingEvent.cancel property
description: Gets or sets whether to cancel the onSettingsClosing event.
ms.assetid: b5a74c26-72e7-45d3-a660-fc01e4d62156
keywords:
- cancel property Windows Sidebar
- cancel property Windows Sidebar , System.Gadget.Settings.ClosingEvent object
- System.Gadget.Settings.ClosingEvent object Windows Sidebar , cancel property
topic_type:
- apiref
api_name:
- System.Gadget.Settings.ClosingEvent.cancel
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

# System.Gadget.Settings.ClosingEvent.cancel property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets whether to cancel the [**onSettingsClosing**](system-gadget-onsettingsclosing.md) event.

This property is read/write.

## Syntax


```JScript
bcancel = System.Gadget.Settings.ClosingEvent.cancel
System.Gadget.Settings.ClosingEvent.cancel = bcancel
```



## Property value

A **Boolean** that specifies or receives whether to cancel the event.

<dt>



 (false)


</dt> <dd>

Default. Event is not canceled.

</dd> <dt>



 (true)


</dt> <dd>

Default. Event is canceled.

</dd> </dl>

## Remarks

Useful for situations where a Settings form requires particular fields to be modified before the user can click **Ok**. This ensures the Settings dialog can stay open until all required information is entered.

## Examples

The following example demonstrates how to ensure the Settings dialog closes when desired.


```JScript
// Delegate for the settings closing event. 
System.Gadget.onSettingsClosing = SettingsClosing;
        
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
        if (txtUserEntry.value != "")
        {        
            System.Gadget.Settings.writeString(
                "settingsUserEntry", txtUserEntry.value);
            // Allow the Settings dialog to close.
            event.cancel = false;
        }
        // No user entry, cancel the Settings closing event.
        else
        {
            event.cancel = true;  
        }
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



 

 





