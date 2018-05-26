---
title: System.Shell.Drive.driveFormat property
description: Gets whether the system storage device is formatted with Microsoft Windows NT File System (NTFS) or FAT32 permissions.
ms.assetid: 16899639-08b0-428b-81cf-bb16aba80bbb
keywords:
- driveFormat property Windows Sidebar
- driveFormat property Windows Sidebar , System.Shell.Drive object
- System.Shell.Drive object Windows Sidebar , driveFormat property
topic_type:
- apiref
api_name:
- System.Shell.Drive.driveFormat
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

# System.Shell.Drive.driveFormat property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets whether the system storage device is formatted with Microsoft Windows NT File System (NTFS) or FAT32 permissions.

This property is read-only.

## Syntax


```JScript
strdriveFormat = System.Shell.Drive.driveFormat
```



## Property value

A **String** that receives the device formatting.

<dt>



 (NTFS)


</dt> <dd>

If the storage device supports NTFS permissions.

</dd> <dt>



 (FAT32)


</dt> <dd>

If the storage device does not support NTFS permissions.

</dd> </dl>

## Remarks

*strDriveFormat* is undefined in the event of an error (the drive is not ready, is invalid, or otherwise unavailable).

## Examples

The following example demonstrates how to get the storage device format.


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

 

 





