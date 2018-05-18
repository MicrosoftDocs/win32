---
title: System.Gadget.Settings.write method
description: Stores a value of unspecified type with an associated Settings key.
ms.assetid: 'cbfb5a31-1d18-4f52-8156-553e8df78f75'
keywords: ["write method Windows Sidebar", "write method Windows Sidebar , System.Gadget.Settings object", "System.Gadget.Settings object Windows Sidebar , write method"]
topic_type:
- apiref
api_name:
- System.Gadget.Settings.write
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.Settings.write method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Stores a value of unspecified type with an associated **Settings** key.

## Syntax


```JScript
System.Gadget.Settings.write(
  strName,
  varValue
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

**String** that specifies the name of the Settings key.

</dd> <dt>

*varValue* \[in\]
</dt> <dd>

The value to store.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Use [**writeString**](system-gadget-settings-writestring.md) for performance and efficiency reasons if the data type is a **String**.

There is a 1024 character limit for Settings keys and a 2048 character limit for Settings values; values longer than these limits will be truncated.

Use [**read**](system-gadget-settings-read.md) or [**readString**](system-gadget-settings-readstring.md) to read Settings values.

The Settings values are unique for each user account, even if the same gadget is used.

## Examples

The following example demonstrates how to store a Settings value.


```JScript
// --------------------------------------------------------------------
// Handle the Settings dialog closing event.
// Parameters:
// event - event arguments.
// --------------------------------------------------------------------
function SettingsClosing(event)
{
    // Save the settings if the user clicked OK.
    if (event.closeAction == event.Action.commit)
    {
        System.Gadget.Settings.write(
            "settingsSelectionIndex", selUserEntry.selectedIndex);
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
| Header<br/>                   | <dl> <dt>Corecrt\_io.h</dt> </dl>                       |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





