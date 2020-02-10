---
title: Cache State in the Virtualization Root
description: Describes the different cache states a file or directory managed by the provider may have. 
ms.assetid: <GUID-GOES-HERE>
ms.date: 01/17/2020
ms.topic: article
---

# Cache State In the Virtualization Root

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
