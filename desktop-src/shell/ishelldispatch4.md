---
Description: Extends the IShellDispatch3 object.
title: IShellDispatch4 object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch4
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch4 object

Extends the [**IShellDispatch3**](ishelldispatch3.md) object. In addition to the properties and methods supported by **IShellDispatch3**, **IShellDispatch4** supports four additional methods.

> [!Note]  
> **IShellDispatch4** is implemented and accessed through the [**Shell**](shell.md) object.

 

## Members

The **IShellDispatch4** object has these types of members:

-   [Methods](#methods)

### Methods

The **IShellDispatch4** object has these methods.



| Method                                                     | Description                                                         |
|:-----------------------------------------------------------|:--------------------------------------------------------------------|
| [**ExplorerPolicy**](ishelldispatch4-explorerpolicy.md)   | Gets the value for a specified Internet Explorer policy.<br/> |
| [**GetSetting**](ishelldispatch4-getsetting.md)           | Retrieves a global Shell setting.<br/>                        |
| [**ToggleDesktop**](ishelldispatch4-toggledesktop.md)     | Displays or hides the desktop.<br/>                           |
| [**WindowsSecurity**](ishelldispatch4-windowssecurity.md) | Displays the **Windows Security** dialog box.<br/>            |



 

## Remarks

For a discussion of Windows services, see the [Services](https://msdn.microsoft.com/en-us/library/ms685141(v=VS.85).aspx) documentation.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx)
</dt> <dt>

[**Shell Object**](shell.md)
</dt> <dt>

[**IShellDispatch**](ishelldispatch.md)
</dt> <dt>

[**IShellDispatch2**](ishelldispatch2-object.md)
</dt> <dt>

[**IShellDispatch3**](ishelldispatch3.md)
</dt> </dl>

 

 




