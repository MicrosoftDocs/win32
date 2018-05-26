---
title: System.Shell.Drive.isReady property
description: Gets whether the system storage device is ready.
ms.assetid: fff17a3f-5e25-431a-a5a3-b7d092935739
keywords:
- isReady property Windows Sidebar
- isReady property Windows Sidebar , System.Shell.Drive object
- System.Shell.Drive object Windows Sidebar , isReady property
topic_type:
- apiref
api_name:
- System.Shell.Drive.isReady
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

# System.Shell.Drive.isReady property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets whether the system storage device is **ready**.

This property is read-only.

## Syntax


```JScript
bisReady = System.Shell.Drive.isReady
```



## Property value

A **Boolean** that receives the ready-state.

<dt>



 (true)


</dt> <dd>

The storage device is ready.

</dd> <dt>



 (false)


</dt> <dd>

The storage device is not ready.

</dd> </dl>

## Remarks

**isReady** returns **true** for removable media and CD-ROM drives when the storage media has been inserted and is ready for access.

## Examples

The following example demonstrates how to get the ready-state of a storage device.


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

 

 





