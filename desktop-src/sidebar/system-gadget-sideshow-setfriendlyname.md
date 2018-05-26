---
title: System.Gadget.SideShow.setFriendlyName method
description: The display name for the SideShow gadget.
ms.assetid: b8f0e2ef-df78-4b77-bf15-b433007f19ec
keywords:
- setFriendlyName method Windows Sidebar
- setFriendlyName method Windows Sidebar , System.Gadget.SideShow object
- System.Gadget.SideShow object Windows Sidebar , setFriendlyName method
topic_type:
- apiref
api_name:
- System.Gadget.SideShow.setFriendlyName
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

# System.Gadget.SideShow.setFriendlyName method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

The display name for the SideShow gadget.

## Syntax


```JScript
iRetVal = System.Gadget.SideShow.setFriendlyName(
  strFriendlyName
)
```



## Parameters

<dl> <dt>

*strFriendlyName* \[in\]
</dt> <dd>

**String** that specifies the display name.

</dd> </dl>

## Remarks

Verify that [**System.Gadget.SideShow.enabled**](system-gadget-sideshow-enabled.md) returns `true` before using other [**System.Gadget.SideShow**](system-gadget-sideshow.md) object members.

## Examples

This image shows a SideShow emulator with a gadget and a friendly display name.

![sideshow gadget friendly name image](images/reference/sideshowfriendlyname.png)

The following example demonstrates how to set the display name for the SideShow gadget.


```JScript
System.Gadget.SideShow.setFriendlyName("Stocks");
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

[**System.Gadget.SideShow**](system-gadget-sideshow.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Windows SideShow: MSDN](http://msdn.microsoft.com/library/ms744202.aspx)
</dt> <dt>

[Windows SideShow: Windows Hardware Developer Central](http://www.microsoft.com/whdc/device/sideshow/default.mspx)
</dt> </dl>

 

 





