---
title: System.Gadget.Settings.ClosingEvent object
description: The event argument that defines the properties for the closing functionality of the gadget Settings dialog.
ms.assetid: '59369e4f-d6b7-4a26-bfe4-0841460dc2dc'
keywords: ["System.Gadget.Settings.ClosingEvent object Windows Sidebar", "System.Gadget.Settings.ClosingEvent object Windows Sidebar , described"]
topic_type:
- apiref
api_name:
- System.Gadget.Settings.ClosingEvent
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.Settings.ClosingEvent object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

The event argument that defines the properties for the closing functionality of the gadget **Settings** dialog.

## Members

The **System.Gadget.Settings.ClosingEvent** object has these types of members:

-   [Properties](#properties)

### Properties

The **System.Gadget.Settings.ClosingEvent** object has these properties.



| Property                                                                          | Access type           | Description                                                                                                        |
|:----------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**Action**](system-gadget-settings-closingevent-action.md)<br/>           | Read-only<br/>  | Contains a value from the enumeration of closing actions for the **Settings** dialog. <br/>                  |
| [**cancel**](system-gadget-settings-closingevent-cancel.md)<br/>           | Read/write<br/> | Gets or sets whether to cancel the [**onSettingsClosing**](system-gadget-onsettingsclosing.md) event. <br/> |
| [**cancellable**](system-gadget-settings-closingevent-cancellable.md)<br/> | Read-only<br/>  | Gets whether the [**onSettingsClosing**](system-gadget-onsettingsclosing.md) event can be canceled. <br/>   |
| [**closeAction**](system-gadget-settings-closingevent-closeaction.md)<br/> | Read-only<br/>  | Gets the **Settings** dialog close request. <br/>                                                            |



 

## Remarks

The functions declared as handlers for the **Settings** events, [**onSettingsClosed**](system-gadget-onsettingsclosed.md) and [**onSettingsClosing**](system-gadget-onsettingsclosing.md), take an event argument of type **System.Gadget.Settings.ClosingEvent**.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 8<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2012<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





