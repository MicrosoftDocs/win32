---
description: Information about file management.
ms.assetid: cf4e69b9-86dd-43a4-9011-6209fc65f550
title: About File Management
ms.topic: article
ms.date: 05/31/2018
---

# About File Management

The following topics contain more information about file management.

## In this section



| Topic                                                                                                 | Description                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [File System Functionality Comparison](filesystem-functionality-comparison.md)<br/>            | Tables that list functionality and feature support comparisons for the four main Windows file systems, NTFS, exFAT, UDF, and FAT32.<br/>                                                                           |
| [Files and Clusters](files-and-clusters.md)<br/>                                               | A *file* is a unit of data in the file system that a user can access and manage.<br/>                                                                                                                              |
| [Creating, Deleting, and Maintaining Files](creating--deleting--and-maintaining-files.md)<br/> | Functions to use to create, delete, and maintain files.<br/>                                                                                                                                                       |
| [Obtaining and Setting File Information](obtaining-and-setting-file-information.md)<br/>       | Functions to use to get and set file information.<br/>                                                                                                                                                             |
| [Reading From and Writing to Files](reading-from-and-writing-to-files.md)<br/>                 | An application reads from and writes to a file by using the [**ReadFile**](/windows/desktop/api/FileAPI/nf-fileapi-readfile), [**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex), [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile), and [**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex) functions.<br/> |
| [File and Directory Linking](file-and-directory-linking.md)<br/>                               | There are two types of links supported in the NTFS file system: [hard links and junctions](hard-links-and-junctions.md).<br/>                                                                                     |
| [Block Cloning](block-cloning.md)<br/>                                                         | A *block clone* operation instructs the file system to copy a range of file bytes on behalf of an application.<br/>                                                                                                |
| [File Compression and Decompression](file-compression-and-decompression.md)<br/>               | The NTFS file system uses Lempel-Ziv compression, which is a lossless compression algorithm.<br/>                                                                                                                  |
| [File Encryption](file-encryption.md)<br/>                                                     | The Encrypted File System (EFS) provides cryptographic protection of individual files on NTFS file system volumes by using a public-key system.<br/>                                                               |
| [File Security and Access Rights](file-security-and-access-rights.md)<br/>                     | Because files are [securable objects](/windows/desktop/SecAuthZ/securable-objects), access to them is regulated by the access-control model that governs access to all other securable objects in Windows.<br/>                     |
| [Input and Output (I/O)](input-and-output--i-o-.md)<br/>                                       | Windows provides the ability to perform input and output (I/O) operations on storage components located on local and remote computers.<br/>                                                                        |
| [Sparse Files](sparse-files.md)<br/>                                                           | File compression of files that contain mostly zeros makes efficient use of disk space.<br/>                                                                                                                        |
| [Symbolic Links](symbolic-links.md)<br/>                                                       | A symbolic link is a file-system object that points to another file system object. The object being pointed to is called the target.<br/>                                                                          |



 

 

