---
description: Control codes used with file compression and decompression and with reparse points.
ms.assetid: e2e671c7-ef65-4401-8016-649e86f84fec
title: Directory Management Control Codes
ms.topic: article
ms.date: 05/31/2018
---

# Directory Management Control Codes

The following control codes are used with [file compression and decompression](file-compression-and-decompression.md).



| Control Code                                             | Meaning                                                                                                                                     |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_GET\_COMPRESSION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_compression) | Retrieves the current compression state of a file or directory on a volume whose file system supports per-stream compression.<br/>    |
| [**FSCTL\_SET\_COMPRESSION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_set_compression) | Sets the compression state of a file or directory on a volume whose file system supports per-file and per-directory compression.<br/> |



 

The following control codes are used with [reparse points](reparse-points.md).

## In this section



| Control Code                                                                   | Description                                                                                                           |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_DELETE\_REPARSE\_POINT**](/windows/win32/api/winioctl/ni-winioctl-fsctl_delete_reparse_point)<br/> | Deletes a reparse point from the specified file or directory.<br/>                                              |
| [**FSCTL\_GET\_REPARSE\_POINT**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_reparse_point)<br/>       | Retrieves the reparse point data associated with the file or directory identified by the specified handle.<br/> |
| [**FSCTL\_SET\_REPARSE\_POINT**](/windows/win32/api/winioctl/ni-winioctl-fsctl_set_reparse_point)<br/>       | Sets a reparse point on a file or directory.<br/>                                                               |



 

## Related topics

<dl> <dt>

[File Management Control Codes](file-management-control-codes.md)
</dt> <dt>

[Volume Management Control Codes](volume-management-control-codes.md)
</dt> </dl>

 

