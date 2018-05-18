---
title: System.Shell.drive method
description: Retrieves a System.Shell.Drive object that represents the specified drive.
ms.assetid: '04f60c48-98a6-42ee-9ad8-8fcfe06f7b5b'
keywords: ["drive method Windows Sidebar", "drive method Windows Sidebar , System.Shell object", "System.Shell object Windows Sidebar , drive method"]
topic_type:
- apiref
api_name:
- System.Shell.drive
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.drive method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves a [**System.Shell.Drive**](system-shell-drive.md) object that represents the specified drive.

## Syntax


```JScript
retVal = System.Shell.drive(
  strDrive
)
```



## Parameters

<dl> <dt>

*strDrive* \[in\]
</dt> <dd>

**String** that represents the drive letter of the system storage device.

> [!Note]  
> A valid drive specification is constrained to one of the following formats: **C**, **C:**, or **C:\\**.

 

</dd> </dl>

## Return value

[**System.Shell.Drive**](system-shell-drive.md) that represents the specified drive, or null if the specified drive is not valid.

## Examples

The following example demonstrates how to assiciate a [**System.Shell.Drive**](system-shell-drive.md) object with the **C:** drive.


```JScript
// Create a System.Shell.Drive object.
function GetADrive()
{
    var oDrive = System.Shell.drive("C:");
}
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



## See also

<dl> <dt>

[**System.Shell**](system-shell.md)
</dt> <dt>

[**System.Shell.Drive**](system-shell-drive.md)
</dt> </dl>

 

 





