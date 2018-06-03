---
title: System.Gadget.settingsUI property
description: Gets or sets the HTML filename for the gadget Settings dialog UI.
ms.assetid: fd8c1b46-7c59-441a-b2f3-78babe26ed15
keywords:
- settingsUI property Windows Sidebar
- settingsUI property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , settingsUI property
topic_type:
- apiref
api_name:
- System.Gadget.settingsUI
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

# System.Gadget.settingsUI property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the HTML filename for the gadget **Settings** dialog UI.

This property is read/write.

## Syntax


```JScript
strsettingsUI = System.Gadget.settingsUI
System.Gadget.settingsUI = strsettingsUI
```



## Property value

A **String** that specifies or receives the HTML filename.

## Remarks

The gadget Settings button is activated when the **settingsUI** property is assigned a value.

## Examples

The following example demonstrates how to use the **settingsUI** property to enable the gadget Settings dialog box.


```JScript
// Enable the gadget settings functionality. 
System.Gadget.settingsUI = "Example.html";
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

[**System.Gadget**](system-gadget.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**System.Gadget.Settings**](system-gadget-settings.md)
</dt> <dt>

[**read**](system-gadget-settings-read.md)
</dt> <dt>

[**write**](system-gadget-settings-write.md)
</dt> <dt>

[**onSettingsClosed**](system-gadget-onsettingsclosed.md)
</dt> <dt>

[**onSettingsClosing**](system-gadget-onsettingsclosing.md)
</dt> <dt>

[**onShowSettings**](system-gadget-onshowsettings.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Developing a Gadget for Windows Sidebar Part 1: The Basics](-sidebar-overview-gdo.md)
</dt> </dl>

 

 





