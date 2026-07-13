---
description: Manage directories with directory entry table, directory handles, reparse points.
title: Local File Systems
ms.topic: concept-article
ms.date: 07/09/2025
# customer intent: As a Windows app developer, I want to understand how local file systems work in Windows, so that I can effectively manage files and directories in my app.
---

# Local file systems

A *file system* enables applications to store and retrieve files on storage devices. Files are placed in a hierarchical structure. The file system specifies naming conventions for files and the format for specifying the path to a file in the tree structure.

Each file system consists of one or more drivers and dynamic-link libraries that define the data formats and features of the file system. File systems can exist on many different types of storage devices, including hard disks, jukeboxes, removable optical disks, tape back-up units, and memory cards.

All file systems supported by Windows have the following storage components:

- **Volumes** - A *volume* is a collection of directories and files.
- **Directories** - A *directory* is a hierarchical collection of directories and files.
- **Files** - A *file* is a logical grouping of related data.

## In this section

The following topics provide information about the file systems supported by Windows, including how to manage files, directories, and volumes:

| Topic | Description |
|-------|-------------|
| [Directory Management](directory-management.md) | A *directory* is a hierarchical collection of directories and files. The only constraint on the number of files that can be contained in a single directory is the physical size of the disk on which the directory is located. |
| [Disk Management](disk-management.md) | A *hard disk* is a rigid disk inside a computer that stores and provides relatively quick access to large amounts of data. It is the type of storage most often used with Windows. The system also supports removable media. |
| [File Management](file-management.md) | A *file object* provides a representation of a resource (either a physical device or a resource located on a physical device) that can be managed by the I/O system. |
| [Transactional NTFS (TxF)](transactional-ntfs-portal.md) | Transactional NTFS (TxF) allows file operations on an NTFS file system volume to be performed in a transaction. |
| [Volume Management](volume-management.md) | The highest level of organization in the file system is the *volume*. A file system resides on a volume. |

## Related content

[FAT Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc758586(v=ws.10))

[File Systems Technologies](/previous-versions/windows/it-pro/windows-server-2003/cc778296(v=ws.10))

[NTFS Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc758691(v=ws.10))
