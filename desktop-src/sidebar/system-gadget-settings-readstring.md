---
title: System.Gadget.Settings.readString method
description: Retrieves a stored String value associated with a gadget Settings key.
ms.assetid: 89d2e8b9-06d1-41ab-aa07-c44022ca9649
keywords:
- readString method Windows Sidebar
- readString method Windows Sidebar , System.Gadget.Settings object
- System.Gadget.Settings object Windows Sidebar , readString method
topic_type:
- apiref
api_name:
- System.Gadget.Settings.readString
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

# System.Gadget.Settings.readString method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves a stored **String** value associated with a gadget **Settings** key.

## Syntax


```JScript
strRetVal = System.Gadget.Settings.readString(
  strName
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

**String** that specifies or receives the name of the Settings key.

</dd> </dl>

## Return value

The **String** value of the Settings key.

## Remarks

Use **readString** for performance and efficiency reasons if the data type is a **String**.

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
            System.Gadget.Settings.readString("settingsUserEntry");
        // Update gadget UI based on user Settings input.
        SetContentText(userEntry);
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
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Gadget.Settings**](system-gadget-settings.md)
</dt> <dt>

[**writeString**](system-gadget-settings-writestring.md)
</dt> </dl>

 

 





