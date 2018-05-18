---
title: System.Gadget.onSettingsClosing event
description: Event fired when the gadget Settings dialog begins the process of closing.
ms.assetid: '748c3f52-7d51-43d5-add0-0873bc372459'
keywords: ["onSettingsClosing event Windows Sidebar", "onSettingsClosing event Windows Sidebar , System.Gadget object", "System.Gadget object Windows Sidebar , onSettingsClosing event"]
topic_type:
- apiref
api_name:
- System.Gadget.onSettingsClosing
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.onSettingsClosing event

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget **Settings** dialog begins the process of closing.

## Syntax


```JScript
iRetVal = System.Gadget.onSettingsClosing(
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

Invoking the **OK** or **Cancel** button of the Settings dialog will begin the process of closing the dialog and fire this event.

This event is asynchronous.

## Examples

The following example demonstrates how to save gadget settings when the **onSettingsClosing** event is fired.


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
    // Save the settings if the user clicked OK.
    if (event.closeAction == event.Action.commit)
    {
        System.Gadget.Settings.writeString(
            "settingsUserEntry", txtUserEntry.value);
    }
    // Allow the Settings dialog to close.
    event.cancel = false;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Gadget**](system-gadget.md)
</dt> </dl>

 

 





