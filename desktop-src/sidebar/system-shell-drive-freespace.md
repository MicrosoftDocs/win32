---
title: System.Shell.Drive.freeSpace property
description: Gets the amount of free space, in megabytes (MB), on the system storage device.
ms.assetid: cd4c6452-92b5-476f-bb73-15ebc4dadfa5
keywords:
- freeSpace property Windows Sidebar
- freeSpace property Windows Sidebar , System.Shell.Drive object
- System.Shell.Drive object Windows Sidebar , freeSpace property
topic_type:
- apiref
api_name:
- System.Shell.Drive.freeSpace
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

# System.Shell.Drive.freeSpace property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the amount of free space, in megabytes (MB), on the system storage device.

This property is read-only.

## Syntax


```JScript
strfreeSpace = System.Shell.Drive.freeSpace
```



## Property value

A **String** that receives the amount of free space.

## Remarks

The value returned by **freeSpace** is typically the same as [**totalFreeSpace**](system-shell-drive-totalfreespace.md). Any difference between the properties occurs on computer systems that support enforced disk storage quotas and can be due to user-privilege configurations assigned to the currently-logged-on user.

## Examples

The following example demonstrates how to get the free space of a storage device.


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

 

 





