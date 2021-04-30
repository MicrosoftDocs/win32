---
description: A symbolic link is a file-system object that points to another file system object. The object being pointed to is called the target.
ms.assetid: 'd6bf5df7-bc12-4dec-b116-95d9109f5eb4'
title: Symbolic Links
ms.topic: article
ms.date: 05/31/2018
---

# Symbolic Links

A symbolic link is a file-system object that points to another file system object. The object being pointed to is called the target.

Symbolic links are transparent to users; the links appear as normal files or directories, and can be acted upon by the user or application in exactly the same manner.

Symbolic links are designed to aid in migration and application compatibility with UNIX operating systems. Microsoft has implemented its symbolic links to function just like UNIX links.

For more information, see the following topics.

## In this section



| Topic                                                                                                             | Description                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Symbolic Link Effects on File Systems Functions](symbolic-link-effects-on-file-systems-functions.md)<br/> | How symbolic links affect standard file functions that use path names to specify one or more files.<br/>                                        |
| [Programming Considerations](symbolic-link-programming-considerations.md)<br/>                             | Programming considerations for working with symbolic links.<br/>                                                                                |
| [Creating Symbolic Links](creating-symbolic-links.md)<br/>                                                 | Create symbolic links that use either an absolute or relative path by using the [**CreateSymbolicLink**](/windows/desktop/api/WinBase/nf-winbase-createsymboliclinka) function.<br/> |



 

## Supported Operating Systems

Symbolic links are available in NTFS starting with Windows Vista.

 

 




