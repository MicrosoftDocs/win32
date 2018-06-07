---
Description: Each reparse point has an identifier tag so that you can efficiently differentiate between the different types of reparse points, without having to examine the user-defined data in the reparse point.
ms.assetid: d02a2f50-d374-4149-bc04-49b7db052f62
title: Reparse Point Tags
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reparse Point Tags

Each reparse point has an identifier tag so that you can efficiently differentiate between the different types of reparse points, without having to examine the user-defined data in the reparse point. The system uses a set of predefined tags and a range of tags reserved for Microsoft. If you use any of the reserved tags when setting a reparse point, the operation fails. Tags not included in these ranges are not reserved and are available for your application.

When you set a reparse point, you must tag the data to be placed in the reparse point. After the reparse point has been established, a new set operation fails if the tag for the new data does not match the tag for the existing data. If the tags match, the set operation overwrites the existing reparse point.

To retrieve the reparse point tag, use the [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea) function. If the **dwFileAttributes** member includes the **FILE\_ATTRIBUTE\_REPARSE\_POINT** attribute, then the **dwReserved0** member specifies the reparse point.

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

-   [**IsReparseTagMicrosoft**](/windows/desktop/api/Winnt/nf-winnt-isreparsetagmicrosoft)
-   [**IsReparseTagNameSurrogate**](/windows/desktop/api/Winnt/nf-winnt-isreparsetagnamesurrogate)

Each macro returns a nonzero value if the associated bit is set.

The following are Microsoft's predefined reparse tag values; they are defined in WinNT.h:

-   **IO\_REPARSE\_TAG\_CSV**
-   **IO\_REPARSE\_TAG\_DEDUP**
-   **IO\_REPARSE\_TAG\_DFS**
-   **IO\_REPARSE\_TAG\_DFSR**
-   **IO\_REPARSE\_TAG\_HSM**
-   **IO\_REPARSE\_TAG\_HSM2**
-   **IO\_REPARSE\_TAG\_MOUNT\_POINT**
-   **IO\_REPARSE\_TAG\_NFS**
-   **IO\_REPARSE\_TAG\_RESERVED\_ONE**
-   **IO\_REPARSE\_TAG\_RESERVED\_RANGE**
-   **IO\_REPARSE\_TAG\_RESERVED\_ZERO**
-   **IO\_REPARSE\_TAG\_SIS**
-   **IO\_REPARSE\_TAG\_SYMLINK**
-   **IO\_REPARSE\_TAG\_WIM**

To ensure uniqueness of tags, Microsoft provides a mechanism to distribute new tags. For more information, see the [Installable File System (IFS) Kit](Http://go.microsoft.com/fwlink/p/?linkid=84079).

 

 



