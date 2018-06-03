---
title: System.Gadget.Settings.ClosingEvent.cancellable property
description: Gets whether the onSettingsClosing event can be canceled.
ms.assetid: 48341a31-2435-4464-b2ac-5f42aba24051
keywords:
- cancellable property Windows Sidebar
- cancellable property Windows Sidebar , System.Gadget.Settings.ClosingEvent object
- System.Gadget.Settings.ClosingEvent object Windows Sidebar , cancellable property
topic_type:
- apiref
api_name:
- System.Gadget.Settings.ClosingEvent.cancellable
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

# System.Gadget.Settings.ClosingEvent.cancellable property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets whether the [**onSettingsClosing**](system-gadget-onsettingsclosing.md) event can be canceled.

This property is read-only.

## Syntax


```JScript
bcancellable = System.Gadget.Settings.ClosingEvent.cancellable
```



## Property value

A **Boolean** that receives whether the dialog box can be canceled.

<dt>



 (TRUE)


</dt> <dd>

The **Settings** dialog can be canceled.

</dd> <dt>



 (FALSE)


</dt> <dd>

The Settings dialog cannot be canceled.

</dd> </dl>

## Remarks

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
        // No user entry and 'Ok' invoked, cancel the Settings closing event.
        else
        {
            if (event.cancellable == false)
            {
                event.cancel = true;  
            }
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



 

 





