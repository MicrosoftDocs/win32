---
Description: 'Describes the reparse point operations that you can perform by using DeviceIoControl.'
ms.assetid: 'c7279203-2443-401e-b541-038954094266'
title: Reparse Point Operations
---

# Reparse Point Operations

To determine whether a file system supports reparse points, call the [**GetVolumeInformation**](getvolumeinformation.md) function and examine the **FILE\_SUPPORTS\_REPARSE\_POINTS** bit flag.

The [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function enables you to set, modify, obtain, and remove reparse points. The following table describes the reparse point operations that you can perform using **DeviceIoControl**.



| Operation                                                           | Description                                                                                     |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**FSCTL\_SET\_REPARSE\_POINT**](fsctl-set-reparse-point.md)       | Allows the calling program to set a new reparse point, or to modify an existing one.<br/> |
| [**FSCTL\_GET\_REPARSE\_POINT**](fsctl-get-reparse-point.md)       | Obtains the information stored in an existing reparse point.<br/>                         |
| [**FSCTL\_DELETE\_REPARSE\_POINT**](fsctl-delete-reparse-point.md) | Removes an existing reparse point.<br/>                                                   |



 

If you are modifying, getting, or deleting a reparse point, you must specify the same reparse tag in the operation that is contained in the file. Otherwise, the operation will fail with the error **ERROR\_REPARSE\_TAG\_MISMATCH**. If you are modifying or deleting a reparse point, you must also specify the reparse **GUID** in the operation that is contained in the file. Otherwise, the operation will fail with the error **ERROR\_REPARSE\_ATTRIBUTE\_CONFLICT**.

To determine whether a file or directory contains a reparse point, use the [**GetFileAttributes**](getfileattributes.md) function. If the file or directory has an associated reparse point, the **FILE\_ATTRIBUTE\_REPARSE\_POINT** attribute is set.

To overwrite an existing reparse point without already having a handle to the file or directory, call [**CreateFile**](createfile.md) with **FILE\_FLAG\_OPEN\_REPARSE\_POINT**. This flag allows you to open the file whether or not the corresponding file system filter is installed and working correctly.

 

 




