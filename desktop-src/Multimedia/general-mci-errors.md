---
title: General MCI Errors
description: General MCI Errors
ms.assetid: be9c4a2b-44bc-410c-be74-ba55bb4e785b
keywords:
- MCIERR return values,general errors
- multimedia reference,MCI errors
- reference for multimedia,MCI errors
- Media Control Interface (MCI),general errors
- MCI (Media Control Interface),general errors
- reference for MCI,general errors
- MCI reference,general errors
- Media Control Interface (MCI),errors
- MCI (Media Control Interface),errors
- reference for MCI,errors
- MCI reference,errors
- mciSendCommand function
- mciSendString function
ms.topic: article
ms.date: 05/31/2018
---

# General MCI Errors

The following error values can be returned by either the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) or [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function:



| Value                            | Meaning                                                                                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MCIERR\_BAD\_TIME\_FORMAT        | The specified value for the time format is invalid.                                                                                                         |
| MCIERR\_CANNOT\_LOAD\_DRIVER     | The specified device driver will not load properly.                                                                                                         |
| MCIERR\_CANNOT\_USE\_ALL         | The device name "all" is not allowed for this command.                                                                                                      |
| MCIERR\_CREATEWINDOW             | Could not create or use window.                                                                                                                             |
| MCIERR\_DEVICE\_LENGTH           | The device or driver name is too long. Specify a device or driver name that is less than 79 characters.                                                     |
| MCIERR\_DEVICE\_LOCKED           | The device is now being closed. Wait a few seconds, then try again.                                                                                         |
| MCIERR\_DEVICE\_NOT\_INSTALLED   | The specified device is not installed on the system. Use the Drivers option from the Control Panel to install the device.                                   |
| MCIERR\_DEVICE\_NOT\_READY       | The device driver is not ready.                                                                                                                             |
| MCIERR\_DEVICE\_OPEN             | The device name is already used as an alias by this application. Use a unique alias.                                                                        |
| MCIERR\_DEVICE\_ORD\_LENGTH      | The device or driver name is too long. Specify a device or driver name that is less than 79 characters.                                                     |
| MCIERR\_DEVICE\_TYPE\_REQUIRED   | The specified device cannot be found on the system. Check that the device is installed and the device name is spelled correctly.                            |
| MCIERR\_DRIVER                   | The device driver exhibits a problem. Check with the device manufacturer about obtaining a new driver.                                                      |
| MCIERR\_DRIVER\_INTERNAL         | The device driver exhibits a problem. Check with the device manufacturer about obtaining a new driver.                                                      |
| MCIERR\_DUPLICATE\_ALIAS         | The specified alias is already used in this application. Use a unique alias.                                                                                |
| MCIERR\_EXTENSION\_NOT\_FOUND    | The specified extension has no device type associated with it. Specify a device type.                                                                       |
| MCIERR\_EXTRA\_CHARACTERS        | You must enclose a string with quotation marks; characters following the closing quotation mark are not valid.                                              |
| MCIERR\_FILE\_NOT\_FOUND         | The requested file was not found. Check that the path and filename are correct.                                                                             |
| MCIERR\_FILE\_NOT\_SAVED         | The file was not saved. Make sure your system has sufficient disk space or has an intact network connection.                                                |
| MCIERR\_FILE\_READ               | A read from the file failed. Make sure the file is present on your system or that your system has an intact network connection.                             |
| MCIERR\_FILE\_WRITE              | A write to the file failed. Make sure your system has sufficient disk space or has an intact network connection.                                            |
| MCIERR\_FILENAME\_REQUIRED       | The filename is invalid. Make sure the filename is no longer than eight characters, followed by a period and an extension.                                  |
| MCIERR\_FLAGS\_NOT\_COMPATIBLE   | The specified parameters cannot be used together.                                                                                                           |
| MCIERR\_GET\_CD                  | The requested file OR MCI device was not found. Try changing directories or restarting your system.                                                         |
| MCIERR\_HARDWARE                 | The specified device exhibits a problem. Check that the device is working correctly or contact the device manufacturer.                                     |
| MCIERR\_ILLEGAL\_FOR\_AUTO\_OPEN | MCI will not perform the specified command on an automatically opened device. Wait until the device is closed, then try to perform the command.             |
| MCIERR\_INTERNAL                 | A problem occurred in initializing MCI. Try restarting the Windows operating system.                                                                        |
| MCIERR\_INVALID\_DEVICE\_ID      | Invalid device ID. Use the ID given to the device when the device was opened.                                                                               |
| MCIERR\_INVALID\_DEVICE\_NAME    | The specified device is not open nor recognized by MCI.                                                                                                     |
| MCIERR\_INVALID\_FILE            | The specified file cannot be played on the specified MCI device. The file may be corrupt or may use an incorrect file format.                               |
| MCIERR\_MISSING\_PARAMETER       | The specified command requires a parameter, which you must supply.                                                                                          |
| MCIERR\_MULTIPLE                 | Errors occurred in more than one device. Specify each command and device separately to identify the devices causing the errors.                             |
| MCIERR\_MUST\_USE\_SHAREABLE     | The device driver is already in use. You must specify the "sharable" parameter with each open command to share the device.                                  |
| MCIERR\_NO\_ELEMENT\_ALLOWED     | The specified device does not use a filename.                                                                                                               |
| MCIERR\_NO\_INTEGER              | The parameter for this MCI command must be an integer value.                                                                                                |
| MCIERR\_NO\_WINDOW               | There is no display window.                                                                                                                                 |
| MCIERR\_NONAPPLICABLE\_FUNCTION  | The specified MCI command sequence cannot be performed in the given order. Correct the command sequence; then, try again.                                   |
| MCIERR\_NULL\_PARAMETER\_BLOCK   | A null parameter block (structure) was passed to MCI.                                                                                                       |
| MCIERR\_OUT\_OF\_MEMORY          | Your system does not have enough memory for this task. Quit one or more applications to increase the available memory, then, try to perform the task again. |
| MCIERR\_OUTOFRANGE               | The specified parameter value is out of range for the specified MCI command.                                                                                |
| MCIERR\_SET\_CD                  | The specified file or MCI device is inaccessible because the application cannot change directories.                                                         |
| MCIERR\_SET\_DRIVE               | The specified file or MCI device is inaccessible because the application cannot change drives.                                                              |
| MCIERR\_UNNAMED\_RESOURCE        | You cannot store an unnamed file. Specify a filename.                                                                                                       |
| MCIERR\_UNRECOGNIZED\_COMMAND    | The driver cannot recognize the specified command.                                                                                                          |
| MCIERR\_UNSUPPORTED\_FUNCTION    | The MCI device driver the system is using does not support the specified command.                                                                           |



 

 

 