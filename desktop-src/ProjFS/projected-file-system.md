---
title: Windows Projected File System
description: Overview of the Windows Projected File System (ProjFS)
ms.assetid: <GUID-GOES-HERE>
ms.date: 09/14/2018
ms.topic: article
---

# Windows Projected File System (ProjFS)

The Windows Projected File System (ProjFS) allows a user-mode application called a "provider" to project hierarchical data from a backing data store into the file system, making it appear as files and directories in the file system. For example, a simple provider could project the Windows registry into the file system, making registry keys and values appear as files and directories, respectively. An example of a more complex provider is [VFS for Git](https://github.com/Microsoft/VFSForGit), which is used to virtualize very large git repos.

> [!NOTE]
> ProjFS is designed for use with high-speed backing data stores. One of its design goals is to make the projected data appear as if it were locally present, hiding the fact that the data may be remote. As such, ProjFS doesn't provide: mechanisms for reporting progress of data recall; indication of the online versus offline state of a file; nor other features that may be desirable when working with backing data stores that are slow. For such scenarios, consider instead using the [Cloud Files API](../cfapi/cloud-files-api-portal.md).

## In this section

| Topic                                                                                                       | Description |
|-------------------------------------------------------------------------------------------------------------|-------------|
| [Windows Projected File System Programming Guide](projfs-programming-guide.md)                              | Conceptual information on implementing a ProjFS provider application.
| [Windows Projected File System API Reference](projfs-reference.md)                                          | Reference information for the ProjFS programming interface.
| [Windows Projected File System glossary](projfs-glossary.md)                                                | Special terms used in ProjFS.

## Additional Resources

| Topic                                                                                                             | Description                                                                                  |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [RegFS Sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/ProjectedFileSystem) | A sample ProjFS provider that projects the Windows registry into the file system. |
<!--
| [ProjFS.Managed API](https://github.com/Microsoft/URL_TBD)                                                   | A .NET wrapper for the ProjFS API.                                                |
-->