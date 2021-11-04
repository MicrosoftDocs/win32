---
title: Projected File System Programming Guide
description: Conceptual information on implementing a ProjFS provider application.
ms.assetid: <GUID-GOES-HERE>
ms.date: 01/17/2020
ms.topic: article
---

# Projected File System (ProjFS) programming guide

The Windows Projected File System (ProjFS) allows a user-mode application called a "provider" to project hierarchical data into the file system, making it appear as files and directories in the file system.

## In this section

| Topic                                                                                                       | Description |
|-------------------------------------------------------------------------------------------------------------|-------------|
| [Provider Overview](provider-overview.md)                                                                   | Conceptual overview of a provider application.
| [Cache State in the Virtualization Root](cache-state.md)                                                    | Describes the different cache states a file or directory managed by the provider may have. 
| [Enabling Windows Projected File System](enabling-windows-projected-file-system.md)                         | Describes how to enable the ProjFS optional component.
| [Virtualization Instance Lifecycle](virtualization-instance-lifecycle.md)                                   | Overview of the lifecycle of a ProjFS virtualization instance.
| [Enumerating Files and Directories](enumerating-files-and-directories.md)                                   | Describes how a ProjFS provider participates in directory enumeration.
| [Providing File Data](providing-file-data.md)                                                               | Describes how a provider supplies placeholder info and file data.
| [File System Operation Notifications](file-system-operation-notifications.md)                               | Describes how a provider can receive notifications of file system operations.
| [Handling View Changes](handling-view-changes.md)                                                           | Describes how to update the client view of a provider's backing store.
| [Asynchronous Callback Handling](asynchronous-callback-handling.md)                                         | Describes how the provider can asynchronously service callbacks.
| [Windows Projected File System API Reference](/windows/desktop/api/_projfs) | Reference information for the ProjFS programming interface.

## Additional Resources

| Topic                                                                                                             | Description                                                                                  |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [RegFS Sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/ProjectedFileSystem) | A sample ProjFS provider that projects the Windows registry into the file system. |
<!--
| [ProjFS.Managed API](https://github.com/Microsoft/URL_TBD)                                                   | A .NET wrapper for the ProjFS API.                                                |
-->