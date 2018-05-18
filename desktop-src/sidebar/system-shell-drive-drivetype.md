---
title: System.Shell.Drive.driveType property
description: Gets the system storage device type.
ms.assetid: '51a0a4e9-4867-4b78-ad65-afcd5f1b74ca'
keywords: ["driveType property Windows Sidebar", "driveType property Windows Sidebar , System.Shell.Drive object", "System.Shell.Drive object Windows Sidebar , driveType property"]
topic_type:
- apiref
api_name:
- System.Shell.Drive.driveType
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Drive.driveType property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the system storage device type.

This property is read-only.

## Syntax


```JScript
idriveType = System.Shell.Drive.driveType
```



## Property value

An **Integer** that receives the device type.

<dt>



 (undefined)


</dt> <dd>

The drive type cannot be determined. For example, this value is returned if no network drive or removable drive is mounted for the drive letter specified.

</dd> <dt>



 (1)


</dt> <dd>

Floppy drive.

</dd> <dt>



 (2)


</dt> <dd>

Removable drive, such as a USB or cartridge drive.

</dd> <dt>



 (3)


</dt> <dd>

Fixed drive.

</dd> <dt>



 (4)


</dt> <dd>

Remote (network) drive.

</dd> <dt>



 (5)


</dt> <dd>

Optical drive.

</dd> <dt>



 (6)


</dt> <dd>

RAM disk.

</dd> </dl>

## Examples

The following example demonstrates how to get the storage device type.


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

 

 





