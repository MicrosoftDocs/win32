---
title: Hard links and junctions
description: Provides an overview of hard links and junctions.
ms.assetid: f9e40a86-a4a6-4524-8045-312da72dc655
ms.topic: article
ms.date: 02/08/2023
---

# Hard links and junctions

The NTFS file system supports three types of file links: hard links, junctions, and symbolic links. This article is an overview of hard links and junctions. For information about symbolic links, see [Create symbolic links](creating-symbolic-links.md).

## Hard links

A *hard link* is the file-system representation of a file by which more than one path references a single file in the same volume. To create a hard link, use the [CreateHardLinkA](/windows/desktop/api/WinBase/nf-winbase-createhardlinka) function.

Any changes to a hard-linked file are instantly visible to applications that access it through the links that reference it. However, the directory entry size and attribute information of the file are updated only at the link through which the change was made. The attributes on the file are reflected in every hard link to that file, and changes to that file's attributes propagate to all the hard links. For example, if you clear the read-only attribute flag on a particular hard link so you can delete that hard link, and there are multiple hard links to the file, then you must set the read-only flag on the file from one of its remaining hard links to bring the file and all remaining hard links back to the read-only state.

For example, in a system where C: and D: are local drives and Z: is a network drive mapped to *\\\\fred\\share*, the following references are permitted as a hard link:

- *C:\\dira\\ethel.txt* linked to *C:\\dirb\\dirc\\lucy.txt*
- *D:\\dir1\\tinker.txt* linked to *D:\\dir2\\dirx\\bell.txt*
- *C:\\diry\\bob.bak* linked to *C:\\dir2\\mina.txt*

The following references aren't permitted:

- *C:\\dira* linked to *C:\\dirb*
- *C:\\dira\\ethel.txt* linked to *D:\\dirb\\lucy.txt*
- *C:\\dira\\ethel.txt* linked to *Z:\\dirb\\lucy.txt*

To delete a hard link, use the [DeleteFileA](/windows/desktop/api/FileAPI/nf-fileapi-deletefilea) function. You can delete hard links in any order regardless of the order in which they're created.

## Junctions

A *junction* (also called a *soft link*) differs from a hard link in that the storage objects it references are separate directories. A junction can also link directories located on different local volumes on the same computer. Otherwise, junctions operate identically to hard links. Junctions are implemented through [reparse points](reparse-points.md).

Assuming the same conditions in the Hard Links section, the following references are permitted as junctions:

- *C:\\dira* linked to *C:\\dirb\\dirc*
- *C:\\dirx* linked to *D:\\diry*

The following references aren't permitted:

- *C:\\dira\\one.txt* linked to *C:\\dirb\\two.txt*
- *C:\\dir1* linked to *Z:\\dir2*

## See also

[Create symbolic links](creating-symbolic-links.md)
