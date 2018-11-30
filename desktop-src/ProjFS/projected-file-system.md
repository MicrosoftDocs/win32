---
title: Windows Projected File System
description: Overview of the Windows Projected File System (ProjFS)
ms.assetid: <GUID-GOES-HERE>
ms.date: 09/14/2018
ms.topic: article
---

# Windows Projected File System (ProjFS)

The Windows Projected File System (ProjFS) allows a user-mode application called a "provider" to project hierarchical data into the file system, making it appear as files and directories in the file system.  For example, a simple provider could project the Windows registry into the file system, making registry keys and values appear as files and directories, respectively.  An example of a more complex provider is [VFS for Git](https://github.com/Microsoft/VFSForGit), used to virtualize very large git repos.

## Provider Overview

The provider maintains and understands a backing data store, and uses the ProjFS API to project this data store into the file system, where it appears to the user as files and directories.  The provider’s backing store may be local to the user’s system, or it may be located remotely.

The part of the file system that the provider owns, where its data is projected, is rooted in a directory called the “virtualization root”.  When the provider wants to start projecting its data it starts a "virtualization instance", which is an object that manages communication between the provider and ProjFS for the set of files and directories located under a particular virtualization root.  Any files and directories that are descendants of the virtualization root that have not been created locally by the user are materialized by the provider via the ProjFS API.  These items start off as virtual files and directories, meaning that they do not exist on the user’s local storage device, but are injected into enumeration results by ProjFS.  As the items are opened and read, ProjFS invokes callbacks implemented by the provider to request data, and the provider uses ProjFS APIs to send that data to the local storage where it is cached for subsequent access.  If the user's view of the backing data store needs to change, for instance if the contents of the data store have changed, the provider can use ProjFS APIs to update or delete local items to reflect the new view of the data store.

### Callback return codes

Each callback lists a number of possible return values specific to that callback.  In addition to the return values listed for a given callback, a callback may also return certain other error codes.  This is the complete list of error codes that a callback may return:

| Error Code                                    | Meaning
|-----------------------------------------------|--------
| S_OK                                          | Operation Successful
| E_OUTOFMEMORY                                 | Failed to allocate necessary memory.
| HRESULT_FROM_WIN32(ERROR_IO_PENDING)          | The provider wishes to complete the operation at a later time.
| HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER) | A buffer passed to a callback was too small.
| HRESULT_FROM_WIN32(ERROR_FILE_NOT_FOUND)      | The file does not exist in the provider’s backing store.
| HRESULT_FROM_WIN32(ERROR_INVALID_PARAMETER)   | A callback argument is invalid.  For example, an enumeration ID doesn't correspond to an active enumeration session.
| HRESULT_FROM_NT(STATUS_CANNOT_DELETE)         | The provider does not want to allow this file or directory to be deleted.

Callbacks may also return any errors they may receive from calls to ProjFS APIs.
If a callback returns an error code that is not on the preceding list or that did not come from a ProjFS API, ProjFS will return it to the file system as STATUS_INTERNAL_ERROR.

## Cache State In the Virtualization Root

The provider uses the local file system under the virtualization root as a cache of the items that it manages.  An item (file or directory) can be in one of six states on the local file system:

* Virtual

  The item does not exist locally on disk.  It is projected, i.e. synthesized, during enumerations of its parent directory.  Virtual items are merged with any items that may exist on disk to present the full contents of the parent directory.

* Placeholder

  For files: The file's content (primary data stream) is not present on the disk.  The file’s metadata (name, size, timestamps, attributes, etc.) is cached on the disk.
  
  For directories: Some or all of the directory’s immediate descendants (the files and directories in the directory) are not present on the disk, i.e. they are still virtual.  The directory’s metadata (name, timestamps, attributes, etc.) is cached on the disk.

* Hydrated placeholder

  For files: The file’s content and metadata have been cached to the disk.  Also referred to as a "partial file".
  
  For directories: A directory that was created on disk as a placeholder never becomes a hydrated placeholder directory.  This allows the provider to add or remove items from the directory in its backing store and have those changes be reflected in the local cache.

