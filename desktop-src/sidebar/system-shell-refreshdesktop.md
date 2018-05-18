---
title: System.Shell.refreshDesktop method
description: Refreshes the desktop after adding or removing files.
ms.assetid: 'aa8802e1-953f-46d6-9c4c-5e9da12c0925'
keywords: ["refreshDesktop method Windows Sidebar", "refreshDesktop method Windows Sidebar , System.Shell object", "System.Shell object Windows Sidebar , refreshDesktop method"]
topic_type:
- apiref
api_name:
- System.Shell.refreshDesktop
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.refreshDesktop method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Refreshes the desktop after adding or removing files.

## Syntax


```JScript
System.Shell.refreshDesktop()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

**refreshDesktop** works across the desktop areas of all monitors connected to the system; not only the monitor displaying the Windows Sidebar.

## Examples

The following example demonstrates how to refresh the desktop.


```JScript
System.Shell.refreshDesktop();
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



 

 





