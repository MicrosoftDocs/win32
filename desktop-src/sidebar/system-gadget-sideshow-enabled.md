---
title: System.Gadget.SideShow.enabled method
description: Retrieves whether SideShow is supported.
ms.assetid: bd0cf4da-7175-4a6e-9f08-b9c456a939b9
keywords:
- enabled method Windows Sidebar
- enabled method Windows Sidebar , System.Gadget.SideShow object
- System.Gadget.SideShow object Windows Sidebar , enabled method
topic_type:
- apiref
api_name:
- System.Gadget.SideShow.enabled
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

# System.Gadget.SideShow.enabled method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves whether SideShow is supported.

## Syntax


```JScript
bRetVal = System.Gadget.SideShow.enabled()
```



## Parameters

This method has no parameters.

## Return value

**Boolean** that specifies the SideShow support.



| Return value                                                                     | Description                            |
|----------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>true</dt> </dl>  | SideShow is supported. <br/>     |
| <dl> <dt>false</dt> </dl> | SideShow is not supported. <br/> |



 

## Remarks

Verify that **System.Gadget.SideShow.enabled** returns `true` before using other [**System.Gadget.SideShow**](system-gadget-sideshow.md) object members.

## Examples

The following example demonstrates how to determine whether SideShow is supported using **enabled**.


```JScript
var sideshowEnabled = System.Gadget.SideShow.enabled();

if (sideshowEnabled) 
{
    // Do something.
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

[**System.Gadget.SideShow**](system-gadget-sideshow.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Windows SideShow: MSDN](http://msdn.microsoft.com/library/ms744202.aspx)
</dt> <dt>

[Windows SideShow: Windows Hardware Developer Central](http://www.microsoft.com/whdc/device/sideshow/default.mspx)
</dt> </dl>

 

 





