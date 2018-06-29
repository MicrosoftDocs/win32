---
Description: Extends the IShellDispatch2 object.
ms.assetid: 89d0aa4d-844d-497d-82bb-bcc2bcf9c78b
title: IShellDispatch3 object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch3
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch3 object

Extends the [**IShellDispatch2**](ishelldispatch2-object.md) object. **IShellDispatch3** supports one new method in addition to the properties and methods supported by **IShellDispatch2**.

> [!Note]  
> **IShellDispatch3** is implemented and accessed through the [**Shell**](shell.md) object.

 

## Members

The **IShellDispatch3** object has these types of members:

-   [Methods](#methods)

### Methods

The **IShellDispatch3** object has these methods.



| Method                                             | Description                                                  |
|:---------------------------------------------------|:-------------------------------------------------------------|
| [**AddToRecent**](ishelldispatch3-addtorecent.md) | Adds a file to the most recently used (MRU) list.<br/> |



 

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
</dt> </dl>

 

 




