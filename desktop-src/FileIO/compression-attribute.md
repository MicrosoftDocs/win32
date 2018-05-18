---
Description: 'On an NTFS file system volume, each file and directory has a compression attribute.'
ms.assetid: '8aca120c-22a7-4dc8-a921-dfcec1277452'
title: Compression Attribute
---

# Compression Attribute

On an NTFS file system volume, each file and directory has a *compression attribute*. Other file systems may also implement a compression attribute for individual files and directories.

You can determine whether a file system supports a compression attribute for files and directories by calling the [**GetVolumeInformation**](getvolumeinformation.md) function and examining the **FILE\_FILE\_COMPRESSION** bit flag.

Use the [**GetFileAttributes**](getfileattributes.md) or [**GetFileAttributesEx**](getfileattributesex.md) function to determine the compression attribute of a file or directory.

If a file's compression attribute is set (**FILE\_ATTRIBUTE\_COMPRESSED**), all data in the file is compressed. If the attribute is clear, none of the data in the file is compressed. There is no partially compressed state from a user-mode programming perspective; the compression attribute is a simple Boolean indicator of compression state.

A directory's compression attribute provides a default compression attribute for newly created files and subdirectories. When you call [**CreateFile**](createfile.md) or [**CreateDirectory**](createdirectory.md) to create a new file or directory, the new file or directory inherits the compression attribute of its parent directory.

To modify the **FILE\_ATTRIBUTE\_COMPRESSED** attribute for a file or directory, you must use the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the [**FSCTL\_SET\_COMPRESSION**](fsctl-set-compression.md) control code.

## Related topics

<dl> <dt>

[**File Attribute Constants**](file-attribute-constants.md)
</dt> </dl>

 

 



