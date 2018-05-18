---
title: System.Shell.Drive.volumeLabel property
description: Gets or sets the volume label of the system storage device.
ms.assetid: '91e68636-2e2e-4b5d-ab8e-8ed64bf08d33'
keywords: ["volumeLabel property Windows Sidebar", "volumeLabel property Windows Sidebar , System.Shell.Drive object", "System.Shell.Drive object Windows Sidebar , volumeLabel property"]
topic_type:
- apiref
api_name:
- System.Shell.Drive.volumeLabel
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Drive.volumeLabel property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the volume label of the system storage device.

This property is read/write.

## Syntax


```JScript
strvolumeLabel = System.Shell.Drive.volumeLabel
System.Shell.Drive.volumeLabel = strvolumeLabel
```



## Property value

A **String** that specifies or receives the volume label.

## Remarks

Administrator privileges are required to change the volume label.

This value is not guaranteed to be unique unless it is used with a drive letter identifier.

The label length is determined by the operating system. For example, NTFS allows a volume label to be up to 32 characters long. Note that null is a valid volume label.

## Examples

The following example demonstrates how to get the total space of a storage device.


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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Shell.Drive**](system-shell-drive.md)
</dt> <dt>

[**System.Shell**](system-shell.md)
</dt> </dl>

 

 





