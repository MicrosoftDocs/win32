---
title: System.Gadget.Settings.writeString method
description: Stores a String value with an associated Settings key.
ms.assetid: 'fcd50d9b-ec5a-4143-8d78-69bb7bb79dfd'
keywords: ["writeString method Windows Sidebar", "writeString method Windows Sidebar , System.Gadget.Settings object", "System.Gadget.Settings object Windows Sidebar , writeString method"]
topic_type:
- apiref
api_name:
- System.Gadget.Settings.writeString
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.Settings.writeString method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Stores a **String** value with an associated **Settings** key.

## Syntax


```JScript
System.Gadget.Settings.writeString(
  strName,
  strValue
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

**String** that specifies the name of the Settings key.

</dd> <dt>

*strValue* \[in\]
</dt> <dd>

> [!Note]  
> The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.

 

The **String** value to store.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Use **writeString** for performance and efficiency reasons if the data type is a **String**.

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

[**System.Gadget.Settings**](system-gadget-settings.md)
</dt> <dt>

[**readString**](system-gadget-settings-readstring.md)
</dt> </dl>

 

 





