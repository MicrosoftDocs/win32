---
title: System.Gadget.Settings.ClosingEvent.Action property
description: Contains a value from the enumeration of closing actions for the Settings dialog.
ms.assetid: a88f3ca3-6f81-48bd-9422-cf2d8af8c690
keywords:
- Action property Windows Sidebar
- Action property Windows Sidebar , System.Gadget.Settings.ClosingEvent object
- System.Gadget.Settings.ClosingEvent object Windows Sidebar , Action property
topic_type:
- apiref
api_name:
- System.Gadget.Settings.ClosingEvent.Action
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

# System.Gadget.Settings.ClosingEvent.Action property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Contains a value from the enumeration of closing actions for the **Settings** dialog.

This property is read-only.

## Syntax


```JScript
objAction = System.Gadget.Settings.ClosingEvent.Action
```



## Property value

An **Object** that receives the closing action.

<dt>



 (commit)


</dt> <dd>

**Ok** button invoked.

</dd> <dt>



 (cancel)


</dt> <dd>

**Cancel** button invoked.

</dd> </dl>

## Remarks

Used in the **Settings** dialog box callbacks ([**onSettingsClosing**](system-gadget-onsettingsclosing.md) and [**onSettingsClosed**](system-gadget-onsettingsclosed.md)).

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



## See also

<dl> <dt>

[**System.Gadget.Settings.ClosingEvent**](system-gadget-settings-closingevent.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**onSettingsClosing**](system-gadget-onsettingsclosing.md)
</dt> <dt>

[**onSettingsClosed**](system-gadget-onsettingsclosed.md)
</dt> <dt>

[**cancel**](system-gadget-settings-closingevent-cancel.md)
</dt> <dt>

[**cancellable**](system-gadget-settings-closingevent-cancellable.md)
</dt> <dt>

[**closeAction**](system-gadget-settings-closingevent-closeaction.md)
</dt> </dl>

 

 





