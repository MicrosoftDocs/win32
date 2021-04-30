---
title: LB_DIR message (Winuser.h)
description: Adds names to the list displayed by a list box. The message adds the names of directories and files that match a specified string and set of file attributes. LB\_DIR can also add mapped drive letters to the list box.
ms.assetid: 5ec134e9-fe42-4cc0-bdea-fa5e66c218f6
keywords:
- LB_DIR message Windows Controls
topic_type:
- apiref
api_name:
- LB_DIR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_DIR message

Adds names to the list displayed by a list box. The message adds the names of directories and files that match a specified string and set of file attributes. **LB\_DIR** can also add mapped drive letters to the list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The attributes of the files or directories to be added to the list box. This parameter can be one or more of the following values.



| Value                                                                                                                                                         | Meaning                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DDL_ARCHIVE"></span><span id="ddl_archive"></span><dl> <dt>**DDL\_ARCHIVE**</dt> </dl>       | Includes archived files.<br/>                                                                                                            |
| <span id="DDL_DIRECTORY"></span><span id="ddl_directory"></span><dl> <dt>**DDL\_DIRECTORY**</dt> </dl> | Includes subdirectories. Subdirectory names are enclosed in square brackets (\[ \]).<br/>                                                |
| <span id="DDL_DRIVES"></span><span id="ddl_drives"></span><dl> <dt>**DDL\_DRIVES**</dt> </dl>          | All mapped drives are added to the list. Drives are listed in the form \[-*x*-\], where *x* is the drive letter.<br/>                    |
| <span id="DDL_EXCLUSIVE"></span><span id="ddl_exclusive"></span><dl> <dt>**DDL\_EXCLUSIVE**</dt> </dl> | Includes only files with the specified attributes. By default, read/write files are listed even if DDL\_READWRITE is not specified.<br/> |
| <span id="DDL_HIDDEN"></span><span id="ddl_hidden"></span><dl> <dt>**DDL\_HIDDEN**</dt> </dl>          | Includes hidden files.<br/>                                                                                                              |
| <span id="DDL_READONLY"></span><span id="ddl_readonly"></span><dl> <dt>**DDL\_READONLY**</dt> </dl>    | Includes read-only files.<br/>                                                                                                           |
| <span id="DDL_READWRITE"></span><span id="ddl_readwrite"></span><dl> <dt>**DDL\_READWRITE**</dt> </dl> | Includes read/write files with no additional attributes. This is the default setting.<br/>                                               |
| <span id="DDL_SYSTEM"></span><span id="ddl_system"></span><dl> <dt>**DDL\_SYSTEM**</dt> </dl>          | Includes system files.<br/>                                                                                                              |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string that specifies an absolute path, relative path, or filename. An absolute path can begin with a drive letter (for example, d:\) or a UNC name (for example, \\\\ *machinename*\\ *sharename*).

If the string specifies a filename or directory that has the attributes specified by the *wParam* parameter, the filename or directory is added to the list. If the filename or directory name contains wildcard characters (? or \*), all files or directories that match the wildcard expression and have the attributes specified by the *wParam* parameter are added to the list.

</dd> </dl>

## Return value

If the message succeeds, the return value is the zero-based index of the last name added to the list.

If an error occurs, the return value is LB\_ERR. If there is insufficient space to store the new strings, the return value is LB\_ERRSPACE.

## Remarks

The [**LB\_INITSTORAGE**](lb-initstorage.md) message helps speed up the initialization of list boxes that have a large number of items (more than 100). It reserves the specified amount of memory so that subsequent **LB\_DIR** messages take the shortest possible time. You can use estimates for the *wParam* and *lParam* parameters. If you overestimate, the extra memory is allocated; if you underestimate, the normal allocation is used for items that exceed the requested amount.

If *wParam* includes the DDL\_DIRECTORY flag and *lParam* specifies all the subdirectories of a first-level directory, such as C:\\TEMP\\\*, the list box will always include a ".." entry for the root directory. This is true even if the root directory has hidden or system attributes and the DDL\_HIDDEN and DDL\_SYSTEM flags are not specified. The root directory of an NTFS volume has hidden and system attributes.

The list displays long filenames, if any.

For an ANSI application, the system converts the text in a list box to Unicode using CP\_ACP. This can cause problems. For example, accented Roman characters in a non-Unicode list box in Japanese Windows will come out garbled. To fix this, either compile the application as Unicode or use an owner-drawn list box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista)
</dt> </dl>

 

 





