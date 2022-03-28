---
description: Extends the IShellDispatch object with a variety of new functionality.
ms.assetid: 74687929-0777-479b-9853-2b0cf4b6adc9
title: IShellDispatch2 object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch2
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch2 object

Extends the [**IShellDispatch**](ishelldispatch.md) object with a variety of new functionality.

> [!Note]  
> **IShellDispatch2** is implemented and accessed through the [**Shell**](shell.md) object.

 

## Members

The **IShellDispatch2** object has these types of members:

- [Methods](#methods)

### Methods

The **IShellDispatch2** object has these methods.



| Method                                                               | Description                                                                        |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**CanStartStopService**](ishelldispatch2-canstartstopservice.md)   | Determines if the current user can start and stop the named service.<br/>    |
| [**FindPrinter**](ishelldispatch2-findprinter.md)                   | Displays the **Find Printer** dialog box.<br/>                               |
| [**GetSystemInformation**](ishelldispatch2-getsysteminformation.md) | Retrieves system information.<br/>                                           |
| [**IsRestricted**](ishelldispatch2-isrestricted.md)                 | Retrieves a group's restriction setting from the registry.<br/>              |
| [**IsServiceRunning**](ishelldispatch2-isservicerunning.md)         | Returns a value that indicates whether a particular service is running.<br/> |
| [**ServiceStart**](ishelldispatch2-servicestart.md)                 | Starts a named service.<br/>                                                 |
| [**ServiceStop**](ishelldispatch2-servicestop.md)                   | Stops a named service.<br/>                                                  |
| [**ShellExecute**](ishelldispatch2-shellexecute.md)                 | Performs a specified operation on a specified file.<br/>                     |
| [**ShowBrowserBar**](ishelldispatch2-showbrowserbar.md)             | Displays a browser bar.<br/>                                                 |



 

## Remarks

For a discussion of Windows services, see the [Services](../services/services.md) documentation.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> <dt>

[**Shell Object**](shell.md)
</dt> <dt>

[**IShellDispatch**](ishelldispatch.md)
</dt> </dl>

 

 
