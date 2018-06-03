---
title: System.Gadget.platformVersion property
description: Gets the Windows Sidebar version.
ms.assetid: fd391b6f-7bb6-4502-9b3c-a94a2bb56627
keywords:
- platformVersion property Windows Sidebar
- platformVersion property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , platformVersion property
topic_type:
- apiref
api_name:
- System.Gadget.platformVersion
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

# System.Gadget.platformVersion property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Windows Sidebar version.

This property is read-only.

## Syntax


```JScript
strplatformVersion = System.Gadget.platformVersion
```



## Property value

A **String** that receives the Sidebar version.

## Remarks

Useful for determining if a particular feature or functionality is available.

## Examples

The following example demonstrates how to get the platform version.


```JScript
var mytext = "platform version: " + System.Gadget.platformVersion;
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
</dt> </dl>

 

 





