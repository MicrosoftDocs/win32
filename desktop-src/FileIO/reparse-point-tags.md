---
description: Each reparse point has an identifier tag so that you can efficiently differentiate between the different types of reparse points, without having to examine the user-defined data in the reparse point.
ms.assetid: d02a2f50-d374-4149-bc04-49b7db052f62
title: Reparse Point Tags
ms.topic: article
ms.date: 05/01/2023
---

# Reparse Point Tags

Each reparse point has an identifier tag so that you can efficiently differentiate between the different types of reparse points, without having to examine the user-defined data in the reparse point. The system uses a set of predefined tags and a range of tags reserved for Microsoft. If you use any of the reserved tags when setting a reparse point, the operation fails. Tags not included in these ranges are not reserved and are available for your application.

When you set a reparse point, you must tag the data to be placed in the reparse point. After the reparse point has been established, a new set operation fails if the tag for the new data does not match the tag for the existing data. If the tags match, the set operation overwrites the existing reparse point.

To retrieve the reparse point tag, use the [FindFirstFile](/windows/win32/api/FileAPI/nf-fileapi-findfirstfilea) function. If the **dwFileAttributes** member includes the **FILE\_ATTRIBUTE\_REPARSE\_POINT** attribute, then the **dwReserved0** member specifies the reparse point.

## Tag Contents

Reparse tags are stored as **DWORD** values. The bits define certain attributes, as shown in the following diagram.

``` syntax
   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
  +-+-+-+-+-----------------------+-------------------------------+
  |M|R|N|R|     Reserved bits     |      Reparse tag value        |
  +-+-+-+-+-----------------------+-------------------------------+
```

The low 16 bits determine the kind of reparse point. The high 16 bits have 12 bits reserved for future use and 4 bits that denote specific attributes of the tags and the data represented by the reparse point. The following table describes these bits.

| Bit | Description                                                                                                  |
|-----|--------------------------------------------------------------------------------------------------------------|
| M   | Microsoft bit. If this bit is set, the tag is owned by Microsoft. All other tags must use zero for this bit. |
| R   | Reserved; must be zero for all non-Microsoft tags.                                                           |
| N   | Name surrogate bit. If this bit is set, the file or directory represents another named entity in the system. |

The following macros exist to assist in testing tags:

- [IsReparseTagMicrosoft](/windows/win32/api/Winnt/nf-winnt-isreparsetagmicrosoft)
- [IsReparseTagNameSurrogate](/windows/win32/api/Winnt/nf-winnt-isreparsetagnamesurrogate)

Each macro returns a nonzero value if the associated bit is set.

The following are Microsoft's predefined reparse tag values; they are defined in WinNT.h:

- **IO_REPARSE_TAG_AF_UNIX**
- **IO_REPARSE_TAG_APPEXECLINK**
- **IO_REPARSE_TAG_CLOUD**
- **IO_REPARSE_TAG_CLOUD_1**
- **IO_REPARSE_TAG_CLOUD_2**
- **IO_REPARSE_TAG_CLOUD_3**
- **IO_REPARSE_TAG_CLOUD_4**
- **IO_REPARSE_TAG_CLOUD_5**
- **IO_REPARSE_TAG_CLOUD_6**
- **IO_REPARSE_TAG_CLOUD_7**
- **IO_REPARSE_TAG_CLOUD_8**
- **IO_REPARSE_TAG_CLOUD_9**
- **IO_REPARSE_TAG_CLOUD_A**
- **IO_REPARSE_TAG_CLOUD_B**
- **IO_REPARSE_TAG_CLOUD_C**
- **IO_REPARSE_TAG_CLOUD_D**
- **IO_REPARSE_TAG_CLOUD_E**
- **IO_REPARSE_TAG_CLOUD_F**
- **IO_REPARSE_TAG_CLOUD_MASK**
- **IO_REPARSE_TAG_CSV**
- **IO_REPARSE_TAG_DEDUP**
- **IO_REPARSE_TAG_DFS**
- **IO_REPARSE_TAG_DFSR**
- **IO_REPARSE_TAG_FILE_PLACEHOLDER**
- **IO_REPARSE_TAG_GLOBAL_REPARSE**
- **IO_REPARSE_TAG_HSM**
- **IO_REPARSE_TAG_HSM2**
- **IO_REPARSE_TAG_MOUNT_POINT**
- **IO_REPARSE_TAG_NFS**
- **IO_REPARSE_TAG_ONEDRIVE**
- **IO_REPARSE_TAG_PROJFS**
- **IO_REPARSE_TAG_PROJFS_TOMBSTONE**
- **IO_REPARSE_TAG_SIS**
- **IO_REPARSE_TAG_STORAGE_SYNC**
- **IO_REPARSE_TAG_SYMLINK**
- **IO_REPARSE_TAG_UNHANDLED**
- **IO_REPARSE_TAG_WCI**
- **IO_REPARSE_TAG_WCI_1**
- **IO_REPARSE_TAG_WCI_LINK**
- **IO_REPARSE_TAG_WCI_LINK_1**
- **IO_REPARSE_TAG_WCI_TOMBSTONE**
- **IO_REPARSE_TAG_WIM**
- **IO_REPARSE_TAG_WOF**

To ensure uniqueness of tags, Microsoft provides a mechanism to distribute new tags. For more information, see the [Installable File System (IFS) Kit](/previous-versions/gg463062(v=msdn.10)).
