---
title: System.Shell.Drive.rootDirectory property
description: Gets the Universal Naming Convention (UNC) path to the root folder of a system storage device.
ms.assetid: df717506-83a1-4256-8b3e-41fdabf37024
keywords:
- rootDirectory property Windows Sidebar
- rootDirectory property Windows Sidebar , System.Shell.Drive object
- System.Shell.Drive object Windows Sidebar , rootDirectory property
topic_type:
- apiref
api_name:
- System.Shell.Drive.rootDirectory
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

# System.Shell.Drive.rootDirectory property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Universal Naming Convention (UNC) path to the root folder of a system storage device.

This property is read-only.

## Syntax


```JScript
strrootDirectory = System.Shell.Drive.rootDirectory
```



## Property value

A **String** that receives the UNC path.

## Remarks

If the location of a drag-and-drop operation is the **rootDirectory**, it cannot be used for a [**moveHere**](system-shell-folder-movehere.md) or [**copyHere**](system-shell-folder-copyhere.md) operation due to operating system restrictions.

## Examples

The following example demonstrates how to get the path to the root folder of a storage device.


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

 

 





