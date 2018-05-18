---
Description: 'Describes how reparse points enable file system behavior that departs from behavior most Windows developers expect.'
ms.assetid: '1aaebda9-0013-4282-9ae1-7c829e171942'
title: Reparse Points and File Operations
---

# Reparse Points and File Operations

*Reparse points* enable file system behavior that departs from the behavior most Windows developers may be accustomed to, therefore being aware of these behaviors when writing applications that manipulate files is vital to robust and reliable applications intended to access file systems that support reparse points. The extent of these considerations will depend on the specific implementation and associated file system filter behavior of a particular reparse point, which can be user-defined. For more information, see [Reparse Points](reparse-points.md).

Consider the following examples regarding NTFS reparse point implementations, which include mounted folders, linked files, and the Microsoft Remote Storage Server:

-   Backup applications that use [file streams](file-streams.md) should specify **BACKUP\_REPARSE\_DATA** in the [**WIN32\_STREAM\_ID**](https://msdn.microsoft.com/library/windows/desktop/aa362667) structure when backing up files with reparse points.
-   Applications that use the [**CreateFile**](createfile.md) function should specify the **FILE\_FLAG\_OPEN\_REPARSE\_POINT** flag when opening the file if it is a reparse point. For more information, see [Creating and Opening Files](creating-and-opening-files.md).
-   The process of [defragmenting files](defragmenting-files.md) requires special handling for reparse points.
-   Virus detection applications should search for reparse points that indicate linked files.
-   Most applications should take special actions for files that have been moved to long-term storage, if only to notify the user that it may take a while to retrieve the file.
-   The [**OpenFileById**](openfilebyid.md) function will either open the file or the reparse point, depending on the use of the **FILE\_FLAG\_OPEN\_REPARSE\_POINT** flag.
-   Symbolic links, as reparse points, have certain [programming considerations](symbolic-link-programming-considerations.md) specific to them.
-   Volume management activities for reading update sequence number (USN) change journal records require special handling for reparse points when using the [**USN\_RECORD**](usn-record-str.md) and [**READ\_USN\_JOURNAL\_DATA**](read-usn-journal-data-str.md) structures.

## Related topics

<dl> <dt>

[Determining Whether a Directory Is a Mounted Folder](determining-whether-a-directory-is-a-volume-mount-point.md)
</dt> <dt>

[Creating Mounted Folders](mounting-and-dismounting-a-volume.md)
</dt> <dt>

[Symbolic Link Effects on File Systems Functions](symbolic-link-effects-on-file-systems-functions.md)
</dt> </dl>

 

 



