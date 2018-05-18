---
title: System.Shell.Drive.totalFreeSpace property
description: Gets the total amount of free space, in megabytes (MB), on the system storage device.
ms.assetid: '92c641d8-b263-4695-ad9c-50cbad4558e5'
keywords: ["totalFreeSpace property Windows Sidebar", "totalFreeSpace property Windows Sidebar , System.Shell.Drive object", "System.Shell.Drive object Windows Sidebar , totalFreeSpace property"]
topic_type:
- apiref
api_name:
- System.Shell.Drive.totalFreeSpace
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Drive.totalFreeSpace property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the total amount of free space, in megabytes (MB), on the system storage device.

This property is read-only.

## Syntax


```JScript
strtotalFreeSpace = System.Shell.Drive.totalFreeSpace
```



## Property value

A **String** that receives the total amount of free space.

## Remarks

The value returned by **totalFreeSpace** is typically the same as [**freeSpace**](system-shell-drive-freespace.md). Any difference between the properties occurs on computer systems that support enforced disk storage quotas, and can be due to user-privilege configurations assigned to the currently-logged-on user.

## Examples

The following example demonstrates how to get the total free space of a storage device.


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

 

 