* Dirty placeholder (hydrated or not)

  The item's metadata has been locally modified and is no longer a cache of its state in the provider's store. Note that creating or deleting a file or directory under a placeholder directory causes that placeholder directory to become dirty.

* Full file/directory

  For files: The file's content (primary data stream) has been modified.  The file is no longer a cache of its state in the provider's store.  Files that have been created on the local file system (i.e. that do not exist in the provider's store at all) are also considered to be full files.
  
  For directories: Directories that have been created on the local file system (i.e. that do not exist in the provider's store at all) are considered to be full directories.  A directory that was created on disk as a placeholder never becomes a full directory.
  
* Tombstone

  A special hidden placeholder that represents an item that has been deleted from the local file system.  When a directory is enumerated ProjFS merges the set of local items (placeholders, full files, etc.) with the set of virtual projected items.  If an item appears in both the local and projected sets, the local item takes precedence.  If a file does not exist in the local file system there is no local state, so it would appear in the enumeration.  However if that item had been deleted, having it appear in the enumeration would be unexpected.  Replacing a deleted item with a tombstone results in the following effects:

  * Enumerations to not reveal the item.
  * File opens that expect the item to exist fail with e.g. "file not found".
  * File creates that expect to succeed only if the item does not exist succeed; ProjFS removes the tombstone as part of the operation.

To illustrate the above states, consider the following sequence, given a ProjFS provider that has a single file "foo.txt" located in the virtualization root C:\root.

1. An app enumerates C:\root.  It sees the virtual file "foo.txt".  Since the file has not yet been accessed, the file does not exist on disk.
1. The app opens a handle to C:\root\foo.txt.  ProjFS tells the provider to create a placeholder for it.
1. The app reads the content of the file.  The provider provides the file content to ProjFS and it is cached to C:\root\foo.txt.  The file is now a hydrated placeholder.
1. The app updates the Last Modified timestamp.  The file is now a dirty hydrated placeholder.
1. The app opens a handle for write access to the file.  C:\root\foo.txt is now a full file.
1. The app deletes C:\root\foo.txt.  ProjFS replaces the file with a tombstone.  Now when the app enumerates C:\root it does not see foo.txt.  If it tries to open the file, the open fails with ERROR_FILE_NOT_FOUND.

## In this section

| Topic                                                                                                       | Description |
|-------------------------------------------------------------------------------------------------------------|-------------|
| [Enabling Windows Projected File System](enabling-windows-projected-file-system.md)                         | Describes how to enable the ProjFS optional component.
| [Virtualization Instance Lifecycle](virtualization-instance-lifecycle.md)                                   | Overview of the lifecycle of a ProjFS virtualization instance.
| [Enumerating Files and Directories](enumerating-files-and-directories.md)                                   | Describes how a ProjFS provider participates in directory enumeration.
| [Providing File Data](providing-file-data.md)                                                               | Describes how a provider supplies placeholder info and file data.
| [File System Operation Notifications](file-system-operation-notifications.md)                               | Describes how a provider can receive notifications of file system operations.
| [Handling View Changes](handling-view-changes.md)                                                           | Describes how to update the client view of a provider's backing store.
| [Asynchronous Callback Handling](asynchronous-callback-handling.md)                                         | Describes how the provider can asynchronously service callbacks.
| [Windows Projected File System API Reference](https://docs.microsoft.com/en-us/windows/desktop/api/_projfs) | Reference information for the ProjFS programming interface.

## Additional Resources

|                                                                                                              |                                                                                   |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [RegFS Sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/ProjectedFileSystem) | A sample ProjFS provider that projects the Windows registry into the file system. |
<!--
| [ProjFS.Managed API](https://github.com/Microsoft/URL_TBD)                                                   | A .NET wrapper for the ProjFS API.                                                |
-->