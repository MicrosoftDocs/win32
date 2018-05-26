---
title: System.Shell.Drive.driveLetter property
description: Gets the system storage device drive letter.
ms.assetid: 106fcb8b-acee-43f5-be12-75c035201a44
keywords:
- driveLetter property Windows Sidebar
- driveLetter property Windows Sidebar , System.Shell.Drive object
- System.Shell.Drive object Windows Sidebar , driveLetter property
topic_type:
- apiref
api_name:
- System.Shell.Drive.driveLetter
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

# System.Shell.Drive.driveLetter property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the system storage device drive letter.

This property is read-only.

## Syntax


```JScript
strdriveLetter = System.Shell.Drive.driveLetter
```



## Property value

A **String** that receives the drive letter.

## Examples

The following example demonstrates how to get the storage device drive letter.


```JScript
// --------------------------------------------------------------------
// Display drive information.
// driveLetter: user input.
// --------------------------------------------------------------------
function GetDriveInfo(driveLetter)
{
    var sDrive = "";
    var drive = System.Shell.drive(driveLetter);

    if (drive)
    {
        if (drive.isReady)
        {
            sDrive = "Label:" + drive.volumeLabel + " for drive(" + drive.driveLetter + ")<br/>";
            sDrive += "FreeSpace: " + drive.freeSpace + "MB<br/>";
            sDrive += "TotalFreeSpace: " + drive.totalFreeSpace + "MB<br/>";
            sDrive += "TotalSpace: " + drive.totalSize + "MB<br/>";
            sDrive += "DriveType: " + drive.driveType + "<br/>";
            sDrive += "DriveFormat: " + drive.driveFormat + "<br/>";
            sDrive += "RootDir: [" + drive.rootDirectory + "]<br/>";
        }
        else
        {
            sDrive = "Drive (" + driveLetter + ") is not ready.<br/>";
        }
    }
    else
    {
        sDrive = "Drive (" + driveLetter + ") is not valid.<br/>";
    }
    spFeedback.innerHTML = sDrive;
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

[**System.Shell.Drive**](system-shell-drive.md)
</dt> <dt>

[**System.Shell**](system-shell.md)
</dt> </dl>

 

 





