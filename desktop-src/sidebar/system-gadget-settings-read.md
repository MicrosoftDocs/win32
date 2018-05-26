---
title: System.Gadget.Settings.read method
description: Retrieves a stored value of unspecified type associated with a gadget Settings key.
ms.assetid: 39120787-6ae1-42de-ac65-1eedc8efcf9d
keywords:
- read method Windows Sidebar
- read method Windows Sidebar , System.Gadget.Settings object
- System.Gadget.Settings object Windows Sidebar , read method
topic_type:
- apiref
api_name:
- System.Gadget.Settings.read
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

# System.Gadget.Settings.read method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves a stored value of unspecified type associated with a gadget **Settings** key.

## Syntax


```JScript
retVal = System.Gadget.Settings.read(
  strName
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

**String** that specifies the name of the Settings key.

</dd> </dl>

## Return value

The value of the Settings key. The data type of the returned value will default to **String** if it cannot be coerced into one of the following: **Boolean**, **Floating-point**, **Floating-point**, or **Integer**.

## Remarks

Use [**readString**](system-gadget-settings-readstring.md) for performance and efficiency reasons if the data type is a **String**.

There is a 1024 character limit for Settings keys and a 2048 character limit for Settings values; values longer than these limits will be truncated.

Use [**write**](system-gadget-settings-write.md) or [**writeString**](system-gadget-settings-writestring.md) to store Settings values.

The Settings values are unique for each user account, even if the same gadget is used.

## Examples

The following example demonstrates how to retrieve a Settings value into a gadget variable.


```JScript
// --------------------------------------------------------------------
// Handle the Settings dialog closed event.
// event = Event argument.
// --------------------------------------------------------------------
function SettingsClosed(event)
{
    // User hit OK on the settings page.
    if (event.closeAction == event.Action.commit)
    {
        userEntry = 
            System.Gadget.Settings.read("settingsSelectionIndex");
        // Update gadget UI based on user Settings selection.
        UpdateSelection(selectionIndex);
    }
    // User hit Cancel on the settings page.
    else if (event.closeAction == event.Action.cancel)
    {
        SetContentText("canceled");
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
| Header<br/>                   | <dl> <dt>Corecrt\_io.h</dt> </dl>                       |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Gadget.Settings**](system-gadget-settings.md)
</dt> <dt>

[**readString**](system-gadget-settings-readstring.md)
</dt> </dl>

 

 





